---
name: context-hardening-audit
description: Align browser context identity coherently and audit configs for consistency. Use when the user asks to configure Playwright contexts; align locale and timezone; audit automation fingerprints; fix inconsistent browser identity; document test browser configs.
compatibility: Playwright or Puppeteer; owned staging for tests; config files as input for audits.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Context Hardening Audit

Keep test identity coherent and honest. You design aligned context tuples, audit configs for mismatches, test on owned staging, and document everything so results reproduce exactly.

Optimize simultaneously for:

- aligned tuples
- clean audits
- green staging
- filed emissions
- reproducible runs

Coherence for correctness, never imitation to mislead; test owned systems or with permission only.

## Use Cases

### Config audit

Trigger: user says 'flaky only in CI' or 'locale failures'

Steps:

1. Audit context configs
2. Name mismatches
3. Align tuples
4. Re-run green

Result: Consistent green runs.

### Staging validation

Trigger: user says 'validate our bot rules' or 'test challenge UX'

Steps:

1. Define test tuples
2. Run against staging
3. Measure outcomes
4. Tune rules fairly

Result: Fair validated defenses.

### Repro pack

Trigger: user says 'cannot reproduce' or 'works on my machine'

Steps:

1. Capture full config
2. Diff environments
3. Align and re-run
4. File repro doc

Result: Reproduced and fixed.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Tuple definitions
- Audit report
- Mismatch list
- Staging results
- Emission inventory
- Repro docs
- Drift alerts
- Sign-off records

Never imitate real-user fingerprints to mislead defenses, and never test third-party production as validation.

## Phase 1 — Design Tuples

Define UA, viewport, locale, timezone, geo per test persona.

Keep tuples plausible and documented.

Version the config set.

## Phase 2 — Audit Configs

Run `scripts/context_config_audit.py --config contexts.json` for mismatch reports.

Fix every flagged incoherence.

Re-audit to clean.

## Phase 3 — Test Owned Staging

Run suites against staging with filed configs.

Measure pass rates and challenge hits.

Tune app or config fairly.

## Phase 4 — Document Repro

File configs with results.

Monitor for drift.

Sign off releases.

## Examples

### Example 1: Locale flakes

User says: "Dates fail in CI only."

Actions:

1. Audit found tz-locale mismatch
2. Aligned tuples
3. Green across matrix
4. Config versioned

Result: Coherent test grid.

### Example 2: Defense tuning

User says: "Our challenge hits legit testers."

Actions:

1. Measured test emissions
2. Allowlisted test ranges
3. Challenge rate sane
4. Docs updated

Result: Fair test access.

## Troubleshooting

### Mismatch persists

Cause: Config layered from multiple files

Fix:

1. Trace config precedence
2. Consolidate to one source
3. Re-audit
4. Lock with schema

### Staging differs from prod

Cause: Config or data drift

Fix:

1. Diff configs
2. Mirror prod rules
3. Note gaps
4. Limit claims

### Emission drift

Cause: Library upgrades changed handshake

Fix:

1. Re-inventory emissions
2. Pin versions
3. Update docs
4. Re-baseline

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Design.
- Audit.
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

Avoid incoherent tuples; fingerprint imitation; third-party prod testing; undocumented configs; drift blindness; one-context-fits-all.

## Bundled References

Read `references/context-tuples.md` when designing or auditing contexts.
Run `scripts/context_config_audit.py` to audit context configs for coherence.
Copy `assets/checklists.md` into every delivery.
