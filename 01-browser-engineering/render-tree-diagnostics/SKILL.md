---
name: render-tree-diagnostics
description: Diagnose parse, style, and layout cost and remove render blockers with measured paint wins. Use when the user asks to find what blocks first paint; audit DOM size and style cost; fix slow render on content pages; place defer, async, and preload correctly; prove a render fix with timings.
compatibility: Any modern browser with DevTools; Python 3.10+ for fetch-side audits; no build tools required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Render Tree Diagnostics

Make rendering cost visible and removable. You census the DOM, rank blockers by paint delay, reorder loading without breaking execution, and verify each change with identical before/after paint evidence.

Optimize simultaneously for:

- attributed paint cost
- ranked blocker list
- order-safe loading changes
- verified paint deltas
- regression-proof reports

Do not reorder scripts or styles without an execution-order proof, and do not claim wins without identical before/after measurements.

## Use Cases

### Slow content page

Trigger: user says 'blog loads slowly' or 'first paint over 3 seconds'

Steps:

1. Census DOM and capture waterfall plus trace
2. Rank blockers by paint delay
3. Defer non-critical scripts and gate non-critical CSS
4. Re-measure with the same protocol and report deltas

Result: Faster paint with an auditable change list.

### Framework template audit

Trigger: user says 'template ships too much CSS' or 'unused styles everywhere'

Steps:

1. Run coverage on key templates
2. Split critical from deferred CSS
3. Preload fonts with display=swap
4. Verify no flash or shift regressions

Result: Leaner critical path without visual regressions.

### Scraper-side render triage

Trigger: user says 'need DOM faster for extraction' or 'page too heavy to automate'

Steps:

1. Measure DOM weight and blocking counts fetch-side
2. Block trackers and lazy-load below-fold work
3. Wait on extraction selectors, not load
4. Document the minimal render needed for data

Result: Lighter automated renders with stable selectors.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- DOM census with counts, depth, and heavy subtrees
- Blocker ranking tied to paint delay, not file size alone
- Coverage evidence for removed or deferred bytes
- Order proof for every deferred or async script
- Before/after paint timings from one protocol
- Shift and flash check for visual regressions
- Change list with file, line, and rationale
- Re-measurement steps a second person can repeat

Never ship reorder or removal changes without order proofs and identical before/after paint evidence.

## Phase 1 — Census and Capture

Run `scripts/render_blockers.py --url <page>` for a fetch-side blocker list and DOM weight estimate.

In DevTools, record Performance with screenshots plus Coverage for JS/CSS on the same page.

Write down node count, max depth, listener count, and long-task count before touching anything.

## Phase 2 — Rank Blockers

Order candidates by paint delay caused: parser-blocking scripts first, then blocking CSS, then fonts, then late-discovered work.

Confirm each with waterfall position and main-thread blocking time, not size alone.

Publish the ranked list with evidence links or trace excerpts.

## Phase 3 — Reorder Safely

Apply defer to order-dependent scripts and async only to independent ones; add console order logs for one verification run.

Preload the hero font and the one critical API; preconnect remaining origins.

Gate non-critical CSS by media or split delivery; keep above-fold styling intact.

## Phase 4 — Verify and Guard

Re-run the identical protocol and report first paint, largest paint, total blocking time, and layout shift deltas.

Screenshot above-fold before/after and confirm no flash or shift.

Leave a three-step re-measurement note so regressions are caught the same way.

## Examples

### Example 1: Blog first paint

User says: "Blog paints in 4 seconds, mostly blank."

Actions:

1. Census: 3,800 nodes, 2 parser-blocking scripts in head
2. Deferred both with order logs proving sequence
3. Gated print CSS and preloaded body font
4. Re-measured: paint 4.1s to 1.6s, shift unchanged

Result: Documented 2.5s win with order proofs.

### Example 2: Heavy category page

User says: "Category page janks when automated."

Actions:

1. Fetch-side audit showed 6 blocking third parties
2. Blocked trackers in automation and lazy-loaded below-fold grids
3. Switched waits to extraction selectors
4. Cut automated render cost by half with stable data

Result: Lighter renders, same records.

## Troubleshooting

### Defer broke page behavior

Cause: Order-dependent scripts or DOM-ready assumptions violated

Fix:

1. Restore order with defer sequencing and re-check logs
2. Move inline dependencies after deferred bundles
3. Gate init on DOMContentLoaded explicitly
4. Keep one async exception list with reasons

### Flash of unstyled content after CSS split

Cause: Above-fold rules moved to deferred bundle

Fix:

1. Inline or prioritize above-fold rules
2. Verify with throttled runs and screenshots
3. Measure shift to confirm the fix
4. Lock the critical set in review

### Paint improved but interaction still slow

Cause: Main-thread script cost after paint, not parse blocking

Fix:

1. Profile long tasks after paint
2. Split or idle-schedule non-critical hydration
3. Reduce listener counts on scroll handlers
4. Treat as runtime work, not render blocking

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Census.
- Changes.
- Verification.

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

Avoid async on order-dependent bundles; critical CSS deferred below the fold cutoff; font preloads without display swap; paint claims from different protocols; DOM advice without node and depth counts; third-party blame before first-party blockers are ranked.

## Bundled References

Read `references/parse-and-paint.md` when deciding what blocks paint and how to reorder it.
Run `scripts/render_blockers.py` to list likely render blockers and DOM weight fetch-side.
Copy `assets/checklists.md` into every delivery.
