---
name: spa-routing-state
description: Enumerate SPA routes and trace client state for complete extraction coverage. Use when the user asks to list all routes in an SPA; map router guards; find hidden SPA pages; trace store state to UI; plan extraction coverage.
compatibility: Any OS with Python 3.10+ and HTTPS; sitemap and bundle access; no browser needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# SPA Routing State

Leave no route unmapped. You enumerate paths from every source, explain guards and fallbacks, trace state to entities, and produce coverage plans with URL templates and schemas per route class.

Optimize simultaneously for:

- reconciled routes
- mapped guards
- traced state
- templated URLs
- verified coverage

Do not claim full coverage from one enumeration source, and never probe gated routes outside permission.

## Use Cases

### Full enumeration

Trigger: user says 'all pages' or 'complete sitemap'

Steps:

1. Harvest sitemaps
2. Mine bundle routes
3. Read manifests
4. Reconcile and verify

Result: Verified route inventory.

### Guard mapping

Trigger: user says 'some routes redirect' or 'login walls'

Steps:

1. Map guards per route class
2. Classify public vs gated
3. Extract public, scope gated
4. Document the matrix

Result: Honest coverage split.

### Coverage plan

Trigger: user says 'plan the crawl' or 'template the URLs'

Steps:

1. Template URLs per class
2. Attach schemas
3. Sample-verify
4. Publish the plan

Result: Executable crawl plan.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Route inventory with sources
- Guard matrix
- State-flow notes
- URL templates per class
- Schema per class
- Coverage percentages
- Gap list with reasons
- Verification samples

Never enumerate gated routes for extraction without permission, and never trust single-source route lists.

## Phase 1 — Harvest Sources

Run `scripts/route_table_miner.py --site <origin>` for sitemap plus bundle routes.

Add manifest and nav-link sources.

Dedupe into canonical paths.

## Phase 2 — Map Guards

Fetch-sample each class; record redirects and walls.

Classify public, gated, and dead routes.

Exclude gated from unauthenticated plans.

## Phase 3 — Trace State

Link routes to stores and data needs.

Attach expected schemas per class.

Template URLs with param rules.

## Phase 4 — Verify Coverage

Sample-fetch across classes.

Measure schema hit rates.

Publish gaps with reasons.

## Examples

### Example 1: Docs crawl

User says: "Crawl all docs pages."

Actions:

1. Sitemap plus bundle mining: 412 routes
2. Verified 98 percent fetchable
3. Templated versions and locales
4. Plan executed cleanly

Result: Complete docs coverage.

### Example 2: Gated split

User says: "Half the app needs login."

Actions:

1. Guard map split 60/40
2. Public extracted, gated scoped
3. Permission filed for gated
4. Two-track plan delivered

Result: Lawful phased coverage.

## Troubleshooting

### Routes 404 in bulk

Cause: Stale sitemap or base-path drift

Fix:

1. Re-harvest live sources
2. Fix base paths
3. Re-verify samples
4. Date the inventory

### Same content many URLs

Cause: Param variants and canonical gaps

Fix:

1. Canonicalize aggressively
2. Read canonical tags
3. Dedupe by content hash
4. Template canonical forms

### Bundle routes miss pages

Cause: Server-driven nav or CMS paths

Fix:

1. Add sitemap and API listing sources
2. Crawl nav links
3. Reconcile all three
4. Schedule re-enumeration

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Harvest.
- Guards.
- Plan.

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

Avoid single-source route claims; gated routes in public plans; uncanonicalized URL floods; schema-free coverage; stale inventories; guards bypassed not mapped.

## Bundled References

Read `references/route-sources.md` when enumerating SPA routes.
Run `scripts/route_table_miner.py` to enumerate routes from sitemaps and bundles.
Copy `assets/checklists.md` into every delivery.
