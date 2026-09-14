#!/usr/bin/env python3
"""Attribute LLM spend from usage JSONL (stdlib only)."""
import argparse, json
from collections import defaultdict

RATES = {"small": (0.15, 0.60), "large": (3.0, 12.0)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--usage", required=True, help="JSONL: task, model_tier, in_tok, out_tok")
    args = ap.parse_args()
    agg = defaultdict(lambda: {"n": 0, "cost": 0.0})
    for line in open(args.usage, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        tier = r.get("model_tier", "small")
        ri, ro = RATES.get(tier, RATES["small"])
        cost = (r.get("in_tok", 0) / 1e6 * ri) + (r.get("out_tok", 0) / 1e6 * ro)
        a = agg[r.get("task", "?")]
        a["n"] += 1
        a["cost"] += cost
    total = sum(a["cost"] for a in agg.values())
    for t, a in sorted(agg.items(), key=lambda x: -x[1]["cost"]):
        print("%-24s calls=%d cost=$%.2f/1k=$%.2f" % (t, a["n"], a["cost"], 1000 * a["cost"] / max(1, a["n"])))
    print("total=$%.2f — edit RATES to your price sheet." % total)

if __name__ == "__main__":
    main()
