---
name: cv-dataset-building
description: Build lawful, deduped, versioned image datasets with provenance. Use when the user asks to build an image dataset; dedupe images; check image licenses; record image provenance; version a dataset.
compatibility: Python 3.10+; Pillow/ImageHash for perceptual work; license review per source.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# CV Dataset Building

Collect pixels with papers. You license-check every source, provenance-log every image, dedupe exactly and perceptually, filter corrupt files, and version datasets so experiments reproduce.

Optimize simultaneously for:

- licensed corpora
- logged provenance
- zero exact dupes
- low near-dupes
- versioned sets

No image without license and provenance; no dataset version without manifest.

## Use Cases

### New corpus

Trigger: user says 'collect training images' or 'build dataset'

Steps:

1. Clear licenses
2. Crawl politely
3. Dedupe both ways
4. Version v1

Result: Clean lawful corpus.

### Dirty set

Trigger: user says 'dupes in training' or 'leakage suspected'

Steps:

1. Hash all
2. Exact plus near pass
3. Split decontaminated
4. Prove clean

Result: Leak-free splits.

### Audit ready

Trigger: user says 'prove sourcing' or 'dataset audit'

Steps:

1. Pull manifests
2. Show licenses
3. List exclusions
4. File report

Result: Auditable dataset.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Source license table
- Provenance schema
- Dedupe reports
- Corrupt filter log
- Manifest v1
- Split record
- Bias notes
- Changelog

Never train on unlicensed images or split before deduping across splits.

## Phase 1 — Clear Sources

License per source; robots and ToS checked.

Consent for personal images.

Document exclusions.

## Phase 2 — Ingest Clean

Run `scripts/img_inventory.py --dir images/` for type/dup/corrupt scan.

Exact-dedupe by hash; quarantine corrupt.

Provenance-log every keeper.

## Phase 3 — Near-Dedupe

Average-hash within 5 bits.

Review clusters; keep best.

Decontaminate across splits.

## Phase 4 — Version

Manifest: files, hashes, licenses, splits.

Changelog per version.

Freeze for experiments.

## Examples

### Example 1: Clean corpus

User says: "50k product photos needed."

Actions:

1. Licensed 3 sources
2. 12 percent dupes removed
3. Manifest v1 frozen
4. Audit passed

Result: Trusted training set.

### Example 2: Leak fixed

User says: "Val accuracy suspiciously high."

Actions:

1. Near-dupes across splits found
2. Decontaminated
3. Honest metrics
4. Lesson filed

Result: True evaluation.

## Troubleshooting

### License gaps

Cause: Scraped without review

Fix:

1. Halt and triage
2. Remove unlicensed
3. Re-source cleanly
4. Gate future ingests

### Corrupt images crash loaders

Cause: No ingest validation

Fix:

1. Verify all at ingest
2. Quarantine bad
3. Test loaders
4. Monitor continually

### Split leakage

Cause: Deduped after splitting

Fix:

1. Dedupe first globally
2. Re-split
3. Verify cross-split
4. Lock procedure

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Clear.
- Clean.
- Freeze.

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

Avoid license-free scraping; provenance-free pixels; split-then-dedupe; corrupt-tolerant ingest; manifest-free versions; bias-blind collection.

## Bundled References

Read `references/dataset-hygiene.md` when building or auditing image datasets.
Run `scripts/img_inventory.py` to inventory image folders.
Copy `assets/checklists.md` into every delivery.
