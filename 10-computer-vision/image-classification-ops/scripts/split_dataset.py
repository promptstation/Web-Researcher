#!/usr/bin/env python3
"""Stratified seeded train/val/test split from manifest JSONL (stdlib only)."""
import argparse, json, random
from collections import defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True, help="JSONL with label field")
    ap.add_argument("--label", default="label")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--ratios", default="0.7,0.15,0.15")
    args = ap.parse_args()
    tr, va, te = map(float, args.ratios.split(","))
    rng = random.Random(args.seed)
    by = defaultdict(list)
    for line in open(args.manifest, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        by[str(r.get(args.label, "?"))].append(r)
    outs = {k: open("split_%s.jsonl" % k, "w") for k in ("train", "val", "test")}
    counts = defaultdict(int)
    for lab, rows in sorted(by.items()):
        rng.shuffle(rows)
        n = len(rows)
        i, j = int(n * tr), int(n * (tr + va))
        for k, part in (("train", rows[:i]), ("val", rows[i:j]), ("test", rows[j:])):
            for r in part:
                outs[k].write(json.dumps(r) + "\n")
            counts[(lab, k)] += len(part)
    for fh in outs.values():
        fh.close()
    for (lab, k), c in sorted(counts.items()):
        print("%-20s %-6s %d" % (lab, k, c))
    print("seed=%d locked; touch test once." % args.seed)

if __name__ == "__main__":
    main()
