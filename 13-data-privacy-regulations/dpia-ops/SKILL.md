---
name: dpia-ops
description: Run DPIAs that find real risks and drive mitigations to done. Use when the user asks to run a DPIA; screen for high-risk processing; assess privacy risk; consult on data protection; track privacy mitigations.
compatibility: DPO access; project intake gate; risk register.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# DPIA Ops

Surface privacy risk before launch. You screen every project, DPIA the risky with rigor, consult DPO and subjects genuinely, track mitigations to done, and keep assessments living — escalating residual high risk before it ships.

Optimize simultaneously for:

- screened intake
- rigorous DPIAs
- real consultation
- done mitigations
- living reviews

High-risk processing waits for DPIA; unmitigated high residual risk escalates, never ships quietly.

## Use Cases

### New feature

Trigger: user says 'launch scoring' or 'new tracking'

Steps:

1. Screen triggers
2. DPIA if hit
3. Mitigate tracked
4. Launch gated

Result: Risk-managed launch.

### Vendor AI

Trigger: user says 'AI vendor processes PII' or 'profiling?'

Steps:

1. Screen high
2. DPIA deep
3. Contract mitigations
4. Monitor live

Result: Controlled adoption.

### DPIA audit

Trigger: user says 'show assessments' or 'regulator asks'

Steps:

1. Pull register
2. Show mitigations
3. List reviews
4. File evidence

Result: Evidenced program.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Screening checklist
- DPIA docs
- Risk scores
- Consult records
- Mitigation tracker
- Residual decisions
- Register
- Review dates

Never skip screening or ship unmitigated high residual risk.

## Phase 1 — Screen All

Triggers: sensitive, large, profiling, monitoring, tech, vulnerable.

Gate intake; log decisions.

DPO triages borderline.

## Phase 2 — Assess Deep

Scaffold with `scripts/dpia_scaffold.py --project NAME`.

Describe, necessity, risks scored.

Mitigations per risk.

## Phase 3 — Consult Real

DPO opinion filed.

Subjects/vendors where apt.

Authority if residual high.

## Phase 4 — Track Living

Owners + dates; verify done.

Review on change/yearly.

Register current.

## Examples

### Example 1: Scoring gated

User says: "Launch lead scoring?"

Actions:

1. DPIA found bias risk
2. Mitigated + monitored
3. Launched scoped
4. Reviewed quarterly

Result: Responsible launch.

### Example 2: Stopped launch

User says: "Track all visitors?"

Actions:

1. High residual unmitigable
2. Escalated, paused
3. Redesigned minimal
4. Shipped safe v2

Result: Harm prevented.

## Troubleshooting

### DPIA theater

Cause: Post-hoc checkbox

Fix:

1. Gate pre-launch
2. DPO challenge
3. Real mitigations
4. Verify done

### Mitigations rot

Cause: Unowned actions

Fix:

1. Owner + date each
2. Track weekly
3. Block launch till done
4. Verify

### Consult skipped

Cause: Speed pressure

Fix:

1. Require evidence
2. DPO veto power
3. Log skips
4. Escalate repeats

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Find.
- Assess.
- Hold.

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

Avoid screen-free intake; checkbox DPIAs; consult-free assessments; owner-free mitigations; residual-blind launches; register-free programs.

## Bundled References

Read `references/dpia-practice.md` when assessing privacy risk.
Run `scripts/dpia_scaffold.py` to scaffold DPIAs.
Copy `assets/checklists.md` into every delivery.
