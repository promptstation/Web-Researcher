#!/usr/bin/env python3
"""PageRank over edge list (stdlib only)."""
import argparse
from collections import defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edges", required=True, help="src<tab>dst per line")
    ap.add_argument("--damping", type=float, default=0.85)
    ap.add_argument("--iters", type=int, default=50)
    ap.add_argument("--top", type=int, default=10)
    args = ap.parse_args()
    out = defaultdict(set)
    nodes = set()
    for line in open(args.edges, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) != 2:
            continue
        s, d = p
        nodes.add(s)
        nodes.add(d)
        if s != d:
            out[s].add(d)
    n = len(nodes)
    rank = {v: 1.0 / n for v in nodes}
    d = args.damping
    for _ in range(args.iters):
        sink = sum(r for v, r in rank.items() if not out[v])
        new = {}
        for v in nodes:
            s = sink / n
            for u, ds in out.items():
                if v in ds:
                    s += rank[u] / len(ds)
            new[v] = (1 - d) / n + d * s
        rank = new
    for v, r in sorted(rank.items(), key=lambda x: -x[1])[:args.top]:
        print("%.5f %s" % (r, v[:100]))
    print("nodes=%d edges=%d" % (n, sum(map(len, out.values()))))

if __name__ == "__main__":
    main()
