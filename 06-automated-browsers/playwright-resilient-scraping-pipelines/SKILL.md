---
name: playwright-resilient-scraping-pipelines
description: Design and operate resilient Playwright scraping pipelines with queued idempotent jobs, per-domain throttling, backoff retries, proxy rotation, challenge triage, and structured observability. Use when the user asks to build, fix, scale, or productionize a Playwright/Puppeteer scraper, handle blocks/CAPTCHAs/429s, add retries/proxies/logging/metrics, resume failed crawls, or run long-lived scraping reliably.
compatibility: Python 3.10+ with playwright installed and browsers downloaded; Node.js 18+ optional for JS pipelines; network egress for targets and proxies; POSIX shell.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-scraping
---

# Playwright Resilient Scraping Pipelines

Build scraping pipelines that survive the real web: rate limits, layout drift, bans, CAPTCHAs, proxy failures, and worker crashes — without losing data, burning budgets, or hammering targets.

Optimize simultaneously for:

- politeness to targets and proxy health
- resumability with no duplicate emission
- debuggability via logs, traces, and failure artifacts
- data quality via validation and deduping
- cost control per 1k pages

Do not add stealth or scale merely because it is technically impressive. Every throttle, retry, proxy, and concurrency choice must trace to a freshness commitment, politeness budget, or observed failure signal.

## Use Cases

### Continuous price and availability monitoring

Trigger: user says "monitor prices daily", "track availability", "keep this dataset fresh", "my price scraper keeps getting blocked".

Steps:

1. Model each product URL as an idempotent job with extraction version.
2. Enforce per-domain throttle plus concurrency cap.
3. Apply backoff retries, challenge triage, and proxy rotation.
4. Validate records, dedupe by stable ID, checkpoint progress.
5. Emit metrics and alerts on success-rate or challenge-rate shifts.

Result: Daily refresh that degrades gracefully during ban waves instead of dying silently.

### One-off research crawl that must not lose progress

Trigger: user says "scrape 50k URLs", "crawl this directory", "resume my failed crawl", "avoid duplicates on re-run".

Steps:

1. Canonicalize URLs and assign stable job IDs.
2. Run workers over a queue with lease timeouts and dead-letter handling.
3. Checkpoint every success; resume from checkpoint on restart.
4. Capture screenshot plus HAR on failure for triage.
5. Validate and dedupe before writing final JSONL.

Result: Killable, resumable crawl with exactly-once emission and an audit trail.

### Hardened scraping for defended targets

Trigger: user says "Cloudflare blocks my Playwright", "DataDome challenge", "handle CAPTCHAs", "make my scraper undetectable but safe".

Steps:

1. Diagnose detection with fingerprint checks and challenge classification.
2. Apply layered context hardening and behavioral pacing.
3. Isolate logins with sticky sessions; rotate otherwise.
4. Back off and park domains on repeated challenges; queue for human review where permitted.
5. Prefer API capture or official APIs when DOM scraping becomes hostile.

Result: Higher success rate with explicit backoff and a defensible, API-first fallback path.

Ask yourself before starting:

- What freshness does the user actually need?
- What is the politeness budget per domain?
- Which failures are retriable vs terminal?
- Where do jobs, checkpoints, and records live?
- What signals prove a run was healthy?

## Core Output Requirements

Every pipeline you produce must include:

- Job model: canonical URL, job ID, extraction version, priority, attempts, lease.
- Throttle: per-domain rate plus max concurrent contexts.
- Retry policy: classified errors, backoff with jitter, max attempts, circuit breaker.
- Proxy policy: pool, rotation rule, sticky-session rule, quarantine rule.
- Challenge handling: detection strings, classification, backoff, park-and-review path.
- Validation: required fields, min-content checks, schema version.
- Deduping: stable record ID plus cross-run seen-store.
- Checkpointing: append-only successes plus done-set for resume.
- Observability: JSON logs with correlation IDs, counters per domain/outcome, failure artifacts.
- Runbook: what to do on ban wave, layout change, proxy failure, cost spike.

Never emit a scraper that loops URLs with bare `try/except: pass`, sleeps instead of waits, treats a challenge page as success, or writes records without IDs and validation.

## Phase 1 — Define Jobs and Success

Pin the contract before writing browser code.

1. Canonicalize inputs: strip tracking params, normalize trailing slashes, lowercase host, sort query keys that do not change content.
2. Assign `job_id = sha1(canonical_url + "|" + extraction_version)[:16]` and `record_id` from the same scheme plus page-level key (SKU, article slug) when available.
3. Define done as validated record written, not page fetched. A 200 with a CAPTCHA is not success.
4. Set budgets: max pages per domain per minute, max concurrent contexts, max retries, max cost per 1k pages.
5. Decide storage: `./out/records.jsonl` for records, `./out/checkpoint.json` for done IDs, `./out/failures/` for artifacts.

Example job record:

```json
{"job_id": "a1b2c3d4e5f60718", "url": "https://example.com/p/123", "domain": "example.com", "priority": 5, "attempts": 0, "version": "v3"}
```

If the brief does not pin freshness or scope, pin it yourself and state the choice: "Refreshing 5k product URLs daily, max 20 req/min per domain, 3 workers."

## Phase 2 — Build the Browser Worker

Use isolated contexts, deterministic waits, and guaranteed cleanup.

1. Launch one browser per worker, many contexts per browser. Never share one context across accounts or geographies.
2. Create each context with aligned identity: user-agent, viewport, locale, timezone, geolocation, color scheme. Read `references/proxy-and-challenge-triage.md` before enabling stealth extras.
3. Navigate with explicit timeouts: `timeout=30000`, `wait_until="domcontentloaded"` by default, upgrade to selector waits for known targets. Avoid `networkidle` unless the target is a standard SPA and you set a hard cap.
4. Wait for the extraction selector, not a sleep. Use `locator.wait_for()` plus assertion retries.
5. Extract DOM plus API evidence: capture useful XHR JSON via response listeners when it yields cleaner records than DOM parsing.
6. Close contexts on challenge, error, or account switch. Recycle the browser every N jobs (start with 100) to bound memory growth.
7. Wrap every job in `try/finally` that closes page and context and releases the throttle lease.

Run the bundled worker as a starting point:

```bash
pip install -r scripts/requirements.txt
python -m playwright install chromium
python scripts/resilient_scrape.py --input urls.txt --out ./out --concurrency 3 --per-domain-rate 20/min --max-attempts 4
```

Expected success: `records.jsonl` grows with validated JSON, `checkpoint.json` tracks done IDs, `metrics.json` shows per-domain success/failure/challenge counts.

## Phase 3 — Throttle, Retry, and Break Circuits

Read `references/queue-and-throttle-patterns.md` before tuning numbers.

1. Enforce per-domain token buckets plus a global concurrency semaphore. Acquire domain token before creating a context.
2. Classify every failure:
   - Retriable: timeout, navigation reset, 429, 502/503/504, challenge page, proxy disconnect.
   - Terminal: 404/410, permanent IP ban after cooldown, login revoked, schema-breaking layout change.
3. Retry retriable with exponential backoff and full jitter: `sleep = random(0, min(cap, base * 2^attempt))` with `base=2s`, `cap=120s`, `max_attempts=4` as defaults.
4. Trip a per-domain circuit breaker after 10 consecutive retriable failures or 30% challenge rate over 5 minutes: halve concurrency, double delays, park new leases for 10 minutes.
5. Send terminal failures to dead-letter with reason, artifact path, and last HTML snippet hash. Never retry terminal failures in the hot loop.

If throughput collapses, reduce concurrency first, then increase delays. Do not add proxies to fix a retry storm you created.

## Phase 4 — Proxies and Challenge Triage

1. Default to no proxy for a handful of polite pages. Add proxies only when you have measured blocks or need geo coverage.
2. Use datacenter pools for tolerant targets, residential for sensitive or geo-locked targets, mobile only when justified by ban data and budget.
3. Keep sticky sessions for logins and multi-step flows (same proxy + same context + same storage state). Rotate otherwise per N requests or per job.
4. Detect challenges by URL, title, and body signals: `captcha`, `turnstile`, `datadome`, `perimeterx`, `just a moment`, `verify you are human`, `request blocked`, plus status 403 with challenge markers. Log the classifier hit.
5. On challenge: close context, back off the domain, rotate egress, record artifact, increment `challenges_total{domain}`. After 3 challenges for one job, park it for human review instead of burning more egress.
6. Quarantine egress showing 403/CHALLENGE spikes or latency shifts. Probe with a known-easy URL before returning it to rotation.
7. Prefer de-escalation: reduce scope, slow down, switch to API capture, or stop and recommend the official API. Document the decision in the run log.

See `references/proxy-and-challenge-triage.md` for detector snippets and pool layouts.

## Phase 5 — Validate, Dedupe, and Checkpoint

Read `references/observability-and-data-quality.md` when defining schemas.

1. Validate every record before writing: required fields present, types correct, price/IDs in range, body length above floor, no challenge markers in extracted text.
2. Compute `record_id` deterministically. Skip write if `record_id` is already in the seen-store, but still mark the job done.
3. Append successes to `records.jsonl` immediately. Fsync the checkpoint every 25 jobs and on graceful shutdown.
4. On worker kill or crash, resume by loading `checkpoint.json` done-set and skipping done jobs. Leases older than 10 minutes return to queued.
5. Track `emitted_total`, `deduped_total`, `validation_failed_total` separately. A silent rise in `validation_failed_total` is a layout-change alarm.

Example validated record:

```json
{"record_id": "9f2c7a1b4e8d03aa", "job_id": "a1b2c3d4e5f60718", "url": "https://example.com/p/123", "title": "Acme Kettle 1.7L", "price": 49.99, "currency": "USD", "scraped_at": "2026-09-14T11:00:00Z", "version": "v3"}
```

## Phase 6 — Observe and Alert

1. Log one JSON line per job with `job_id`, `domain`, `attempt`, `outcome`, `latency_ms`, `proxy_pool`, `challenge_class`, `artifact_path`, and `trace_id`. Never log passwords, full cookies, or raw PII.
2. Keep counters: `jobs_total`, `success_total`, `retriable_total`, `terminal_total`, `challenges_total`, `proxy_failures_total`, `cost_usd_estimate`. Scrape or print them every minute.
3. Capture on failure only: screenshot plus HTML snippet hash always, HAR when network debugging is needed, video only for flake reproduction. Redact inputs and cap retention (default 14 days).
4. Alert on: success rate below 85% over 15 minutes, challenge rate above 10% over 15 minutes, queue age above SLA, dead-letter growth, cost above budget. Page on ban-wave pattern (multiple domains spiking together).
5. Ship a one-page run summary at end of run: totals, per-domain table, top failure reasons, top challenged URLs, cost estimate, next actions.

## Examples

### Example 1: Resumable 5k-URL research crawl

User says: "Scrape these 5k category URLs, resume if it dies, no duplicates."

Actions:

1. Canonicalize list into `urls.txt`, generate job IDs.
2. Run `python scripts/resilient_scrape.py --input urls.txt --out ./out --concurrency 4 --per-domain-rate 30/min --max-attempts 4`.
3. Kill and rerun mid-way to prove resume skips done IDs.
4. Inspect `metrics.json` and `failures/` for top errors.

Result: `records.jsonl` with validated unique records, `checkpoint.json` with done IDs, reruns emit zero duplicates.

### Example 2: Defended target with challenges

User says: "Target throws Cloudflare Turnstile every 20 pages, don't get us banned."

Actions:

1. Lower to `--concurrency 2 --per-domain-rate 12/min`, enable challenge detector.
2. Recycle context on challenge, rotate proxy, back off domain 5 minutes after 3 hits.
3. Park repeatedly challenged jobs to `review_queue.jsonl` with artifacts.
4. Recommend API or reduced scope if challenge rate stays above 15%.

Result: Stable trickle with explicit parks and artifacts instead of a subnet-wide ban.

## Troubleshooting

### Success rate collapses suddenly

Cause: Layout change, new challenge, proxy pool burned, or target deploy.

Fix:

1. Open latest `failures/` screenshot and HTML hash. Compare selector vs live DOM.
2. Check `challenges_total` vs `validation_failed_total`. Challenge spike means triage path; validation spike means extractor update.
3. Halve concurrency, extend backoff cap, quarantine suspect egress.
4. Pin a fix, bump extraction version, requeue only affected job IDs.

### Retry storm and 429 flood

Cause: Too many workers, no jitter, or breaker disabled.

Fix:

1. Stop workers, drain leases, enable full jitter and breaker.
2. Set per-domain rate to half the last known-good value.
3. Add `Retry-After` honoring when the header is present.
4. Re-enable one worker, then scale only when 429s stay near zero for 10 minutes.

### Logins drop mid-flow

Cause: Rotating proxy or context inside an authenticated flow.

Fix:

1. Pin login flows to sticky proxy plus dedicated context plus persisted `storage_state.json`.
2. Refresh tokens before expiry; re-login on 401 once, then park on repeat.
3. Isolate accounts: one context per account, never shared.

### Duplicates after resume

Cause: Marking done before validated write, or nondeterministic record IDs.

Fix:

1. Mark done only after append plus fsync.
2. Derive `record_id` from canonical URL plus stable page key plus version.
3. Rebuild seen-store from `records.jsonl` on startup.

### Workers OOM or slow down over hours

Cause: Context leak, unclosed pages, video left on, browser never recycled.

Fix:

1. Enforce `try/finally` close, recycle browser every 100 jobs, cap concurrency by RAM (roughly 1 context per 300-500MB headroom).
2. Disable video except for repro runs. Cap HAR to failures.
3. Add memory guard that pauses new leases above 80% RSS.

## Checklists

Copy from `assets/pipeline-checklists.md` into the delivery PR. Do not ship without all boxes checked or explicitly waived with a reason.

- Pre-flight: scope, freshness, budgets, storage, PII handling, ToS review.
- Throttle-and-retry: rates, caps, jitter, breaker, dead-letter.
- Proxy-and-challenge: pools, stickiness, detectors, parks, quarantine.
- Observability: logs, metrics, artifacts, alerts, run summary.
- Data-quality-and-resume: schema, IDs, dedupe, checkpoint, restore test.

## Decision Heuristic

Before adding concurrency, stealth, or proxies, ask:

1. What freshness SLA requires more speed?
2. What politeness or cost budget caps it?
3. What failure signal justifies this escalation?
4. What happens on challenge, ban, or layout change?
5. What happens on worker kill?
6. What proves data quality did not regress?
7. What is the API-first alternative?

If the main justification is "faster", prove the target and budget tolerate it first.

## Anti-Patterns

Avoid fixed sleeps instead of waits, single shared contexts, hardcoded credentials, unbounded retries without jitter, rotating egress inside logins, treating challenge HTML as success, silent field drops, duplicate emission on resume, PII in logs/screenshots, missing checkpoints, and stealth escalation without backoff and human-review escape hatches.

## Bundled References

Read `references/queue-and-throttle-patterns.md` when modeling jobs, queues, throttles, retries, and breakers.
Read `references/proxy-and-challenge-triage.md` when choosing pools, hardening contexts, detecting challenges, or handling logins.
Read `references/observability-and-data-quality.md` when defining schemas, IDs, logs, metrics, artifacts, and alerts.
Run `scripts/resilient_scrape.py` as the reference worker; adapt selectors and schema per target but keep its throttle, retry, checkpoint, and observability skeleton intact.
Copy `assets/pipeline-checklists.md` into every delivery.
