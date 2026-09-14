---
name: scrape-data-retrieval
description: Turn scraped corpora into searchable products with trusted relevance. Use when the user asks to search scraped data; build full-text search; add faceted filters; tune search relevance; index JSONL with SQLite.
compatibility: Python 3.10+ with SQLite FTS5; Elasticsearch/OpenSearch when scale demands.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Scrape Data Retrieval

Make corpora answer questions. You index with FTS5, rank BM25 with freshness boosts, facet for navigation, snippet with highlights, and judge queries so relevance improves measurably.

Optimize simultaneously for:

- indexed corpora
- sane ranking
- useful facets
- clear snippets
- judged relevance

Relevance judged by humans on real queries; no ranking change without judged comparison.

## Use Cases

### Corpus search

Trigger: user says 'search our archive' or 'find in scraped data'

Steps:

1. Index FTS
2. Rank baseline
3. Facet key fields
4. Judge and tune

Result: Working search.

### Bad results

Trigger: user says 'search useless' or 'wrong top hits'

Steps:

1. Judge failures
2. Tune boosts
3. Re-judge
4. Ship winner

Result: Trusted ranking.

### Scale up

Trigger: user says 'FTS too slow' or '10M docs'

Steps:

1. Measure pain
2. Graduate engine
3. Migrate index
4. Verify parity

Result: Scaled search.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Index spec
- Tokenizer choice
- Boost rules
- Facet list
- Judged query set
- Relevance scores
- Latency SLO
- Scale plan

Never ship ranking changes unjudged or index without update and rebuild plans.

## Phase 1 — Index

Build with `scripts/fts_index.py --in corpus.jsonl --db search.db`.

Tokenizer per language; triggers for updates.

Rebuild procedure tested.

## Phase 2 — Rank Baseline

BM25 default; boost title over body.

Freshness and source boosts documented.

Latency measured.

## Phase 3 — Facet and Snippet

Facets: category, date, source; price ranges.

Snippets 2-3 with highlights.

Zero-result help.

## Phase 4 — Judge and Tune

50+ judged queries; NDCG-ish eyeball or grades.

One change at a time.

Ship judged winners.

## Examples

### Example 1: Archive alive

User says: "2M articles, unfindable."

Actions:

1. FTS5 indexed
2. Facets plus snippets
3. Judged 80 queries
4. Usage up 5x

Result: Loved search.

### Example 2: Ranking fixed

User says: "Stale docs rank first."

Actions:

1. Freshness boost added
2. Re-judged +18
3. Shipped
4. Complaints gone

Result: Fresh relevance.

## Troubleshooting

### Index bloat

Cause: Unused columns or no vacuum

Fix:

1. Index needed columns
2. Optimize/rebuild
3. Monitor size
4. Prune stale

### Slow queries

Cause: Leading wildcards or huge facets

Fix:

1. Forbid leading wildcards
2. Limit facet depth
3. Add trigram only if needed
4. Cache hot queries

### Judging churn

Cause: Vague relevance grades

Fix:

1. 3-grade rubric
2. Two judges
3. Adjudicate splits
4. Lock rubric

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Index.
- Rank.
- Prove.

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

Avoid LIKE-based search; unjudged ranking; boost soup; facet-free results; snippet-free hits; rebuild-free indexes.

## Bundled References

Read `references/corpus-search.md` when indexing or tuning search.
Run `scripts/fts_index.py` to index and query JSONL with FTS5.
Copy `assets/checklists.md` into every delivery.
