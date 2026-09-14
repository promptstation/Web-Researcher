---
name: lawful-basis-ops
description: Ground every flow in documented basis, purpose, and necessity. Use when the user asks to choose a GDPR lawful basis; write a legitimate interest assessment; define data purposes; check necessity and proportionality; stop purpose creep.
compatibility: Counsel for basis sign-off; flow docs; review gates in launch process.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Lawful Basis Ops

Collect nothing without a reasoned basis. You select bases per purpose, write purposes narrowly, test necessity honestly, balance interests with opt-outs, and gate launches so creep dies at review.

Optimize simultaneously for:

- selected bases
- narrow purposes
- tested necessity
- balanced interests
- blocked creep

Basis decided before collection; counsel signs novel or sensitive bases; no repurposing without re-basis.

## Use Cases

### New collection

Trigger: user says 'scrape profiles' or 'collect PII'

Steps:

1. Define purpose
2. Select basis
3. Test necessity
4. Sign + gate

Result: Grounded collection.

### Repurpose ask

Trigger: user says 'use this data for X too' or 'new purpose'

Steps:

1. Test compatibility
2. Re-basis or refuse
3. Document call
4. Control enforced

Result: Principled answer.

### LIA needed

Trigger: user says 'legitimate interest?' or 'balance this'

Steps:

1. Purpose + necessity
2. Balance + safeguards
3. Opt-out live
4. Review dated

Result: Defensible LIA.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Basis record per flow
- Purpose statements
- Necessity notes
- LIA docs
- Counsel sign-offs
- Review dates
- Creep log
- Gate evidence

Never collect first and basis later, and never stretch purposes silently.

## Phase 1 — Define Purpose

Narrow, explicit, written before code.

One purpose per basis record.

Consumer-visible wording.

## Phase 2 — Select Basis

Consent/contract/legal/LI per regime.

Scaffold with `scripts/basis_pack.py --flow NAME`.

Counsel signs novel/sensitive.

## Phase 3 — Test Necessity

Less-data alternatives considered.

Proportionality weighed.

LIA with opt-out where LI.

## Phase 4 — Gate and Watch

Launch gate requires pack.

Repurpose triggers re-basis.

Review yearly or on change.

## Examples

### Example 1: Grounded scrape

User says: "Collect public profiles?"

Actions:

1. Purpose narrow, LI tested
2. Minimized + opt-out
3. Counsel signed
4. Gated launch

Result: Defensible collection.

### Example 2: Creep refused

User says: "Also use for ads?"

Actions:

1. Incompatible purpose
2. Refused with memo
3. Separate consent path
4. Trust kept

Result: Principled no.

## Troubleshooting

### Basis shopping

Cause: Picking easiest ex post

Fix:

1. Decide pre-collection
2. Document reasoning
3. Counsel review
4. Lock process

### Vague purposes

Cause: 'Improve services' catch-all

Fix:

1. Split narrowly
2. Re-basis each
3. Update notices
4. Gate future

### LIA rubber-stamp

Cause: No real balancing

Fix:

1. Affected-rights analysis
2. Safeguards added
3. Opt-out real
4. Review dated

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ground.
- Guard.
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

Avoid collect-then-basis; catch-all purposes; basis shopping; rubber-stamp LIAs; silent repurposing; gateless launches.

## Bundled References

Read `references/basis-discipline.md` when basing flows or reviewing purposes.
Run `scripts/basis_pack.py` to scaffold basis records.
Copy `assets/checklists.md` into every delivery.
