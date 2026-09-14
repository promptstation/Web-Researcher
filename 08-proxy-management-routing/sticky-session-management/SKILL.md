---
name: sticky-session-management
description: Keep authenticated multi-step flows coherent with pinned, leak-free sessions. Use when the user asks to pin accounts to proxies; keep checkout sessions stable; manage session affinity; persist cookies across steps; prevent session leaks.
compatibility: Provider sticky support or own affinity layer; per-account egress budget; cookie jars per flow.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Sticky Session Management

Hold journeys together. You pin accounts 1:1, freeze flows against mid-flight change, persist cookies without leaks, and expire affinity with draining — so checkouts and wizards complete coherently.

Optimize simultaneously for:

- explicit affinity
- 1:1 pins
- leak-free jars
- frozen flows
- safe expiry

Legitimate accounts and flows only; affinity serves coherence, never identity spoofing.

## Use Cases

### Authed flows

Trigger: user says 'logins drop mid-flow' or 'session lost'

Steps:

1. Pin account to egress
2. Freeze flow config
3. Persist jar
4. Verify coherence

Result: Stable authed journeys.

### Checkout safety

Trigger: user says 'cart empties' or 'checkout flakes'

Steps:

1. Freeze all mid-flow change
2. Pin plus persist
3. Verify each step
4. Alert on drift

Result: Completing checkouts.

### Leak audit

Trigger: user says 'sessions mixing' or 'wrong account data'

Steps:

1. Halt and isolate
2. Trace the leak
3. Fix scope
4. Prove separation

Result: Isolated sessions.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Affinity map
- Pin table
- Jar policy
- Flow-freeze spec
- Expiry procedure
- Leak-test evidence
- Coherence checks
- Audit trail

Never share pins across accounts or change egress, UA, or geo mid-flow.

## Phase 1 — Map Affinity

Key = account or flow ID; scope documented.

Generate maps with `scripts/affinity_manager.py`.

Review before going live.

## Phase 2 — Pin 1:1

One egress per account; no sharing.

Freeze UA, geo, cookies for the flow.

Verify pin on every step.

## Phase 3 — Persist Safely

Jar per flow; encrypt at rest.

Never log jar contents.

Refresh before expiry.

## Phase 4 — Expire Clean

Drain in-flight before release.

Re-auth path tested.

Audit trail complete.

## Examples

### Example 1: Checkout fixed

User says: "Checkout fails halfway."

Actions:

1. Pinned plus froze flow
2. Completion 40 to 98 percent
3. Drift alerts live
4. Stable months

Result: Coherent checkout.

### Example 2: Leak contained

User says: "Account B saw A data."

Actions:

1. Halted, isolated, traced
2. Shared jar found and split
3. Separation proven
4. Test added

Result: Trusted isolation.

## Troubleshooting

### Pin drifts mid-flow

Cause: TTL expiry or pool rebalance

Fix:

1. Extend TTL past flow
2. Exclude pinned from rebalance
3. Freeze harder
4. Alert on drift

### Jar bloats

Cause: Unbounded cookie growth

Fix:

1. Prune per policy
2. Cap jar size
3. Refresh routinely
4. Monitor bytes

### Re-auth loops

Cause: Expired tokens plus tight pins

Fix:

1. Refresh proactively
2. Re-auth path first-class
3. Loosen pin on auth only
4. Verify flow

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Run.
- End.

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

Avoid shared pins; mid-flow changes; jar mixing; TTL-free affinity; unaudited maps; spoof-framed pinning.

## Bundled References

Read `references/affinity-design.md` when pinning sessions or freezing flows.
Run `scripts/affinity_manager.py` to generate and audit affinity maps.
Copy `assets/checklists.md` into every delivery.
