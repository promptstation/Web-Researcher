---
name: graph-query-ops
description: Answer graph questions with traversals, paths, and patterns — fast. Use when the user asks to shortest path in graph; BFS traversal tutorial; k-hop neighbors query; find patterns in graphs; serve graph queries fast.
compatibility: Python 3.10+; NetworkX or graph DB per scale; adjacency indexes.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Graph Query Ops

Make graphs answer. You traverse for reachability, path for attribution, expand hoods with budgets, match motifs for insight, and serve interactively with indexes and caches.

Optimize simultaneously for:

- correct traversals
- fast paths
- bounded hoods
- found motifs
- served queries

Every query budgeted; no unbounded expansion in production.

## Use Cases

### Attribution

Trigger: user says 'how linked' or 'path between'

Steps:

1. Shortest path
2. Show evidence
3. Verify meaningful
4. Report

Result: Explained connection.

### Discovery

Trigger: user says 'what is nearby' or 'expand this'

Steps:

1. Budgeted hood
2. Rank inside
3. Present + why
4. Log query

Result: Guided discovery.

### Motif hunt

Trigger: user says 'find rings' or 'pattern search'

Steps:

1. Define motif
2. Match bounded
3. Verify samples
4. Report

Result: Found structures.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Query catalog
- Budget table
- Index design
- Latency SLO
- Cache policy
- Query log
- Sample verifications
- Scale plan

Never run unbounded traversals in production or serve unverified motif hits as fact.

## Phase 1 — Catalog Queries

Reachability, paths, hoods, motifs.

Budget each (hops, nodes, ms).

Prototype with `scripts/graph_query.py --edges e.txt`.

## Phase 2 — Index

Adjacency + reverse; label indexes.

Precompute hot paths.

Cache frequent queries.

## Phase 3 — Serve

Latency SLO; timeouts enforced.

Degrade to samples on overload.

Log all queries.

## Phase 4 — Verify

Sample-verify motif hits.

Tune from logs.

Scale plan ready.

## Examples

### Example 1: Attribution done

User says: "How is X connected to Y?"

Actions:

1. 3-hop path found
2. Evidence shown
3. Verified meaningful
4. Answered with proof

Result: Trusted answer.

### Example 2: Discovery live

User says: "Recommend related pages."

Actions:

1. Hood + rank served
2. p95 120ms
3. CTR up
4. Logged + tuned

Result: Fast discovery.

## Troubleshooting

### Hood explosion

Cause: Hub nodes unbounded

Fix:

1. Degree caps
2. Rank-gated expand
3. Sample hubs
4. Budget hard

### Slow paths

Cause: No index or huge graph

Fix:

1. Bidirectional BFS
2. Landmark precompute
3. Cache hot
4. Shard by hood

### Motif noise

Cause: Loose patterns

Fix:

1. Tighten constraints
2. Verify samples
3. Score hits
4. Threshold

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ask.
- Run.
- Trust.

## Decision Heuristic

Before adding complexity, ask:

1. What outcome requires this step?
2. What evidence justifies it?
3. What happens when it fails?
4. What is the cheaper alternative?
5. What proves quality did not regress?
6. What must be logged for audit?
7. What is the rollback plan?

If the main justification is "more", prove the outcome needs it first.

## Anti-Patterns

Avoid unbounded traversals; index-free serving; timeout-free queries; verify-free motifs; log-free tuning; budget-free hoods.

## Bundled References

Read `references/graph-serving.md` when querying or serving graphs.
Run `scripts/graph_query.py` to prototype graph queries.
Copy `assets/checklists.md` into every delivery.
