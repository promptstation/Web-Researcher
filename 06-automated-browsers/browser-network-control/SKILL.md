---
name: browser-network-control
description: Route, block, mock, and mine browser traffic for speed and API-first wins. Use when the user asks to block ads in Playwright; mock API responses; capture APIs from browser traffic; mine HAR files for endpoints; speed up page loads in automation.
compatibility: Playwright or Puppeteer; HAR files for mining; no proxy needed for route-level work.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Browser Network Control

Own the traffic your browsers generate. You observe everything, block dead weight safely, mock for determinism, mine HARs for contracts, and pair DOM with API channels for unbreakable collection.

Optimize simultaneously for:

- observed traffic
- safe blocks
- pinned mocks
- mined contracts
- dual channels

Block only what you prove unnecessary; mock only in tests, never to fake production data.

## Use Cases

### Speed up

Trigger: user says 'pages slow in automation' or 'block trackers'

Steps:

1. Log traffic
2. Prove dead weight
3. Block with allowlist care
4. Verify data intact

Result: Faster renders, same data.

### Deterministic tests

Trigger: user says 'API flaky in tests' or 'need fixtures'

Steps:

1. Capture real responses
2. Author mocks
3. Pin versions
4. Verify fidelity

Result: Stable hermetic tests.

### API discovery

Trigger: user says 'find page APIs' or 'HAR to contract'

Steps:

1. Record HAR of flow
2. Mine endpoints
3. Document contracts
4. Build API-first path

Result: Contracts from traffic.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Traffic inventory
- Blocklist with rationale
- Mock catalog versioned
- HAR archive
- Contract docs
- Fidelity checks
- Route cleanup proof
- Perf deltas

Never block first-party data paths, and never ship mocks outside test scope.

## Phase 1 — Observe Traffic

Log all requests for the flow with types and sizes.

Rank by weight and necessity.

Save a baseline HAR.

## Phase 2 — Block and Mock

Block proven dead weight with logged rules.

Author mocks from real captures.

Version every mock with source date.

## Phase 3 — Mine Contracts

Run `scripts/har_api_miner.py --har flow.har` for endpoint inventory.

Document auth, params, paging.

Verify with live calls.

## Phase 4 — Pair Channels

Build DOM plus API extraction.

Cross-check values between channels.

Alert on divergence.

## Examples

### Example 1: Tracker diet

User says: "News pages take 20s automated."

Actions:

1. Logged 180 third-party requests
2. Blocked 150 safely
3. Load to 4s, data same
4. Blocklist versioned

Result: 5x faster renders.

### Example 2: Contract win

User says: "DOM parsing breaks monthly."

Actions:

1. Mined article API from HAR
2. Built API-first extractor
3. DOM kept as fallback
4. Breakage ended

Result: Stable dual channel.

## Troubleshooting

### Block broke the page

Cause: First-party misclassified as tracker

Fix:

1. Allowlist by exact URL
2. Re-verify data
3. Tighten patterns
4. Add regression test

### Mocks drift from reality

Cause: API evolved, fixtures stale

Fix:

1. Re-capture quarterly
2. Contract-test mocks
3. Alert on drift
4. Version strictly

### HAR mining noise

Cause: Analytics and polling floods

Fix:

1. Filter by content-type and size
2. Focus XHR/fetch to first-party
3. Rank by data value
4. Ignore beacons

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Observe.
- Control.
- Mine.

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

Avoid blind blocklists; mocks in production; stale fixtures; HAR noise treated as signal; single-channel fragility; unlogged route rules.

## Bundled References

Read `references/traffic-routes.md` when routing, blocking, or mocking traffic.
Run `scripts/har_api_miner.py` to mine API contracts from HAR files.
Copy `assets/checklists.md` into every delivery.
