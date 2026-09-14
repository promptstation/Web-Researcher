---
name: web-knowledge-graphs
description: Build queryable knowledge graphs from crawls with provenance. Use when the user asks to extract knowledge triples; build a knowledge graph; link entities across pages; resolve conflicting facts; query a knowledge graph.
compatibility: Python 3.10+; triple store or SQLite; 300+ judged triples for eval.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Web Knowledge Graphs

Turn crawls into knowledge. You extract triples to a relation schema, link entities canonically, fuse confidence across sources, resolve conflicts by policy, and answer queries with provenance attached.

Optimize simultaneously for:

- rich triples
- linked entities
- honest confidence
- resolved conflicts
- provenanced answers

Every triple sourced; conflicts surfaced, never silently averaged.

## Use Cases

### Domain KG

Trigger: user says 'product knowledge graph' or 'org chart from web'

Steps:

1. Schema relations
2. Extract + link
3. Conflicts resolved
4. Eval + serve

Result: Queryable KG.

### Fact QA

Trigger: user says 'answer from KG' or 'cite sources'

Steps:

1. Query patterns
2. Provenance attach
3. Confidence show
4. Eval answers

Result: Cited answers.

### Conflict audit

Trigger: user says 'sources disagree' or 'which is true'

Steps:

1. Surface conflicts
2. Apply policy
3. Human-review top
4. Log decisions

Result: Honest knowledge.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Relation schema
- Extraction eval
- Linking eval
- Confidence model
- Conflict policy
- Provenance schema
- Query log
- KG eval

Never serve unsourced triples or hide conflicts from consumers.

## Phase 1 — Schema Relations

Predicates with domains/ranges.

Closed core, open extension.

Review with consumers.

## Phase 2 — Extract and Link

Triples from text/tables/infoboxes.

Prototype co-occurrence with `scripts/kg_build.py --in entities.jsonl`.

Link to canonical nodes.

## Phase 3 — Score and Resolve

Confidence from sources+agreement.

Conflicts: recency/authority/multi-truth.

Review top conflicts.

## Phase 4 — Serve and Eval

Query API with provenance.

Eval 300+ triples.

Refresh scheduled.

## Examples

### Example 1: Product KG

User says: "Specs scattered everywhere."

Actions:

1. 40k triples, linked
2. Conflicts resolved
3. QA served cited
4. Precision 0.93

Result: Single spec truth.

### Example 2: Conflict honesty

User says: "Prices differ by source."

Actions:

1. Multi-truth served
2. Sources shown
3. Users choose
4. Trust up

Result: Honest answers.

## Troubleshooting

### Triple noise

Cause: Open extraction unfiltered

Fix:

1. Schema-constrain
2. Confidence floor
3. Judge samples
4. Filter hard

### Entity splits

Cause: Weak linking

Fix:

1. Alias tables
2. Blocking
3. Review band
4. Re-link

### Stale facts

Cause: No refresh

Fix:

1. Change-driven updates
2. Recency scoring
3. Refresh SLA
4. Verify live

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Build.
- Trust.
- Serve.

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

Avoid schemaless triples; link-free mentions; confidence-free facts; conflict-hiding merges; provenance-free answers; eval-free KGs.

## Bundled References

Read `references/kg-building.md` when building knowledge graphs.
Run `scripts/kg_build.py` to prototype co-occurrence graphs.
Copy `assets/checklists.md` into every delivery.
