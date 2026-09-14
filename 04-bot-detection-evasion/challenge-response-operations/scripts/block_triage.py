#!/usr/bin/env python3
"""Triage blocks/challenges from JSONL logs (stdlib only)."""
import argparse, json
from collections import Counter, defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True)
    args = ap.parse_args()
    by_dom = defaultdict(Counter)
    total = Counter()
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        d = r.get("domain", "?")
        o = r.get("outcome", "?")
        if r.get("challenge_class"):
            o = "challenge:" + str(r["challenge_class"])
        by_dom[d][o] += 1
        total[o] += 1
    for d, c in sorted(by_dom.items()):
        n = sum(c.values())
        ch = sum(v for k, v in c.items() if str(k).startswith("challenge"))
        print("%s: n=%d challenge=%.1f%% top=%s" % (d, n, 100 * ch / n, c.most_common(3)))
        if ch / n > 0.3:
            print("  ACTION: trip breaker, park domain, canary later")
        elif ch / n > 0.1:
            print("  ACTION: halve concurrency, watch")
    print("total outcomes: %s" % dict(total.most_common(6)))

if __name__ == "__main__":
    main()
