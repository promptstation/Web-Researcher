---
name: crawl-frontier-ops
description: Run polite priority frontiers that finish domains completely. Use when the user asks to build a web crawler frontier; prioritize crawl URLs; polite crawling per host; schedule URL revisits; track crawl coverage.
compatibility: Python 3.10+; robots parser; queue store per scale.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Crawl Frontier Ops

Crawl completely and politely. You score every URL, queue per host with delays, honor robots strictly, dedupe with canonical seen-sets, and revisit by measured change — proving coverage and courtesy.

Optimize simultaneously for:

- scored frontiers
- polite hosts
- complete coverage
- fresh revisits
- proven courtesy

Robots and delays are law; coverage never justifies hammering.

## Use Cases

### Domain crawl

Trigger: user says 'crawl our site' or 'full domain'

Steps:

1. Seed + score
2. Queue polite
3. Crawl + track
4. Report coverage

Result: Complete polite crawl.

### Freshness loop

Trigger: user says 'keep updated' or 'recrawl changed'

Steps:

1. Measure change
2. Schedule revisits
3. Fetch deltas
4. Verify fresh

Result: Fresh corpus.

### Politeness proof

Trigger: user says 'prove we're polite' or 'complaint received'

Steps:

1. Pull delay logs
2. Show robots hits
3. Tune if needed
4. Respond data

Result: Defensible crawling.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Seed list
- Priority formula
- Host table
- Robots cache
- Seen-store design
- Revisit policy
- Coverage report
- Politeness log

Never crawl without robots checks or exceed per-host politeness budgets.

## Phase 1 — Seed and Score

Canonicalize seeds; score depth/inlink/value.

Prototype with `scripts/frontier.py --seed URL`.

Budget per host.

## Phase 2 — Queue Polite

Per-host FIFO with delay >= max(robots, 1s).

Concurrency 1-2 per host.

Log every fetch decision.

## Phase 3 — Crawl and Track

Seen-set gate; extract outlinks.

Coverage vs sitemap/known.

Quarantine traps.

## Phase 4 — Revisit

Change-rate per URL class.

Schedule by freshness need.

Prove lag vs SLA.

## Examples

### Example 1: Full domain

User says: "Crawl 200k pages politely."

Actions:

1. Frontier scored
2. 1s delays, 2 workers
3. Complete in 6 days
4. Zero complaints

Result: Complete courteous crawl.

### Example 2: Trap escaped

User says: "Calendar trap exploding."

Actions:

1. Pattern detected
2. Quarantined + capped
3. Coverage true
4. Rule kept

Result: Finite crawl.

## Troubleshooting

### Frontier explodes

Cause: Traps, facets, sessions

Fix:

1. Canonicalize hard
2. Cap per pattern
3. Blacklist traps
4. Budget strictly

### Slow crawl

Cause: Serial per-host + many hosts

Fix:

1. Parallelize across hosts
2. Keep per-host polite
3. Tune workers
4. Respect delays

### Stale corpus

Cause: No revisit schedule

Fix:

1. Measure change
2. Schedule revisits
3. Track lag
4. Alert SLA

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Seed.
- Run.
- Keep.

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

Avoid unscored frontiers; delay-free hosts; robots-free crawling; uncanonicalized seen; trap-blind budgets; revisit-free corpora.

## Bundled References

Read `references/frontier-design.md` when building or tuning crawlers.
Run `scripts/frontier.py` to prototype a polite priority frontier.
Copy `assets/checklists.md` into every delivery.
