#!/usr/bin/env python3
"""Score blind proxy trials from JSONL outcomes (stdlib only)."""
import argparse, json
from collections import defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True, help="JSONL: provider, ok, ms, banned")
    args = ap.parse_args()
    agg = defaultdict(lambda: {"n": 0, "ok": 0, "ms": [], "ban": 0})
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        a = agg[r.get("provider", "?")]
        a["n"] += 1
        a["ok"] += 1 if r.get("ok") else 0
        a["ban"] += 1 if r.get("banned") else 0
        if isinstance(r.get("ms"), (int, float)):
            a["ms"].append(r["ms"])
    for p, a in sorted(agg.items()):
        ms = sorted(a["ms"])
        p95 = ms[int(0.95 * len(ms))] if ms else 0
        print("%s n=%d success=%.1f%% p95=%dms bans=%d" % (
            p, a["n"], 100 * a["ok"] / max(1, a["n"]), p95, a["ban"]))
    print("unblind labels only after scoring; weight per your scorecard.")

if __name__ == "__main__":
    main()
