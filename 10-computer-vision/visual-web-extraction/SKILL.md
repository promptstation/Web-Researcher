---
name: visual-web-extraction
description: Extract from pixels when markup fails, fused with DOM for robustness. Use when the user asks to screenshot-based extraction; locate canvas elements; golden image regression; extract from rendered layout; combine DOM and visual signals.
compatibility: Playwright/Puppeteer screenshots; template matching or VLM per need; masked diffing.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# Visual Web Extraction

Read pages like users see them. You capture reproducibly, locate the unlocatable, recover layout from pixels, regress goldens with masks, and fuse visual with DOM so either channel can carry the extraction.

Optimize simultaneously for:

- reproducible shots
- found widgets
- recovered layouts
- trusted goldens
- fused extractors

Mask volatile regions; goldens updated deliberately, never auto-accepted blindly.

## Use Cases

### Canvas content

Trigger: user says 'data in canvas' or 'no DOM to parse'

Steps:

1. Capture element
2. OCR or template
3. Verify values
4. Fuse with API if any

Result: Canvas data flowing.

### Layout QA

Trigger: user says 'design broke' or 'visual regression'

Steps:

1. Golden baseline
2. Mask volatile
3. Diff per commit
4. Triage diffs

Result: Caught visual breaks.

### Fragile DOM

Trigger: user says 'selectors rot weekly' or 'obfuscated markup'

Steps:

1. Add visual channel
2. Cross-check DOM
3. Alert on diverge
4. Ship fused

Result: Rot-proof extraction.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Capture spec
- Locator gallery
- Layout method
- Golden set masked
- Diff policy
- Fusion design
- Triage log
- Flake metrics

Never auto-accept golden updates or ship unmasked volatile diffs as failures.

## Phase 1 — Capture Well

Fixed viewport, fonts, timezone; hide carets.

Full-page, element, viewport as needed.

Manage set with `scripts/visual_golden.py`.

## Phase 2 — Locate and Read

Template/OCR/VLM per content.

Verify values against DOM/API.

Gallery of locators kept.

## Phase 3 — Golden Regression

Mask dates, ads, avatars.

Threshold per page; triage diffs.

Update goldens deliberately.

## Phase 4 — Fuse Channels

DOM primary, visual fallback or check.

Diverge alerts.

Either channel valid alone.

## Examples

### Example 1: Map data

User says: "Prices only on map pins."

Actions:

1. Element shots plus OCR
2. Verified vs API
3. Fused extractor
4. Stable feed

Result: Unreachable data reached.

### Example 2: Break caught

User says: "Checkout button vanished."

Actions:

1. Golden diff flagged
2. Fixed pre-release
3. Masks tuned
4. Suite trusted

Result: Visual safety net.

## Troubleshooting

### Shot flakes

Cause: Fonts, animations, async content

Fix:

1. Pin fonts
2. Freeze animations
3. Wait network-stable
4. Mask residuals

### OCR misreads

Cause: Small text or low contrast

Fix:

1. Upscale element shots
2. Preprocess
3. Constrain vocab
4. Cross-check DOM

### Diff floods

Cause: Unmasked volatility

Fix:

1. Mask aggressively
2. Threshold per region
3. Triage daily
4. Stabilize capture

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Shot.
- Read.
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

Avoid nondeterministic shots; unmasked goldens; auto-accepted updates; visual-only fragility; diff-flood tolerance; verify-free OCR.

## Bundled References

Read `references/visual-extraction.md` when extracting visually or regressing goldens.
Run `scripts/visual_golden.py` to manage golden screenshot sets.
Copy `assets/checklists.md` into every delivery.
