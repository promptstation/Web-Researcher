---
name: web-quality-mining
description: Score page quality with fused signals and filter junk provably. Use when the user asks to detect spam pages; score content quality; filter thin content; tune quality thresholds; evaluate spam filters.
compatibility: Python 3.10+; crawl features; 200+ judged pages for tuning.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Web Quality Mining

Keep junk out with receipts. You catalog signals, fuse them into scores, tune thresholds on judged samples, filter thin and spam, and track precision so appeals stay rare and fair.

Optimize simultaneously for:

- rich signals
- fused scores
- tuned thresholds
- clean corpora
- tracked precision

Filters judged before enforcing; appeals heard; borderline humans review.

## Use Cases

### Index clean

Trigger: user says 'spam in index' or 'junk ranking'

Steps:

1. Score all
2. Tune threshold
3. Filter + appeal
4. Track precision

Result: Clean index.

### Corpus quality

Trigger: user says 'thin content' or 'training data dirty'

Steps:

1. Filter thin/dupe
2. Judge samples
3. Verify lift
4. Lock pipeline

Result: Quality corpus.

### Farm removal

Trigger: user says 'link spam' or 'scraped copies'

Steps:

1. Detect clusters
2. Confirm evidence
3. Demote/remove
4. Monitor

Result: Spam out.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Signal catalog
- Fusion weights
- Threshold rationale
- Judged set 200+
- Precision report
- Appeal log
- Filter code version
- Review cadence

Never auto-filter without judged tuning or block appeals.

## Phase 1 — Signal Up

Content + link + behavior features.

Baseline with `scripts/quality_score.py --file page.html`.

Coverage per signal.

## Phase 2 — Fuse and Tune

Weighted score; threshold on judged.

Precision target (e.g., 0.95+).

Borderline band to humans.

## Phase 3 — Filter

Apply versioned; log decisions.

Appeal path live.

Monitor rates.

## Phase 4 — Track

Precision sampled monthly.

Adversarial review.

Re-tune quarterly.

## Examples

### Example 1: Index detox

User says: "Spam ranking top 10."

Actions:

1. Fused scorer
2. Precision 0.97
3. Spam out
4. Appeals 3, all fair

Result: Trusted index.

### Example 2: Training clean

User says: "Model parrots spam."

Actions:

1. Filtered 22 percent junk
2. Quality up
3. Retrained better
4. Pipeline kept

Result: Clean training.

## Troubleshooting

### Good filtered

Cause: Threshold hot or signal biased

Fix:

1. Review appeals fast
2. Tune cooler
3. Fix signal
4. Restore + apologize

### Spam adapts

Cause: Static signals

Fix:

1. Adversarial review
2. New signals
3. Re-tune
4. Rotate features

### Precision unknown

Cause: No judging habit

Fix:

1. Judge 200 now
2. Monthly samples
3. Track trend
4. Gate changes

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Build.
- Run.
- Keep.

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

Avoid signal-poor filters; judge-free thresholds; appeal-free blocks; static spam defenses; precision-blind ops; viewpoint filtering.

## Bundled References

Read `references/quality-spam.md` when scoring quality or fighting spam.
Run `scripts/quality_score.py` to sketch content quality signals.
Copy `assets/checklists.md` into every delivery.
