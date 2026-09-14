---
name: framework-gatekeeping-triage
description: Detect framework gates from evidence and answer with permission and APIs, not circumvention. Use when the user asks to classify a redirect wall; detect signed URL gating; separate bot walls from CSR; request scraping permission; find API alternatives to gated pages.
compatibility: Any OS with Python 3.10+ and HTTPS; no bypass tooling included or needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# Framework Gatekeeping Triage

Read gates honestly and answer lawfully. You classify middleware and signing from response evidence, separate gating from rendering faults, and convert blocks into permission requests, API alternatives, or reduced scope.

Optimize simultaneously for:

- classified gates
- mapped chains
- correct triage
- filed permissions
- viable alternatives

Never circumvent signing, tokens, or access checks; probe minimally, log fully, and seek permission or APIs.

## Use Cases

### Wall triage

Trigger: user says 'redirect loop' or 'blocked after 10 pages'

Steps:

1. Capture chains and headers
2. Classify the gate
3. Stop automated pressure
4. File permission or API path

Result: Correct classification, lawful next step.

### Signed feed

Trigger: user says 'URLs expire' or 'tokens in links'

Steps:

1. Confirm signing shape
2. Find the lawful issuance path
3. Use issued URLs in scope
4. Never forge or extend

Result: Working within issuance.

### Scope rescue

Trigger: user says 'need something, blocked on all'

Steps:

1. Inventory public surfaces
2. Map official APIs
3. Draft permission request
4. Deliver reduced-scope plan

Result: Viable lawful plan.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Chain transcripts
- Gate classification with evidence
- Triage verdict
- Probe log
- Permission draft
- API alternative map
- Reduced-scope plan
- Stop/continue decision

Never forge signatures or tokens, and never probe gates aggressively to wear them down.

## Phase 1 — Capture Evidence

Run `scripts/middleware_probe.py --url <page>` and save chains plus headers.

Record cookies set, edge headers, and timing per hop.

Stop automated fetching once gating is confirmed.

## Phase 2 — Classify the Gate

Distinguish middleware redirect, signed URL, token wall, rate shape, and consent/geo.

Quote the exact evidence per classification.

Separate from CSR and render faults explicitly.

## Phase 3 — Seek Lawful Paths

Map official APIs and public surfaces.

Draft a permission request with scope, rate, and purpose.

Define reduced scope that still delivers value.

## Phase 4 — Decide and File

Recommend proceed, permission-first, or stop.

File evidence, drafts, and decision.

Set review dates for pending permissions.

## Examples

### Example 1: Middleware wall

User says: "Listings redirect to verify page."

Actions:

1. Classified edge middleware gate
2. Stopped scraping pressure
3. Found official catalog API
4. Permission granted in a week

Result: API access, wall respected.

### Example 2: Expiring links

User says: "Media URLs die in minutes."

Actions:

1. Confirmed signed issuance
2. Used in-scope issued URLs fast
3. Never forged extensions
4. Pipeline within terms

Result: Compliant media flow.

## Troubleshooting

### Gate triggers inconsistently

Cause: Sampling, geo, or reputation thresholds

Fix:

1. Log trigger conditions
2. Reduce rate and scope
3. Seek permission early
4. Never tune to evade

### Permission pending, deadline near

Cause: Slow access processes

Fix:

1. Deliver public-surface interim
2. Escalate request politely
3. Narrow scope to speed approval
4. Never self-authorize

### API lacks needed fields

Cause: Public API subset smaller than UI

Fix:

1. Document the gap precisely
2. Request field expansion
3. Combine API plus public HTML
4. Accept partial coverage honestly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Evidence.
- Classify.
- Lawful.

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

Avoid gate circumvention; signature forging; aggressive gate probing; self-authorized access; render theories over gate evidence; pressure after classification.

## Bundled References

Read `references/gate-shapes.md` when classifying walls and planning responses.
Run `scripts/middleware_probe.py` to capture gate evidence politely.
Copy `assets/checklists.md` into every delivery.
