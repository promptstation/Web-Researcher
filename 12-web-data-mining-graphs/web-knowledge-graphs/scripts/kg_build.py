#!/usr/bin/env python3
"""Co-occurrence entity graph from JSONL mentions (stdlib only)."""
import argparse, json
from collections import Counter, defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="JSONL: doc, entities[]")
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()
    deg = Counter()
    pair = Counter()
    for line in open(args.inp, encoding="utf-8"):
        try:
            ents = json.loads(line).get("entities", [])
        except Exception:
            continue
        ents = sorted(set(ents))
        deg.update(ents)
        for i in range(len(ents)):
            for j in range(i + 1, len(ents)):
                pair[(ents[i], ents[j])] += 1
    print("entities=%d pairs=%d" % (len(deg), len(pair)))
    print("top entities: %s" % [e for e, _ in deg.most_common(8)])
    for (a, b), n in pair.most_common(args.top):
        print("  %dx %.40s <-> %.40s" % (n, a, b))

if __name__ == "__main__":
    main()
