---
name: access-law-literacy
description: Touch only authorized systems — with written, expiring, provable scope. Use when the user asks to CFAA and web scraping; prove authorization to access; exceeds authorized access meaning; scope penetration tests; document access permission.
compatibility: Counsel for interpretations; access inventory; evidence store.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Access Law Literacy

Never touch a system on vibes. You learn access law's shape, scope every permission in writing, expire and re-verify on schedule, test gates honestly, and pack evidence that proves authorization on demand.

Optimize simultaneously for:

- literate teams
- written scopes
- fresh access
- tested gates
- packed proof

Authorization in writing before access; gray areas get counsel, not creativity. Not legal advice.

## Use Cases

### New target

Trigger: user says 'can we scrape X' or 'access this API'

Steps:

1. Check authorization
2. Scope writing
3. Counsel gray
4. Access logged

Result: Permitted access.

### Pentest scope

Trigger: user says 'test our app' or 'rules of engagement'

Steps:

1. Write ROE
2. Sign both sides
3. Test inside
4. Report + attest

Result: Scoped test.

### Proof demand

Trigger: user says 'prove permission' or 'access challenged'

Steps:

1. Pull pack
2. Show scope+time
3. Confirm logs
4. File response

Result: Defended access.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Law brief
- Scope docs
- Evidence packs
- Expiry table
- Gate tests
- Counsel memos
- Training log
- Audit trail

Never access on implied permission or stretch scope without re-authorization.

## Phase 1 — Learn Shape

Access without authorization; gates-not-purposes.

Regime variants per country.

Brief with `scripts/authz_checklist.py --brief`.

## Phase 2 — Scope Writing

System, actions, data, time, purpose.

Signed by granter; filed.

Machine-readable where possible.

## Phase 3 — Expire and Verify

Expiry per scope; re-verify to renew.

Revoked on role change.

Access reviews quarterly.

## Phase 4 — Prove on Demand

Pack: scope + logs + time.

Challenge response in days.

Audit trail immutable.

## Examples

### Example 1: API cleared

User says: "Use partner API for research?"

Actions:

1. Scope written + signed
2. Logged access
3. Expired on term
4. Proof filed

Result: Clean Records.

### Example 2: Challenge won

User says: "Access questioned by vendor."

Actions:

1. Pack produced day 1
2. Logs matched scope
3. Upheld
4. Process kept

Result: Defended work.

## Troubleshooting

### Implied permission

Cause: 'Public' confused with authorized

Fix:

1. Get writing
2. Counsel gray
3. Log decision
4. Never assume

### Scope drift

Cause: Helpful extras

Fix:

1. Stop + re-scope
2. Document
3. Re-authorize
4. Train team

### Stale access

Cause: No expiry

Fix:

1. Expire all
2. Re-verify
3. Schedule reviews
4. Automate

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Know.
- Hold.
- Show.

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

Avoid vibes-based access; verbal permission; expiry-free grants; scope-stretching; counsel-free gray; proof-free touching.

## Bundled References

Read `references/access-authorization.md` when scoping or proving access.
Run `scripts/authz_checklist.py` to brief teams and check grants.
Copy `assets/checklists.md` into every delivery.
