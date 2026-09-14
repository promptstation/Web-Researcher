---
name: anti-debug-triage
description: Catalog anti-analysis traps and neutralize them in lab copies. Use when the user asks to defeat debugger traps; bypass DevTools detection in lab; map domain locks; neutralize self-defending JS; analyze tamper-proofed code.
compatibility: Any OS with Python 3.10+ and Node 18+; lab copies only; production integrity untouched.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Anti Debug Triage

Keep analysis moving through hostile code. You catalog every trap, map locks and self-defense, patch lab copies reproducibly, and verify equivalence so findings rest on solid ground.

Optimize simultaneously for:

- cataloged traps
- mapped locks
- reproducible patches
- verified equivalence
- reported findings

Lab copies only; never strip protections from production assets or redistribute weakened code.

## Use Cases

### Debugger loop

Trigger: user says 'debugger fires forever' or 'cannot step through'

Steps:

1. Locate trap sites
2. Patch lab copy
3. Verify behavior same
4. Analyze freely

Result: Traps gone, logic kept.

### Domain lock

Trigger: user says 'only runs on their domain' or 'lock mapping'

Steps:

1. Map lock checks
2. Stub domain in lab
3. Verify gated paths
4. Report the mechanism

Result: Mechanism understood.

### Self-defense

Trigger: user says 'code deletes itself' or 'tamper response'

Steps:

1. Map integrity checks
2. Patch lab copy
3. Verify equivalence
4. Document the design

Result: Analyzable copy, design filed.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Trap inventory
- Lock map
- Patch diff per trap
- Equivalence samples
- Repro commands
- Upstream notes
- Lab-only markings
- Review sign-off

Never patch production assets or share deprotected code beyond the analysis team.

## Phase 1 — Catalog Traps

Run `scripts/trap_finder.py --file sample.js` for trap inventory.

Classify debugger, timing, DevTools, lock, integrity.

Quote each site with context.

## Phase 2 — Map Locks

Trace domain and integrity checks to decisions.

List gated paths and payloads.

Document trigger conditions.

## Phase 3 — Patch Lab Copies

Neutralize one trap class at a time.

Keep patches minimal and reviewable.

Version each patched copy.

## Phase 4 — Verify Equivalence

Sample behaviors pre/post patch.

Confirm only traps changed.

Sign off the lab copy.

## Examples

### Example 1: Infinite debugger

User says: "DevTools unusable on this file."

Actions:

1. Found 6 debugger sites plus timing
2. Patched lab copy
3. Analysis completed
4. Traps documented

Result: Analyzable in an hour.

### Example 2: Licensed widget

User says: "Widget locks to domains; audit needed."

Actions:

1. Mapped lock to license check
2. Stubbed in lab only
3. Audited gated paths
4. Reported mechanism

Result: Lawful audit complete.

## Troubleshooting

### Patch breaks logic

Cause: Trap entangled with real checks

Fix:

1. Narrow the patch
2. Stub instead of delete
3. Re-verify finely
4. Document the tangle

### Traps regenerate

Cause: Self-healing from pristine copies

Fix:

1. Map the healing path
2. Patch the source copy
3. Verify persistence
4. Note the design

### Timing still trips

Cause: Multiple coupled timers

Fix:

1. Find all timer sites
2. Stub Date coherently
3. Re-run to green
4. Log each site

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Catalog.
- Patch.
- Verify.

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

Avoid production patching; deprotected redistribution; unverified patches; trap classes mixed in diffs; originals unhashed; lawful-purpose skipping.

## Bundled References

Read `references/trap-patterns.md` when finding or neutralizing traps.
Run `scripts/trap_finder.py` to inventory anti-analysis traps.
Copy `assets/checklists.md` into every delivery.
