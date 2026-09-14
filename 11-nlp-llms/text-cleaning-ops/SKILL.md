---
name: text-cleaning-ops
description: Clean scraped text with repaired encoding and meaning-preserving normalization. Use when the user asks to clean scraped text; fix mojibake; remove boilerplate from articles; normalize unicode text; dedupe repeated content.
compatibility: Python 3.10+ stdlib; ftfy optional for hard mojibake; 100+ sample docs for verification.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# Text Cleaning Ops

Turn scraped soup into clean text. You repair encodings, normalize unicode and whitespace, strip boilerplate measurably, dedupe repeats, and verify on before/after samples with locked fixtures.

Optimize simultaneously for:

- repaired encoding
- sane unicode
- no boilerplate
- lean text
- verified meaning

Cleaning never invents content; structure that matters (lists, headings) survives.

## Use Cases

### Dirty corpus

Trigger: user says 'text full of junk' or 'menus in articles'

Steps:

1. Profile dirt classes
2. Clean staged
3. Verify sampled
4. Lock fixtures

Result: Clean corpus.

### Mojibake

Trigger: user says 'weird characters' or 'encoding broken'

Steps:

1. Detect truly
2. Repair mapped
3. Verify reads
4. Fix pipeline

Result: Readable text.

### Syndication

Trigger: user says 'same article 50 times' or 'copies everywhere'

Steps:

1. Hash normalized
2. Keep canonical
3. Link copies
4. Prove lean

Result: Canonical corpus.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Dirt taxonomy
- Cleaning config
- Before/after samples
- Quality metrics
- Fixtures
- Encoding log
- Dedupe report
- Pipeline fix

Never clean destructively without raw kept or ship uninspected normalization.

## Phase 1 — Profile Dirt

Sample 200; classes of junk.

Measure with `scripts/text_clean.py --in sample.txt --report`.

Prioritize by frequency x harm.

## Phase 2 — Clean Staged

Encoding, unicode, whitespace, boilerplate, dedupe in order.

Config versioned.

Raw always kept.

## Phase 3 — Verify Meaning

100 before/after by eye.

Structure spot-checks.

Fix over-cleaning.

## Phase 4 — Lock

Fixtures 50+.

Metrics per batch.

Alert on drift.

## Examples

### Example 1: News cleanup

User says: "Crawl text unusable."

Actions:

1. Staged cleaning
2. Boilerplate 30 to 1 percent
3. Fixtures locked
4. Downstream happy

Result: Usable corpus.

### Example 2: Encoding rescue

User says: "Accents destroyed."

Actions:

1. True encoding found
2. Repaired plus pipeline fix
3. Verified reads
4. Never again

Result: Faithful text.

## Troubleshooting

### Over-cleaning

Cause: Aggressive rules eat content

Fix:

1. Soften rules
2. Allowlist structures
3. Re-verify
4. Fixture the case

### Mixed languages mangled

Cause: One-size normalization

Fix:

1. Detect per doc
2. Normalize per script
3. Test multilingual
4. Fixture each

### Cleaning drifts

Cause: Unversioned ad-hoc fixes

Fix:

1. Version config
2. Gate on fixtures
3. Review changes
4. Changelog

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Profile.
- Clean.
- Lock.

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

Avoid destructive cleaning; raw-discarding; one-shot scripts; eye-free normalization; fixture-free changes; structure-flattening.

## Bundled References

Read `references/text-cleaning.md` when cleaning scraped text.
Run `scripts/text_clean.py` to clean text files.
Copy `assets/checklists.md` into every delivery.
