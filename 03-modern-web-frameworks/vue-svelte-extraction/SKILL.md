---
name: vue-svelte-extraction
description: Mine Nuxt, Vue, SvelteKit, and Astro embedded state fetch-first. Use when the user asks to scrape a Nuxt site fetch-first; parse __NUXT__ payloads; extract SvelteKit data nodes; handle Astro islands; inventory embedded JSON state.
compatibility: Any OS with Python 3.10+ and outbound HTTPS; no browser or Node required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# Vue Svelte Extraction

Treat every framework as a state-delivery system. You census embedded JSON islands, parse each format safely, map state keys to entities, and ship version-tolerant fetch-first extractors.

Optimize simultaneously for:

- complete state census
- parsed payloads
- mapped stores
- scoped islands
- tolerant extractors

Do not execute page scripts to read state, and do not assume one framework per site without a census.

## Use Cases

### Nuxt catalog

Trigger: user says 'scrape this Nuxt store' or 'payload parsing fails'

Steps:

1. Census state scripts
2. Parse payload with reviver handling
3. Map keys to records
4. Validate and emit

Result: Fetch-first Nuxt pipeline.

### SvelteKit content

Trigger: user says 'SvelteKit pages' or 'data nodes'

Steps:

1. Extract data nodes per route
2. Template data URLs
3. Handle form actions where needed
4. Verify across routes

Result: Node-driven extraction.

### Mixed stack

Trigger: user says 'multiple frameworks' or 'migrating stack'

Steps:

1. Run generic miner everywhere
2. Classify per route
3. Build per-class extractors
4. Unify records downstream

Result: Coverage across the migration.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- State census per route
- Format notes per framework
- Key-to-entity mapping
- Schema versions
- Validation rules
- Drift alerts
- Re-run commands
- Migration notes where mixed

Never eval page scripts for state, and never ship without key mapping and validation.

## Phase 1 — Census State

Run `scripts/spa_state_miner.py --url <page>` per template.

List every application/json script with id, size, and top keys.

Classify the framework per route from markers.

## Phase 2 — Parse Formats

Handle Nuxt reviver formats by version.

Read Pinia/Vuex stores as plain JSON.

Extract SvelteKit nodes and Astro props.

## Phase 3 — Map Entities

Map state keys to products, articles, or events.

Define schemas with versions.

Validate rows before writing.

## Phase 4 — Tolerate Change

Alert on new or renamed keys.

Dual-read during transitions.

Re-census after upgrades.

## Examples

### Example 1: Nuxt migration

User says: "Site moved Nuxt 2 to 3, extractor broke."

Actions:

1. Census showed payload format change
2. Added reviver v2 parsing
3. Dual-read both shapes
4. Stable within a day

Result: Upgrade-proof pipeline.

### Example 2: Astro islands

User says: "Mostly static but prices load late."

Actions:

1. Scoped islands carrying prices
2. Mapped island APIs
3. Static HTML plus island fetches
4. Fast hybrid extraction

Result: Correct hybrid path.

## Troubleshooting

### Payload parse throws

Cause: Reviver format or truncated capture

Fix:

1. Check payload version markers
2. Capture full script bounds
3. Add version branch
4. Test on fixtures

### Keys present, values empty

Cause: Auth-gated or lazy state

Fix:

1. Compare authed vs anon state
2. Trigger the lazy route
3. Map the gated API
4. Document the gate

### Framework misdetected

Cause: Mixed stack or leftover markers

Fix:

1. Trust per-route census
2. Weight payload presence over meta
3. Split extractors per class
4. Re-census quarterly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Census.
- Parse.
- Change.

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

Avoid eval on payload scripts; one-framework assumptions; unmapped store keys; reviver formats guessed; islands scraped without scope; upgrades without re-census.

## Bundled References

Read `references/embedded-state.md` when mining framework payloads.
Run `scripts/spa_state_miner.py` to inventory embedded JSON state on any page.
Copy `assets/checklists.md` into every delivery.
