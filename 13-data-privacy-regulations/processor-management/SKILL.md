---
name: processor-management
description: Keep vendors inside your Records perimeter with diligence and DPAs. Use when the user asks to review a vendor DPA; diligence a data processor; control subprocessors; audit a vendor; plan vendor exit and deletion.
compatibility: Procurement gate; legal for DPA review; audit rights in contracts.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Processor Management

Extend your perimeter to every processor. You tier by risk, diligence deeply, paper DPAs with teeth, control subprocessors, audit with evidence, and exit with deletion proof — gating renewals on all of it.

Optimize simultaneously for:

- tiered vendors
- vetted highs
- toothed DPAs
- controlled subs
- proven exits

No personal data to vendors without DPA; renewals gated on audit posture.

## Use Cases

### New vendor

Trigger: user says 'use vendor X' or 'new SaaS with PII'

Steps:

1. Tier + diligence
2. DPA papered
3. Security verified
4. Approve gated

Result: Safe onboarding.

### Sub change

Trigger: user says 'vendor added subprocessor' or 'notice received'

Steps:

1. Review risk
2. Object or accept
3. Document
4. Monitor

Result: Controlled chain.

### Vendor exit

Trigger: user says 'leave vendor' or 'contract ends'

Steps:

1. Export data
2. Delete + proof
3. Verify absent
4. Close file

Result: Clean exit.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Vendor register
- Tier rationale
- Diligence packs
- Signed DPAs
- Sub lists
- Audit reports
- Remediation log
- Exit proofs

Never onboard processors without DPAs or renew failing vendors unremediated.

## Phase 1 — Tier and Vet

Risk by data/work/criticality.

Diligence highs deeply.

Register with `scripts/vendor_register.py`.

## Phase 2 — Paper DPAs

Instructions, security, breach-72h, audit, delete, flow-downs.

Legal reviews; signed before data.

Subs listed + change control.

## Phase 3 — Audit

Yearly highs; evidence-based.

Remediation owned + dated.

Renewals gated.

## Phase 4 — Exit Clean

Export + delete + proof.

Verify absence.

Close with file.

## Examples

### Example 1: Blocked vendor

User says: "Cheap analytics, no DPA?"

Actions:

1. Refused without paper
2. Chose compliant alt
3. Cost +5, risk gone
4. Policy kept

Result: Principled procurement.

### Example 2: Exit proven

User says: "Leaving CRM vendor."

Actions:

1. Exported, deleted, verified
2. Proof filed
3. Zero residue
4. Closed clean

Result: Clean break.

## Troubleshooting

### Vendor breach

Cause: Their incident, your data

Fix:

1. 72h clock starts
2. Scope + contain
3. Notify per duty
4. Postmortem + remediate

### Audit refused

Cause: Weak DPA rights

Fix:

1. Invoke contract
2. Escalate
3. Non-renew
4. Fix template

### Shadow SaaS

Cause: Teams buy direct

Fix:

1. Discover + register
2. Retro-diligence
3. Gate procurement
4. Train buyers

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Take.
- Hold.
- Leave.

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

Avoid DPA-free vendors; diligence-free onboarding; sub-blind chains; audit-free renewals; proof-free exits; gate-free procurement.

## Bundled References

Read `references/processor-control.md` when onboarding or auditing vendors.
Run `scripts/vendor_register.py` as a vendor/DPA register.
Copy `assets/checklists.md` into every delivery.
