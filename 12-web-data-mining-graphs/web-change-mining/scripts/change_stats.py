#!/usr/bin/env python3
"""Change rates per class from fetch history JSONL (stdlib only)."""
import argparse, json
from collections import defaultdict
from datetime import datetime

def ts(s):
    return datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--history", required=True, help="JSONL: url, class, fetched_at, hash")
    args = ap.parse_args()
    last, agg = {}, defaultdict(lambda: {"urls": set(), "changes": 0, "span": [1e18, 0]})
    for line in open(args.history, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        u, cl = r.get("url"), r.get("class", "?")
        try:
            t = ts(r.get("fetched_at"))
        except Exception:
            continue
        a = agg[cl]
        a["urls"].add(u)
        a["span"][0] = min(a["span"][0], t)
        a["span"][1] = max(a["span"][1], t)
        if u in last and last[u] != r.get("hash"):
            a["changes"] += 1
        last[u] = r.get("hash")
    for cl, a in sorted(agg.items()):
        days = max(1 / 24, (a["span"][1] - a["span"][0]) / 86400)
        rate = a["changes"] / max(1, len(a["urls"])) / days
        print("%-20s urls=%d changes/day/url=%.3f suggest=%s" % (
            cl, len(a["urls"]), rate,
            "hourly" if rate > 1 else ("daily" if rate > 0.2 else "weekly+")))

if __name__ == "__main__":
    main()
