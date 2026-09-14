#!/usr/bin/env python3
"""Partition JSONL into key=value folders with manifest (stdlib only)."""
import argparse, json, os
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--by", default="fetched_date")
    ap.add_argument("--out", default="dataset")
    args = ap.parse_args()
    counts, files = Counter(), {}
    for line in open(args.inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        key = str(r.get(args.by, "unknown"))[:32].replace("/", "-")
        d = os.path.join(args.out, "%s=%s" % (args.by, key))
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "part.jsonl")
        fh = files.get(p)
        if not fh:
            fh = files[p] = open(p, "a", encoding="utf-8")
        fh.write(json.dumps(r) + "\n")
        counts[key] += 1
    for fh in files.values():
        fh.close()
    man = {"by": args.by, "partitions": dict(counts), "total": sum(counts.values())}
    json.dump(man, open(os.path.join(args.out, "manifest.json"), "w"), indent=1)
    print("partitions=%d total=%d manifest written" % (len(counts), man["total"]))

if __name__ == "__main__":
    main()
