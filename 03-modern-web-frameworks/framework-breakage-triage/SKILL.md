---
name: framework-breakage-triage
description: Catch upgrade breakage from contract diffs and recover with versioned fixes and backfills. Use when the user asks to detect site changes breaking scrapers; diff DOM contracts; triage extractor failures; backfill after a fix; monitor for site deploys.
compatibility: Any OS with Python 3.10+ and HTTPS; snapshot storage (files or git); no browsers needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# Framework Breakage Triage

Turn surprise breakage into routine maintenance. You watch deploy signals, diff contracts every run, classify scope fast, ship versioned fixes, and backfill windows without gaps or duplicates.

Optimize simultaneously for:

- watched deploys
- diffed contracts
- classified scope
- versioned fixes
- clean backfills

Do not hot-patch extractors without version bumps, and never backfill without idempotent record IDs.

## Use Cases

### Morning breakage

Trigger: user says 'feed empty since last night' or 'selectors dead'

Steps:

1. Confirm deploy signals
2. Diff contracts to the change
3. Classify scope
4. Fix, version, backfill

Result: Recovered feed with trail.

### Drift watch

Trigger: user says 'catch changes early' or 'alert before empty'

Steps:

1. Snapshot contracts nightly
2. Diff and alert on deltas
3. Triage before data loss
4. Fix proactively

Result: Breakage caught pre-impact.

### Template rollout

Trigger: user says 'new design rolling out' or 'A/B layouts'

Steps:

1. Detect variant split
2. Support both shapes versioned
3. Route by detected variant
4. Retire old on completion

Result: Coverage through redesign.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Signal checks with thresholds
- Contract snapshots
- Diff reports
- Scope classification
- Versioned fix notes
- Backfill receipts
- Alert tuning log
- Run timeline

Never hot-patch without versions, and never skip backfill verification.

## Phase 1 — Watch Signals

Track buildId, chunk names, headers, and payload versions per run.

Alert on any rotation or rename.

Snapshot contracts on every green run.

## Phase 2 — Diff on Red

Run `scripts/dom_contract_diff.py --old snap.html --new now.html` to localize changes.

Separate cosmetic from structural diffs.

Name the changed template and region.

## Phase 3 — Fix Versioned

Bump extractor and schema versions.

Dual-read during transitions.

Verify on fixtures plus live samples.

## Phase 4 — Backfill Clean

Define the affected window precisely.

Re-run idempotently with record IDs.

Verify counts and dedupe rates.

## Examples

### Example 1: Overnight restyle

User says: "Prices vanished overnight."

Actions:

1. Diff showed class rename in price region
2. Shipped v4 selectors same morning
3. Backfilled 9 hours
4. Zero gaps

Result: Fast clean recovery.

### Example 2: A/B templates

User says: "Half the pages look different."

Actions:

1. Detected 50/50 variant split
2. Supported both shapes
3. Routed by marker
4. Retired old post-rollout

Result: Coverage through redesign.

## Troubleshooting

### Diffs too noisy

Cause: Timestamps, ads, and A/B noise

Fix:

1. Normalize volatile regions
2. Scope diffs to data regions
3. Allowlist known noise
4. Re-tune to signal

### Backfill duplicates

Cause: Non-idempotent writes or changed IDs

Fix:

1. Enforce stable record IDs
2. Dedupe on re-emit
3. Verify counts pre/post
4. Fix ID derivation

### Fix works then breaks again

Cause: Rolling deploy with mixed versions

Fix:

1. Support N and N-1 shapes
2. Detect version per response
3. Route accordingly
4. Retire when stable

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Watch.
- Triage.
- Recover.

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

Avoid hot-patches without versions; undiffed breakage fixes; scope guessed not classified; backfills without idempotency; noisy undifferentiated diffs; single-shape fixes during rollouts.

## Bundled References

Read `references/contract-diffs.md` when snapshotting or diffing templates.
Run `scripts/dom_contract_diff.py` to diff data-region contracts between snapshots.
Copy `assets/checklists.md` into every delivery.
