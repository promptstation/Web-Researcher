---
name: llm-cost-ops
description: Keep LLM pipelines inside budgets and SLOs with caching and routing. Use when the user asks to cut LLM costs; cache LLM responses; route across model tiers; set LLM latency SLOs; track token spend.
compatibility: Usage logs with tokens; cache store; 2+ model tiers for routing.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# LLM Cost Ops

Spend tokens like money — because they are. You budget per task, cache by hash, batch for throughput, route by difficulty, SLO latency with fallbacks, and alert before overruns — guarding quality on every cut.

Optimize simultaneously for:

- live budgets
- hit caches
- tuned batches
- smart routes
- met SLOs

Quality guards block every savings change; no silent model downgrades.

## Use Cases

### Bill shock

Trigger: user says 'LLM bill exploded' or 'cut spend'

Steps:

1. Attribute tokens
2. Cache + route
3. Verify quality
4. Track savings

Result: Controlled spend.

### Slow responses

Trigger: user says 'too slow' or 'p95 high'

Steps:

1. Budget latency
2. Batch/stream
3. Fallback chain
4. Verify SLO

Result: Fast pipeline.

### Tier routing

Trigger: user says 'cheap model first' or 'route by difficulty'

Steps:

1. Classify difficulty
2. Route tiers
3. Escalate on fail
4. Verify kept

Result: Cost-right quality.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Token budgets
- Attribution table
- Cache policy
- Batch config
- Routing rules
- Latency SLO
- Alert rules
- Quality guards

Never cut quality silently to save cost or run budget-free LLM workloads.

## Phase 1 — Account Tokens

Log tokens per call per task.

Run `scripts/llm_cost_tracker.py --usage usage.jsonl`.

Attribute 100 percent.

## Phase 2 — Cache and Batch

Hash-key caches; TTLs by freshness.

Batch offline; stream online.

Measure hit rates.

## Phase 3 — Route Tiers

Easy->small/fast, hard->large.

Escalate on low confidence.

Verify quality kept.

## Phase 4 — SLO and Alert

p95 latency SLO with fallback.

Spend alerts 80/100.

Weekly unit review.

## Examples

### Example 1: 60 percent cut

User says: "Summarization costs a fortune."

Actions:

1. Cached 50 percent hits
2. Routed 70 small
3. Quality kept
4. Down 60

Result: Affordable scale.

### Example 2: SLO met

User says: "Chat p95 8 seconds."

Actions:

1. Streamed + small-first
2. Fallback chain
3. p95 to 1.8s
4. Guarded quality

Result: Snappy chat.

## Troubleshooting

### Cache stale

Cause: No TTL or version

Fix:

1. TTL by freshness
2. Version keys
3. Invalidate on change
4. Monitor hits

### Routing misfires

Cause: Weak difficulty signal

Fix:

1. Better classifier
2. Confidence escalate
3. Audit routes
4. Tune weekly

### Latency tails

Cause: Retries and big contexts

Fix:

1. Cap context
2. Timeout + fallback
3. Hedge rare
4. Alert tails

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Know.
- Save.
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

Avoid budget-free usage; cache-free repeats; single-tier-everything; SLO-free serving; guard-free cuts; attribution-free bills.

## Bundled References

Read `references/llm-economics.md` when budgeting or optimizing LLM spend.
Run `scripts/llm_cost_tracker.py` to attribute LLM spend.
Copy `assets/checklists.md` into every delivery.
