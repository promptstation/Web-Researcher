---
name: rag-pipeline-ops
description: Answer from your corpus with citations, abstention, and faithfulness proof. Use when the user asks to build a RAG pipeline; add citations to answers; evaluate RAG faithfulness; tune retrieval and reranking; make RAG abstain correctly.
compatibility: Vector store + LLM; 50+ judged QA pairs; permission metadata per chunk.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# RAG Pipeline Ops

Answer only what the corpus supports. You retrieve hybrid and rerank hard, bind every claim to citations, abstain cleanly on gaps, filter by freshness and permission, and eval faithfulness relentlessly.

Optimize simultaneously for:

- ranked contexts
- bound citations
- honest abstention
- safe filtering
- measured faithfulness

Every factual claim cited; no answer from missing context; permissions filter before retrieval.

## Use Cases

### Docs QA

Trigger: user says 'QA over our docs' or 'support bot'

Steps:

1. Index + retrieve
2. Cite answers
3. Abstain tuned
4. Eval faithful

Result: Trusted QA.

### Hallucination cut

Trigger: user says 'bot invents facts' or 'wrong answers'

Steps:

1. Bind citations
2. Faithfulness eval
3. Fix top class
4. Verify lift

Result: Grounded answers.

### Stale answers

Trigger: user says 'old info served' or 'outdated docs'

Steps:

1. Freshness filters
2. Version index
3. Re-eval
4. SLA freshness

Result: Current answers.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Retrieval config
- Rerank eval
- Citation spec
- Abstention policy
- Filter rules
- Faithfulness scores
- QA eval set 50+
- Failure log

Never serve uncited factual claims or retrieve across permission boundaries.

## Phase 1 — Retrieve Well

Dense + BM25 + filters, rerank top-50 to 5.

Eval recall@5 on judged set.

Tune from failures.

## Phase 2 — Cite Everything

Inline [n] per claim bound to chunks.

Verify citations resolve.

Score with `scripts/rag_eval.py --qa qa.jsonl`.

## Phase 3 — Abstain and Filter

Abstain on insufficient context.

Freshness + permission + source filters.

Log abstentions; review weekly.

## Phase 4 — Eval Faithfulness

Claim-level support checks.

Fix top failure class monthly.

Report trend.

## Examples

### Example 1: Support bot

User says: "Answer from 5k help docs."

Actions:

1. Reranked retrieval
2. Cited answers
3. Faithful 0.93
4. Deflection up, complaints down

Result: Trusted bot.

### Example 2: Leak prevented

User says: "Bot quoted internal docs."

Actions:

1. Permission filters pre-retrieval
2. Verified isolation
3. Audit passed
4. Monitor kept

Result: Safe RAG.

## Troubleshooting

### Cites wrong chunks

Cause: Rerank weak or k too big

Fix:

1. Stronger rerank
2. Smaller k
3. Citation verify
4. Re-eval

### Over-abstains

Cause: Threshold too strict

Fix:

1. Tune on judged edge
2. Partial-answer policy
3. Review abstains
4. Re-tune monthly

### Slow answers

Cause: Retrieve+rereank+generate chain

Fix:

1. Cache hot queries
2. Smaller k
3. Faster rerank
4. Budget latency

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Get.
- Say.
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

Avoid citation-free answers; abstain-free bots; filter-after-generate; faithfulness-free claims; rerank-free retrieval; stale-index QA.

## Bundled References

Read `references/grounded-rag.md` when building or evaluating RAG.
Run `scripts/rag_eval.py` to score RAG cite/abstain behavior.
Copy `assets/checklists.md` into every delivery.
