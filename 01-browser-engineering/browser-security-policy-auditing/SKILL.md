---
name: browser-security-policy-auditing
description: Audit same-origin, CORS, CSP, framing, and sandbox controls and tighten them safely. Use when the user asks to explain a CORS error precisely; write or fix a content security policy; audit security headers on a site; lock down third-party embeds; verify framing and isolation controls.
compatibility: Any modern browser with DevTools; Python 3.10+ for header audits; staging environment for policy rollouts.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Browser Security Policy Auditing

Make browser security boundaries explicit and correct. You map origins, trace CORS failures to exact checks, draft CSP from real violation data, and tighten embedding controls with compatibility proof for every change.

Optimize simultaneously for:

- mapped trust boundaries
- exact CORS diagnoses
- violation-free CSP rollouts
- closed framing gaps
- proven compatibility

Do not loosen any control to fix a bug without naming the exact check, the minimal exception, and the re-tightening plan.

## Use Cases

### CORS failure

Trigger: user says 'blocked by CORS policy' or 'preflight fails'

Steps:

1. Reproduce with headers captured
2. Name the failing check: origin, method, headers, or credentials
3. Fix server response minimally
4. Verify credentialed and anon paths

Result: Exact fix instead of wildcard.

### CSP rollout

Trigger: user says 'add CSP' or 'CSP blocks our scripts'

Steps:

1. Ship report-only and collect violations
2. Draft policy from real source lists
3. Tighten nonces and hashes
4. Enforce with violation monitoring

Result: Enforced CSP with zero surprise breakage.

### Embed lockdown

Trigger: user says 'audit third-party embeds' or 'prevent clickjacking'

Steps:

1. Inventory frames and their privileges
2. Set framing and sandbox attributes per embed
3. Verify function preserved
4. Document the embedding matrix

Result: Least-privilege embeds that still work.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Origin map with trust levels per origin
- Header dumps for audited routes
- CORS traces naming the failing check
- CSP drafts with source justification per directive
- Violation report summaries
- Framing and sandbox matrix per embed
- Compatibility proof per change
- Rollback steps for each rollout

Never recommend Access-Control-Allow-Origin *, unsafe-inline, or sandbox removal without a written risk note and expiry.

## Phase 1 — Map Boundaries

List origins, subdomains, and third parties with trust levels.

Run `scripts/security_headers_audit.py --url <route>` per key route and save output.

Mark data flows that cross origins with their mechanisms.

## Phase 2 — Trace Failures

Reproduce CORS or CSP failures with full request and response headers.

Name the exact failing directive or check; quote the header and the error.

Distinguish browser enforcement from server rejection.

## Phase 3 — Draft Tight Policies

Write CSP from report-only violations, preferring nonces and hashes over allowlists.

Scope CORS origins explicitly; pair credentials only with explicit origins.

Set frame-ancestors, sandbox, COOP, and COEP as one embedding story.

## Phase 4 — Roll Out Safely

Ship report-only first, then enforce with violation alerts.

Verify critical flows: login, payments, embeds, and downloads.

Keep rollback one revert away and document it.

## Examples

### Example 1: Wildcard CORS removal

User says: "API uses CORS star with credentials attempt."

Actions:

1. Traced failure to credentialed wildcard rejection
2. Scoped origins explicitly per client
3. Verified both web and mobile callers
4. Removed wildcard with proof

Result: Working CORS without the hole.

### Example 2: CSP without breakage

User says: "CSP keeps breaking marketing tags."

Actions:

1. Collected two weeks of report-only data
2. Hashed inline needs, nonced bundles
3. Enforced during low traffic with alerts
4. Zero new violations at enforce

Result: Strict policy, quiet rollout.

## Troubleshooting

### Preflight passes but response blocked

Cause: Actual response missing ACAO or Vary mishandling

Fix:

1. Compare preflight and actual response headers
2. Add explicit origin to actual responses
3. Fix Vary: Origin on dynamic ACAO
4. Re-test credentialed and cached paths

### CSP blocks blob or data workers

Cause: worker-src or script-src missing schemes

Fix:

1. Add minimal worker-src entries
2. Prefer blob: scoped to self
3. Verify in all supported browsers
4. Monitor reports for a week

### Sandboxed frame lost needed ability

Cause: Missing allow token for scripts, forms, or same-origin

Fix:

1. Add the single missing token
2. Re-test the embed function
3. Keep allow-top-navigation off by default
4. Document the token rationale

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Policy.
- Rollout.

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

Avoid credentialed wildcard CORS; unsafe-inline as a permanent fix; report-only left unenforced forever; sandbox tokens copied blindly; framing controls tested in one browser; policy changes without rollback.

## Bundled References

Read `references/origin-controls.md` when tracing failures or drafting policies.
Run `scripts/security_headers_audit.py` to grade security headers route by route.
Copy `assets/checklists.md` into every delivery.
