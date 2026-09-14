---
name: string-array-decoding
description: Emulate string-array rotation and restore readable literals safely. Use when the user asks to decode obfuscator string arrays; emulate array rotation; resolve _0x decoder calls; restore hidden string literals; unwrap rotated string tables.
compatibility: Any OS with Python 3.10+; sample files; no JS execution required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# String Array Decoding

Return hidden strings to daylight. You extract arrays, emulate rotation arithmetically, resolve decoder calls with context, decode nested layers, and verify every restoration by sampling.

Optimize simultaneously for:

- extracted arrays
- emulated rotation
- resolved calls
- decoded layers
- verified literals

Emulate, never execute; verify literals in context before trusting restored code.

## Use Cases

### Array unpack

Trigger: user says 'all strings hidden' or '_0x everywhere'

Steps:

1. Extract array plus decoder
2. Emulate rotation
3. Resolve call sites
4. Verify samples

Result: Readable literals restored.

### Nested entries

Trigger: user says 'decoded strings still encoded' or 'base64 inside'

Steps:

1. Detect entry encoding
2. Decode per entry
3. Re-resolve calls
4. Verify readable

Result: Fully plain strings.

### Batch decode

Trigger: user says 'twenty files, same obfuscator' or 'campaign set'

Steps:

1. Template the decoder shape
2. Batch-resolve all
3. Sample-verify each
4. Report coverage

Result: Decoded corpus with proof.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Array dump with indices
- Rotation math notes
- Decoder mapping
- Rewrite rules
- Before/after samples
- Verification counts
- Unresolved list with reasons
- Re-run commands

Never execute decoder IIFEs from untrusted samples, and never trust unrestored-context literals.

## Phase 1 — Extract Array

Run `scripts/string_array_decoder.py --file sample.js --dump` to list entries.

Identify rotation loop and shift count pattern.

Save the raw array with hashes.

## Phase 2 — Emulate Rotation

Reimplement rotation arithmetic in the script, not by running the IIFE.

Verify first and last entries against known markers.

Lock the rotated table.

## Phase 3 — Resolve Calls

Map decoder aliases and wrappers.

Rewrite call sites to literals with originals in comments.

Count resolved versus remaining.

## Phase 4 — Verify Literals

Sample 20 in context for sense.

Re-parse the output for syntax.

Decode nested layers where found.

## Examples

### Example 1: Skimmer strings

User says: "Payment script hides all URLs."

Actions:

1. Emulated rotation, resolved 300 calls
2. Exfil URLs revealed
3. Blocked and reported
4. Evidence preserved

Result: Hidden IOCs exposed.

### Example 2: Adware batch

User says: "Same packer, many files."

Actions:

1. Templated decoder once
2. Batch-resolved 18 files
3. Sample-verified each
4. Campaign mapped

Result: Corpus decoded fast.

## Troubleshooting

### Rotation mismatch

Cause: Self-modifying or environment-keyed rotation

Fix:

1. Trace rotation inputs
2. Emulate key derivation statically
3. Fall back to sandbox observation
4. Document the keying

### Decoder aliases multiply

Cause: Wrapper chains and re-exports

Fix:

1. Map alias graph first
2. Collapse wrappers stepwise
3. Re-run resolution
4. Verify counts climb

### Literals still encoded

Cause: Second encoding inside entries

Fix:

1. Detect per-entry scheme
2. Decode with codec toolkit
3. Re-verify readability
4. Note the layering

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Extract.
- Resolve.
- Verify.

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

Avoid executing rotation IIFEs; hardcoded offsets; unverified literal trust; alias graphs skipped; nested layers missed; context-free restoration.

## Bundled References

Read `references/array-shapes.md` when emulating rotation or resolving decoders.
Run `scripts/string_array_decoder.py` to dump arrays and decode entry encodings.
Copy `assets/checklists.md` into every delivery.
