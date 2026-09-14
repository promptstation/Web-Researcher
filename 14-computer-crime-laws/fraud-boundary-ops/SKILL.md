---
name: fraud-boundary-ops
description: Operate accounts with real identities, 1:1 discipline, zero sharing. Use when the user asks to fake accounts policy; credential sharing rules; identity theft boundaries; audit account usage; respond to compromised accounts.
compatibility: Identity proofing per platform; vault; account inventory.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Fraud Boundary Ops

Keep every account legitimate. You brief fraud lines plainly, use real authorized identities, map accounts 1:1 to purposes, vault every credential, ban sharing absolutely, and drill compromise response.

Optimize simultaneously for:

- briefed teams
- real identities
- mapped accounts
- vaulted creds
- drilled response

No fake identities, no borrowed credentials, no account sharing — ever. Not legal advice.

## Use Cases

### Account fleet

Trigger: user says 'need accounts' or 'manage logins'

Steps:

1. Real identities
2. 1:1 map
3. Vault + rotate
4. Audit quarterly

Result: Clean fleet.

### Sharing find

Trigger: user says 'shared login?' or 'audit finds sharing'

Steps:

1. Stop + split
2. Rotate all
3. Discipline + train
4. Verify zero

Result: Sharing ended.

### Compromise

Trigger: user says 'account hacked' or 'creds leaked'

Steps:

1. Revoke + rotate
2. Scope impact
3. Notify + file
4. Harden

Result: Contained breach.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Line brief
- Account inventory
- 1:1 map
- Vault report
- Sharing attestations
- Rotation log
- Compromise playbook
- Audit reports

Never create fake identities or share credentials for any reason.

## Phase 1 — Brief Lines

Fraud, identity theft, credential misuse shapes.

Platform + criminal consequences.

Sign acknowledgments.

## Phase 2 — Map 1:1

Account -> human + purpose + scope.

Audit with `scripts/account_integrity.py --map accounts.json`.

Fix sharing instantly.

## Phase 3 — Vault All

Every credential vaulted; unique; rotated.

MFA where offered; no SMS-only for critical.

Access logged.

## Phase 4 — Drill Compromise

Revoke/rotate/scope/notify playbook.

Yearly drill.

Vendor accounts included.

## Examples

### Example 1: Fleet cleaned

User says: "Logins shared across team?"

Actions:

1. Split to named
2. Rotated all
3. Zero sharing attested
4. Quarterly audits

Result: Accountable access.

### Example 2: Leak contained

User says: "Creds in chat logs."

Actions:

1. Revoked in 15 min
2. Scoped: no misuse
3. Purged + trained
4. Monitor kept

Result: Fast containment.

## Troubleshooting

### Fake-account ask

Cause: 'Just for testing'

Fix:

1. Refuse in writing
2. Offer test accounts
3. Document
4. Protect asker too

### Vendor shares

Cause: One login for team

Fix:

1. Demand named seats
2. Contract terms
3. Migrate or exit
4. Log risk

### Rotation gaps

Cause: Forgotten services

Fix:

1. Inventory sweep
2. Vault all
3. Rotate
4. Monitor

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Prove.
- Hold.
- Check.

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

Avoid fake test accounts; shared logins; vault-free creds; rotation-free years; attest-free fleets; drill-free teams.

## Bundled References

Read `references/account-integrity.md` when managing operational accounts.
Run `scripts/account_integrity.py` to audit account maps.
Copy `assets/checklists.md` into every delivery.
