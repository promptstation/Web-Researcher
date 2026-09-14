---
name: research-ethics-ops
description: Run credible web research: reviewed, undeceived, pre-registered. Use when the user asks to IRB for web research; deception in research ethics; pre-register a study; protect vulnerable research subjects; publish reproducible research.
compatibility: Review board (internal/external); pre-registration venue; repro norms.
metadata:
  author: Promptstation
  version: 1.0.0
  category: ethics
---

# Research Ethics Ops

Earn belief. You review protocols before fieldwork, bar deception presumptively, protect the vulnerable with exclusions, pre-register questions and methods, and publish repro with limits — debriefing where owed.

Optimize simultaneously for:

- reviewed protocols
- zero deception
- protected vulnerable
- registered studies
- reproducible pubs

No fieldwork without review; no deception without extraordinary board approval (rarely).

## Use Cases

### Study launch

Trigger: user says 'research on users' or 'new study'

Steps:

1. Protocol + review
2. Pre-register
3. Fieldwork
4. Debrief + publish

Result: Credible study.

### Deception ask

Trigger: user says 'sockpuppets?' or 'fake accounts for research'

Steps:

1. Presumptive no
2. Alt designs
3. Board only if vital
4. Debrief plan

Result: Honest methods.

### Vulnerable pop

Trigger: user says 'study patients/minors' or 'sensitive group'

Steps:

1. Screen high
2. Safeguards/exclude
3. Consent robust
4. Review tight

Result: Protected subjects.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Protocol docs
- Review decisions
- Pre-registrations
- Consent materials
- Debrief plans
- Repro packages
- Board roster
- Limit statements

Never deceive subjects or study the vulnerable without robust safeguards.

## Phase 1 — Protocol Review

Questions, methods, risks, consent, data.

Scaffold with `scripts/ethics_review_pack.py`.

Board approves pre-field.

## Phase 2 — Bar Deception

No fakes, sockpuppets, false pretenses.

Extraordinary exceptions: board + debrief.

Document alternatives tried.

## Phase 3 — Pre-register

Questions + methods + analyses public.

Deviations logged.

Nulls publishable.

## Phase 4 — Debrief and Publish

Subjects debriefed where owed.

Repro + limits published.

Corrections welcomed.

## Examples

### Example 1: Trusted study

User says: "Measure platform bias?"

Actions:

1. Reviewed + registered
2. No deception design
3. Published repro
4. Cited widely

Result: Believed findings.

### Example 2: Deception killed

User says: "Sockpuppets needed?"

Actions:

1. Alt: consented panel
2. Better data, honest
3. Board praised
4. Standard set

Result: Methods matter.

## Troubleshooting

### Review bottleneck

Cause: Board slow

Fix:

1. Tiered review
2. SLA + triage
3. Templates
4. Staff board

### Repro fails

Cause: Messy methods

Fix:

1. Package code+data
2. Fresh-clone test
3. Version all
4. Publish v2

### Null suppressed

Cause: Publish-or-perish

Fix:

1. Register guarantees
2. Publish nulls
3. Reward rigor
4. Culture fix

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Plan.
- Field.
- Share.

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

Avoid review-free fieldwork; deception-by-default; vulnerability blindness; registration-free HARKing; repro-free pubs; null-burying.

## Bundled References

Read `references/web-research-review.md` when running web studies.
Run `scripts/ethics_review_pack.py` to scaffold review packs.
Copy `assets/checklists.md` into every delivery.
