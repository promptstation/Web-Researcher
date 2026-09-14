---
name: session-state-management
description: Run login-once automation with isolated, refreshed, secret-safe sessions. Use when the user asks to reuse logins in Playwright; manage storageState files; isolate test accounts; refresh auth tokens; keep secrets out of traces.
compatibility: Playwright or Puppeteer; secret manager for credentials; legitimate accounts you own or may use.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Session State Management

Authenticate once, reuse safely. You capture minimal state, isolate every account, refresh before expiry, handle MFA lawfully, and audit relentlessly so secrets never escape.

Optimize simultaneously for:

- login-once flows
- isolated accounts
- fresh tokens
- lawful MFA
- leak-free artifacts

Legitimate credentials and permission only; MFA never bypassed; secrets never in repos, logs, or traces.

## Use Cases

### Authed suite

Trigger: user says 'login every test is slow' or 'share sessions'

Steps:

1. Build login-once setup
2. Snapshot per role
3. Reuse across tests
4. Refresh on schedule

Result: Fast authed suite.

### Multi-account

Trigger: user says 'three roles' or 'tenant isolation'

Steps:

1. One state file per account
2. Isolated contexts
3. No cross-use
4. Audit separation

Result: Clean role coverage.

### Secret hygiene

Trigger: user says 'tokens in traces' or 'audit artifacts'

Steps:

1. Scan states and traces
2. Redact and rotate
3. Fix capture config
4. Verify clean

Result: Leak-free pipeline.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Login-once design doc
- State files per account
- Refresh schedule
- MFA policy
- Secret audit report
- Rotation runbook
- Access review log
- Artifact retention

Never commit state files or credentials, and never bypass MFA or share sessions across accounts.

## Phase 1 — Capture Once

Log in via UI once per role with vaulted credentials.

Snapshot minimal storage state per account.

Run `scripts/storage_state_audit.py --file state.json` and confirm no over-collection.

## Phase 2 — Isolate Accounts

One state file and context per account.

Separate cookies, origins, and egress.

Verify no cross-account leakage.

## Phase 3 — Refresh Proactively

Schedule refresh at 80 percent token life.

Re-login on 401 once, then park.

Alert on repeated auth failures.

## Phase 4 — Audit Secrets

Scan states, traces, videos, screenshots.

Redact, rotate, and fix capture.

Review access quarterly.

## Examples

### Example 1: Role matrix

User says: "Admin, editor, viewer suites."

Actions:

1. Three state files, isolated
2. Refresh nightly
3. Suites 5x faster
4. Zero leaks in audit

Result: Fast safe authed suites.

### Example 2: Leak cleanup

User says: "Tokens found in traces."

Actions:

1. Rotated immediately
2. Disabled sensitive capture
3. Purged artifacts
4. Guard added to CI

Result: Clean pipeline, guard live.

## Troubleshooting

### State expires mid-suite

Cause: Short tokens, long suites

Fix:

1. Shorten suites or refresh mid-run
2. Checkpoint progress
3. Re-auth and resume
4. Size runs under token life

### Accounts cross-contaminate

Cause: Shared context or state file

Fix:

1. Split states immediately
2. Isolate contexts
3. Verify with identity checks
4. Add separation test

### MFA blocks automation

Cause: Policy requires human verification

Fix:

1. Use human-in-the-loop setup
2. Persist lawful session
3. Never automate the factor
4. Document the flow

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Capture.
- Run.
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

Avoid login per test; shared state files; committed credentials; MFA bypass attempts; secrets in artifacts; unreviewed account access.

## Bundled References

Read `references/session-ops.md` when designing or auditing session reuse.
Run `scripts/storage_state_audit.py` to audit storage-state files without leaking values.
Copy `assets/checklists.md` into every delivery.
