#!/usr/bin/env python3
"""Summarize test-run artifacts dir (stdlib only)."""
import argparse, os
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()
    kinds, total = Counter(), 0
    biggest = []
    for root, _, files in os.walk(args.dir):
        for f in files:
            p = os.path.join(root, f)
            try:
                sz = os.path.getsize(p)
            except OSError:
                continue
            total += sz
            kinds[os.path.splitext(f)[1] or "noext"] += 1
            biggest.append((sz, p))
    print("files: %d bytes: %.1fMB" % (sum(kinds.values()), total / 1e6))
    for k, n in kinds.most_common(10):
        print("  %s: %d" % (k, n))
    for sz, p in sorted(biggest)[-5:]:
        print("  big: %.1fMB %s" % (sz / 1e6, p[-100:]))
    print("policy hint: failures-only capture, 14-30d retention, purge job scheduled.")

if __name__ == "__main__":
    main()
