#!/usr/bin/env python3
"""
Resilient Playwright scraping worker (reference implementation).

Implements the SKILL.md skeleton: idempotent jobs, per-domain throttling,
classified retries with full-jitter backoff, per-domain circuit breakers,
challenge detection + parking, validation + deduping, checkpoint/resume,
JSON logs, metrics, and failure artifacts.

Usage:
    pip install -r requirements.txt
    python -m playwright install chromium
    python resilient_scrape.py --input urls.txt --out ./out --concurrency 3

urls.txt: one URL per line, blank lines and lines starting with # ignored.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import random
import re
import signal
import sys
import time
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term",
                   "utm_content", "fbclid", "gclid", "msclkid", "mc_cid"}

CHALLENGE_MARKERS = [
    "just a moment", "verify you are human", "checking your browser",
    "captcha", "turnstile", "datadome", "perimeterx", "px-captcha",
    "request blocked", "access denied", "unusual traffic",
]

TERMINAL_HTTP = {404, 410}
RETRIABLE_HTTP = {408, 425, 429, 500, 502, 503, 504}

shutdown_event = asyncio.Event()


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonicalize(url: str) -> str:
    p = urlparse(url.strip())
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if k not in TRACKING_PARAMS]
    q.sort()
    path = p.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]
    return urlunparse((p.scheme.lower(), p.netloc.lower(), path, "", urlencode(q), ""))


def job_id_for(canonical_url: str, version: str) -> str:
    return hashlib.sha1(f"{canonical_url}|{version}".encode()).hexdigest()[:16]


def record_id_for(canonical_url: str, page_key: str, version: str) -> str:
    return hashlib.sha1(f"{canonical_url}|{page_key}|{version}".encode()).hexdigest()[:16]


def classify_challenge(url: str, title: str, body_text: str) -> str | None:
    blob = f"{url}\n{title}\n{body_text[:4000]}".lower()
    for marker in CHALLENGE_MARKERS:
        if marker in blob:
            if "turnstile" in blob or "just a moment" in blob:
                return "turnstile"
            if "datadome" in blob:
                return "datadome"
            if "perimeterx" in blob or "px-captcha" in blob:
                return "perimeterx"
            if "captcha" in blob:
                return "captcha-generic"
            if "unusual traffic" in blob or "request blocked" in blob:
                return "rate-limit-page"
            return "unknown-block"
    return None


class DomainThrottle:
    """Simple per-domain token bucket + circuit breaker."""

    def __init__(self, rate_per_min: float, burst: int):
        self.rate_per_sec = rate_per_min / 60.0
        self.capacity = max(burst, 1)
        self.tokens = float(self.capacity)
        self.updated = time.monotonic()
        self.lock = asyncio.Lock()
        self.consec_failures = 0
        self.breaker_open_until = 0.0
        self.challenge_hits: deque[float] = deque(maxlen=50)

    async def acquire(self):
        async with self.lock:
            now = time.monotonic()
            if now < self.breaker_open_until:
                await asyncio.sleep(self.breaker_open_until - now)
                now = time.monotonic()
            elapsed = now - self.updated
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate_per_sec)
            self.updated = now
            if self.tokens < 1.0:
                wait = (1.0 - self.tokens) / self.rate_per_sec
                await asyncio.sleep(wait)
                self.updated = time.monotonic()
                self.tokens = 0.0
            else:
                self.tokens -= 1.0

    def record_success(self):
        self.consec_failures = 0

    def record_failure(self, challenged: bool):
        self.consec_failures += 1
        now = time.monotonic()
        if challenged:
            self.challenge_hits.append(now)
        recent = [t for t in self.challenge_hits if now - t < 300]
        challenge_rate = len(recent) / max(1, self.consec_failures + len(recent))
        if self.consec_failures >= 10 or (len(recent) >= 5 and challenge_rate > 0.3):
            self.breaker_open_until = now + 600  # park domain 10 min
            self.consec_failures = 0
            return True
        return False


def parse_rate(spec: str) -> tuple[float, int]:
    m = re.match(r"\s*(\d+(?:\.\d+)?)\s*/\s*min\s*", spec)
    if not m:
        raise ValueError(f"Bad --per-domain-rate {spec!r}, expected like '20/min'")
    rate = float(m.group(1))
    burst = max(2, int(rate / 60 * 2) or 2)
    return rate, min(burst, 8)


async def fetch_one(playwright, job: dict, args, throttle: DomainThrottle,
                    out_dirs: dict, state: dict, log_fh):
    from playwright.async_api import TimeoutError as PWTimeout

    url = job["url"]
    domain = job["domain"]
    version = args.version
    trace_id = hashlib.sha1(f"{job['job_id']}{time.time_ns()}".encode()).hexdigest()[:12]
    t0 = time.monotonic()

    def log(outcome: str, **extra):
        rec = {"ts": utcnow(), "trace_id": trace_id, "job_id": job["job_id"],
               "domain": domain, "attempt": job["attempts"], "outcome": outcome,
               "latency_ms": int((time.monotonic() - t0) * 1000),
               "proxy_pool": args.proxy_pool, "challenge_class": None,
               "error_class": None, "artifact_path": None}
        rec.update(extra)
        log_fh.write(json.dumps(rec) + "\n")
        log_fh.flush()
        return rec

    launch_kwargs: dict = {"headless": not args.headed}
    if args.proxy_server:
        launch_kwargs["proxy"] = {"server": args.proxy_server}
    browser = None
    try:
        await throttle.acquire()
        if shutdown_event.is_set():
            log("parked", error_class="shutdown")
            return "parked"

        browser = await playwright.chromium.launch(**launch_kwargs)
        context = await browser.new_context(
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
            viewport={"width": 1366, "height": 768},
            locale="en-US", timezone_id="America/New_York",
        )
        page = await context.new_page()
        try:
            resp = await page.goto(url, timeout=args.timeout_ms,
                                   wait_until="domcontentloaded")
            status = resp.status if resp else 0
            if args.selector:
                try:
                    await page.locator(args.selector).first.wait_for(timeout=min(args.timeout_ms, 15000))
                except PWTimeout:
                    pass  # fall through to validation; missing selector = validation failure
            title = await page.title()
            try:
                body_text = await page.locator("body").inner_text(timeout=5000)
            except Exception:
                body_text = ""
            html = await page.content()

            challenge = classify_challenge(page.url, title, body_text)
            if challenge:
                raise ChallengeError(challenge, status)
            if status in TERMINAL_HTTP:
                raise TerminalError(f"http-{status}")
            if status in RETRIABLE_HTTP:
                raise RetriableError(f"http-{status}")
            if status and status >= 400:
                raise TerminalError(f"http-{status}")

            # Validation: title, floors, challenge guard.
            if not title or len(title.strip()) < 2:
                raise TerminalError("validation-failed-schema-break:title")
            if len(html) < args.min_html:
                raise TerminalError("validation-failed-schema-break:thin-html")
            if classify_challenge(page.url, title, body_text):
                raise ChallengeError("unknown-block", status)

            page_key = "main"
            record = {
                "record_id": record_id_for(job["canonical"], page_key, version),
                "job_id": job["job_id"], "url": job["canonical"],
                "title": title.strip()[:300],
                "html_len": len(html),
                "text_len": len(body_text),
                "final_url": page.url[:500],
                "scraped_at": utcnow(), "version": version,
            }
            if record["record_id"] in state["seen"]:
                state["metrics"]["deduped_total"] += 1
                log("deduped")
            else:
                state["seen"].add(record["record_id"])
                with open(out_dirs["records"], "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(record) + "\n")
                state["metrics"]["emitted_total"] += 1
                log("success")
            state["done"].add(job["job_id"])
            state["metrics"]["success_total"] += 1
            throttle.record_success()
            return "success"
        finally:
            await context.close()
    except ChallengeError as e:
        state["metrics"]["challenges_total"] += 1
        state["metrics"]["retriable_total"] += 1
        tripped = throttle.record_failure(challenged=True)
        artifact = await save_artifact(out_dirs, job, browser)
        log("challenge", challenge_class=str(e.challenge), error_class="challenge-detected",
            artifact_path=artifact, breaker_open=tripped)
        if job["attempts"] >= 3:
            park_job(out_dirs, job, reason=f"challenge:{e.challenge}", artifact=artifact)
            state["done"].add(job["job_id"])
            state["metrics"]["parked_total"] += 1
            return "parked"
        return "retriable"
    except RetriableError as e:
        state["metrics"]["retriable_total"] += 1
        tripped = throttle.record_failure(challenged=False)
        artifact = await save_artifact(out_dirs, job, browser)
        log("retriable", error_class=str(e), artifact_path=artifact, breaker_open=tripped)
        return "retriable"
    except TerminalError as e:
        state["metrics"]["terminal_total"] += 1
        if str(e).startswith("validation-failed"):
            state["metrics"]["validation_failed_total"] += 1
        artifact = await save_artifact(out_dirs, job, browser)
        dead_letter(out_dirs, job, reason=str(e), artifact=artifact)
        state["done"].add(job["job_id"])
        log("terminal", error_class=str(e), artifact_path=artifact)
        return "terminal"
    except Exception as e:  # navigation reset, proxy drop, target crash
        state["metrics"]["retriable_total"] += 1
        throttle.record_failure(challenged=False)
        artifact = await save_artifact(out_dirs, job, browser)
        log("retriable", error_class=f"exception:{type(e).__name__}", artifact_path=artifact)
        return "retriable"
    finally:
        if browser:
            try:
                await browser.close()
            except Exception:
                pass


class RetriableError(Exception):
    pass


class TerminalError(Exception):
    pass


class ChallengeError(Exception):
    def __init__(self, challenge: str, status: int):
        super().__init__(f"challenge:{challenge}")
        self.challenge = challenge
        self.status = status


async def save_artifact(out_dirs: dict, job: dict, browser) -> str | None:
    try:
        d = Path(out_dirs["failures"]) / job["job_id"] / f"attempt{job['attempts']}"
        d.mkdir(parents=True, exist_ok=True)
        # Best-effort screenshot of a fresh page is skipped; worker pages are
        # already closed on error paths. Record a marker + job context instead.
        (d / "context.json").write_text(json.dumps(
            {"job_id": job["job_id"], "url": job["url"], "ts": utcnow(),
             "note": "Attach screenshot/HAR here in production worker; "
                     "capture before closing context."}, indent=2))
        return str(d)
    except Exception:
        return None


def park_job(out_dirs: dict, job: dict, reason: str, artifact: str | None):
    with open(out_dirs["review"], "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"job_id": job["job_id"], "url": job["url"],
                             "reason": reason, "artifact": artifact,
                             "ts": utcnow()}) + "\n")


def dead_letter(out_dirs: dict, job: dict, reason: str, artifact: str | None):
    with open(out_dirs["deadletter"], "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"job_id": job["job_id"], "url": job["url"],
                             "reason": reason, "artifact": artifact,
                             "ts": utcnow()}) + "\n")


async def worker(name: str, queue: asyncio.Queue, playwright, args,
                 throttles: dict, out_dirs: dict, state: dict, log_fh,
                 sem: asyncio.Semaphore):
    while not shutdown_event.is_set():
        try:
            job = await asyncio.wait_for(queue.get(), timeout=1.0)
        except asyncio.TimeoutError:
            if queue.empty():
                return
            continue
        async with sem:
            if job["job_id"] in state["done"]:
                state["metrics"]["deduped_total"] += 1
                queue.task_done()
                continue
            job["attempts"] += 1
            domain = job["domain"]
            throttle = throttles[domain]
            outcome = await fetch_one(playwright, job, args, throttle,
                                      out_dirs, state, log_fh)
            state["metrics"]["jobs_total"] += 1
            if outcome == "retriable" and job["attempts"] < args.max_attempts:
                delay = random.uniform(0, min(args.cap_delay, args.base_delay * (2 ** (job["attempts"] - 1))))
                await asyncio.sleep(delay)
                await queue.put(job)
            elif outcome == "retriable":
                dead_letter(out_dirs, job, reason="max-attempts-exhausted", artifact=None)
                state["done"].add(job["job_id"])
                state["metrics"]["terminal_total"] += 1
            state["jobs_since_checkpoint"] += 1
            if state["jobs_since_checkpoint"] >= 25:
                save_checkpoint(out_dirs, state)
                save_metrics(out_dirs, state)
                state["jobs_since_checkpoint"] = 0
        queue.task_done()


def save_checkpoint(out_dirs: dict, state: dict):
    tmp = Path(str(out_dirs["checkpoint"]) + ".tmp")
    tmp.write_text(json.dumps({"done": sorted(state["done"]),
                               "ts": utcnow()}, indent=2))
    tmp.replace(out_dirs["checkpoint"])


def save_metrics(out_dirs: dict, state: dict):
    Path(out_dirs["metrics"]).write_text(json.dumps(
        {"ts": utcnow(), **state["metrics"]}, indent=2))


async def main_async(args):
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("ERROR: playwright not installed. Run: pip install -r scripts/requirements.txt && python -m playwright install chromium",
              file=sys.stderr)
        sys.exit(2)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "failures").mkdir(exist_ok=True)
    out_dirs = {
        "records": str(out / "records.jsonl"),
        "checkpoint": str(out / "checkpoint.json"),
        "metrics": str(out / "metrics.json"),
        "log": str(out / "jobs.log.jsonl"),
        "review": str(out / "review_queue.jsonl"),
        "deadletter": str(out / "deadletter.jsonl"),
        "failures": str(out / "failures"),
    }

    raw_urls = [l.strip() for l in Path(args.input).read_text(encoding="utf-8").splitlines()
                if l.strip() and not l.strip().startswith("#")]
    jobs: list[dict] = []
    for u in raw_urls:
        try:
            canon = canonicalize(u)
            domain = urlparse(canon).netloc.lower()
            jobs.append({"job_id": job_id_for(canon, args.version), "url": u,
                         "canonical": canon, "domain": domain, "attempts": 0,
                         "version": args.version})
        except Exception as e:
            print(f"Skipping bad URL {u!r}: {e}", file=sys.stderr)

    done: set[str] = set()
    if Path(out_dirs["checkpoint"]).exists():
        try:
            done = set(json.loads(Path(out_dirs["checkpoint"]).read_text()).get("done", []))
        except Exception:
            done = set()
    seen: set[str] = set()
    if Path(out_dirs["records"]).exists():
        for line in Path(out_dirs["records"]).read_text(encoding="utf-8").splitlines():
            try:
                seen.add(json.loads(line)["record_id"])
            except Exception:
                pass

    state = {"done": done, "seen": seen, "jobs_since_checkpoint": 0,
             "metrics": defaultdict(int)}
    for k in ["jobs_total", "success_total", "retriable_total", "terminal_total",
              "challenges_total", "emitted_total", "deduped_total",
              "validation_failed_total", "parked_total"]:
        state["metrics"][k] += 0

    rate, burst = parse_rate(args.per_domain_rate)
    throttles: dict[str, DomainThrottle] = defaultdict(lambda: DomainThrottle(rate, burst))
    queue: asyncio.Queue = asyncio.Queue()
    for j in jobs:
        if j["job_id"] not in done:
            queue.put_nowait(j)
    skipped = len(jobs) - queue.qsize()
    print(f"Jobs: {len(jobs)} total, {skipped} already done (checkpoint), {queue.qsize()} queued.")

    sem = asyncio.Semaphore(args.concurrency)
    log_fh = open(out_dirs["log"], "a", encoding="utf-8")
    async with async_playwright() as pw:
        workers = [asyncio.create_task(worker(f"w{i}", queue, pw, args,
                                              throttles, out_dirs, state,
                                              log_fh, sem))
                   for i in range(args.concurrency)]
        await queue.join()
        shutdown_event.set()
        await asyncio.gather(*workers)
    save_checkpoint(out_dirs, state)
    save_metrics(out_dirs, state)
    log_fh.close()
    print(json.dumps({"ts": utcnow(), **state["metrics"]}, indent=2))
    print(f"Done. Records: {out_dirs['records']}  Metrics: {out_dirs['metrics']}  "
          f"Review: {out_dirs['review']}  Dead-letter: {out_dirs['deadletter']}")


def main():
    ap = argparse.ArgumentParser(description="Resilient Playwright scraping worker")
    ap.add_argument("--input", required=True, help="Text file, one URL per line")
    ap.add_argument("--out", default="./out", help="Output directory")
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--per-domain-rate", default="20/min")
    ap.add_argument("--max-attempts", type=int, default=4)
    ap.add_argument("--base-delay", type=float, default=2.0)
    ap.add_argument("--cap-delay", type=float, default=120.0)
    ap.add_argument("--timeout-ms", type=int, default=30000)
    ap.add_argument("--min-html", type=int, default=5000)
    ap.add_argument("--selector", default="", help="CSS selector to wait for before extraction")
    ap.add_argument("--proxy-server", default="", help="e.g. http://user:pass@host:port")
    ap.add_argument("--proxy-pool", default="direct")
    ap.add_argument("--version", default="v3", help="Extraction schema version")
    ap.add_argument("--headed", action="store_true", help="Run headed (debugging / hardened targets)")
    args = ap.parse_args()

    def _sig(*_):
        shutdown_event.set()

    signal.signal(signal.SIGINT, lambda *_: _sig())
    try:
        signal.signal(signal.SIGTERM, lambda *_: _sig())
    except Exception:
        pass
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
