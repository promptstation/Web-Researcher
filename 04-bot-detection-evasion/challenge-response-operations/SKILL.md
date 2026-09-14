---
name: challenge-response-operations
description: Detect challenges, back off, park, review, and resume with canaries. Use when the user asks to handle CAPTCHAs in pipelines lawfully; back off on bot challenges; park blocked scraping jobs; resume after a ban wave; prevent retry storms.
compatibility: Any OS with Python 3.10+; pipeline logs as input; human reviewers for permitted manual steps.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Challenge Response Operations

Meet challenges with discipline, not force. You detect from existing responses, break and park fast, review lawfully where allowed, and resume through canaries with staged ramps and storm guards.

Optimize simultaneously for:

- fast detection
- clean parks
- lawful reviews
- canary resumptions
- storm-free recovery

Never auto-solve challenges against terms; back off and seek permission or stop.

## Use Cases

### Ban wave

Trigger: user says 'challenges spiking' or 'sudden blocks'

Steps:

1. Detect and break fast
2. Park with evidence
3. Diagnose scope
4. Canary-resume staged

Result: Contained wave, calm return.

### Review queue

Trigger: user says 'manual review for blocks' or 'human fallback'

Steps:

1. Queue with evidence packs
2. Review per terms
3. Decide solve, skip, or stop
4. Log every decision

Result: Accountable human loop.

### Resume protocol

Trigger: user says 'when to retry' or 'safe resume'

Steps:

1. Canary single requests
2. Stage the ramp
3. Watch signals
4. Full flow on green

Result: Verified safe resume.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Detector rules with tests
- Breaker thresholds
- Park records with evidence
- Review decisions logged
- Canary results
- Ramp schedule
- Storm guards armed
- Recovery report

Never retry-storm a challenged domain, and never automate challenge solving against terms.

## Phase 1 — Detect Fast

Run `scripts/block_triage.py --logs jobs.jsonl` to classify and scope.

Alert on challenge-rate thresholds.

Freeze new leases on trip.

## Phase 2 — Park Clean

Move affected jobs with evidence links.

Stamp cause and time.

Notify owners with scope.

## Phase 3 — Review Lawfully

Check terms for manual access.

Decide per item: solve, skip, stop.

Log rationale each time.

## Phase 4 — Resume via Canary

Probe single requests first.

Ramp in stages on green.

Abort to park on re-trip.

## Examples

### Example 1: Overnight wave

User says: "Woke to 80 percent challenges."

Actions:

1. Breaker tripped in 4 minutes
2. Parked 2k jobs clean
3. Canary next morning green
4. Staged resume, no storm

Result: Calm overnight handling.

### Example 2: Manual queue

User says: "Some pages need human eyes."

Actions:

1. Queued 40 with evidence
2. Reviewed per terms
3. Solved 12, skipped 28
4. All decisions logged

Result: Accountable fallback.

## Troubleshooting

### Detector misses new shape

Cause: Vendor changed markers

Fix:

1. Add shape from samples
2. Backtest on history
3. Deploy with tests
4. Watch for a week

### Canary green, ramp red

Cause: Volume-triggered shaping

Fix:

1. Lower ramp ceiling
2. Lengthen stages
3. Find the volume knee
4. Budget under it

### Parks grow unbounded

Cause: No review capacity or no path forward

Fix:

1. Triage to stop decisions
2. Seek access or APIs
3. Close with documented rationale
4. Never auto-expire to retry

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Detect.
- Park.
- Resume.

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

Avoid retry storms; parks that auto-retry; solving against terms; canary skipping; unbounded review queues; unlogged manual solves.

## Bundled References

Read `references/challenge-playbook.md` when handling live challenges.
Run `scripts/block_triage.py` to triage blocks from pipeline logs.
Copy `assets/checklists.md` into every delivery.
