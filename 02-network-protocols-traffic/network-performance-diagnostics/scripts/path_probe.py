#!/usr/bin/env python3
"""Path latency/TTFB percentiles over repeated fetches (stdlib only)."""
import argparse, json, statistics, time, urllib.request

def pct(xs, p):
    return statistics.quantiles(sorted(xs), n=100)[min(99, max(0, p - 1))] if xs else 0

def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 path-probe"})
    t0 = time.monotonic()
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        first = (time.monotonic() - t0) * 1000
        n = len(r.read(65536))
        total = (time.monotonic() - t0) * 1000
        return {"ttfb_ms": round(first, 1), "total_ms": round(total, 1), "bytes": n, "status": r.status}
    except Exception as e:
        return {"error": str(e)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--samples", type=int, default=30)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--pause", type=float, default=0.5)
    args = ap.parse_args()
    rows = []
    for _ in range(args.samples):
        rows.append(fetch(args.url, args.timeout))
        time.sleep(args.pause)
    ok = [r for r in rows if "ttfb_ms" in r]
    print(json.dumps({
        "url": args.url, "samples": len(rows), "errors": len(rows) - len(ok),
        "ttfb_p50": round(pct([r["ttfb_ms"] for r in ok], 50), 1),
        "ttfb_p95": round(pct([r["ttfb_ms"] for r in ok], 95), 1),
        "total_p95": round(pct([r["total_ms"] for r in ok], 95), 1),
    }, indent=2))

if __name__ == "__main__":
    main()
