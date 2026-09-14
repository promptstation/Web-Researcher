---
name: ocr-operations
description: Run OCR with measured accuracy, honest limits, and review routing. Use when the user asks to choose an OCR engine; measure OCR accuracy; preprocess scans for OCR; handle OCR tables; route low-confidence OCR to review.
compatibility: Tesseract/paddle/cloud OCR per bake-off; 100+ ground-truth pages for eval.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# OCR Operations

Read documents with receipts. You preprocess deliberately, bake engines off on your pages, score CER/WER honestly, handle tables and handwriting within stated limits, and route weak spans to review.

Optimize simultaneously for:

- tuned preprocessing
- judged engines
- scored accuracy
- handled tables
- routed review

No accuracy claim without CER/WER on representative ground truth; no critical field without review path.

## Use Cases

### Engine pick

Trigger: user says 'Tesseract or cloud' or 'best OCR'

Steps:

1. Ground-truth 100 pages
2. Bake off engines
3. Score CER/WER
4. Decide with cost

Result: Evidence-backed engine.

### Bad scans

Trigger: user says 'OCR garbage' or 'old documents'

Steps:

1. Preprocess sweep
2. Measure lift
3. Limit scope honestly
4. Review the rest

Result: Best-possible reads.

### Critical fields

Trigger: user says 'invoice totals must be right' or 'IDs'

Steps:

1. Field-level eval
2. Confidence routing
3. Human SLA
4. Verify precision

Result: Trusted fields.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Ground-truth set
- Preprocess spec
- Bake-off scores
- CER/WER report
- Table method
- Review SLA
- Cost model
- Limit statement

Never claim accuracy without ground-truth eval or auto-accept critical fields.

## Phase 1 — Ground Truth

100+ representative pages transcribed.

Tables and hard cases included.

Version the set.

## Phase 2 — Preprocess

Deskew, denoise, 300 DPI, gentle binarize.

Ablate each step on CER.

Lock winners.

## Phase 3 — Bake Off

Score engines with `scripts/ocr_eval.py --ref ref.txt --hyp hyp.txt`.

CER plus WER plus table checks.

Decide with cost.

## Phase 4 — Route Review

Confidence thresholds per field.

Human SLA and queue.

Reprocess loop for fixes.

## Examples

### Example 1: Engine truth

User says: "Cloud OCR worth it?"

Actions:

1. Bake-off: CER 8 to 2
2. Cost 20x
3. Hybrid: cloud for tables only
4. Best of both

Result: Cost-smart OCR.

### Example 2: Totals trusted

User says: "Invoice totals must hit 99.9."

Actions:

1. Field eval plus review
2. Precision 99.95
3. SLA met
4. Auditors calm

Result: Trusted extraction.

## Troubleshooting

### CER varies wildly

Cause: Unrepresentative eval set

Fix:

1. Stratify ground truth
2. Add hard buckets
3. Re-score
4. Report by bucket

### Tables collapse

Cause: Line-based OCR on tables

Fix:

1. Table-aware engine
2. Cell eval
3. Review tables
4. State limits

### Review queue floods

Cause: Threshold too high

Fix:

1. Tune per field value
2. Calibrate confidence
3. Sample audit
4. Re-tune monthly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Truth.
- Score.
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

Avoid ground-truth-free claims; preprocess-free OCR; engine hype picks; table-blind eval; review-free criticals; bucket-free scores.

## Bundled References

Read `references/ocr-eval.md` when evaluating or routing OCR.
Run `scripts/ocr_eval.py` to score CER/WER.
Copy `assets/checklists.md` into every delivery.
