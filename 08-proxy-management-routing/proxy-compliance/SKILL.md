---
name: proxy-compliance
description: Keep egress inside provider terms, target terms, and data law — provably. Use when the user asks to audit proxy usage; document lawful basis for scraping; enforce geo restrictions; review provider terms; handle ToS violations.
compatibility: Legal counsel for basis review; router and queue controls; audit log retention.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Proxy Compliance

Make compliance the default path. You map every applicable term, document basis per flow, enforce controls in code, audit monthly with evidence, and respond to violations with containment and learning.

Optimize simultaneously for:

- mapped terms
- filed bases
- live controls
- monthly audits
- clean responses

When terms conflict or basis is unclear, pause and escalate — never route around the question.

## Use Cases

### New flow review

Trigger: user says 'new collection' or 'approve this crawl'

Steps:

1. Check terms
2. Document basis
3. Encode controls
4. Approve with scope

Result: Approved lawful flow.

### Monthly audit

Trigger: user says 'prove compliance' or 'audit egress'

Steps:

1. Pull decision logs
2. Check vs policy
3. List exceptions
4. File report

Result: Evidence-backed audit.

### Violation drill

Trigger: user says 'blocked target hit' or 'ToS complaint'

Steps:

1. Contain immediately
2. Preserve evidence
3. Disclose per policy
4. Prevent recurrence

Result: Handled with integrity.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Terms register
- Basis docs per flow
- Control matrix
- Audit reports
- Exception log
- Training records
- Escalation paths
- Violation log

Never route around geo, sanction, or ToS controls, and never operate flows without filed basis.

## Phase 1 — Map Terms

Providers, targets, data laws, sanctions.

Encode as allow/block plus geo rules.

Review on every contract change.

## Phase 2 — Document Basis

Basis, scope, retention per flow.

Legal sign-off where needed.

Generate packs with `scripts/compliance_pack.py`.

## Phase 3 — Enforce in Code

Router and queue deny by default.

Block lists versioned.

Alerts on denied attempts.

## Phase 4 — Audit Monthly

Decisions vs policy; exceptions explained.

File report; train gaps.

Drill violation response yearly.

## Examples

### Example 1: Clean audit

User says: "Enterprise security review."

Actions:

1. Basis docs plus logs shown
2. Zero exceptions
3. Passed first try
4. Template adopted

Result: Trusted egress program.

### Example 2: Complaint handled

User says: "Target alleges ToS breach."

Actions:

1. Paused flow same day
2. Evidence reviewed
3. Scope narrowed
4. Relationship kept

Result: Integrity preserved.

## Troubleshooting

### Basis unclear

Cause: Novel target or data type

Fix:

1. Pause the flow
2. Legal review
3. Document decision
4. Encode controls

### Controls bypassed

Cause: Shadow routing or direct egress

Fix:

1. Force all via router
2. Block direct
3. Audit paths
4. Alert on bypass

### Audit gaps

Cause: Missing logs or decisions

Fix:

1. Fix logging first
2. Backfill what possible
3. Note gaps honestly
4. Prevent recurrence

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- File.
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

Avoid basis-free flows; control-free routers; audit-free years; bypass-tolerant plumbing; undocumented exceptions; legal-last reviews.

## Bundled References

Read `references/egress-compliance.md` when reviewing flows or auditing use.
Run `scripts/compliance_pack.py` to scaffold per-flow compliance packs.
Copy `assets/checklists.md` into every delivery.
