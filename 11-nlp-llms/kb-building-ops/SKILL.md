---
name: kb-building-ops
description: Resolve entities and build knowledge bases with provenance. Use when the user asks to resolve duplicate entities; build a knowledge base; merge company mentions; cluster product names; link records across sources.
compatibility: Python 3.10+; recordlinkage/splink optional at scale; 500+ judged pairs for tuning.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# KB Building Ops

Turn mentions into entities. You normalize aggressively, block to cut pairs, score with rules plus similarity, cluster with audits, survive merges by policy, and provenance every fact to its sources.

Optimize simultaneously for:

- clean mentions
- lean pairs
- scored matches
- audited clusters
- provenanced facts

Merge only with rules and audits; every fact traceable to sources.

## Use Cases

### Company KB

Trigger: user says 'same company many names' or 'merge vendors'

Steps:

1. Normalize + alias
2. Block + score
3. Cluster + review
4. Merge ruled

Result: Single company view.

### Product linking

Trigger: user says 'link listings' or 'same product cross-site'

Steps:

1. Block by brand/cat
2. Score pairs
3. Cluster
4. Eval precision

Result: Linked catalog.

### KB eval

Trigger: user says 'KB quality?' or 'audit entities'

Steps:

1. Sample clusters
2. Judge precision
3. Fix rules
4. Re-eval

Result: Measured KB.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Normalization spec
- Alias tables
- Blocking design
- Scoring weights
- Cluster audit
- Survivorship rules
- Provenance schema
- KB eval

Never merge across types or ship facts without provenance.

## Phase 1 — Normalize

Case, punctuation, legal suffixes, aliases.

Prototype with `scripts/entity_merge.py --in mentions.txt`.

Alias tables versioned.

## Phase 2 — Block and Score

Keys: brand, category, geo, phone.

Rules + similarity; tune on 500 judged.

Precision over recall first.

## Phase 3 — Cluster

Connected components + review band.

Audit every cluster decision.

Human-review low-confidence.

## Phase 4 — Merge and Prove

Survivorship per attribute.

Provenance per fact.

Eval precision/recall sampled.

## Examples

### Example 1: Vendor master

User says: "5k vendor spellings."

Actions:

1. Resolved to 900 entities
2. Precision 0.97
3. Provenanced
4. Procurement happy

Result: Clean master.

### Example 2: Product graph

User says: "Link cross-site products."

Actions:

1. Blocked + scored
2. Clusters reviewed
3. Linked 80 percent
4. Eval'd quarterly

Result: Linked catalog.

## Troubleshooting

### Over-merge

Cause: Loose thresholds

Fix:

1. Tighten
2. Add negative rules
3. Review band wider
4. Re-cluster

### Under-merge

Cause: Strict blocking

Fix:

1. More blocking passes
2. Alias growth
3. Fuzzy keys
4. Recall push

### Provenance gaps

Cause: Merges drop sources

Fix:

1. Carry all sources
2. Audit merges
3. Backfill
4. Gate future

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Prep.
- Match.
- Ship.

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

Avoid normalize-free matching; block-free pairs; judge-free thresholds; audit-free clusters; provenance-free facts; type-crossing merges.

## Bundled References

Read `references/entity-resolution.md` when resolving entities or building KBs.
Run `scripts/entity_merge.py` to prototype mention clustering.
Copy `assets/checklists.md` into every delivery.
