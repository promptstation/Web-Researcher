---
name: react-nextjs-extraction
description: Extract Next.js data from payloads and data routes fetch-first with build-safe URLs. Use when the user asks to scrape a Next.js site without a browser; parse __NEXT_DATA__ reliably; build _next/data URLs; handle Next.js locales in scraping; find the API behind Next.js pages.
compatibility: Any OS with Python 3.10+ and outbound HTTPS; no browser or Node required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# React Nextjs Extraction

Turn Next.js conventions into fetch-first pipelines. You parse payloads with schemas, construct data URLs that survive rebuilds and locales, and fall back to version-pinned APIs when markup shifts.

Optimize simultaneously for:

- parsed payloads
- build-safe URLs
- locale-correct routes
- pinned fallbacks
- browser-free pipelines

Do not hardcode buildIds or locales, and do not parse flight streams by hand when HTML or JSON channels suffice.

## Use Cases

### Listing extraction

Trigger: user says 'scrape this Next.js shop' or 'get products fetch-first'

Steps:

1. Fetch and parse __NEXT_DATA__
2. Validate pageProps schema
3. Page via data routes
4. Emit versioned records

Result: Fast fetch-first pipeline.

### Multi-locale catalog

Trigger: user says 'all locales' or 'regions break URLs'

Steps:

1. Discover locale prefixes and default
2. Parameterize routes by locale
3. Verify each locale separately
4. Publish the locale matrix

Result: Complete regional coverage.

### Payload shift

Trigger: user says 'props changed shape' or 'buildId expired'

Steps:

1. Detect schema or build drift
2. Refresh buildId from HTML
3. Re-pin schema version
4. Backfill affected window

Result: Self-healing extractor.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Payload schema with version
- BuildId discovery steps
- Data-route templates
- Locale matrix
- Fallback API contract
- Drift detectors
- Record versioning
- Re-run commands

Never hardcode buildIds, and never ship extractors without schema validation and drift detection.

## Phase 1 — Parse Payloads

Run `scripts/nextjs_data_miner.py --url <page>` and inspect pageProps keys.

Define the record schema from observed keys with types.

Validate every row before writing.

## Phase 2 — Build Data Routes

Extract buildId from HTML on each run; never cache across days blindly.

Template _next/data URLs with locale and query handling.

Verify JSON responses parse to the same schema.

## Phase 3 — Cover Locales

Enumerate locales from HTML and headers.

Test default plus each prefixed locale.

Record the working matrix.

## Phase 4 — Pin Fallbacks

Map the underlying API behind data routes.

Pin versions and auth handling.

Alert on schema drift with samples.

## Examples

### Example 1: Catalog pipeline

User says: "Daily products from a Next.js store."

Actions:

1. Parsed pageProps, paged data routes
2. Validated 12k rows nightly
3. BuildId auto-refresh
4. Zero browsers, stable for months

Result: Cheap reliable feed.

### Example 2: Locale expansion

User says: "Add DE and FR catalogs."

Actions:

1. Found locale prefixes in HTML
2. Parameterized extractor
3. Verified per-locale counts
4. Matrix published

Result: Full regional coverage.

## Troubleshooting

### data routes 404 suddenly

Cause: New deploy rotated buildId

Fix:

1. Refresh buildId from HTML
2. Rebuild URL templates
3. Add buildId age alert
4. Backfill missed window

### pageProps keys renamed

Cause: App refactor changed payload shape

Fix:

1. Diff old vs new keys
2. Update schema version
3. Dual-read during transition
4. Alert on future renames

### Locale returns default content

Cause: Wrong prefix or cookie-based locale

Fix:

1. Inspect locale detection logic
2. Send correct prefix plus headers
3. Verify content language markers
4. Lock the working combo

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Payload.
- Routes.
- Guard.

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

Avoid hardcoded buildIds; single-locale extractors; unvalidated props parsing; flight hand-parsing first; silent schema drift; browsers before payload checks.

## Bundled References

Read `references/nextjs-channels.md` when choosing payload, data-route, or API extraction.
Run `scripts/nextjs_data_miner.py` to extract payloads and data-route templates.
Copy `assets/checklists.md` into every delivery.
