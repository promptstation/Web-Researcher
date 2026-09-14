---
name: egress-health-scoring
description: Score every egress continuously and quarantine with canary recovery. Use when the user asks to score proxy health; set quarantine thresholds; rank egress by quality; recover quarantined IPs; dashboard proxy fleet health.
compatibility: Outcome logs (JSONL); any provider; scheduler for scoring cadence.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Egress Health Scoring

Know every egress by number. You score health from five signals with decay, trip thresholds from data, quarantine in minutes, recover through canaries, and retire the hopeless — with dashboards telling the story.

Optimize simultaneously for:

- scored egress
- tuned thresholds
- fast quarantine
- canaried recovery
- live dashboards

Scores from measured outcomes only; quarantine protects targets and budgets, not just success rates.

## Use Cases

### Fleet ranking

Trigger: user says 'which IPs are bad' or 'rank egress'

Steps:

1. Score all egress
2. Rank and explain
3. Act on bottom decile
4. Track trend

Result: Ranked healthy fleet.

### Auto-heal

Trigger: user says 'automate quarantine' or 'stop manual blocks'

Steps:

1. Set thresholds
2. Automate lifecycle
3. Canary recoveries
4. Audit weekly

Result: Self-healing fleet.

### Provider evidence

Trigger: user says 'prove quality drop' or 'claim SLA'

Steps:

1. Export score history
2. Show thresholds
3. File claim
4. Migrate or credit

Result: Data-backed claim.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Signal catalog
- Scoring formula
- Threshold table
- Lifecycle log
- Canary results
- Dashboards
- SLA evidence
- Tuning history

Never score on vibes or skip canary before returning egress to full traffic.

## Phase 1 — Score All

Run `scripts/egress_scorer.py --logs outcomes.jsonl` on schedule.

Five signals, decayed, 0-100.

Publish rankings.

## Phase 2 — Trip Fast

Warn at 70, quarantine at 50, retire at 3 failed probes.

Automate transitions.

Log every state change.

## Phase 3 — Canary Back

3 cheap probes, then 5 percent traffic.

Graduate on sustained green.

Retire on repeated red.

## Phase 4 — Tune Quarterly

Review threshold hits.

Adjust weights by cost of errors.

File tuning notes.

## Examples

### Example 1: Silent rot

User says: "Success sagging for weeks."

Actions:

1. Scores showed bottom-third rot
2. Quarantined, canaried
3. Success back in a day
4. Decay tuned

Result: Caught slow rot.

### Example 2: SLA claim

User says: "Provider denies issues."

Actions:

1. Score history exported
2. Claim filed, credits won
3. Egress replaced
4. Monitoring kept

Result: Paid for proof.

## Troubleshooting

### Scores noisy

Cause: Small samples or no decay

Fix:

1. Minimum 20 outcomes
2. Exponential decay
3. Smooth weekly
4. Verify stable

### Quarantine too eager

Cause: Thresholds above noise

Fix:

1. Require consecutive fails
2. Widen bands
3. Add ban-signal weight
4. Re-tune

### Canary passes, full fails

Cause: Load-sensitive target

Fix:

1. Graduate in steps
2. Watch at each
3. Cap below knee
4. Document ceiling

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Score.
- Act.
- Tune.

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

Avoid vibes-based blocks; threshold-free fleets; canary-free returns; decay-free scores; unlogged transitions; evidence-free SLA talks.

## Bundled References

Read `references/health-scoring.md` when scoring egress or tuning thresholds.
Run `scripts/egress_scorer.py` to score egress from outcome logs.
Copy `assets/checklists.md` into every delivery.
