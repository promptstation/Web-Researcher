---
name: js-encoding-decoding
description: Identify and decode JS encoding and cipher layers with documented keys. Use when the user asks to decode base64 blobs in JS; crack XOR-encoded strings; decode RC4 in obfuscators; identify custom encodings; peel multi-layer JS encoding.
compatibility: Any OS with Python 3.10+; blob files; no JS execution needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# JS Encoding Decoding

Turn blobs into evidence. You recognize alphabets on sight, crack XOR, implement RC4 variants, harvest keys from context, and chain layers with verification at every step.

Optimize simultaneously for:

- named schemes
- cracked keys
- decoded layers
- verified plaintext
- tested codecs

Decode for analysis and reporting; handle recovered secrets and PII as sensitive evidence.

## Use Cases

### Blob decode

Trigger: user says 'what is this blob' or 'decode this string'

Steps:

1. Identify alphabet
2. Decode with codec
3. Verify plaintext
4. Report with method

Result: Plaintext with proof.

### RC4 layer

Trigger: user says 'RC4 in this sample' or 'key nearby?'

Steps:

1. Harvest key candidates
2. Try variants
3. Verify readable output
4. Document key plus variant

Result: Decoded layer, key filed.

### Layer chain

Trigger: user says 'still encoded after decode' or 'triple wrapped'

Steps:

1. Decode layer by layer
2. Verify each step
3. Stop at readable code
4. Map the full chain

Result: Complete decode chain.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Scheme IDs with evidence
- Keys with sources
- Decode commands
- Per-layer verification
- Plaintext samples
- Codec tests
- Sensitive-data handling
- Chain diagrams

Never publish recovered secrets, and never claim decodes without readability verification.

## Phase 1 — Identify Scheme

Inspect alphabet, length mod, and padding.

Run `scripts/codec_toolkit.py --probe BLOB` for ranked guesses.

Confirm with decoder-context code.

## Phase 2 — Recover Keys

Harvest literals near decoder calls.

Try XOR brute force first.

Test RC4 variants systematically.

## Phase 3 — Decode Layers

Decode outermost first.

Verify readability per layer.

Recurse until plain code.

## Phase 4 — Verify and File

Check output parses or reads.

File keys with sources.

Add codec regression tests.

## Examples

### Example 1: Config blob

User says: "C2 config in this blob?"

Actions:

1. ID base64 plus XOR
2. Cracked key 0x42
3. Config with 3 URLs extracted
4. Blocked and reported

Result: IOCs from blob.

### Example 2: RC4 strings

User says: "Strings RC4 with nearby key."

Actions:

1. Harvested key literal
2. Decoded 120 strings
3. Verified readable
4. Key plus variant filed

Result: Strings restored.

## Troubleshooting

### XOR scores flat

Cause: Multi-byte key or non-text plaintext

Fix:

1. Try repeating-key lengths
2. Check for binary payloads
3. Look for key schedule nearby
4. Escalate to dynamic

### RC4 output garbage

Cause: Wrong variant or key encoding

Fix:

1. Try key as utf8, hex, base64
2. Test skip-first-N variants
3. Verify against known marker
4. Log attempts

### Decoded but still code-like gibberish

Cause: Another layer beneath

Fix:

1. Re-identify the inner blob
2. Chain the next decode
3. Verify per layer
4. Map full stack

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- ID.
- Keys.
- Decode.

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

Avoid unverified decodes; keys unrecorded; secrets published; single-layer assumptions; variant guessing without markers; tests skipped.

## Bundled References

Read `references/codec-shapes.md` when identifying schemes or keys.
Run `scripts/codec_toolkit.py` to probe and decode blobs.
Copy `assets/checklists.md` into every delivery.
