---
name: circumvention-boundaries
description: Stay on the lawful side of every technical gate with decided trees. Use when the user asks to DMCA 1201 and scraping; is bypassing this gate circumvention; TPM decision tree; interoperability exemption; security research exemption.
compatibility: Counsel for all TPM calls; gate inventory; alternative-path mindset.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Circumvention Boundaries

Treat technical gates as legal lines. You inventory every gate, analyze access honestly, test exemptions narrowly, gate all TPM-adjacent work on counsel, and document every call — preferring lawful alternative paths.

Optimize simultaneously for:

- inventoried gates
- honest analyses
- narrow exemptions
- gated work
- filed calls

Any gate-defeat question goes to counsel before code; default to the lawful path. Not legal advice.

## Use Cases

### Gate question

Trigger: user says 'bypass login' or 'defeat check'

Steps:

1. Name the gate
2. Run decision tree
3. Counsel gate
4. Lawful path

Result: Principled answer.

### Research claim

Trigger: user says 'security research' or 'interoperability'

Steps:

1. Test exemption narrowly
2. Document factors
3. Counsel confirms
4. Scope tightly

Result: Scoped research.

### Alt path

Trigger: user says 'blocked, what now' or 'lawful options'

Steps:

1. List alternatives
2. Rank lawful-first
3. Pursue top
4. File decision

Result: Lawful progress.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Gate inventory
- Decision trees
- Analyses
- Exemption memos
- Counsel gates
- Alt-path log
- Training record
- Call register

Never defeat gates on self-serving readings or skip counsel on TPM questions.

## Phase 1 — Inventory Gates

Auth, encryption, checks, gates per target.

Classify: credential vs protection vs rate.

Owner per gate question.

## Phase 2 — Analyze Access

Walk `scripts/tpm_decision.py` per gate.

Ordinary use vs defeat, honestly.

Document factors.

## Phase 3 — Gate Counsel

TPM-adjacent = counsel before code.

Exemptions narrow + evidenced.

Written go/no-go filed.

## Phase 4 — Prefer Alt Paths

APIs, partnerships, public sources.

Log alternatives considered.

Brief teams on lines.

## Examples

### Example 1: No-go respected

User says: "Can we defeat this check?"

Actions:

1. Tree said counsel
2. Counsel said no
3. Alt path via API
4. Shipped lawfully

Result: Line held.

### Example 2: Research scoped

User says: "Analyze our own DRM?"

Actions:

1. Owned-system research
2. Exemption memo'd
3. Scoped tightly
4. Findings used defensively

Result: Lawful research.

## Troubleshooting

### Gate ambiguity

Cause: Rate vs protection blur

Fix:

1. Classify conservatively
2. Counsel decides
3. Document
4. Revisit on change

### Exemption stretch

Cause: Wishful research claims

Fix:

1. Narrow factors
2. Independent review
3. Scope or stop
4. File honestly

### Pressure to defeat

Cause: Deadline over lines

Fix:

1. Escalate in writing
2. Offer alt paths
3. Refuse undocumented
4. Protect team

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- See.
- Decide.
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

Avoid gate-blind automation; self-serving exemptions; counsel-free TPM work; tree-free decisions; alt-path blindness; pressure-caved lines.

## Bundled References

Read `references/tpm-lines.md` when facing technical gates.
Run `scripts/tpm_decision.py` to walk TPM decisions.
Copy `assets/checklists.md` into every delivery.
