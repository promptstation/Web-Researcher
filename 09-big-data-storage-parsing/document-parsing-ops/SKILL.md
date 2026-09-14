---
name: document-parsing-ops
description: Triage document sets and extract text plus tables with honest OCR calls. Use when the user asks to extract text from PDFs; parse tables from documents; decide when to OCR; handle scanned PDFs; preserve document layout.
compatibility: Python 3.10+; pypdf/pdfplumber/python-docx/openpyxl per format; tesseract for OCR samples.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Document Parsing Ops

Turn document piles into data deliberately. You triage by type and value, extract native text cleanly, OCR only where sampling justifies cost, recover tables with structure, and preserve the layout signals downstream needs.

Optimize simultaneously for:

- triaged corpora
- clean native text
- justified OCR
- structured tables
- kept layout

Sample before committing: no bulk OCR or reprocessing without measured quality and cost.

## Use Cases

### PDF backlog

Trigger: user says 'thousands of PDFs' or 'extract all text'

Steps:

1. Triage the set
2. Extract native first
3. Sample OCR need
4. Process by value

Result: Prioritized extraction.

### Table recovery

Trigger: user says 'tables lost' or 'need spreadsheet data'

Steps:

1. Pick table tool
2. Recover structured
3. Verify cells
4. Lock method

Result: True tables.

### Scan decision

Trigger: user says 'scanned documents' or 'OCR everything?'

Steps:

1. Sample 50 pages
2. Score quality
3. Cost the run
4. Decide by value

Result: Honest OCR call.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Triage report
- Tool choices
- OCR sample scores
- Cost estimate
- Table method
- Layout spec
- Quality dashboard
- Reprocess log

Never bulk-OCR without sampling or flatten tables into unordered text.

## Phase 1 — Triage Set

Scan with `scripts/doc_triage.py --dir docs/` for type/size/native signals.

Bucket native, scanned, mixed, corrupt.

Rank by value x feasibility.

## Phase 2 — Extract Native

pdf: pypdf then pdfplumber; docx: python-docx; xlsx: openpyxl.

Keep headings, lists, order.

Quarantine failures coded.

## Phase 3 — Decide OCR

Sample 50+ pages; score CER roughly.

Cost full run; decide by value.

Pilot 5 percent before all.

## Phase 4 — Recover Tables

Bordered: camelot/tabula; borderless: pdfplumber.

Verify headers and totals.

Store with cell coordinates.

## Examples

### Example 1: Triage win

User says: "50k PDFs, where to start?"

Actions:

1. 70 percent native-easy
2. 20 OCR-worthy, 10 skip
3. Value-ordered queue
4. Done in weeks not months

Result: Smart sequencing.

### Example 2: Tables saved

User says: "Financial tables garbled."

Actions:

1. pdfplumber lattice mode
2. Totals verified
3. Structured store
4. Auditors happy

Result: True financial tables.

## Troubleshooting

### Text order scrambled

Cause: Multi-column or absolute positioning

Fix:

1. Layout-aware extraction
2. Column detection
3. Reading-order pass
4. Verify samples

### OCR garbage

Cause: Low DPI or skew

Fix:

1. Preprocess (deskew, 300dpi)
2. Resample
3. Limit to worthy
4. Human-review critical

### Tables merge/split

Cause: Borderless or spanning cells

Fix:

1. Tune table settings
2. Manual rules per template
3. Verify totals
4. Quarantine odd

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Triage.
- Extract.
- Decide.

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

Avoid OCR-everything; sample-free commitments; flattened tables; layout-blind extraction; tool-monoculture; quality-blind bulk.

## Bundled References

Read `references/document-extraction.md` when extracting from PDFs or Office files.
Run `scripts/doc_triage.py` to triage document folders.
Copy `assets/checklists.md` into every delivery.
