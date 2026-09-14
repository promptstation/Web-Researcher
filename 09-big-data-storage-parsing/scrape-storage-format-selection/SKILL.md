---
name: scrape-storage-format-selection
description: Choose storage formats per stage with honest tradeoff math. Use when the user asks to JSONL or Parquet for scraped data; choose a storage format; SQLite vs Postgres for datasets; structure raw and clean layers; evolve dataset schemas.
compatibility: Python 3.10+; pyarrow/pandas for Parquet conversion; disk per retention plan.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Scrape Storage Format Selection

Store every byte in its right shape. You compare formats honestly, separate raw/clean/serve layers, size SQLite correctly, adopt Parquet where scans pay, and version schemas so readers never break.

Optimize simultaneously for:

- honest comparisons
- clean layers
- sized stores
- cheap scans
- safe evolution

Raw stays immutable; every derived layer rebuildable from raw plus versioned code.

## Use Cases

### New dataset

Trigger: user says 'storing scraped data' or 'which format'

Steps:

1. Profile volume and queries
2. Choose per layer
3. Prove with sample
4. Document choice

Result: Right formats day one.

### Messy growth

Trigger: user says 'CSVs everywhere' or 'cannot query this'

Steps:

1. Inventory stores
2. Layer properly
3. Migrate staged
4. Verify queries

Result: Queryable estate.

### Schema change

Trigger: user says 'add fields' or 'rename columns'

Steps:

1. Version schema
2. Dual-read window
3. Backfill clean
4. Retire old

Result: Painless evolution.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Volume and query profile
- Format decision per layer
- Encoding standard (UTF-8)
- Schema versions
- Migration plan
- Size benchmarks
- Reader docs
- Retention map

Never mutate raw or break readers with unversioned schema changes.

## Phase 1 — Profile Needs

Volume, growth, query patterns, retention.

Sample with `scripts/jsonl_tools.py --file sample.jsonl --stats`.

Set layer SLAs.

## Phase 2 — Choose per Layer

Raw: JSONL gzipped, immutable.

Clean: SQLite or Parquet, validated.

Serve: indexed per query.

## Phase 3 — Standardize

UTF-8 everywhere; UTC timestamps; documented nulls.

Compress raw; checksum archives.

Document readers.

## Phase 4 — Evolve Safely

Version schemas; dual-read windows.

Backfill with checks.

Retire with notice.

## Examples

### Example 1: CSV swamp drained

User says: "2TB of random CSVs."

Actions:

1. Layered raw/clean/serve
2. SQLite clean, Parquet serve
3. Queries 100x faster
4. Docs current

Result: Queryable data.

### Example 2: Safe rename

User says: "Rename price_cents everywhere."

Actions:

1. V2 schema, dual readers
2. Backfilled verified
3. Retired v1
4. Zero breakage

Result: Clean evolution.

## Troubleshooting

### Encoding soup

Cause: Mixed source encodings

Fix:

1. Detect at fetch
2. Normalize to UTF-8
3. Replace with logging
4. Validate layer-wide

### SQLite too slow

Cause: Missing indexes or oversized

Fix:

1. Index query paths
2. Vacuum and analyze
3. Shard or graduate
4. Re-measure

### Parquet unreadable

Cause: Writer version skew

Fix:

1. Pin writer version
2. Test readers
3. Standardize engine
4. Re-encode once

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Choose.
- Build.
- Grow.

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

Avoid csv-for-raw; pretty-json dumps; mutable raw; unversioned schemas; index-free SQLite; encoding soup.

## Bundled References

Read `references/format-guide.md` when choosing formats or layering stores.
Run `scripts/jsonl_tools.py` to profile and sample JSONL files.
Copy `assets/checklists.md` into every delivery.
