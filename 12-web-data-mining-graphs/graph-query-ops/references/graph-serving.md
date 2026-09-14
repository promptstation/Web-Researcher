# Graph Serving

Queries: reachability (BFS/DFS with visited + depth cap), shortest path (bidirectional BFS unweighted, Dijkstra weighted), k-hop hoods (degree-capped, rank-gated), motifs (bounded pattern match with scoring). Budget: hops<=4, nodes<=100k, ms<=500 defaults.

Serving: adjacency + reverse indexes in memory to ~100M edges; shard by community beyond; cache hot queries (paths, hoods) with TTL; timeouts enforced; degrade to sampled answers with labels. Log (query, budget, ms, result size) always.

Correctness: verify paths exist in current graph; motif hits sample-verified before reporting; hub handling documented (caps + sampling); tests on fixed graphs gate changes.

Scale: precompute PageRank + communities offline; online serves traversals + lookups; batch motif jobs, never interactive unbounded. Latency SLO p95 (e.g., 300ms); tune from logs monthly.
