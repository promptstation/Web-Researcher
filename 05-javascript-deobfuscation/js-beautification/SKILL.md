---
name: js-beautification
description: Format and normalize minified JS into readable, diffable baselines. Use when the user asks to beautify minified JavaScript; normalize unicode escapes; unwrap packed JS safely; format JS for review; baseline code before analysis.
compatibility: Any OS with Python 3.10+; sample files; no execution of untrusted code.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# JS Beautification

Make code readable without changing it. You format with brace awareness, normalize escapes, unwrap trivial packers safely, and snapshot baselines that later passes diff cleanly against.

Optimize simultaneously for:

- readable formatting
- sane escapes
- safe unwraps
- saved baselines
- clean diffs

Formatting must be semantics-preserving and idempotent; never eval untrusted code to pretty-print it.

## Use Cases

### Review prep

Trigger: user says 'unreadable bundle' or 'format this'

Steps:

1. Format brace-aware
2. Normalize escapes
3. Snapshot baseline
4. Hand to review

Result: Reviewable code.

### Packer peel

Trigger: user says 'eval-packed file' or 'unwrap this'

Steps:

1. Identify packer
2. Decode payload statically
3. Verify output parses
4. Re-baseline

Result: Unwrapped layer.

### Diff setup

Trigger: user says 'compare versions' or 'what changed'

Steps:

1. Normalize both sides
2. Diff cleanly
3. Highlight real changes
4. Report

Result: Signal-only diff.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Formatted output files
- Escape report
- Unwrap log
- Baselines hashed
- Idempotency proof
- Diff samples
- Tool versions
- Review notes

Never eval untrusted code for formatting, and never hand-edit baselines without re-snapshotting.

## Phase 1 — Format Readable

Run `scripts/js_normalize.py --file sample.js --out clean.js` for baseline formatting.

Verify braces balance and strings intact.

Confirm idempotency by reformatting.

## Phase 2 — Normalize Escapes

Decode unicode and hex escapes to readable forms.

Unify quote styles conservatively.

Log every normalization applied.

## Phase 3 — Peel Trivial Packs

Detect eval-pack wrappers statically.

Decode payloads without execution.

Re-baseline each peeled layer.

## Phase 4 — Snapshot Baseline

Hash inputs and outputs.

Store with tool versions.

Diff later passes against it.

## Examples

### Example 1: Vendor review

User says: "Review this 2MB vendor file."

Actions:

1. Formatted to readable tree
2. Normalized escapes
3. Review completed in hours
4. Baseline archived

Result: Reviewable vendor code.

### Example 2: Packed widget

User says: "Widget ships packed."

Actions:

1. Unwrapped one pack layer
2. Revealed plain config plus loader
3. Cleared with evidence
4. Baseline saved

Result: Transparent widget.

## Troubleshooting

### Formatter mangles strings

Cause: Regex formatting inside template literals

Fix:

1. Use string-aware splitting
2. Verify string hashes pre/post
3. Hand-check flagged regions
4. Fix tool, not code

### Unwrap output will not parse

Cause: Partial decode or multi-layer pack

Fix:

1. Validate layer boundaries
2. Peel one layer only
3. Re-triage remainder
4. Never force-parse garbage

### Non-idempotent output

Cause: Stateful rules or line-length churn

Fix:

1. Pin formatter version
2. Freeze rule set
3. Prove fixpoint
4. Re-baseline corpus

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Format.
- Normalize.
- Base.

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

Avoid eval-based formatting; string-mangling regexes; unlogged normalizations; baselines skipped; multi-layer forced parses; hand-edited baselines.

## Bundled References

Read `references/normalization-rules.md` when formatting or peeling code.
Run `scripts/js_normalize.py` to format minified JS readably.
Copy `assets/checklists.md` into every delivery.
