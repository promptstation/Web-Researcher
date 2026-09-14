---
name: pipeline-observability
description: Make pipeline failures cheap with correlated logs, metrics, and traces. Use when the user asks to add structured logging; trace jobs across workers; summarize pipeline runs; alert on error budgets; debug distributed failures.
compatibility: Python 3.10+ stdlib logging; any metrics backend; JSONL for run reports.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Pipeline Observability

Make every failure explain itself. You structure logs with correlation, emit RED/USE metrics, trace across workers, auto-report every run, and alert on burn so signal beats noise.

Optimize simultaneously for:

- correlated logs
- live metrics
- end-to-end traces
- auto reports
- signal alerts

No run ships without report; no alert without runbook; no PII in logs.

## Use Cases

### Blind pipeline

Trigger: user says 'failures take hours' or 'no visibility'

Steps:

1. Structure logs
2. Add run reports
3. Emit metrics
4. Alert on burn

Result: Minutes to answer.

### Cross-worker bug

Trigger: user says 'lost between workers' or 'which stage failed'

Steps:

1. Propagate correlation
2. Trace the job
3. Name the stage
4. Fix with proof

Result: Stage-named failure.

### Noise cut

Trigger: user says 'alert fatigue' or 'too many pages'

Steps:

1. Move to burn rates
2. Tune windows
3. Add runbooks
4. Verify signal

Result: Quiet accurate paging.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Log schema
- Correlation coverage
- Metric catalog
- Trace sampling
- Run report template
- Alert rules plus runbooks
- Dashboard links
- PII scrub proof

Never log secrets or PII, and never page without a runbook.

## Phase 1 — Structure Logs

JSON with ts, level, run_id, job_id, stage, msg.

Propagate IDs across queue and HTTP.

Scrub secrets at emission.

## Phase 2 — Emit Metrics

RED per stage; USE per host.

Cardinality bounded.

Dashboards per pipeline.

## Phase 3 — Trace Jobs

Sample traces per run.

Link logs to spans.

Keep tail exemplars.

## Phase 4 — Report and Alert

Run `scripts/run_report.py --logs run.jsonl` after every run.

Alert on burn, age, and stalls.

Postmortem monthly.

## Examples

### Example 1: MTTR cut

User says: "Debug takes half a day."

Actions:

1. Correlated logs plus reports
2. MTTR to 20 minutes
3. Top-error weekly fixes
4. Reliability up

Result: Cheap failures.

### Example 2: Silent stall

User says: "Pipeline stalls without errors."

Actions:

1. Age and stall alerts added
2. Caught in 10 minutes
3. Root cause fixed
4. Never silent again

Result: Watched pipeline.

## Troubleshooting

### Correlation gaps

Cause: IDs dropped at boundaries

Fix:

1. Audit handoffs
2. Inject at edges
3. Test propagation
4. Verify e2e

### Metric cardinality explosion

Cause: High-card labels (URL, ID)

Fix:

1. Bucket labels
2. Drop raw IDs
3. Exemplars for detail
4. Cap series

### Reports ignored

Cause: Too long or no owner

Fix:

1. One-page template
2. Owner assigned
3. Review ritual
4. Act on top errors

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Logs.
- Metrics.
- Alert.

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

Avoid printf debugging; ID-free logs; metric-free stages; traceless hops; report-free runs; runbook-free alerts.

## Bundled References

Read `references/observability-stack.md` when instrumenting or alerting.
Run `scripts/run_report.py` to summarize JSONL run logs.
Copy `assets/checklists.md` into every delivery.
