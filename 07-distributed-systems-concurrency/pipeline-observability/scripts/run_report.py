#!/usr/bin/env python3
"""Summarize JSONL run logs: counts, tails, top errors (stdlib only)."""
import argparse, json
from collections import Counter

def pct(xs, q):
    if not xs:
        return 0
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True)
    args = ap.parse_args()
    lv, durs, errs, stages = Counter(), [], Counter(), Counter()
    n = 0
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        n += 1
        lv[r.get("level", "?")] += 1
        stages[r.get("stage", "?")] += 1
        if isinstance(r.get("dur_ms"), (int, float)):
            durs.append(r["dur_ms"])
        if r.get("level") == "ERROR":
            errs[str(r.get("error_class", r.get("msg", "?")))[:80]] += 1
    print("events=%d levels=%s" % (n, dict(lv)))
    print("stages=%s" % dict(stages))
    print("dur_ms p50=%.0f p95=%.0f p99=%.0f" % (pct(durs, .5), pct(durs, .95), pct(durs, .99)))
    print("top errors:")
    for e, c in errs.most_common(8):
        print("  %dx %s" % (c, e))
    print("error_rate=%.2f%%" % (100 * lv.get("ERROR", 0) / max(1, n)))

if __name__ == "__main__":
    main()
