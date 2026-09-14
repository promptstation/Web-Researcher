---
name: tls-fingerprint-analysis
description: Audit TLS client profiles and interpret handshake behavior for research and defense. Use when the user asks to explain what JA3 fingerprints; audit my TLS client profile; interpret TLS handshake failures; compare client cipher suites; check research profile coherence.
compatibility: Any OS with Python 3.10+ and OpenSSL; no packet capture or privileged access required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# TLS Fingerprint Analysis

Make TLS identity legible for research and defense. You inventory handshake inputs, audit local profiles, interpret server decisions from alerts and fallbacks, and keep every recommendation inside documented, defensive scope.

Optimize simultaneously for:

- inventoried handshake inputs
- audited client profiles
- interpreted server decisions
- coherent research setups
- documented scope

Measurement and defense only. Do not build or advise handshake mimicry to evade access controls or fraud defenses.

## Use Cases

### Handshake failure

Trigger: user says 'TLS handshake fails' or 'alert unknown'

Steps:

1. Capture client offer and server alert
2. Name the rejected input or policy
3. Fix version, cipher, or SNI at the source
4. Verify with a clean handshake

Result: Named cause, clean retry.

### Profile audit

Trigger: user says 'audit our scraper TLS' or 'compare client profiles'

Steps:

1. Dump local ciphers, versions, and ALPN
2. Compare against intended platform profile
3. Flag incoherent mixes
4. Align library and config to spec

Result: Coherent documented profile.

### Server behavior study

Trigger: user says 'why does this server downgrade us'

Steps:

1. Vary one input at a time
2. Record version and cipher responses
3. Infer policy vs fingerprint logic
4. Report with handshake transcripts

Result: Evidence-backed interpretation.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- ClientHello input inventory
- Local profile dump with library versions
- Handshake transcripts for claims
- Alert interpretation per failure
- Coherence table vs intended platform
- Fix at config or library source
- Scope note with limits
- Re-audit commands

Never advise handshake spoofing against defenses, and never claim fingerprint conclusions from single handshakes.

## Phase 1 — Inventory Inputs

List versions, cipher suites, extensions, curves, point formats, and ALPN for the client.

Run `scripts/tls_client_profile.py` and save the JSON as the profile baseline.

Record library name and version alongside every dump.

## Phase 2 — Capture Behavior

Handshake against staging or owned endpoints first.

Record negotiated version, cipher, ALPN, and any alerts across runs.

Vary one input at a time when studying server logic.

## Phase 3 — Interpret Outcomes

Map alerts to causes: version, cipher, SNI, cert, or policy.

Distinguish fingerprint-shaped rejections from capacity or config faults.

State confidence and alternative explanations plainly.

## Phase 4 — Align and Document

Align libraries and configs to the intended platform spec.

Re-dump and diff the profile after changes.

File the scope note with purpose and limits.

## Examples

### Example 1: Mystery alert

User says: "Handshake fails with illegal parameter."

Actions:

1. Dump showed legacy curve offered first
2. Server policy rejected the group
3. Updated library and curve order
4. Clean handshake, alert gone

Result: Fixed at the true input.

### Example 2: Fleet drift

User says: "Workers behave differently per host."

Actions:

1. Profiles showed mixed OpenSSL versions
2. Pinned versions and re-dumped
3. Behavior converged across fleet
4. Version pin added to images

Result: Coherent fleet profile.

## Troubleshooting

### Profile changes after upgrade

Cause: Library defaults moved ciphers or extensions

Fix:

1. Diff pre and post dumps
2. Pin or explicitly configure suites
3. Re-verify against staging
4. Record the new baseline

### Server picks weak cipher

Cause: Client offers weak first or server honors client order

Fix:

1. Reorder client preferences
2. Drop weak suites explicitly
3. Confirm negotiation improves
4. Document the suite policy

### SNI-related failures

Cause: Missing or mismatched server name indication

Fix:

1. Confirm SNI sent matches host
2. Check proxy SNI passthrough
3. Fix client or egress config
4. Re-handshake clean

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Inventory.
- Behavior.
- Align.

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

Avoid handshake mimicry advice; single-handshake conclusions; version upgrades without re-baselining; mixed-signal research profiles; alert guessing without transcripts; fingerprint work without scope notes.

## Bundled References

Read `references/clienthello-fields.md` when auditing profiles or interpreting handshakes.
Run `scripts/tls_client_profile.py` to dump the local TLS client profile.
Copy `assets/checklists.md` into every delivery.
