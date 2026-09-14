---
name: own-defense-testing
description: Red-team bot defenses you own with scoped probes and verified fixes. Use when the user asks to test my own rate limits; red-team our bot defenses; scope a defense self-test; verify a bot-control fix; review challenge UX impact.
compatibility: Systems you own or are contracted to test; staging preferred; written authorization required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Own Defense Testing

Harden your own gates fairly. You scope engagements in writing, probe staging safely, grade findings honestly, report reproducibly, and verify fixes with identical retests.

Optimize simultaneously for:

- written scope
- safe probes
- graded findings
- reproducible reports
- verified fixes

Owned or contracted systems only with written authorization; staging first, production only if explicitly approved.

## Use Cases

### Pre-launch test

Trigger: user says 'test before launch' or 'are limits right'

Steps:

1. Scope in writing
2. Probe staging safely
3. Grade findings
4. Fix and retest

Result: Hardened launch.

### False-positive check

Trigger: user says 'legit users blocked' or 'challenge too harsh'

Steps:

1. Replay legit journeys
2. Measure challenge rates
3. Tune thresholds
4. Verify UX recovery

Result: Balanced defense.

### Fix verification

Trigger: user says 'confirm the patch' or 'retest needed'

Steps:

1. Rerun identical probes
2. Compare to baseline
3. Sign off or iterate
4. File the record

Result: Proven fix.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Authorization letter
- Scope sheet
- Probe log
- Finding reports
- Severity grades
- Fix advice
- Retest evidence
- Sign-off record

Never test systems without authorization, and never probe production beyond the written scope.

## Phase 1 — Scope in Writing

Define hosts, paths, windows, and stop conditions.

Get signed authorization.

Confirm staging parity or production approval.

## Phase 2 — Probe Safely

Run `scripts/defense_selftest.py --target <staging> --rate 5` within scope.

Log every probe with purpose.

Stop on unexpected impact.

## Phase 3 — Grade and Report

Severity by exploitability times impact.

Write reproduction per finding.

Advise precise fixes.

## Phase 4 — Retest and Sign Off

Rerun identical probes post-fix.

Compare to baseline evidence.

Sign off with records filed.

## Examples

### Example 1: Limit tuning

User says: "Are our API limits sane?"

Actions:

1. Scoped staging test
2. Found 10x-loose limit
3. Tightened with UX check
4. Retest green

Result: Right-sized limits.

### Example 2: Challenge UX

User says: "Users complain about checks."

Actions:

1. Measured 22 percent challenged
2. Tuned to 4 percent, attacks still blocked
3. UX recovered
4. Monitoring kept

Result: Balanced friction.

## Troubleshooting

### Staging differs from prod

Cause: Config or data drift

Fix:

1. Diff configs first
2. Mirror production rules
3. Note residual gaps
4. Limit claims accordingly

### Probe causes incident

Cause: Scope or rate exceeded

Fix:

1. Stop immediately
2. Notify owner
3. Roll back change
4. Tighten future scopes

### Fix fails retest

Cause: Partial deploy or cached rules

Fix:

1. Confirm deploy scope
2. Purge edge caches
3. Rerun identical probes
4. Iterate to green

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Scope.
- Probe.
- Close.

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

Avoid unauthorized testing; production-first probes; scope creep mid-test; unlogged probes; findings without retests; results reused offensively.

## Bundled References

Read `references/selftest-rules.md` when scoping or running defense tests.
Run `scripts/defense_selftest.py` to probe owned staging limits within scope.
Copy `assets/checklists.md` into every delivery.
