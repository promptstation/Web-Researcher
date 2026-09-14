---
name: rag-chunking-ops
description: Chunk for retrieval with sentence awareness, metadata, and token budgets. Use when the user asks to chunk documents for RAG; choose chunk size and overlap; prepare embeddings; budget embedding tokens; improve retrieval recall.
compatibility: Python 3.10+; tiktoken optional for exact counts; embedding API or local model.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# RAG Chunking Ops

Make retrieval find things. You chunk by sentences with tuned overlap, carry metadata everywhere, budget tokens honestly, keep vector spaces deduped and versioned, and eval recall before claiming wins.

Optimize simultaneously for:

- sane chunks
- tuned overlap
- rich metadata
- honest budgets
- measured recall

No index without recall eval; no chunk without source metadata.

## Use Cases

### RAG corpus

Trigger: user says 'index docs for QA' or 'build retrieval'

Steps:

1. Chunk sensibly
2. Embed versioned
3. Eval recall
4. Tune once

Result: Retrieving index.

### Recall rescue

Trigger: user says 'retrieval misses' or 'wrong chunks'

Steps:

1. Judge failures
2. Fix chunking
3. Re-eval
4. Ship winner

Result: Found answers.

### Cost control

Trigger: user says 'embedding bill high' or 'too many tokens'

Steps:

1. Budget tokens
2. Dedupe
3. Right-size
4. Track spend

Result: Affordable index.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Chunk spec
- Overlap rationale
- Metadata schema
- Token budget
- Embedding model pin
- Recall eval
- Index version
- Cost tracking

Never chunk mid-sentence blindly or index without recall measurement.

## Phase 1 — Chunk Sensibly

Sentences, 200-800 tokens, 10-20 percent overlap.

Prototype with `scripts/chunker.py --in doc.txt`.

Compare 3 strategies.

## Phase 2 — Carry Metadata

Source, title, section, date, lang, version.

Filterable fields indexed.

Provenance queryable.

## Phase 3 — Embed Versioned

Pin model; dedupe texts first.

Budget tokens; track cost.

Version index with model+chunk spec.

## Phase 4 — Eval Recall

50+ judged queries; recall@k.

Fix chunking from failures.

Ship judged winner.

## Examples

### Example 1: Recall doubled

User says: "RAG answers miss sources."

Actions:

1. Sentence chunks plus metadata
2. Recall 0.4 to 0.8
3. Filters added
4. Users notice

Result: Working RAG.

### Example 2: Bill halved

User says: "Embeddings cost too much."

Actions:

1. Deduped 40 percent
2. Right-sized chunks
3. Cost down 55
4. Recall kept

Result: Lean index.

## Troubleshooting

### Fragments retrieved

Cause: Chunks too small or split mid-thought

Fix:

1. Bigger chunks
2. Section-aware splits
3. More overlap
4. Re-eval

### Context drowns

Cause: Chunks too big

Fix:

1. Smaller + rerank
2. Parent-child retrieval
3. Summaries for context
4. Tune k

### Stale index

Cause: No update pipeline

Fix:

1. Incremental upserts
2. Version indexes
3. Rebuild scheduled
4. Freshness SLA

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Chunk.
- Embed.
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

Avoid fixed-blind chunking; metadata-free vectors; budget-free embedding; recall-free indexes; unversioned spaces; stale-index serving.

## Bundled References

Read `references/chunking-guide.md` when chunking or indexing.
Run `scripts/chunker.py` to prototype sentence chunking.
Copy `assets/checklists.md` into every delivery.
