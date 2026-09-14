---
name: browser-storage-forensics
description: Audit cookies and browser storage for flags, quotas, lifetimes, and secret leakage. Use when the user asks to audit cookie Secure and SameSite flags; inspect localStorage and IndexedDB usage; fix sessions lost on storage clear; migrate IndexedDB schemas safely; find tokens stored in the wrong place.
compatibility: Any modern browser with DevTools Application panel; Python 3.10+ for header-side cookie audits; no extensions needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Browser Storage Forensics

Make stored state legible and safe. You inventory every tier, verify flags and lifetimes, measure quota pressure, and migrate or clear state without breaking sessions or stranding secrets.

Optimize simultaneously for:

- complete storage inventory
- correct cookie flags
- measured quota headroom
- lossless migrations
- secret-free tiers

Do not change flags, expiries, or clearing logic without a per-cookie and per-store inventory showing current behavior.

## Use Cases

### Login hardening

Trigger: user says 'harden session cookies' or 'cookie audit for review'

Steps:

1. Dump Set-Cookie headers across the login flow
2. Check Secure, HttpOnly, SameSite, Path, and Max-Age per cookie
3. Fix flags and shrink lifetimes
4. Re-run the audit and prove the session still works

Result: Minimal, correctly flagged session surface.

### Quota pressure

Trigger: user says 'offline cache fills up' or 'storage quota errors'

Steps:

1. Census usage per origin and store
2. Rank caches by size and staleness
3. Add eviction and versioning
4. Verify headroom under repeat runs

Result: Bounded storage with eviction rules.

### Automation state reuse

Trigger: user says 'persist logins for scraping' or 'export session state'

Steps:

1. Separate session cookies from cache and prefs
2. Export minimal state with secrets redacted in logs
3. Restore into isolated contexts per account
4. Verify expiry and refresh behavior

Result: Portable sessions without secret sprawl.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Cookie table: name, flags, scope, expiry, purpose
- Storage census: usage and quota per origin and store
- Lifetime map: what survives restart, clear, and partition
- Migration plan: versions, backfill, and rollback
- Clear procedure: selective steps that preserve sessions
- Secret sweep: tokens and PII absent from wrong tiers
- Partition verdict: embedded flows tested partitioned
- Evidence: header dumps and panel exports attached

Never alter storage behavior without inventories, and never log raw session values.

## Phase 1 — Inventory Tiers

Dump cookies, localStorage keys, sessionStorage keys, IndexedDB stores, and Cache Storage keys for the origin.

Run `scripts/cookie_audit.py --url <login-or-home>` to capture Set-Cookie flags header-side.

Record usage and quota via `navigator.storage.estimate()` in console.

## Phase 2 — Audit Flags and Lifetimes

Mark every cookie: Secure required on HTTPS, HttpOnly for session, SameSite=Lax default or Strict where safe, minimal Max-Age.

Classify each stored item by tier fitness: session, preference, cache, or offline data.

List violations with exact header or key plus recommended value.

## Phase 3 — Migrate or Clear

Version IndexedDB changes and test upgrade plus downgrade paths on fixture data.

Write selective clear steps: caches first, then prefs, session last and only with re-login plan.

Verify the app works after each clear tier before proceeding.

## Phase 4 — Verify Partition and Secrets

Test embedded flows with third-party cookies blocked and partitioned storage on.

Grep exports for tokens, emails, and keys; move secrets to HttpOnly cookies or memory.

Re-run inventory and confirm deltas match the plan.

## Examples

### Example 1: Session cookie fix

User says: "Session cookie missing flags, flagged in review."

Actions:

1. Dumped headers: no Secure, SameSite=None without need
2. Set Secure, HttpOnly, SameSite=Lax, 12h Max-Age
3. Re-ran login plus refresh flows green
4. Attached before/after header diff

Result: Review cleared with evidence.

### Example 2: Scraper session export

User says: "Reuse logins across scrape workers."

Actions:

1. Separated session cookies from cache blobs
2. Exported minimal state per account with redacted logs
3. Restored into isolated contexts, sticky egress
4. Verified refresh before expiry

Result: Stable authed scraping without leaks.

## Troubleshooting

### Users logged out after deploy

Cause: Clear-all on version change or cookie scope narrowed

Fix:

1. Scope clears to caches, not session cookies
2. Version migrations with backfill instead of wipe
3. Test upgrade on real profiles
4. Add session-preservation check to release

### Embedded widget broke recently

Cause: Third-party storage now partitioned or blocked

Fix:

1. Reproduce with third-party cookies blocked
2. Move widget state first-party or request access properly
3. Redesign cross-site joins around partitioning
4. Document the supported embed matrix

### QuotaExceededError on repeat visits

Cause: Unbounded cache keys without eviction

Fix:

1. Version cache names and delete old versions
2. Cap entries with LRU eviction
3. Shrink stored payloads
4. Monitor usage versus quota in telemetry

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Cookies.
- Storage.
- Safety.

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

Avoid secrets in localStorage; session cookies without HttpOnly; SameSite=None without Secure and need; wipe-all clears as routine hygiene; unversioned IndexedDB changes; raw session values in logs or screenshots.

## Bundled References

Read `references/storage-tiers.md` when choosing tiers or clearing state.
Run `scripts/cookie_audit.py` to audit Set-Cookie flags header-side.
Copy `assets/checklists.md` into every delivery.
