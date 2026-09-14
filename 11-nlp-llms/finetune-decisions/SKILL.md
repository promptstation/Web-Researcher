---
name: finetune-decisions
description: Choose adaptation by pilot eval and run clean, honestly-measured tunes. Use when the user asks to fine-tune or RAG; curate instruction data; run a small fine-tune; distill a model; decide LLM adaptation strategy.
compatibility: GPU access for tunes; eval suites; 500+ curated pairs minimum.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# Finetune Decisions

Adapt deliberately, not by hype. You ladder methods by need, pilot cheaply with gates, curate quality data, tune parameter-efficiently, and measure lift against cost — deciding with numbers.

Optimize simultaneously for:

- laddered choices
- cheap pilots
- clean data
- measured tunes
- honest decisions

No full fine-tune without pilot win; no data without quality rubric and dedupe.

## Use Cases

### Adapt choice

Trigger: user says 'fine-tune for us' or 'RAG vs tune'

Steps:

1. Ladder the need
2. Pilot top 2
3. Compare gated
4. Decide numbers

Result: Right method.

### Small tune

Trigger: user says 'tune 7B' or 'LoRA pilot'

Steps:

1. Curate 500+
2. Tune PEFT
3. Eval + ablate
4. Ship or stop

Result: Measured tune.

### Distill

Trigger: user says 'smaller cheaper' or 'distill teacher'

Steps:

1. Teacher labels
2. Student trains
3. Gap measured
4. Ship if worthy

Result: Cheap student.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Ladder doc
- Pilot results
- Curation rubric
- Dataset audit
- Tune config
- Eval comparison
- Cost model
- Decision memo

Never fine-tune on uncurated data or claim wins without ablation and cost math.

## Phase 1 — Ladder Need

Prompt < RAG < PEFT < full < distill by cost.

Match method to gap type.

Set pilot gates.

## Phase 2 — Curate Data

Audit with `scripts/ft_dataset_audit.py --in ft.jsonl`.

Rubric-graded, diverse, deduped.

500+ minimum for pilots.

## Phase 3 — Pilot Cheap

PEFT small, few epochs.

Eval vs baseline + RAG.

Ablate size and quality.

## Phase 4 — Decide

Lift vs cost vs risk.

Memo with numbers.

Ship or stop explicitly.

## Examples

### Example 1: RAG won

User says: "Fine-tune for support?"

Actions:

1. Piloted RAG vs LoRA
2. RAG +12, LoRA +3
3. Shipped RAG
4. Saved months

Result: Evidence over hype.

### Example 2: Tune earned

User says: "Style transfer at scale."

Actions:

1. Curated 2k pairs
2. LoRA +18 style
3. Cost 1/10th teacher
4. Shipped measured

Result: Worthy tune.

## Troubleshooting

### Tune underperforms

Cause: Dirty or tiny data

Fix:

1. Curate harder
2. Grow quality
3. Check eval
4. Stop if flat

### Catastrophic forgetting

Cause: Narrow data, big steps

Fix:

1. Mix general data
2. Lower LR
3. PEFT not full
4. Re-eval broad

### Pilot unclear

Cause: Weak eval

Fix:

1. Harden suite
2. Add ablations
3. Judge blind
4. Decide again

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Choose.
- Feed.
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

Avoid hype-led tuning; pilot-free commits; rubric-free data; ablation-free claims; safety-rerun-free tunes; memo-free decisions.

## Bundled References

Read `references/adaptation-ladder.md` when choosing adaptation methods.
Run `scripts/ft_dataset_audit.py` to audit instruction-tuning data.
Copy `assets/checklists.md` into every delivery.
