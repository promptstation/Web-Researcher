---
name: dataset-partitioning
description: Partition datasets for fast scans, cheap storage, and one-command expiry. Use when the user asks to partition large datasets; compact small files; organize data lake folders; expire old partitions; speed up dataset scans.
compatibility: Any filesystem or object store; Parquet tools for columnar; scheduler for compaction.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Dataset Partitioning

Shape data for its access patterns. You partition by query and expiry, size files for scans, compact the small-file sprawl, manifest everything, and expire whole partitions with one command.

Optimize simultaneously for:

- right partitions
- sized files
- compacted stores
- live manifests
- cheap expiry

Queries prune partitions; no full scans for dated questions; expiry never touches live partitions.

## Use Cases

### Slow scans

Trigger: user says 'queries scan everything' or 'too slow'

Steps:

1. Learn query patterns
2. Partition by them
3. Verify pruning
4. Measure wins

Result: Pruned fast scans.

### Small-file sprawl

Trigger: user says 'millions of tiny files' or 'listing slow'

Steps:

1. Compact per partition
2. Size 128MB+
3. Manifest
4. Verify counts

Result: Compact store.

### Retention purge

Trigger: user says 'delete old data' or 'GDPR purge'

Steps:

1. Drop partitions
2. Verify manifest
3. Prove deletion
4. File evidence

Result: Provable purge.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Query pattern analysis
- Partition spec
- File-size policy
- Compaction schedule
- Manifest schema
- Expiry policy
- Scan benchmarks
- Deletion proofs

Never partition by high-cardinality IDs or expire without manifest proof.

## Phase 1 — Design Keys

Date first, then source/class.

Cardinality under 10k partitions.

Prototype with `scripts/partition_jsonl.py --in data.jsonl --by fetched_date`.

## Phase 2 — Size Files

Target 128-512MB per file.

Compact below 64MB.

Verify counts and hashes.

## Phase 3 — Manifest

Files, counts, hashes, schema version.

Readers use manifest, not listings.

Regenerate per write.

## Phase 4 — Expire

Drop whole partitions.

Prove with manifest diff.

Archive before delete per policy.

## Examples

### Example 1: Scan 50x

User says: "Daily queries take hours."

Actions:

1. Date-partitioned
2. Pruning verified
3. Minutes now
4. Costs down 90

Result: Partitioned speed.

### Example 2: Purge proven

User says: "Delete 2023 personal data."

Actions:

1. Dropped 12 partitions
2. Manifest diff filed
3. Deletion attested
4. Audit passed

Result: Provable compliance.

## Troubleshooting

### Partition skew

Cause: Hot source or date

Fix:

1. Sub-partition hot keys
2. Split by hash bucket
3. Rebalance
4. Monitor sizes

### Compaction churn

Cause: Compacting live partitions

Fix:

1. Compact sealed only
2. Schedule off-peak
3. Verify idempotent
4. Alert on fail

### Manifest drift

Cause: Writes bypass manifest

Fix:

1. Write via manifest writer
2. Regenerate and diff
3. Block direct writes
4. Audit weekly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Design.
- Build.
- Keep.

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

Avoid ID partitioning; tiny-file sprawl; listing-based readers; manifest-free lakes; live-partition rewrites; proof-free deletes.

## Bundled References

Read `references/partition-guide.md` when partitioning or compacting.
Run `scripts/partition_jsonl.py` to partition JSONL by a key.
Copy `assets/checklists.md` into every delivery.
