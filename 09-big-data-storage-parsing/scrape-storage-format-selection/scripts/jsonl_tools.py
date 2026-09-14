#!/usr/bin/env python3
"""Profile + sample JSONL files (stdlib only)."""
import argparse, json
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--sample", type=int, default=0)
    ap.add_argument("--keys", action="store_true")
    args = ap.parse_args()
    n, bad, keys = 0, 0, Counter()
    fh = open(args.file, encoding="utf-8")
    for line in fh:
        line = line.strip()
        if not line:
            continue
        n += 1
        try:
            r = json.loads(line)
        except Exception:
            bad += 1
            continue
        if isinstance(r, dict):
            keys.update(r.keys())
        if args.sample and n <= args.sample:
            print(json.dumps(r)[:300])
    print("lines=%d bad_json=%d" % (n, bad))
    if args.stats or args.keys:
        for k, c in keys.most_common(40):
            print("  %-30s %d (%.0f%%)" % (k, c, 100 * c / max(1, n)))

if __name__ == "__main__":
    main()
