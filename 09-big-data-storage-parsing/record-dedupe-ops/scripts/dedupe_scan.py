#!/usr/bin/env python3
"""Exact + shingle near-duplicate scan over JSONL (stdlib only)."""
import argparse, json
from collections import defaultdict

def shingles(text, k=5):
    w = text.lower().split()
    return {" ".join(w[i:i + k]) for i in range(max(0, len(w) - k + 1))}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--key", default="record_id")
    ap.add_argument("--text", default="title")
    ap.add_argument("--threshold", type=float, default=0.8)
    args = ap.parse_args()
    seen, exact = set(), 0
    sigs = {}
    near = 0
    n = 0
    for line in open(args.inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        n += 1
        k = str(r.get(args.key, ""))
        if k and k in seen:
            exact += 1
        seen.add(k)
        s = shingles(str(r.get(args.text, "")))
        if not s:
            continue
        for prev_fp, prev in list(sigs.items())[-200:]:
            inter = len(s & prev)
            union = len(s | prev)
            if union and inter / union >= args.threshold:
                near += 1
                break
        sigs[k or str(n)] = s
    print("records=%d exact_dupes=%d near_dup_hits=%d (threshold=%.2f)" % (n, exact, near, args.threshold))
    print("exact must be 0 after gates; tune threshold on 200+ sampled pairs.")

if __name__ == "__main__":
    main()
