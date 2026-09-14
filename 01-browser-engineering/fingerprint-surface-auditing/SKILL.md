---
name: fingerprint-surface-auditing
description: Inventory fingerprint signals and measure exposure for research consistency and defense. Use when the user asks to list what fingerprints a browser; measure my fingerprint exposure; check signal consistency of a profile; explain canvas and WebGL fingerprinting; harden a research browser defensively.
compatibility: Any modern browser; fingerprint test pages for measurement; no spoofing tooling included or required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Fingerprint Surface Auditing

Make browser identity legible for research and defense. You inventory every signal layer, measure exposure with repeatable probes, audit configurations for consistency, and recommend only defensive, scope-bound changes.

Optimize simultaneously for:

- complete surface inventory
- measured exposure
- consistency verdicts
- defensive hardening
- documented scope

This skill is for measurement and defense. Do not build or advise deception against access controls, fraud systems, or Terms of Service.

## Use Cases

### Exposure baseline

Trigger: user says 'how fingerprintable am I' or 'baseline this profile'

Steps:

1. Dump local probe signals
2. Record two test-page verdicts
3. Rank highest-entropy surfaces
4. Recommend defensive reductions

Result: Measured baseline with a defense list.

### Research consistency check

Trigger: user says 'verify my test profile matches spec' or 'signals disagree'

Steps:

1. Dump signals and compare to spec
2. Flag mismatched locale, timezone, and platform tuples
3. Correct configuration, not spoofing
4. Re-measure and sign off

Result: Consistent, spec-matching profile.

### Defense review

Trigger: user says 'reduce tracking surface' or 'harden researcher workstation'

Steps:

1. Inventory extensions, plugins, and custom settings
2. Standardize viewport and reduce standout signals
3. Verify breakage-free browsing
4. Document residual exposure honestly

Result: Smaller surface with honest residual notes.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Surface inventory grouped by layer with signal names
- Probe dump: values plus hashes for render-dependent signals
- Test-page verdicts from two independent pages
- Consistency table: expected vs observed per tuple
- Defense list: change, rationale, breakage check
- Scope note: purpose, limits, and prohibited uses
- Before/after deltas for any change
- Re-measurement steps with exact pages and snippet

Never provide spoofing recipes against bot defenses or fraud controls, and never claim anonymity from partial changes.

## Phase 1 — Inventory Surfaces

List JS navigator properties, screen and viewport tuples, canvas and WebGL outputs, audio fingerprints, font sets, TLS parameters, and behavioral channels.

Paste `scripts/fingerprint_probe.js` in DevTools console and save the JSON dump.

Group findings by layer so entropy reasoning stays organized.

## Phase 2 — Measure Exposure

Visit two established test pages and record uniqueness verdicts plus standout signals.

Hash render-dependent outputs to compare runs without storing images.

Rank surfaces by contribution to the verdict.

## Phase 3 — Audit Consistency

Check tuple coherence: platform with user agent, locale with timezone, touch with mobile viewport, GPU with vendor strings.

Flag every mismatch with expected and observed values.

Fix configuration at the source; do not patch single properties.

## Phase 4 — Harden Defensively

Apply standard viewport, minimal extensions, and reduced standout settings.

Verify daily workflows still function after each change.

Re-measure and document residual exposure without overclaiming.

## Examples

### Example 1: Profile sign-off

User says: "Verify this research profile before a study."

Actions:

1. Dumped 40 signals, found timezone-locale mismatch
2. Corrected OS timezone to match locale
3. Re-measured consistent across pages
4. Signed off with attached dumps

Result: Consistent profile with evidence.

### Example 2: Workstation hardening

User says: "Reduce my tracking surface."

Actions:

1. Found rare viewport plus 14 extensions
2. Standardized viewport, trimmed to 4 extensions
3. Confirmed workflows intact
4. Reported residual uniqueness honestly

Result: Smaller surface, honest residual.

## Troubleshooting

### Test pages disagree

Cause: Different signal sets, datasets, or visit timing

Fix:

1. Record both verdicts with dates
2. Compare standout signal lists
3. Trust shared standouts first
4. Re-test after each single change

### One spoofed value increased uniqueness

Cause: Incoherent tuple draws attention

Fix:

1. Revert to coherent defaults
2. Change tuples together or not at all
3. Prefer standard configurations
4. Document the lesson

### Canvas hash differs per run

Cause: GPU driver variance, font updates, or noise injection

Fix:

1. Note run variance explicitly
2. Compare distributions, not single hashes
3. Check driver and font changes
4. Avoid single-hash identity claims

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Inventory.
- Measure.
- Harden.

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

Avoid single-property spoofing advice; anonymity claims from partial tweaks; deception tooling for guarded targets; single-run hash identity claims; ignoring TLS and behavior layers; research without a scope note.

## Bundled References

Read `references/signal-layers.md` when inventorying or reasoning about entropy.
Run `scripts/fingerprint_probe.js` to dump local fingerprint signals in DevTools console.
Copy `assets/checklists.md` into every delivery.
