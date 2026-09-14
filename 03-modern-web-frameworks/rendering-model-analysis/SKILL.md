---
name: rendering-model-analysis
description: Identify CSR, SSR, SSG, and hydration from HTML evidence and pick the cheapest extraction path. Use when the user asks to tell if a site is CSR or SSR; find data payloads in HTML; decide fetch versus browser scraping; explain hydration mismatches; map rendering models across routes.
compatibility: Any OS with Python 3.10+ and outbound HTTPS; browser DevTools optional for confirmation.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# Rendering Model Analysis

Stop guessing how pages render. You read HTML evidence, score fetch-side completeness, locate data payloads, and route each flow to the cheapest extraction path that provably works.

Optimize simultaneously for:

- evidence-backed verdicts
- located payloads
- scored completeness
- correct path choices
- route-wide maps

Do not launch browsers for pages whose data already ships in HTML or payloads, and never verdict from one route alone.

## Use Cases

### Model verdict

Trigger: user says 'is this site CSR' or 'can I scrape without a browser'

Steps:

1. Fetch representative routes
2. Inventory markers and payloads
3. Score completeness
4. Verdict with evidence

Result: Verdict plus cheapest path.

### Payload discovery

Trigger: user says 'data must be somewhere in HTML' or 'find the JSON'

Steps:

1. List embedded JSON scripts
2. Parse state keys
3. Map keys to visible data
4. Extract fetch-first

Result: Direct data access, no browser.

### Hydration fault

Trigger: user says 'content flashes' or 'hydration error in console'

Steps:

1. Capture server HTML versus client render
2. Diff the mismatching subtree
3. Name the nondeterministic source
4. Fix and verify clean hydrate

Result: Stable hydration with cause named.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Marker table per route
- Completeness scores with method
- Payload inventory with keys
- Path decision with rationale
- Route map for the section
- Fetch commands recorded
- Re-verification steps
- Exception routes listed

Never default to browsers without fetch-side evidence, and never verdict a whole site from its homepage.

## Phase 1 — Fetch and Inventory

Run `scripts/rendering_mode_probe.py --url <page>` on representative routes.

Record markers: payload scripts, meta generator, root fullness, header hints.

Save raw HTML samples for the record.

## Phase 2 — Score Completeness

Measure text length, link counts, and target-data presence fetch-side.

Grade each route: complete, payload-backed, or browser-required.

Note which data lives in payloads versus post-load fetches.

## Phase 3 — Decide the Path

Route complete and payload-backed pages fetch-first.

Reserve browsers for proven client-only flows.

Document the decision tree with thresholds.

## Phase 4 — Map and Verify

Extend the verdict across the section's routes.

Re-verify monthly or after framework upgrades.

Flag exception routes explicitly.

## Examples

### Example 1: Storefront verdict

User says: "Do we need Playwright for this shop?"

Actions:

1. Probed 8 routes: SSR with __NEXT_DATA__
2. Prices in payload scripts
3. Built fetch-first extractor
4. Browsers dropped entirely

Result: 10x cheaper extraction.

### Example 2: Mixed models

User says: "Some pages work with curl, some do not."

Actions:

1. Mapped: listings SSR, checkout CSR
2. Split paths per route class
3. Browsers only for checkout
4. Map published with markers

Result: Right tool per route.

## Troubleshooting

### Payload present but data missing

Cause: Client-only fetch after hydrate or auth-gated props

Fix:

1. Check for post-load API calls
2. Verify auth state in fetch
3. Fall back to API mapping
4. Document the split source

### SSR verdict but empty fetch

Cause: Bot-gated SSR or geo/consent wall

Fix:

1. Compare headers and cookies
2. Test consent and geo variants
3. Classify as gating, not CSR
4. Route to challenge triage

### Hydration errors in console

Cause: Nondeterministic render: dates, random, extensions

Fix:

1. Diff server vs client subtree
2. Stabilize the random source
3. Suppress extension interference in tests
4. Verify clean hydrate

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Evidence.
- Scores.
- Map.

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

Avoid browser-first by default; one-route whole-site verdicts; payloads ignored in HTML; hydration blamed before evidence; framework guesses without markers; stale verdicts after upgrades.

## Bundled References

Read `references/rendering-markers.md` when classifying pages or finding payload scripts.
Run `scripts/rendering_mode_probe.py` to classify rendering models fetch-side.
Copy `assets/checklists.md` into every delivery.
