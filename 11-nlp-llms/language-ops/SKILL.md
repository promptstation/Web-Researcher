---
name: language-ops
description: Detect languages reliably and run fair per-language pipelines. Use when the user asks to detect document language; handle multilingual corpus; route by language; evaluate non-English quality; manage code-switched text.
compatibility: Python 3.10+; fasttext/langdetect optional; per-language eval sets.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# Language Ops

Treat every language first-class. You detect with script plus model signals, route to per-language configs, handle mixed content explicitly, and evaluate each language on its own judged set.

Optimize simultaneously for:

- reliable detection
- routed pipelines
- correct scripts
- handled mixing
- fair eval

No language shunted through English-only tooling; low-confidence detections quarantined, not guessed.

## Use Cases

### Mixed crawl

Trigger: user says 'many languages' or 'split by language'

Steps:

1. Detect all
2. Route per lang
3. Eval each
4. Report coverage

Result: Organized corpus.

### Bad detection

Trigger: user says 'wrong language tags' or 'short text'

Steps:

1. Add script signals
2. Threshold confidence
3. Quarantine unsure
4. Fix routing

Result: Trusted tags.

### Fair eval

Trigger: user says 'English metrics only' or 'other languages worse'

Steps:

1. Judge per language
2. Fix gaps
3. Report all
4. Ship fairly

Result: Multilingual quality.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Detection eval
- Routing table
- Per-lang configs
- Mixed policy
- Per-lang eval sets
- Coverage report
- Quarantine log
- Locale table

Never guess low-confidence languages or eval multilingual systems on English alone.

## Phase 1 — Detect

Script ratios plus model vote.

Sketch with `scripts/lang_guess.py --in docs.txt`.

Confidence threshold; quarantine below.

## Phase 2 — Route

Per-language clean/chunk/eval configs.

Mixed docs split or flagged.

Log routing decisions.

## Phase 3 — Eval per Language

Judged sets per top language.

Report all; fix worst first.

Low-resource gets care budget.

## Phase 4 — Govern

Locale table versioned.

Coverage dashboard.

Review quarterly.

## Examples

### Example 1: Crawl organized

User says: "20 languages mixed."

Actions:

1. Detected 98 percent
2. Routed 8 pipelines
3. Eval per lang
4. Quality up everywhere

Result: Multilingual order.

### Example 2: Short-text fix

User says: "Titles mistagged."

Actions:

1. Script priors added
2. Threshold quarantine
3. Accuracy 70 to 95
4. Locked

Result: Reliable tags.

## Troubleshooting

### Short text wrong

Cause: N-grams starved

Fix:

1. Script priors
2. Metadata hints
3. Higher threshold
4. Quarantine more

### Code-switch chaos

Cause: One label per doc

Fix:

1. Segment by script
2. Multi-label
3. Route mixed pipeline
4. Eval mixed set

### Low-resource neglected

Cause: No eval set

Fix:

1. Build 100+ judged
2. Care budget
3. Report gap
4. Fix deliberately

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Detect.
- Route.
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

Avoid english-only eval; threshold-free guessing; script-blind chunking; mixed-ignoring routes; locale-free ops; low-resource neglect.

## Bundled References

Read `references/multilingual-ops.md` when detecting or routing languages.
Run `scripts/lang_guess.py` to sketch script-based language signals.
Copy `assets/checklists.md` into every delivery.
