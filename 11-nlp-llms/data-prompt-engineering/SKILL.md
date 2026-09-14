---
name: data-prompt-engineering
description: Engineer versioned prompts for data tasks with eval-gated changes. Use when the user asks to classify text with LLMs; write few-shot prompts; version prompts; test prompt changes; constrain LLM outputs.
compatibility: Any LLM; eval sets 100+ per task; prompt registry (files + versions).
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# Data Prompt Engineering

Make prompts engineering, not incantation. You write explicit instructions, pick covering few-shots, constrain outputs strictly, version everything, and gate every change on eval suites with A/B proof.

Optimize simultaneously for:

- explicit prompts
- covering shots
- strict outputs
- versioned history
- gated changes

No prompt change ships without eval-suite pass and diff review.

## Use Cases

### Classifier prompt

Trigger: user says 'categorize listings' or 'label tickets'

Steps:

1. Write + constrain
2. Few-shot cover
3. Eval gate
4. Ship versioned

Result: Reliable classifier.

### Prompt regress

Trigger: user says 'new prompt worse' or 'outputs changed'

Steps:

1. Suite catches
2. Diff versions
3. Fix or rollback
4. Gate tighter

Result: Caught regression.

### Normalization

Trigger: user says 'standardize names' or 'clean with LLM'

Steps:

1. Constrain mapping
2. Eval on goldens
3. Review band
4. Ship

Result: Consistent mapping.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Prompt registry
- Version history
- Few-shot rationale
- Eval suite 100+
- Gate thresholds
- A/B results
- Cost per 1k
- Rollback path

Never edit prompts in prod directly or ship without eval-suite pass.

## Phase 1 — Write Explicit

Role, task, constraints, format, edge cases.

Scaffold with `scripts/prompt_card.py --task classify`.

Review before testing.

## Phase 2 — Cover with Shots

One per class plus edges.

Diverse lengths and styles.

Document why each.

## Phase 3 — Constrain Output

Labels, enums, schemas only.

Parse strictly; reject rest.

Repair once max.

## Phase 4 — Gate Changes

Eval suite 100+; thresholds per metric.

A/B vs current; ship winners.

Version + changelog + rollback.

## Examples

### Example 1: Ticket router

User says: "Route 10k tickets weekly."

Actions:

1. 8 shots, strict labels
2. F1 0.91 gated
3. Versioned v3
4. Stable months

Result: Trusted router.

### Example 2: Caught regress

User says: "Tweaked prompt Friday."

Actions:

1. Suite failed Monday
2. Rolled back in minutes
3. Fixed properly
4. Gate saved us

Result: Process works.

## Troubleshooting

### Label drift

Cause: Model paraphrases labels

Fix:

1. Exact-match constraint
2. Logit bias if available
3. Normalize mapping
4. Re-gate

### Edge failures

Cause: Shots miss the tail

Fix:

1. Mine failures
2. Add edge shots
3. Re-eval
4. Track tail metric

### Cost creep

Cause: Long prompts, big models

Fix:

1. Trim shots
2. Smaller model trial
3. Cache
4. Budget alert

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Write.
- Cover.
- Gate.

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

Avoid vibe prompting; shot-free tasks; unconstrained outputs; version-free edits; gate-free ships; rollback-free prod.

## Bundled References

Read `references/prompt-registry.md` when writing or changing prompts.
Run `scripts/prompt_card.py` to scaffold prompt cards.
Copy `assets/checklists.md` into every delivery.
