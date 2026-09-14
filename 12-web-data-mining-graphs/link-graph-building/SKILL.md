---
name: link-graph-building
description: Build link graphs and rank them honestly for priority and quality. Use when the user asks to compute PageRank; build a link graph; rank crawled pages; handle link spam; prioritize crawl by importance.
compatibility: Python 3.10+; NetworkX optional; 10k-10M edge scale per method.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Link Graph Building

Turn links into judgment. You build canonical adjacency, iterate PageRank to convergence, fix sinks and traps, seed trust against spam, and apply rank to priority and quality with evals.

Optimize simultaneously for:

- clean graphs
- converged rank
- tamed sinks
- resisted spam
- applied scores

Rank computed transparently; spam resistance explicit; no rank claim without convergence proof.

## Use Cases

### Crawl priority

Trigger: user says 'important pages first' or 'rank URLs'

Steps:

1. Build graph
2. Rank converged
3. Prioritize frontier
4. Verify coverage

Result: Importance-ordered crawl.

### Quality signal

Trigger: user says 'find authoritative' or 'score pages'

Steps:

1. Rank + trust
2. Threshold bands
3. Sample verify
4. Apply signal

Result: Authority scoring.

### Spam fight

Trigger: user says 'link farm' or 'spam polluting'

Steps:

1. Detect clusters
2. Seed trust
3. Prune/weight
4. Re-rank

Result: Spam-resistant rank.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Edge inventory
- Canonicalization
- Rank config
- Convergence log
- Trust seeds
- Spam report
- Application design
- Quality eval

Never rank uncanonicalized graphs or apply rank without spam review.

## Phase 1 — Build Graph

Canonical nodes; dedupe edges.

Filter nav/boilerplate links.

Stats: nodes, edges, density.

## Phase 2 — Rank

Run `scripts/pagerank.py --edges edges.txt` to baseline.

Damping 0.85; iterate to 1e-6.

Personalize with trust seeds.

## Phase 3 — Harden

Sinks redistributed; traps capped.

Spam clusters pruned/weighted.

Re-converge; diff ranks.

## Phase 4 — Apply

Frontier priority; quality bands.

Sample-verify top/bottom.

Monitor rank drift.

## Examples

### Example 1: Priority win

User says: "Crawl finds junk first."

Actions:

1. Ranked 500k graph
2. Frontier by rank
3. Value pages day 1
4. Coverage better

Result: Smart ordering.

### Example 2: Farm drained

User says: "Spam outranks real."

Actions:

1. Trust-seeded
2. Farm pruned
3. Real restored
4. Monitor kept

Result: Honest rank.

## Troubleshooting

### Rank concentrates

Cause: Traps or sinks

Fix:

1. Find top accumulators
2. Fix structure
3. Re-run
4. Cap per pattern

### No convergence

Cause: Too strict or oscillating

Fix:

1. Loosen epsilon
2. Cap iterations
3. Check dangling
4. Log residuals

### Rank != quality

Cause: Spam or nav links

Fix:

1. Filter link types
2. Trust seeds
3. Sample eval
4. Weight edges

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Build.
- Rank.
- Use.

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

Avoid uncanonicalized nodes; unconverged rank; sink-ignoring math; trust-free ranking; spam-blind application; sample-free bands.

## Bundled References

Read `references/link-rank.md` when building graphs or ranking.
Run `scripts/pagerank.py` to baseline PageRank.
Copy `assets/checklists.md` into every delivery.
