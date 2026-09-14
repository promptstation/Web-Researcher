#!/usr/bin/env python3
"""BFS shortest path + k-hop hood over edge list (stdlib only)."""
import argparse
from collections import defaultdict, deque

def load(path):
    adj = defaultdict(set)
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) == 2:
            adj[p[0]].add(p[1])
            adj[p[1]].add(p[0])
    return adj

def path(adj, a, b):
    q, prev = deque([a]), {a: None}
    while q:
        v = q.popleft()
        if v == b:
            out = []
            while v:
                out.append(v)
                v = prev[v]
            return out[::-1]
        for u in adj[v]:
            if u not in prev:
                prev[u] = v
                q.append(u)
    return []

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edges", required=True)
    ap.add_argument("--from", dest="a", default="")
    ap.add_argument("--to", dest="b", default="")
    ap.add_argument("--hood", default="")
    ap.add_argument("--k", type=int, default=2)
    args = ap.parse_args()
    adj = load(args.edges)
    if args.a and args.b:
        p = path(adj, args.a, args.b)
        print("hops=%d %s" % (len(p) - 1 if p else -1, " -> ".join(x[:50] for x in p[:8])))
    if args.hood:
        seen, frontier = {args.hood}, {args.hood}
        for _ in range(args.k):
            nxt = set()
            for v in frontier:
                nxt |= adj[v]
            frontier = nxt - seen
            seen |= frontier
        print("hood(k=%d) nodes=%d" % (args.k, len(seen)))

if __name__ == "__main__":
    main()
