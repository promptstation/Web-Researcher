#!/usr/bin/env python3
"""Label propagation communities over edge list (stdlib only)."""
import argparse, random
from collections import Counter, defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edges", required=True)
    ap.add_argument("--iters", type=int, default=10)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    adj = defaultdict(set)
    for line in open(args.edges, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) != 2:
            continue
        adj[p[0]].add(p[1])
        adj[p[1]].add(p[0])
    rng = random.Random(args.seed)
    lab = {v: i for i, v in enumerate(adj)}
    nodes = list(adj)
    for _ in range(args.iters):
        rng.shuffle(nodes)
        for v in nodes:
            if adj[v]:
                lab[v] = Counter(lab[u] for u in adj[v]).most_common(1)[0][0]
    sizes = Counter(lab.values())
    print("nodes=%d communities=%d" % (len(adj), len(sizes)))
    for c, n in sizes.most_common(15):
        members = [v for v, l in lab.items() if l == c][:3]
        print("  size=%d e.g. %s" % (n, [m[:60] for m in members]))

if __name__ == "__main__":
    main()
