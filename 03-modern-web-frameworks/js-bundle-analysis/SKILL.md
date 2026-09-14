---
name: js-bundle-analysis
description: Map JS bundles by weight and structure and surface secrets and endpoints responsibly. Use when the user asks to analyze webpack bundles; find source maps; scan JS for leaked API keys; map chunks to features; shrink bundle weight.
compatibility: Any OS with Python 3.10+ and HTTPS; published source maps only; no decompilers needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# JS Bundle Analysis

Turn opaque chunks into mapped surfaces. You census weight, recover structure from published maps, trace module boundaries, and surface secrets and endpoints with responsible handling.

Optimize simultaneously for:

- weighted census
- recovered structure
- traced boundaries
- triaged secrets
- mapped surfaces

Use only published maps and code; report leaked secrets to owners and never exploit them.

## Use Cases

### Weight audit

Trigger: user says 'bundle too big' or 'what ships this JS'

Steps:

1. Census and rank chunks
2. Attribute weight to modules
3. Recommend splits
4. Verify savings

Result: Sized, owned weight plan.

### Secret scan

Trigger: user says 'keys in frontend?' or 'audit client secrets'

Steps:

1. Scan with patterns
2. Triage true vs false hits
3. Rotate and disclose
4. Prevent recurrence

Result: Closed leaks with disclosure.

### Surface mapping

Trigger: user says 'what APIs does this app call'

Steps:

1. Extract endpoints and configs
2. Verify live
3. Document contracts
4. Feed API-first work

Result: Mapped call surface.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Chunk census with weights
- Map inventory
- Boundary notes
- Secret findings with severity
- Disclosure records
- Endpoint list
- Config notes
- Re-scan commands

Never exploit leaked secrets, and never publish live credentials in reports.

## Phase 1 — Census Chunks

Run `scripts/bundle_audit.py --url <page> --max-js 8` for weights, maps, and secret hits.

Rank by bytes and note vendor versus app.

Save the census with dates.

## Phase 2 — Recover Structure

Fetch published source maps only.

List modules and their sizes.

Attribute weight to owners.

## Phase 3 — Triage Secrets

Verify each hit manually; most patterns over-fire.

Severity-rate true positives.

Disclose to owners with evidence and redaction.

## Phase 4 — Map Surfaces

Extract endpoints and config keys.

Verify live before documenting.

Hand endpoint lists to API-first work.

## Examples

### Example 1: Key leak

User says: "Is our Maps key exposed?"

Actions:

1. Found key in main chunk
2. Restricted and rotated it
3. Disclosed internally with proof
4. Added build-time scan

Result: Leak closed, guard added.

### Example 2: Vendor bloat

User says: "Vendor chunk is 2MB."

Actions:

1. Attributed to three libs
2. Split and lazy-loaded two
3. Saved 1.2MB
4. Budget set

Result: Measured slim-down.

## Troubleshooting

### No source maps found

Cause: Maps withheld or external-pathed

Fix:

1. Check map headers and URLs
2. Work from chunk names
3. Ask owners for staging maps
4. Never brute-force map URLs

### Secret scanner noise

Cause: Hashes and test fixtures matching patterns

Fix:

1. Verify entropy and context
2. Test against provider validators
3. Tune patterns per repo
4. Keep human triage

### Chunks rename each deploy

Cause: Content hashing working as designed

Fix:

1. Re-census from HTML each run
2. Key analysis by module not filename
3. Automate the census step
4. Version findings by deploy

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Census.
- Secrets.
- Surface.

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

Avoid secret exploitation; live creds in reports; unpublished map hunting; weight claims without bytes; single-deploy conclusions; findings without owners.

## Bundled References

Read `references/bundle-reading.md` when attributing weight or triaging secrets.
Run `scripts/bundle_audit.py` to census chunks, maps, and secret patterns.
Copy `assets/checklists.md` into every delivery.
