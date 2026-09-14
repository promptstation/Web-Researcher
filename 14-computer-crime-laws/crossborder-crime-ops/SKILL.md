---
name: crossborder-crime-ops
description: Navigate cross-border cyber law with maps, corridors, and counsel. Use when the user asks to Budapest Convention explained; MLAT requests; conflicting data laws; data localization rules; cross-border incident response.
compatibility: Counsel network per key jurisdiction; jurisdiction map; corridor playbooks.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Cross-border Crime Ops

Act lawfully across borders. You map every asset to jurisdictions, know cooperation paths per corridor, route preservation fast, memo conflicts honestly, localize where due — with local counsel deciding, never HQ guessing.

Optimize simultaneously for:

- mapped estates
- known corridors
- fast preservation
- honest conflicts
- due localization

Local counsel decides local questions; never comply with foreign compulsion blindly. Not legal advice.

## Use Cases

### Multi-country incident

Trigger: user says 'breach spans 3 countries' or 'which law'

Steps:

1. Map + counsel each
2. Sequence duties
3. Preserve routed
4. Notify per law

Result: Coordinated response.

### Foreign request

Trigger: user says 'foreign police ask' or 'overseas order'

Steps:

1. No direct comply
2. MLAT/counsel path
3. Verify + scope
4. Log all

Result: Proper channel.

### Localize build

Trigger: user says 'store data in X' or 'localization rule'

Steps:

1. Table rules
2. Design residency
3. Verify enforced
4. Audit yearly

Result: Resident data.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Jurisdiction map
- Corridor playbooks
- Counsel roster
- Preservation log
- Conflict memos
- Localization table
- Sequence plans
- Audit reports

Never honor foreign compulsion without local counsel or assume one law travels.

## Phase 1 — Map Estate

Infra, data, subjects, staff per country.

Build with `scripts/jurisdiction_map.py`.

Counsel per key jurisdiction.

## Phase 2 — Playbook Corridors

Preservation, access, notice per pair.

MLAT vs direct vs emergency.

Contacts + timelines.

## Phase 3 — Handle Conflicts

Memo competing duties honestly.

Sequence: preserve, consult, comply-valid.

Log diplomatic all.

## Phase 4 — Localize and Drill

Residency enforced + verified.

Cross-border drill yearly.

Review on law change.

## Examples

### Example 1: Coordinated breach

User says: "EU + BR + US breach."

Actions:

1. 3 counsels, sequenced
2. Notices per law
3. Preservation routed
4. Clean Records

Result: Global poise.

### Example 2: Conflict navigated

User says: "US order vs EU block?"

Actions:

1. Memo'd conflict
2. MLAT path taken
3. Both counsels aligned
4. Lawful result

Result: No-violation path.

## Troubleshooting

### Racing clocks

Cause: Multiple notice SLAs

Fix:

1. Sequence earliest first
2. Parallelize counsel
3. Phased notices
4. Log timeline

### Blocking statute

Cause: Local ban on foreign produce

Fix:

1. Local counsel leads
2. MLAT route
3. Narrow scope
4. Document bind

### Rogue direct order

Cause: Foreign shortcut attempt

Fix:

1. Decline direct
2. Offer MLAT
3. Log + counsel
4. Notify affected apt

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Know.
- Act.
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

Avoid map-free estates; counsel-free foreign; MLAT-skipping comply; conflict-ignoring; localization theater; drill-free global.

## Bundled References

Read `references/crossborder-cyber.md` when operating across jurisdictions.
Run `scripts/jurisdiction_map.py` to scaffold jurisdiction maps.
Copy `assets/checklists.md` into every delivery.
