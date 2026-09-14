---
name: wait-synchronization-mastery
description: Synchronize with layered waits and eliminate flakes by classified cause. Use when the user asks to fix flaky waits; remove sleep calls; size Playwright timeouts; classify test flakes; debug timing failures.
compatibility: Playwright, Puppeteer, or Selenium; traces for debugging; no new libraries.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Wait Synchronization Mastery

Make timing deterministic. You layer waits by purpose, size retries from data, scope network waits safely, classify every flake, and hunt sleeps to zero with repeat-run proof.

Optimize simultaneously for:

- layered waits
- sized retries
- safe scoping
- classified flakes
- zero sleeps

No sleeps in committed code; every flake gets a class, a trace, and a fix.

## Use Cases

### Flake triage

Trigger: user says 'intermittent failures' or 'CI roulette'

Steps:

1. Collect traces
2. Classify each flake
3. Fix by class
4. Prove with repeats

Result: Deterministic suite.

### Sleep purge

Trigger: user says 'sleeps everywhere' or 'slow suite'

Steps:

1. Inventory sleeps
2. Replace per need
3. Verify faster and stable
4. Forbid regressions

Result: Fast stable suite.

### Timeout policy

Trigger: user says 'timeouts too short' or 'CI slower'

Steps:

1. Measure timing distributions
2. Size per operation
3. Separate CI multipliers
4. Document policy

Result: Calibrated timeouts.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Wait map per flow
- Retry sizing notes
- Scope justifications
- Flake log classified
- Sleep inventory at zero
- Repeat-run evidence
- Timeout policy
- Quarantine rules

Never merge sleeps or unscoped networkidle, and never close flakes without classification.

## Phase 1 — Map Waits

List every wait per flow with its purpose.

Run `scripts/flake_classifier.py --logs failures.jsonl` on recent failures for cause hints.

Mark sleeps and global idles for removal.

## Phase 2 — Layer Correctly

URL assertions for navigation, locator assertions for data.

Response waits scoped to exact endpoints.

Auto-retry as the default mechanism.

## Phase 3 — Classify Flakes

Read traces: timing, selector, data, env, product.

Fix the class, not the symptom.

Quarantine only with expiry and owner.

## Phase 4 — Prove Stable

Repeat runs 20-50x per fix.

Chart flake rate to near zero.

Lock policy in review.

## Examples

### Example 1: CI roulette

User says: "30 percent flake rate in CI."

Actions:

1. Classified: 60 timing, 30 data, 10 env
2. Fixed per class in 2 weeks
3. Rate to under 1 percent
4. Policy locked

Result: Trusted CI.

### Example 2: Idle deadlock

User says: "Waits hang on dashboard."

Actions:

1. Polling endpoint found
2. Scoped to data responses
3. Suite 3x faster
4. Pattern documented

Result: Correct scoping.

## Troubleshooting

### Assertion timeout spikes

Cause: Undersized retries on slow env

Fix:

1. Measure p95 per operation
2. Size retries above it
3. Separate CI multipliers
4. Re-verify

### Fixed locally, flakes in CI

Cause: Resource or parallelism gaps

Fix:

1. Match CI resources
2. Reduce workers
3. Raise retries for CI
4. Prove with CI repeats

### One flake resists classification

Cause: Product race or A/B variant

Fix:

1. Capture video plus trace
2. Bisect with feature flags
3. File as product bug
4. Quarantine with expiry

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Fix.
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

Avoid sleep-driven sync; unscoped networkidle; unclassified flakes; quarantine forever; timeout guessing; single-run proof.

## Bundled References

Read `references/wait-layers.md` when designing waits or fixing flakes.
Run `scripts/flake_classifier.py` to triage failure logs by likely cause.
Copy `assets/checklists.md` into every delivery.
