---
name: geo-exit-verification
description: Target egress geography precisely and verify every exit independently. Use when the user asks to verify proxy geolocation; test localized content; check exit IP and ASN; detect geo drift; build geo test matrix.
compatibility: Geo database or API for checks; provider geo controls; owned or permitted test targets.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Geo Exit Verification

Prove where traffic exits. You target only what localization needs, verify exits with independent checks, catch drift in minutes, cover matrices measurably, and file scope for every audit.

Optimize simultaneously for:

- precise targeting
- verified exits
- fast drift catch
- covered matrices
- filed scopes

Geo testing for legitimate localization on permitted targets only; never to bypass geo-restrictions or licensing.

## Use Cases

### Localization QA

Trigger: user says 'test 5 locales' or 'verify translations'

Steps:

1. Define matrix
2. Target per locale
3. Verify exits
4. Test and file

Result: Covered localization.

### Drift alarm

Trigger: user says 'wrong country content' or 'geo mismatch'

Steps:

1. Verify exit now
2. Quarantine egress
3. Escalate evidence
4. Re-verify fix

Result: Corrected targeting.

### Audit proof

Trigger: user says 'prove test scope' or 'geo audit'

Steps:

1. Pull scope docs
2. Show verifications
3. List targets
4. File report

Result: Auditable geo testing.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Geo needs per locale
- Test matrix
- Verification log
- Drift alerts
- Mismatch tickets
- Scope docs
- Consent records
- Coverage report

Never target geo to bypass restrictions, and never trust provider labels without verification.

## Phase 1 — Define Matrix

Locales, tiers, targets, consent.

Minimize: country over city unless needed.

Sign off scope.

## Phase 2 — Verify Exits

Run `scripts/exit_verify.py --proxy URL` per egress.

Cross-check two geo sources.

Log IP, geo, ASN, rDNS.

## Phase 3 — Detect Drift

Verify on schedule plus on mismatch signal.

Quarantine drifted egress.

Escalate with evidence.

## Phase 4 — Prove Coverage

Matrix green per locale.

File scope and logs.

Review quarterly.

## Examples

### Example 1: Locale launch

User says: "Launch in 8 countries."

Actions:

1. Matrix built, exits verified
2. QA per locale green
3. Scope filed
4. Launch clean

Result: Verified localization.

### Example 2: Drift caught

User says: "German users see US prices."

Actions:

1. Exit verified wrong in 5 min
2. Egress quarantined
3. Provider fixed
4. Monitoring added

Result: Fast correction.

## Troubleshooting

### Geo flaps

Cause: Anycast or pool mixing

Fix:

1. Pin per-locale egress
2. Verify per session
3. Exclude flapping
4. Escalate

### rDNS mismatches geo

Cause: Stale PTR or multi-geo block

Fix:

1. Weight IP-geo over rDNS
2. Document exception
3. Verify content locale
4. Monitor

### Provider disputes

Cause: Their DB differs

Fix:

1. Present dual-source proof
2. Request re-target
3. Withhold payment per SLA
4. Switch egress

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Define.
- Verify.
- Watch.

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

Avoid restriction bypass; label-trusting; verification-free geo; drift-blind pools; scope-free testing; city-by-default.

## Bundled References

Read `references/geo-testing.md` when targeting or verifying egress geo.
Run `scripts/exit_verify.py` to verify exit IP via echo endpoints.
Copy `assets/checklists.md` into every delivery.
