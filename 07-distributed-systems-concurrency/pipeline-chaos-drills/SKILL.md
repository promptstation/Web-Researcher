---
name: pipeline-chaos-drills
description: Prove pipelines recover with safe drills and blameless hardening. Use when the user asks to run a game day; chaos-test my pipeline; kill-test workers; drill failover scenarios; write blameless postmortems.
compatibility: Staging first, production only with approvals; injection tooling per layer; observers rostered.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Pipeline Chaos Drills

Replace hope with proof. You plan game days with hypotheses and abort lines, inject failures inside blast radii, kill-test to zero loss, drill partitions and failovers, and postmortem blamelessly into shipped hardening.

Optimize simultaneously for:

- planned days
- safe injections
- clean kills
- survived partitions
- shipped lessons

Stage first; blast radius bounded; abort criteria honored instantly; never drill what you cannot roll back.

## Use Cases

### First game day

Trigger: user says 'never tested failure' or 'prove resume works'

Steps:

1. Hypothesize recovery
2. Bound blast radius
3. Inject and observe
4. Harden gaps

Result: Proven recovery.

### Kill test

Trigger: user says 'worker died in prod' or 'prove zero loss'

Steps:

1. Kill at 30/60/90
2. Replay to completion
3. Reconcile counts
4. File proof

Result: Zero-loss confidence.

### Partition drill

Trigger: user says 'split-brain worry' or 'leader safety'

Steps:

1. Partition staging
2. Watch election
3. Heal and verify
4. Document behavior

Result: Known partition behavior.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Game-day plan
- Hypothesis plus abort
- Blast-radius sign-off
- Injection log
- Recovery metrics
- Postmortem doc
- Hardening backlog
- Re-drill date

Never drill production without sign-off, and never skip the postmortem or the hardening.

## Phase 1 — Plan the Day

Hypothesis: what should survive and how fast.

Blast radius, observers, abort criteria.

Sign-off from owners.

## Phase 2 — Inject Safely

Rehearse with `scripts/chaos_runner.py --scenario kill` on simulators first.

Latency, errors, kills, partitions in order.

Abort instantly on breach.

## Phase 3 — Observe Recovery

Time detection, failover, full recovery.

Reconcile: inputs vs outputs vs DLQ.

Capture every surprise.

## Phase 4 — Harden Forever

Blameless postmortem within 48h.

Dated actions with owners.

Re-drill to verify fixes.

## Examples

### Example 1: Resume proven

User says: "Prove crash recovery."

Actions:

1. Killed at 3 points
2. Zero loss each
3. Dupes bounded
4. Proof filed, drill yearly

Result: Trusted recovery.

### Example 2: Partition known

User says: "What if network splits?"

Actions:

1. Split staging 10 min
2. Single leader held
3. Healed clean
4. Behavior documented

Result: Understood failure.

## Troubleshooting

### Drill finds nothing

Cause: Too gentle or wrong layer

Fix:

1. Raise realism
2. Target past incidents
3. Inject combined faults
4. Review hypothesis

### Abort triggered

Cause: Blast radius breached

Fix:

1. Stop and heal
2. Postmortem the drill
3. Shrink next radius
4. Re-plan

### Lessons rot

Cause: Actions unowned or undated

Fix:

1. Owner plus date each
2. Track to shipped
3. Re-drill verify
4. Report monthly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Plan.
- Run.
- Learn.

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

Avoid hope-based reliability; plan-free drills; radius-free injection; abort-ignored runs; postmortem-free incidents; lesson-free repeats.

## Bundled References

Read `references/game-day-guide.md` when planning, running, or learning from drills.
Run `scripts/chaos_runner.py` to rehearse failure scenarios on simulators.
Copy `assets/checklists.md` into every delivery.
