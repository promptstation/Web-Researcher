---
name: scrape-schema-design
description: Design strict record schemas and validate with actionable quarantine. Use when the user asks to design a scraping schema; validate JSONL records; handle bad scraped data; quarantine invalid records; track data validation rates.
compatibility: Python 3.10+; JSON Schema optional; quarantine store per volume.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Scrape Schema Design

Let only good records through. You design minimal complete schemas, type strictly, validate at every boundary, quarantine rejects with codes, and track rates so quality stays visible.

Optimize simultaneously for:

- complete schemas
- strict types
- validated boundaries
- coded rejects
- visible rates

No record enters clean without passing schema; no reject without code and owner.

## Use Cases

### New extraction

Trigger: user says 'define output format' or 'schema for products'

Steps:

1. Draft minimal schema
2. Validate samples
3. Tighten types
4. Publish v1

Result: Contract-grade schema.

### Dirty feed

Trigger: user says 'bad records downstream' or 'types wrong'

Steps:

1. Validate at boundary
2. Quarantine coded
3. Fix extractor
4. Verify rate

Result: Clean downstream.

### Consumer contract

Trigger: user says 'API broke us' or 'fields changed'

Steps:

1. Contract-test schema
2. Version change
3. Dual-read
4. Retire old

Result: Stable contract.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Schema doc versioned
- Identity spec
- Type table
- Validation rules
- Reject taxonomy
- Quarantine location
- Rate dashboard
- Contract tests

Never loosen schemas to hide extractor bugs, and never drop rejects silently.

## Phase 1 — Author Schema

Identity, timestamps, required, optional, enums.

Money minor-units, dates UTC, URLs normalized.

Review with consumers.

## Phase 2 — Validate Boundaries

Run `scripts/schema_guard.py --schema s.json --in records.jsonl`.

Fail fast per record; never partial writes.

Track pass rate.

## Phase 3 — Quarantine Coded

Codes: MISSING, TYPE, RANGE, ENUM, IDENTITY, STALE.

Owner per code; SLA per code.

Review daily to weekly.

## Phase 4 — Contract-Test

Consumers test against schema.

Version bumps announced.

Dual-read windows honored.

## Examples

### Example 1: Feed cleaned

User says: "Null prices reaching prod."

Actions:

1. Required price_cents
2. Quarantined 2 percent coded
3. Extractor fixed
4. Rate 99.9 held

Result: Trusted feed.

### Example 2: Contract saved

User says: "Partner changed fields silently."

Actions:

1. Contract test caught day 0
2. Pinned v1, dual v2
3. Zero downtime
4. SLA credited

Result: Change absorbed.

## Troubleshooting

### Validation too strict

Cause: Optional reality marked required

Fix:

1. Downgrade to optional
2. Version the change
3. Backfill nulls
4. Notify consumers

### Quarantine floods

Cause: Source change or extractor bug

Fix:

1. Pause intake
2. Fix the class
3. Replay sample
4. Then drain

### Identity collisions

Cause: Weak key derivation

Fix:

1. Strengthen key
2. Rebuild index
3. Reconcile dupes
4. Test uniqueness

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Author.
- Guard.
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

Avoid schemaless clean; loose-to-hide-bugs; silent drops; codeless rejects; unversioned changes; contract-free consumers.

## Bundled References

Read `references/schema-discipline.md` when authoring or enforcing schemas.
Run `scripts/schema_guard.py` to validate JSONL against a simple schema.
Copy `assets/checklists.md` into every delivery.
