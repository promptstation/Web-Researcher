---
name: cv-deployment-ops
description: Deploy vision with cards, canaries, live monitoring, and fast rollback. Use when the user asks to deploy a vision model; write a model card; canary ML releases; monitor model drift; optimize inference latency.
compatibility: Serving stack (TorchServe/Triton/ONNX); metrics backend; versioned model registry.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# CV Deployment Ops

Ship vision that stays trustworthy. You card every model honestly, serve inside latency budgets, shadow then canary every release, watch drift and slices live, and roll back in minutes when signals turn.

Optimize simultaneously for:

- honest cards
- budgeted serving
- safe canaries
- watched drift
- fast rollbacks

No prod traffic without card, canary, monitors, and one-command rollback.

## Use Cases

### First deploy

Trigger: user says 'serve this model' or 'go live'

Steps:

1. Card it
2. Budget latency
3. Shadow then canary
4. Monitor live

Result: Safe launch.

### Slow inference

Trigger: user says 'too slow' or 'GPU costs'

Steps:

1. Profile
2. Optimize ladder
3. Verify metrics kept
4. Ship faster

Result: Budget met.

### Drift alarm

Trigger: user says 'accuracy dropping' or 'inputs changed'

Steps:

1. Confirm drift
2. Triage cause
3. Adapt or rollback
4. Postmortem

Result: Drift handled.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Model card
- Latency budget
- Optimization record
- Shadow results
- Canary analysis
- Monitor dashboards
- Rollback command
- Incident log

Never deploy cardless or canary-free, and never ignore drift alerts.

## Phase 1 — Card Honestly

Draft with `scripts/model_card_gen.py --model NAME`.

Data, eval slices, limits, ethics, owner.

Review before serving.

## Phase 2 — Serve in Budget

Batch, quantize, cache in order.

p95 latency SLO; verify metrics kept.

Load-test to knee.

## Phase 3 — Shadow and Canary

Shadow 100 percent, compare offline.

Canary 5-25-100 with gates.

Auto-rollback armed.

## Phase 4 — Monitor Live

Input drift, confidence shift, slice proxies.

Alert on budget burn.

Rollback one command, drilled.

## Examples

### Example 1: Safe launch

User says: "Deploy defect detector."

Actions:

1. Card plus shadow plus canary
2. Caught lighting shift early
3. Adapted, relaunched
4. Stable months

Result: Trusted deployment.

### Example 2: Fast rollback

User says: "New model degrading."

Actions:

1. Drift alert in 20 min
2. Rolled back in 3
3. Root-caused
4. Re-shipped fixed

Result: Minutes-long incident.

## Troubleshooting

### Canary blind

Cause: No live labels or proxies

Fix:

1. Proxy metrics (confidence, drift)
2. Human sample audits
3. Shadow longer
4. Gate on proxies

### Latency spikes

Cause: Cold starts or big inputs

Fix:

1. Warm pools
2. Cap input size
3. Batch sanely
4. Autoscale tested

### Rollback slow

Cause: Unversioned artifacts

Fix:

1. Registry versioned
2. One-command rollback
3. Drill quarterly
4. Time it

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Card.
- Ship.
- Watch.

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

Avoid cardless deploys; canary-free releases; budget-free serving; drift-blind prod; rollback-free launches; monitor-free models.

## Bundled References

Read `references/vision-serving.md` when deploying or monitoring vision.
Run `scripts/model_card_gen.py` to draft model cards.
Copy `assets/checklists.md` into every delivery.
