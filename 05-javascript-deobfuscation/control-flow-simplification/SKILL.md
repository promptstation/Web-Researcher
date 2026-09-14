---
name: control-flow-simplification
description: Unflatten dispatcher loops and prune dead branches with proof. Use when the user asks to simplify flattened JavaScript; understand switch dispatchers; remove dead obfuscator branches; recover logic from control-flow flattening; evaluate opaque predicates.
compatibility: Any OS with Python 3.10+; sample files; graphviz optional for drawings.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Control Flow Simplification

Restore logic from spaghetti. You sketch dispatchers as graphs, prove predicates constant, prune only the provably dead, and relink survivors into linear code reviewers can follow.

Optimize simultaneously for:

- sketched graphs
- proven predicates
- pruned dead code
- linear logic
- sampled equivalence

Prune only with proof and keep originals referenced; never delete what you cannot prove dead.

## Use Cases

### Flat function

Trigger: user says 'one giant switch' or 'unreadable loop'

Steps:

1. Sketch the dispatcher
2. Evaluate predicates
3. Prune dead cases
4. Relink linearly

Result: Readable function.

### Branch audit

Trigger: user says 'which branches run' or 'dead code?'

Steps:

1. Trace state variable
2. Prove reachability
3. Mark live vs dead
4. Report with proof

Result: Reachability verdicts.

### Equivalence check

Trigger: user says 'prove same behavior' or 'safe to simplify'

Steps:

1. Sample inputs both versions
2. Compare outputs
3. Document coverage
4. Sign off

Result: Trusted simplification.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Dispatcher sketch
- Predicate table
- Prune proofs
- Relinked code
- Equivalence samples
- Complexity deltas
- Original references
- Review notes

Never prune without proof, and never present simplified code as original behavior without sampling.

## Phase 1 — Sketch Dispatch

Run `scripts/cfg_sketch.py --file flat.js --fn target` for case inventory.

Draw blocks and transitions with state values.

Mark entry, exits, and loops.

## Phase 2 — Evaluate Predicates

List opaque conditions with constant-folding attempts.

Prove constant or mark dynamic honestly.

Record the proof per predicate.

## Phase 3 — Prune Dead

Remove only proven-unreachable cases.

Keep originals in comments or appendix.

Re-sketch after each prune.

## Phase 4 — Relink and Verify

Order surviving blocks linearly.

Sample inputs for equivalence.

Report complexity deltas.

## Examples

### Example 1: License check

User says: "Understand this validation logic."

Actions:

1. Sketched 40-case dispatcher
2. Pruned 28 dead cases proven
3. Recovered 12-step check
4. Reviewed in an hour

Result: Logic laid bare.

### Example 2: Checkout guard

User says: "Is this branch reachable?"

Actions:

1. Traced state: unreachable
2. Proved with predicate table
3. Flagged as decoy
4. Skipped safely

Result: Decoy identified.

## Troubleshooting

### State threading unclear

Cause: Aliased state variables

Fix:

1. Rename consistently first
2. Trace assignments
3. Re-sketch clean
4. Verify with samples

### Predicate resists folding

Cause: Genuinely dynamic or environment-fed

Fix:

1. Mark dynamic honestly
2. Keep both branches
3. Note the input source
4. Move on

### Simplified output misbehaves

Cause: Over-pruned live path

Fix:

1. Diff against original
2. Restore suspect prunes
3. Re-prove narrower
4. Expand sampling

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Sketch.
- Prune.
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

Avoid proof-free pruning; originals discarded; dynamic predicates forced; graphs skipped; equivalence unsampled; complexity unmeasured.

## Bundled References

Read `references/dispatcher-patterns.md` when sketching or pruning flattened code.
Run `scripts/cfg_sketch.py` to inventory dispatcher cases.
Copy `assets/checklists.md` into every delivery.
