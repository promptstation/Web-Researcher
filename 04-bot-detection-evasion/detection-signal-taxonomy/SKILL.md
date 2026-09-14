---
name: detection-signal-taxonomy
description: Inventory what your clients emit and keep legitimate automation transparent. Use when the user asks to list bot detection signals; audit my crawler headers; explain bot scores; document automation for allowlisting; check client consistency.
compatibility: Any OS with Python 3.10+; your own clients and test endpoints; no target probing needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Detection Signal Taxonomy

Know exactly what you emit. You inventory signals per layer, audit your clients honestly, keep identity consistent, and document automation so operators can say yes with confidence.

Optimize simultaneously for:

- complete signal lists
- audited emissions
- consistent identity
- transparent docs
- allowlist-ready packs

Transparency only: identify honestly, document purpose, request access; never imitate other clients to mislead scoring.

## Use Cases

### Crawler identity

Trigger: user says 'identify our crawler' or 'allowlist request'

Steps:

1. Audit emissions fully
2. Write transparency doc
3. Add contact and purpose
4. Submit allowlist pack

Result: Professional access request.

### False-positive review

Trigger: user says 'legit users flagged' or 'our app blocked'

Steps:

1. Inventory app emissions
2. Find inconsistent or missing identity
3. Fix honestly at source
4. Re-verify with operator

Result: Restored access, clean identity.

### Fleet consistency

Trigger: user says 'workers differ' or 'one pool flagged'

Steps:

1. Diff emissions per pool
2. Align versions and configs
3. Document the standard
4. Monitor drift

Result: Uniform honest fleet.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Signal list per layer
- Emission audit per client
- Consistency verdict
- Transparency doc
- Allowlist pack
- Change log
- Contact and purpose headers
- Review date

Never imitate browser or user signals to mislead scoring, and never omit identity to dodge classification.

## Phase 1 — List Signals

Enumerate network, TLS, HTTP, browser, and behavior signals from docs.

Mark which your clients emit and which they never should.

Date the list; signals evolve.

## Phase 2 — Audit Emissions

Run `scripts/request_anatomy.py --url <echo>` to record exactly what you send.

Diff across clients and pools.

Flag inconsistencies and missing identity.

## Phase 3 — Align Honestly

Set truthful user agents with contact URLs.

Standardize versions fleet-wide.

Fix inconsistencies at config source.

## Phase 4 — Document Access

Write purpose, scope, rate, and retention.

Package allowlist requests professionally.

Track responses and renewals.

## Examples

### Example 1: Research crawler

User says: "Crawl 10k pages for research."

Actions:

1. Audited emissions, added contact UA
2. Published purpose page
3. Requested access per domain
4. 80 percent allowlisted

Result: Welcomed, not blocked.

### Example 2: App flagged

User says: "Our mobile API calls flagged."

Actions:

1. Found missing app identity headers
2. Added documented client ID
3. Operator allowlisted
4. Flags stopped

Result: Clean identity, access restored.

## Troubleshooting

### Allowlist denied

Cause: Vague purpose or missing contact

Fix:

1. Sharpen purpose and scope
2. Add abuse contact
3. Offer rate caps
4. Re-apply professionally

### One pool flagged, others fine

Cause: Config drift in that pool

Fix:

1. Diff emissions to find drift
2. Realign to standard
3. Re-verify clean
4. Add drift alerts

### Identity ignored by defense

Cause: Reputation or behavior dominates

Fix:

1. Slow rates further
2. Narrow scope
3. Ask operator for terms
4. Accept no when given

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- List.
- Audit.
- Access.

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

Avoid browser imitation; identity omission; header-order mimicry; vague purpose statements; unlogged emission drift; allowlist as entitlement.

## Bundled References

Read `references/signal-layers.md` when listing signals or auditing clients.
Run `scripts/request_anatomy.py` to record exactly what your client sends.
Copy `assets/checklists.md` into every delivery.
