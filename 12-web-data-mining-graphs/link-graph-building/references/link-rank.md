# Link Rank

Graph: nodes = canonical URLs; edges = content links (filter nav/footer/ads/templates by block signals); dedupe; store adjacency + reverse. Stats first: nodes, edges, components, sinks, max indegree (trap smell).

PageRank: damping 0.85; dangling nodes redistribute uniformly; iterate to L1 < 1e-6 (log residuals); personalized with trust-seed teleport for spam resistance. HITS for hub/authority splits on topic subgraphs. Report top/bottom samples with reasons.

Spam: farm clusters (dense, new, cross-linked); weight edges by source trust; prune confirmed; re-rank and diff. Traps: cap out-neighbors per pattern; canonicalize sessions/facets. Sinks: redistribute, never delete silently.

Application: frontier priority (rank deciles), quality bands (authoritative/ok/junk with thresholds), canonical-choice signal, dedupe preference. Sample-verify 100+ per band; monitor rank drift monthly; recompute on corpus change.
