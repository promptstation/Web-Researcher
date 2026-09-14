---
name: interop-reversing
description: Recover endpoints and protocols for lawful interoperability with clean-room docs. Use when the user asks to reverse engineer for interoperability; recover undocumented endpoints lawfully; document a frontend protocol; build a compatible integration; scope clean-room reversing.
compatibility: Any OS with Python 3.10+; lawfully observed code and traffic; counsel for gray areas.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Interop Reversing

Interoperate without overstepping. You scope to interfaces, recover endpoints and shapes from lawful observation, document behavior clean-room style, and build compatible clients inside terms and permission.

Optimize simultaneously for:

- scoped goals
- recovered interfaces
- clean specs
- compatible clients
- filed trails

Interfaces only, lawful observation only, counsel on gray areas; never copy creative expression or bypass access controls.

## Use Cases

### Integration need

Trigger: user says 'no official API' or 'integrate anyway'

Steps:

1. Scope interop goal
2. Recover interface lawfully
3. Spec behavior cleanly
4. Build compatible client

Result: Working lawful integration.

### Migration support

Trigger: user says 'migrate off vendor X' or 'compatible reader'

Steps:

1. Document formats
2. Build reader
3. Test compatibility
4. File trail

Result: Clean migration path.

### Accessibility fix

Trigger: user says 'inaccessible widget' or 'compatible alternative'

Steps:

1. Spec the interface
2. Build accessible client
3. Test parity
4. Publish notes

Result: Accessible equivalent.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Interop scope memo
- Observation log
- Interface specs
- Clean-room notes
- Terms analysis
- Compat test results
- Permission trail
- Review dates

Never copy implementation code, and never defeat access controls in the name of interop.

## Phase 1 — Scope Interop

Write the interface goal and its lawful basis.

Exclude creative expression explicitly.

Get review on gray areas.

## Phase 2 — Recover Interfaces

Run `scripts/endpoint_extractor.py --file bundle.js` for endpoint candidates.

Confirm with lawful traffic observation.

Document shapes with examples.

## Phase 3 — Spec Cleanly

Write behavior specs from observation.

Separate ideas from expression.

Review notes for contamination.

## Phase 4 — Build Compatible

Implement from specs only.

Test compatibility thoroughly.

File the full trail.

## Examples

### Example 1: Feed reader

User says: "Read our own data back out."

Actions:

1. Scoped to export format
2. Spec documented
3. Reader built
4. Migrated cleanly

Result: Lawful data freedom.

### Example 2: Bridge client

User says: "Bridge two tools we own."

Actions:

1. Interfaces spec'd both sides
2. Bridge from specs
3. Parity tested
4. Trail filed

Result: Clean integration.

## Troubleshooting

### Terms restrict reversing

Cause: Contractual anti-reverse clauses

Fix:

1. Read clause scope carefully
2. Brief counsel
3. Seek permission
4. Pause if unclear

### Interface drifts

Cause: Undocumented changes

Fix:

1. Re-observe and re-spec
2. Version specs
3. Alert on drift
4. Maintain actively

### Notes contaminated

Cause: Implementation detail copied

Fix:

1. Rewrite from behavior
2. Purge expression
3. Re-review
4. Retrain the habit

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Scope.
- Spec.
- Build.

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

Avoid expression copying; access-control defeat; terms ignored; notes contaminated; counsel skipped on gray; trails built after-the-fact.

## Bundled References

Read `references/clean-room.md` when documenting or building interop.
Run `scripts/endpoint_extractor.py` to recover endpoint candidates with context.
Copy `assets/checklists.md` into every delivery.
