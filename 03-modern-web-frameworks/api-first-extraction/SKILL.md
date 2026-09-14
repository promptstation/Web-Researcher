---
name: api-first-extraction
description: Discover hidden REST and GraphQL APIs and extract API-first with documented contracts. Use when the user asks to find the API behind a website; mine endpoints from JS bundles; document a GraphQL schema; replace DOM scraping with APIs; map API pagination and auth.
compatibility: Any OS with Python 3.10+ and HTTPS; permission or public access for gated APIs.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# API First Extraction

Make DOM scraping the last resort. You mine endpoints from frontend evidence, discover schemas, document contracts with auth and pagination, and extract through the cleanest lawful channel available.

Optimize simultaneously for:

- mined endpoints
- found schemas
- documented contracts
- faithful replays
- API-first pipelines

Use only public or permitted endpoints; authenticate legitimately and honor rate limits and terms.

## Use Cases

### Bundle mining

Trigger: user says 'find hidden API' or 'endpoints in JS'

Steps:

1. Fetch bundles with caps
2. Mine and rank endpoints
3. Verify with live calls
4. Document contracts

Result: Verified endpoint inventory.

### GraphQL mapping

Trigger: user says 'map this GraphQL API' or 'introspection?'

Steps:

1. Find the endpoint lawfully
2. Request or derive schema subset
3. Document queries needed
4. Extract with paging

Result: Minimal working query set.

### DOM replacement

Trigger: user says 'replace brittle scraping' or 'stable feed'

Steps:

1. Map current DOM fields to API fields
2. Build API extractor
3. Parallel-run and diff
4. Cut over with monitoring

Result: Stable API pipeline.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Endpoint inventory with confidence
- Schema or subset docs
- Auth documentation
- Param and paging maps
- Rate-limit notes
- Replay transcripts
- Contract version stamps
- Access records where gated

Never hammer undocumented endpoints, and never bypass API auth or quota controls.

## Phase 1 — Mine Endpoints

Run `scripts/api_surface_mapper.py --url <page> --max-js 6` for ranked endpoints.

Verify each candidate with a live call.

Rank by data value and stability.

## Phase 2 — Discover Schemas

Probe well-known schema paths and developer pages.

Use introspection only where permitted.

Record the minimal schema subset needed.

## Phase 3 — Document Contracts

Write auth, params, paging, errors, and limits per endpoint.

Stamp versions and dates.

Note deprecation signals.

## Phase 4 — Extract API-First

Build paged extraction with backoff.

Validate rows against schemas.

Monitor contract drift.

## Examples

### Example 1: Listing API

User says: "Product pages break weekly."

Actions:

1. Mined search API from bundle
2. Documented paging and filters
3. Cut over from DOM
4. Breakage ended

Result: Stable feed from API.

### Example 2: GraphQL subset

User says: "Need three fields, huge schema."

Actions:

1. Derived minimal queries
2. Tested with paging
3. Documented the subset
4. Lean stable pulls

Result: Minimal durable queries.

## Troubleshooting

### Endpoints 401/403

Cause: Missing auth, token, or header

Fix:

1. Replay browser headers exactly
2. Complete legitimate auth
3. Request access if gated
4. Never strip protections

### Pagination gaps

Cause: Cursor expiry or offset drift

Fix:

1. Use cursors over offsets
2. Checkpoint per page
3. Dedupe by stable IDs
4. Verify counts

### Schema drift breaks pulls

Cause: Unversioned API changes

Fix:

1. Version contracts
2. Alert on unknown fields
3. Dual-read transitions
4. Pin to versioned paths

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Mine.
- Document.
- Run.

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

Avoid blind endpoint greps; introspection without permission; undocumented endpoints at scale; auth bypass attempts; quota ignoring; contracts without versions.

## Bundled References

Read `references/api-discovery.md` when mining endpoints or documenting contracts.
Run `scripts/api_surface_mapper.py` to mine and rank API endpoints from frontend code.
Copy `assets/checklists.md` into every delivery.
