#!/usr/bin/env python3
"""Batch data-quality check: fills, ranges, dup keys (stdlib only)."""
import argparse, json
from collections import Counter
from datetime import datetime, timezone

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--key", default="record_id")
    ap.add_argument("--fields", default="")
    args = ap.parse_args()
    want = [f for f in args.fields.split(",") if f]
    n, keys, fills = 0, Counter(), Counter()
    lags = []
    now = datetime.now(timezone.utc).timestamp()
    for line in open(args.inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        n += 1
        keys[str(r.get(args.key))] += 1
        for f in want:
            if r.get(f) not in (None, ""):
                fills[f] += 1
        fa = r.get("fetched_at")
        try:
            lags.append(now - datetime.fromisoformat(str(fa).replace("Z", "+00:00")).timestamp())
        except Exception:
            pass
    print("records=%d dup_keys=%d" % (n, sum(1 for c in keys.values() if c > 1)))
    for f in want:
        print("  fill %-24s %.1f%%" % (f, 100 * fills[f] / max(1, n)))
    if lags:
        lags.sort()
        print("lag_s p50=%.0f p95=%.0f" % (lags[len(lags) // 2], lags[int(len(lags) * 0.95)]))
    print("gate serve promotion on these numbers.")

if __name__ == "__main__":
    main()
