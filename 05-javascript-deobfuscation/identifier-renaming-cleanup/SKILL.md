---
name: identifier-renaming-cleanup
description: Rename mangled identifiers deterministically and inline trivial aliases. Use when the user asks to rename _0x variables; clean mangled JavaScript; inline JS aliases; stabilize builds for diffing; prepare JS for review.
compatibility: Any OS with Python 3.10+; sample files; parser tools optional for deep AST work.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Identifier Renaming Cleanup

Give mangled code stable names. You scope identifiers correctly, rename from usage roles deterministically, inline trivial aliases with proof, and keep every build diffable against the last.

Optimize simultaneously for:

- correct scopes
- stable names
- inlined aliases
- folded constants
- diffable builds

Rename by scope and role with deterministic rules; never hand-rename what automation must reproduce.

## Use Cases

### Review prep

Trigger: user says 'a, b, c everywhere' or 'hex names'

Steps:

1. Map scopes
2. Rename by role
3. Inline aliases
4. Deliver readable file

Result: Review-ready code.

### Build diffing

Trigger: user says 'what changed upstream' or 'vendor update'

Steps:

1. Rename both builds same rules
2. Diff normalized
3. Report real changes
4. Archive

Result: True-change diff.

### Handoff

Trigger: user says 'analyst-readable version' or 'document this'

Steps:

1. Clean fully
2. Annotate roles
3. Package with maps
4. Hand off

Result: Documented code.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Scope map
- Rename table
- Inline log
- Fold log
- Stability proof
- Diff samples
- Rule version
- Original archive

Never rename across scopes blindly, and never inline without single-use proof.

## Phase 1 — Map Scopes

List functions and blocks with their declared identifiers.

Infer roles from usage: counter, decoder, store, flag.

Record the scope tree.

## Phase 2 — Rename Deterministic

Run `scripts/identifier_mapper.py --file sample.js --out renamed.js` for the first pass.

Review the rename table for collisions.

Re-run to prove identical output.

## Phase 3 — Inline and Fold

Inline single-use aliases with call counts.

Fold provable constants only.

Log every transformation.

## Phase 4 — Stabilize Builds

Freeze rule version.

Diff across builds cleanly.

Archive maps with outputs.

## Examples

### Example 1: Skimmer review

User says: "Make this readable for the report."

Actions:

1. Renamed 200 identifiers by role
2. Inlined 30 aliases
3. Report written from clean copy
4. Map archived with case

Result: Court-readable code.

### Example 2: Vendor delta

User says: "Vendor shipped an update."

Actions:

1. Renamed both with v3 rules
2. Diff showed 40 real lines
3. Reviewed same day
4. Approved with notes

Result: Fast confident review.

## Troubleshooting

### Rename collision

Cause: Same name across scopes merged

Fix:

1. Scope-qualify names
2. Re-run deterministically
3. Verify no shadow breaks
4. Freeze the fix

### Inlined alias breaks code

Cause: Hidden second use or side effect

Fix:

1. Restore from map
2. Require strict single-use
3. Check side effects
4. Re-verify

### Builds still undiffable

Cause: Nondeterministic ordering or timestamps

Fix:

1. Sort declarations canonically
2. Strip volatile metadata
3. Re-run both sides
4. Lock the pipeline

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Scope.
- Clean.
- Stable.

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

Avoid cross-scope merges; hand renames; unproven inlines; volatile folding; nondeterministic numbering; maps discarded.

## Bundled References

Read `references/rename-rules.md` when renaming or inlining code.
Run `scripts/identifier_mapper.py` to rename hex identifiers deterministically.
Copy `assets/checklists.md` into every delivery.
