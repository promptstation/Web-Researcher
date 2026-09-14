---
name: llm-extraction-ops
description: Extract structure with LLMs under schema, validation, and field-level eval. Use when the user asks to extract structured data with LLMs; validate LLM JSON output; evaluate extraction accuracy; fix LLM extraction failures; control extraction costs.
compatibility: Any LLM API or local model; JSON schemas; 100+ gold records for eval.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# LLM Extraction Ops

Turn prose into records you can query. You schema-constrain every call, validate outputs strictly, repair failures deliberately, score fields against gold, and route models by difficulty — with humans on the risky band.

Optimize simultaneously for:

- constrained calls
- valid outputs
- repaired failures
- scored fields
- controlled cost

No extracted record ships without schema pass; no accuracy claim without gold eval.

## Use Cases

### New extractor

Trigger: user says 'pull fields from text' or 'structure this'

Steps:

1. Schema first
2. Prompt + validate
3. Gold-eval
4. Ship gated

Result: Trusted extractor.

### Malformed outputs

Trigger: user says 'bad JSON' or 'fields missing'

Steps:

1. Harden schema
2. Repair retry
3. Validate strict
4. Verify rate

Result: Robust outputs.

### Cost squeeze

Trigger: user says 'extraction expensive' or 'cheaper model'

Steps:

1. Route by difficulty
2. Cache repeats
3. Batch smart
4. Verify kept

Result: Cheaper extraction.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- JSON schemas
- Prompt versions
- Validation rules
- Gold set 100+
- Field scores
- Repair log
- Routing policy
- Cost dashboard

Never accept unvalidated LLM output or ship extraction without field eval.

## Phase 1 — Schema First

Fields, types, enums, required defined.

Prompt references schema explicitly.

Version both together.

## Phase 2 — Validate All

Parse JSON; check schema; business rules.

Repair retry once, then escalate model.

Quarantine persistent fails.

## Phase 3 — Eval Fields

Score with `scripts/extract_eval.py --gold gold.jsonl --pred pred.jsonl`.

Per-field P/R; fix worst first.

Human-review risky band.

## Phase 4 — Route and Save

Easy->small model, hard->large.

Cache by content hash.

Batch; track cost per 1k.

## Examples

### Example 1: Spec sheets

User says: "Extract specs from PDFs text."

Actions:

1. Schema 24 fields
2. Field F1 0.94
3. Review band 5 percent
4. Shipped to catalog

Result: Queryable specs.

### Example 2: Cost down

User says: "GPT-4 everything bankrupting."

Actions:

1. Routed 80 percent small
2. Quality kept
3. Cost down 70
4. Monitored

Result: Smart routing.

## Troubleshooting

### Schema drift

Cause: Model improvises fields

Fix:

1. Strict mode + enums
2. Reject unknowns
3. Repair prompt
4. Re-eval

### Silent wrong values

Cause: Plausible hallucinations

Fix:

1. Constrain to quotes
2. Verify against source
3. Review band
4. Gold-test adversarial

### Cost spikes

Cause: Retries and big contexts

Fix:

1. Cap retries
2. Trim context
3. Cache more
4. Alert budgets

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Constrain.
- Check.
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

Avoid schemaless prompting; validate-free outputs; gold-free claims; single-model-everything; cache-free repeats; review-free criticals.

## Bundled References

Read `references/llm-extraction.md` when extracting structure with LLMs.
Run `scripts/extract_eval.py` to score field-level extraction.
Copy `assets/checklists.md` into every delivery.
