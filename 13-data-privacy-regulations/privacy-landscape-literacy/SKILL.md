---
name: privacy-landscape-literacy
description: Map every data flow to its privacy laws, duties, and rights. Use when the user asks to GDPR or CCPA for my data; which privacy laws apply; compare privacy regimes; map data flows to laws; privacy rights by regulation.
compatibility: Counsel for scope calls; flow inventory; regulator guidance feeds.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Privacy Landscape Literacy

Know which law governs what. You compare regimes honestly, scope each flow, map duties and rights, brief teams plainly, and update on rulings — escalating gray calls to counsel, never guessing.

Optimize simultaneously for:

- compared regimes
- scoped flows
- mapped duties
- matrixed rights
- briefed teams

Operational literacy only — not legal advice; scope calls confirmed with counsel.

## Use Cases

### New market

Trigger: user says 'expand to EU' or 'new region launch'

Steps:

1. Scope laws
2. Map duties
3. Gap current
4. Remediate dated

Result: Lawful launch.

### Flow review

Trigger: user says 'is this flow ok' or 'privacy check'

Steps:

1. Scope + duties
2. Check controls
3. File decision
4. Review dated

Result: Reviewed flow.

### Ruling update

Trigger: user says 'new guidance' or 'fine in the news'

Steps:

1. Read ruling
2. Assess impact
3. Update map
4. Brief teams

Result: Current program.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Regime comparison
- Scope memos
- Duty maps
- Rights matrix
- Guidance log
- Training record
- Escalation log
- Review dates

Never guess scope on gray flows or treat literacy as legal advice.

## Phase 1 — Compare Regimes

Scope, basis, rights, transfers, penalties.

Generate matrix with `scripts/law_matrix.py`.

Counsel-review yearly.

## Phase 2 — Scope Flows

Subjects + establishment + targeting tests.

Memo per flow; gray to counsel.

File with flow docs.

## Phase 3 — Map Duties

Notices, records, DPO, DPIA, breach per law.

Gap vs current; dated remediation.

Owner per duty.

## Phase 4 — Stay Current

Guidance watch monthly.

Brief teams quarterly.

Re-scope on change.

## Examples

### Example 1: EU launch

User says: "Ship to Europe next quarter."

Actions:

1. Scoped GDPR
2. 12 gaps dated
3. Fixed pre-launch
4. DPO signed

Result: Clean launch.

### Example 2: Gray call

User says: "Does CCPA cover this?"

Actions:

1. Memo'd both readings
2. Counsel decided
3. Controlled accordingly
4. Filed

Result: Defensible call.

## Troubleshooting

### Scope creep

Cause: New subjects unreviewed

Fix:

1. Re-scope on launch
2. Gate deploys
3. Audit quarterly
4. Catch early

### Stale map

Cause: No guidance habit

Fix:

1. Monthly watch
2. Quarterly brief
3. Owner assigned
4. Log kept

### Advice confusion

Cause: Ops treated as counsel

Fix:

1. Label literacy
2. Escalate gray
3. Counsel signs
4. Train all

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Know.
- Scope.
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

Avoid single-regime thinking; guess scoping; literacy-as-advice; stale regime maps; unbriefed teams; escalation-free gray.

## Bundled References

Read `references/regime-map.md` when scoping flows or briefing teams.
Run `scripts/law_matrix.py` to generate regime comparison matrices.
Copy `assets/checklists.md` into every delivery.
