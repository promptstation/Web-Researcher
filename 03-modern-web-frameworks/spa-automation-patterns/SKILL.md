---
name: spa-automation-patterns
description: Automate SPAs with route-aware waits, resilient selectors, and hydration gates. Use when the user asks to fix flaky SPA tests; wait for Next.js route changes; choose Playwright selectors; handle hydration in automation; stop networkidle deadlocks.
compatibility: Playwright or Puppeteer with any SPA; Python or Node; no extra libraries.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# SPA Automation Patterns

Make SPA automation boring and green. You replace sleeps with route and assertion waits, scope network waits safely, climb the selector ladder, gate on hydration, and debug flakes from traces.

Optimize simultaneously for:

- sleep-free suites
- scoped network waits
- resilient selectors
- gated hydration
- trace-fixed flakes

Do not add sleeps to fix flakes, and do not use networkidle on pages with polling or streams.

## Use Cases

### Flake cleanup

Trigger: user says 'tests flaky' or 'passes locally, fails in CI'

Steps:

1. Classify flakes from traces
2. Replace sleeps with waits
3. Fix selectors and scoping
4. Verify with repeated runs

Result: Stable suite with proof.

### New SPA suite

Trigger: user says 'automate this SPA' or 'page objects for Next.js'

Steps:

1. Map flows and routes
2. Build flow page objects
3. Add hydration gates
4. Wire traces and retries

Result: Green suite from day one.

### Data scraping via browser

Trigger: user says 'SPA needs browser' or 'extract after hydrate'

Steps:

1. Prove API paths exhausted first
2. Wait on data selectors
3. Extract with validation
4. Checkpoint and resume

Result: Minimal-browser extraction.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Wait inventory with rationale
- Network-wait scoping notes
- Selector choices with ladder rank
- Hydration gates
- Page-object map
- Flake log with fixes
- Repeat-run evidence
- Trace retention policy

Never commit sleeps or unconditional networkidle, and never automate SPAs without hydration awareness.

## Phase 1 — Audit Waits

List every sleep, timeout, and networkidle in the suite.

Paste `scripts/spa_probe.js` in console to read route, hydration, and pending-request state.

Classify each wait as route, data, or assertion need.

## Phase 2 — Rewrite Waits

Use route events and URL assertions for navigation.

Use locator assertions with auto-retry for data.

Scope response waits to exact URLs; avoid global idle.

## Phase 3 — Harden Selectors

Climb the ladder: role plus name, test-id, text, then CSS last.

Verify uniqueness and stability across runs.

Document why each selector survives refactors.

## Phase 4 — Gate and Verify

Gate interactions on hydration markers.

Run suites 20x and count flakes.

Fix from traces until clean.

## Examples

### Example 1: CI flakes

User says: "Green locally, red in CI."

Actions:

1. Traces showed hydration races
2. Added route plus assertion waits
3. Removed 12 sleeps
4. 50 clean CI runs

Result: Trusted suite.

### Example 2: Stream deadlock

User says: "networkidle never resolves."

Actions:

1. Page polls forever by design
2. Scoped to response URLs
3. Suite time halved
4. Deadlock gone

Result: Correct scoping.

## Troubleshooting

### Click misses after navigation

Cause: Detached element across route change

Fix:

1. Re-query locators after nav
2. Assert URL first
3. Use strict locators
4. Verify with traces

### Strict-mode violations

Cause: Duplicate matches from lists or portals

Fix:

1. Scope to containers
2. Filter by role and name
3. Use nth only with reason
4. Re-check uniqueness

### Hydration double-render flake

Cause: Interacting before client takeover

Fix:

1. Gate on hydration markers
2. Assert stable content first
3. Slow CI runners need longer retries
4. Prove with traces

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Waits.
- Selectors.
- Stable.

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

Avoid sleep-driven suites; global networkidle; XPath-first selectors; pre-hydration clicks; component-tree page objects; untriaged flakes.

## Bundled References

Read `references/spa-waits.md` when writing waits or debugging flakes.
Run `scripts/spa_probe.js` to read SPA route, hydration, and network state in console.
Copy `assets/checklists.md` into every delivery.
