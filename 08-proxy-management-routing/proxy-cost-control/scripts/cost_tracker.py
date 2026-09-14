#!/usr/bin/env python3
"""Unit cost per pool from JSONL outcomes (stdlib only)."""
import argparse, json
from collections import defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True, help="JSONL: pool, ok")
    ap.add_argument("--rate", type=float, default=3.5, help="cost per 1k requests")
    args = ap.parse_args()
    agg = defaultdict(lambda: {"n": 0, "ok": 0})
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        a = agg[r.get("pool", "?")]
        a["n"] += 1
        a["ok"] += 1 if r.get("ok") else 0
    for pool, a in sorted(agg.items()):
        spend = a["n"] / 1000 * args.rate
        unit = spend / max(1, a["ok"]) * 1000
        print("%-20s req=%d succ=%d spend=$%.2f per1k-succ=$%.2f" % (pool, a["n"], a["ok"], spend, unit))
    print("budget per1k-succ per pool; alert 80/100; fix retries + types first.")

if __name__ == "__main__":
    main()
