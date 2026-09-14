---
name: proxy-credential-ops
description: Vault proxy secrets and rotate credentials with zero downtime. Use when the user asks to store proxy passwords safely; rotate proxy credentials; set up IP allowlisting; audit secrets in repos; inject secrets at runtime.
compatibility: Secret manager (Vault, AWS SM, Doppler, or env files); provider rotation support; CI scanning.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Proxy Credential Ops

Keep egress secrets secret. You allowlist tightly, vault everything, rotate with dual validity and zero downtime, inject at runtime only, and scan plus drill so leaks stay theoretical.

Optimize simultaneously for:

- tight allowlists
- vaulted secrets
- clean rotations
- runtime-only injection
- zero leaks

No credential in code, image, log, or ticket; rotation tested before it is needed.

## Use Cases

### First vaulting

Trigger: user says 'passwords in config' or 'secure this'

Steps:

1. Inventory secrets
2. Move to vault
3. Inject at runtime
4. Verify clean

Result: Vaulted egress auth.

### Planned rotation

Trigger: user says 'rotate quarterly' or 'provider asks'

Steps:

1. Issue new creds
2. Dual-run window
3. Cut over workers
4. Revoke old

Result: Invisible rotation.

### Leak response

Trigger: user says 'key exposed' or 'repo leaked'

Steps:

1. Revoke immediately
2. Rotate everywhere
3. Purge history
4. Postmortem

Result: Contained exposure.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Secret inventory
- Vault design
- Allowlist table
- Rotation runbook
- Injection proof
- Scan reports
- Drill log
- Access reviews

Never commit, log, or paste credentials; never rotate without dual validity.

## Phase 1 — Inventory and Vault

List every proxy secret and its scope.

Move to vault with least privilege.

Delete from code, images, tickets.

## Phase 2 — Prefer Allowlists

Allowlist static egress IPs.

Scope to /32s; review quarterly.

Credentials only where allowlists cannot reach.

## Phase 3 — Rotate Cleanly

Use `scripts/rotation_checklist.py --step plan` to walk rotations.

Dual-validity 24-48h; cut over; revoke.

Verify zero auth failures.

## Phase 4 — Scan and Drill

Scan repos and images in CI.

Drill emergency rotation yearly.

Review access quarterly.

## Examples

### Example 1: Zero-downtime

User says: "Rotate 40 workers live."

Actions:

1. Dual window 48h
2. Rolling cutover
3. Zero failures
4. Old revoked

Result: Invisible rotation.

### Example 2: Leak contained

User says: "Key in public repo 2 hours."

Actions:

1. Revoked in 10 min
2. Rotated all
3. History purged
4. Scanning added

Result: Contained fast.

## Troubleshooting

### Auth failures after rotation

Cause: Stale worker or missed scope

Fix:

1. Find stragglers via logs
2. Widen window next time
3. Inventory scopes
4. Verify 100 percent

### Allowlist too broad

Cause: Ranges instead of hosts

Fix:

1. Narrow to /32s
2. Remove stale
3. Automate updates
4. Review quarterly

### Secrets in artifacts

Cause: Debug logs or traces capture

Fix:

1. Scrub at emission
2. Purge artifacts
3. Rotate exposed
4. Test scrubbing

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Vault.
- Rotate.
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

Avoid plaintext credentials; committed secrets; rotation-free years; single-validity cutovers; scan-free repos; review-free access.

## Bundled References

Read `references/secret-ops.md` when vaulting, rotating, or auditing secrets.
Run `scripts/rotation_checklist.py` to walk credential rotations.
Copy `assets/checklists.md` into every delivery.
