---
name: automation-framework-ops
description: Structure automation frameworks for CI scale and years of maintenance. Use when the user asks to structure a Playwright framework; shard tests in CI; manage test artifacts; assign test ownership; maintain automation long-term.
compatibility: Playwright or Puppeteer with any CI (GitHub Actions, Jenkins, GitLab); artifact storage per policy.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Automation Framework Ops

Build automation that ages well. You structure around flows, shard CI fairly, keep artifacts useful and bounded, assign every area an owner, and deprecate with care.

Optimize simultaneously for:

- clean layouts
- fair shards
- bounded artifacts
- clear owners
- safe deprecations

No ownerless areas and no unbounded artifacts; every helper earns its keep or retires.

## Use Cases

### New framework

Trigger: user says 'start test automation right' or 'framework layout'

Steps:

1. Lay out flows and fixtures
2. Wire CI sharded
3. Set artifact policy
4. Assign owners

Result: Team-ready framework.

### Slow CI

Trigger: user says 'suite takes hours' or 'shard this'

Steps:

1. Measure per-test times
2. Shard balanced
3. Parallelize safely
4. Verify faster green

Result: Fast fair CI.

### Legacy cleanup

Trigger: user says 'crufty helpers' or 'dead tests'

Steps:

1. Audit usage
2. Deprecate gently
3. Migrate callers
4. Delete with proof

Result: Lean living suite.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Layout doc
- Fixture catalog
- CI config sharded
- Artifact policy
- Ownership map
- Helper docs
- Deprecation log
- Health metrics

Never merge ownerless code, and never keep artifacts or helpers without retention and usage proof.

## Phase 1 — Lay Out

Organize by user flows, not components.

Centralize fixtures with clear lifetimes.

Document the map on one page.

## Phase 2 — Wire CI

Shard by timing with retries fenced.

Upload traces on failure only.

Gate merges on green.

## Phase 3 — Triage Artifacts

Run `scripts/artifact_triage.py --dir artifacts/` nightly for failure summaries.

Retain per policy; purge on schedule.

Link artifacts from reports.

## Phase 4 — Own and Prune

Assign every area; review coverage quarterly.

Deprecate with migration windows.

Track health metrics monthly.

## Examples

### Example 1: Hour to minutes

User says: "Suite takes 3 hours."

Actions:

1. Sharded 8 ways balanced
2. Fixed serial bottlenecks
3. Down to 22 minutes
4. Green stable

Result: Fast CI.

### Example 2: Cruft purge

User says: "Nobody knows what half does."

Actions:

1. Audited usage: 40 percent dead
2. Deprecated with windows
3. Deleted with proof
4. Docs current

Result: Lean suite.

## Troubleshooting

### Shard imbalance

Cause: Alphabetical splits, heavy files

Fix:

1. Split by measured time
2. Rebalance quarterly
3. Isolate slow outliers
4. Verify even runtimes

### Artifact bloat

Cause: Videos always-on, no retention

Fix:

1. Failures-only capture
2. Retention windows
3. Purge jobs
4. Monitor storage

### Ownership gaps

Cause: Authors left, areas orphaned

Fix:

1. Map orphans fast
2. Assign plus onboard
3. Review stale areas
4. Never re-orphan

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Lay.
- CI.
- Own.

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

Avoid component-tree layouts; unsharded mega-suites; always-on videos; ownerless areas; undead helpers; metrics-free maintenance.

## Bundled References

Read `references/framework-layout.md` when structuring or reviewing frameworks.
Run `scripts/artifact_triage.py` to summarize run artifacts nightly.
Copy `assets/checklists.md` into every delivery.
