---
name: angular-spa-analysis
description: Map Angular routes and APIs and extract with permissioned enterprise sessions. Use when the user asks to scrape an Angular app lawfully; map lazy routes in Angular; find API base URLs in bundles; handle SSO for automation; audit enterprise SPA extraction.
compatibility: Any OS with Python 3.10+ and HTTPS; legitimate credentials and written permission for gated targets.
metadata:
  author: Promptstation
  version: 1.0.0
  category: web-frameworks
---

# Angular SPA Analysis

Navigate enterprise SPAs correctly and lawfully. You fingerprint builds, reconstruct routes, discover APIs from evidence, and operate only with permissioned sessions, least scope, and audit trails.

Optimize simultaneously for:

- fingerprinted builds
- reconstructed routes
- evidenced APIs
- permissioned sessions
- auditable runs

Gated enterprise data requires written permission and legitimate credentials; never bypass SSO, MFA, or access controls.

## Use Cases

### Portal extraction

Trigger: user says 'extract from our vendor portal' or 'Angular dashboard data'

Steps:

1. Confirm permission and scope
2. Map routes and APIs
3. Authenticate legitimately
4. Extract with audit

Result: Compliant dataset with trail.

### Route inventory

Trigger: user says 'map this Angular app' or 'find hidden routes'

Steps:

1. Fingerprint the build
2. Read chunk manifests
3. Reconstruct route table
4. Verify each route

Result: Complete route map.

### API discovery

Trigger: user says 'find the backend API' or 'skip the UI'

Steps:

1. Extract base URLs from bundles
2. Confirm with network evidence
3. Document contracts
4. Use API-first with auth

Result: Direct API access, same permission.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Permission record with scope
- Build fingerprint
- Route table with evidence
- API inventory
- Auth map
- Session handling notes
- Audit log of runs
- Data minimization statement

Never bypass access controls, and never extract gated data without written permission on file.

## Phase 1 — Confirm Permission

Record who authorized access, which data, and until when.

Use legitimate credentials; store in a secret manager.

Scope sessions to least privilege.

## Phase 2 — Fingerprint and Map

Run `scripts/angular_probe.py --url <app>` for version, chunks, and API hints.

Reconstruct routes from manifests and router code.

Verify routes by fetching with the session.

## Phase 3 — Discover APIs

Extract base URLs from bundles with context lines.

Confirm endpoints with authed requests.

Document request shapes and pagination.

## Phase 4 — Extract with Audit

Pull minimal fields at polite rates.

Log every run: time, scope, counts.

Package the audit trail with data.

## Examples

### Example 1: Vendor reports

User says: "Monthly data from a vendor portal."

Actions:

1. Permission filed, SSO login
2. Mapped reports API
3. Monthly pull with audit
4. Stable for a year

Result: Compliant recurring feed.

### Example 2: Hidden routes

User says: "App has more sections than nav shows."

Actions:

1. Manifest revealed 6 more routes
2. Two in scope, four excluded
3. Extracted the two with logs
4. Map filed with scope notes

Result: Scoped complete coverage.

## Troubleshooting

### Session expires mid-run

Cause: Short tokens without refresh

Fix:

1. Implement refresh before expiry
2. Checkpoint progress
3. Resume after re-auth
4. Size runs under token life

### API returns generic 403

Cause: Missing role, header, or origin check

Fix:

1. Diff browser vs script requests
2. Add required headers legitimately
3. Confirm role grants
4. Never forge entitlements

### Routes 404 after upgrade

Cause: Router refactor or base-href change

Fix:

1. Re-fingerprint the build
2. Rebuild route table
3. Update base paths
4. Re-verify scope

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Permission.
- Map.
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

Avoid gated extraction without permission; SSO or MFA bypass attempts; role forging; unscoped sessions; audit-free runs; tenant bases guessed.

## Bundled References

Read `references/angular-maps.md` when fingerprinting builds or reconstructing routes.
Run `scripts/angular_probe.py` to fingerprint Angular builds and surface API hints.
Copy `assets/checklists.md` into every delivery.
