#!/usr/bin/env python3
"""Score egress health from JSONL outcomes (stdlib only)."""
import argparse, json
from collections import defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True, help="JSONL: egress, ok, ms, banned")
    args = ap.parse_args()
    agg = defaultdict(lambda: {"n": 0, "ok": 0, "ms": [], "ban": 0})
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        a = agg[r.get("egress", "?")]
        a["n"] += 1
        a["ok"] += 1 if r.get("ok") else 0
        a["ban"] += 1 if r.get("banned") else 0
        if isinstance(r.get("ms"), (int, float)):
            a["ms"].append(r["ms"])
    rows = []
    for e, a in agg.items():
        succ = a["ok"] / max(1, a["n"])
        score = 100 * succ - 10 * a["ban"]
        ms = sorted(a["ms"])
        p95 = ms[int(0.95 * len(ms))] if ms else 0
        rows.append((score, e, a["n"], succ, p95, a["ban"]))
    for score, e, n, succ, p95, ban in sorted(rows):
        state = "QUARANTINE" if score < 50 else ("WARN" if score < 70 else "active")
        print("%-24s score=%5.1f n=%d succ=%.0f%% p95=%dms bans=%d %s" % (e, score, n, 100 * succ, p95, ban, state))

if __name__ == "__main__":
    main()
