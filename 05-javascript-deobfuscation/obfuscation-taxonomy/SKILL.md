---
name: obfuscation-taxonomy
description: Classify obfuscated JavaScript from fingerprints and route each class correctly. Use when the user asks to identify what obfuscator was used; classify packed JavaScript; triage suspicious scripts; estimate deobfuscation effort; separate minified from obfuscated.
compatibility: Any OS with Python 3.10+; sample files only; never execute untrusted code on host.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Obfuscation Taxonomy

Name the obscurity before fighting it. You fingerprint families, score signals, estimate effort honestly, and route each sample to the cheapest technique that actually works.

Optimize simultaneously for:

- correct classes
- cited fingerprints
- honest estimates
- right routes
- archived corpus

Classify from static evidence first; never execute suspicious samples outside sandboxes.

## Use Cases

### Suspicious tag

Trigger: user says 'what is this script' or 'packed third party'

Steps:

1. Fingerprint statically
2. Score signals
3. Classify with evidence
4. Route to technique

Result: Named class, correct path.

### Queue triage

Trigger: user says 'fifty samples' or 'prioritize analysis'

Steps:

1. Batch-classify all
2. Estimate effort each
3. Order by risk times effort
4. Assign with routes

Result: Ordered, routed queue.

### Family tracking

Trigger: user says 'same actor?' or 'campaign link'

Steps:

1. Compare fingerprints
2. Cluster by boilerplate
3. Link with shared markers
4. Report clusters

Result: Evidence-linked clusters.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Class per sample with evidence
- Fingerprint quotes
- Signal scores
- Effort estimates
- Routing decisions
- Archive with hashes
- Corpus notes
- Review dates

Never execute untrusted samples on analyst hosts, and never skip hashing and archiving.

## Phase 1 — Fingerprint Static

Run `scripts/obfuscation_classifier.py --file sample.js` and save scores.

Quote boilerplate and structural markers.

Hash and archive the original.

## Phase 2 — Score Signals

Record entropy, identifier randomness, string density.

Compare against baseline corpus.

Grade confidence per signal.

## Phase 3 — Classify and Estimate

Assign class with cited evidence.

Estimate effort in hours honestly.

Note alternative hypotheses.

## Phase 4 — Route Work

Map class to technique: beautify, decode, AST, sandbox.

Order queues by risk over effort.

File routing with reasons.

## Examples

### Example 1: Packed redirector

User says: "Suspicious redirect script."

Actions:

1. Fingerprinted packer boilerplate
2. Classified packed-plus-encoded
3. Routed to unpack then decode
4. Resolved in an hour

Result: Fast correct route.

### Example 2: Vendor bundle

User says: "Is our vendor bundle obfuscated?"

Actions:

1. Scored as minified only
2. No obfuscator markers
3. Cleared with evidence
4. Baseline saved

Result: Cleared, not chased.

## Troubleshooting

### No fingerprint matches

Cause: Custom packer or layered tools

Fix:

1. Score signals manually
2. Peel one layer at a time
3. Catalog new markers
4. Estimate conservatively

### Minified flagged obfuscated

Cause: Aggressive mangling resembles obfuscation

Fix:

1. Check for string arrays and traps
2. Beautify to confirm readability
3. Downgrade to minified
4. Tune thresholds

### Layered samples

Cause: Pack then obfuscate then encode

Fix:

1. Peel outside-in
2. Re-classify per layer
3. Track layer stack
4. Budget per layer

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Print.
- Score.
- Route.

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

Avoid execution before classification; host detonation; unhashed samples; single-signal verdicts; effort underestimated; families guessed not fingerprinted.

## Bundled References

Read `references/obfuscation-families.md` when fingerprinting or routing samples.
Run `scripts/obfuscation_classifier.py` to fingerprint and score samples statically.
Copy `assets/checklists.md` into every delivery.
