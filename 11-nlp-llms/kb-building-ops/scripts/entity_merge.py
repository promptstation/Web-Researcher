#!/usr/bin/env python3
"""Normalize + fuzzy-cluster entity mentions (stdlib only)."""
import argparse, difflib, re
from collections import defaultdict

SUFFIX = re.compile(r"\b(inc|llc|ltd|gmbh|sarl|corp|co)\b\.?")

def norm(s):
    s = s.lower().strip()
    s = SUFFIX.sub("", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--threshold", type=float, default=0.85)
    args = ap.parse_args()
    mentions = [l.strip() for l in open(args.inp, encoding="utf-8") if l.strip()]
    clusters = []
    for m in mentions:
        n = norm(m)
        hit = None
        for c in clusters:
            if difflib.SequenceMatcher(None, n, c[0]).ratio() >= args.threshold:
                hit = c
                break
        if hit:
            hit[1].append(m)
        else:
            clusters.append((n, [m]))
    print("mentions=%d clusters=%d" % (len(mentions), len(clusters)))
    for key, members in sorted(clusters, key=lambda c: -len(c[1]))[:20]:
        print("  [%s] %s" % (key[:40], members[:4]))

if __name__ == "__main__":
    main()
