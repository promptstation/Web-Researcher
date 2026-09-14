---
name: browser-interaction-patterns
description: Automate forms, files, frames, and gestures with verification after every act. Use when the user asks to automate file uploads; handle downloads in Playwright; work with iframes; manage popups and tabs; script drag-and-drop reliably.
compatibility: Playwright or Puppeteer in Python or Node; download directories configured; no extras.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Browser Interaction Patterns

Make every interaction trustworthy. You cover all control types, handle files and frames explicitly, script gestures deterministically, and verify state after every single action.

Optimize simultaneously for:

- covered controls
- clean file flows
- explicit frames
- stable gestures
- verified steps

Every action asserts its result; no blind click-type-and-hope sequences.

## Use Cases

### Form flow

Trigger: user says 'long application form' or 'multi-step wizard'

Steps:

1. Map controls per step
2. Fill with verification
3. Handle conditional branches
4. Submit and confirm

Result: Reliable form automation.

### File exchange

Trigger: user says 'upload then download' or 'export flow'

Steps:

1. Set chooser and download paths
2. Upload with confirmation
3. Await download event
4. Verify file integrity

Result: Deterministic file flow.

### Frame maze

Trigger: user says 'nested iframes' or 'popup windows'

Steps:

1. Map frame tree
2. Use frame locators
3. Handle popup events
4. Verify per frame

Result: Clean multi-frame flow.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Control inventory
- File-path config
- Frame map
- Verification per action
- Pattern docs
- Cross-browser notes
- Failure artifacts
- Re-run evidence

Never chain unverified actions, and never rely on OS dialogs you cannot drive.

## Phase 1 — Map Controls

Inventory every control, frame, and dialog in the flow.

Note conditional branches and validations.

Choose locators per the ladder.

## Phase 2 — Script Explicitly

See `references/interaction-recipes.md` for per-control recipes.

Handle chooser, download, popup, and dialog events explicitly.

Keep one action per verified step.

## Phase 3 — Verify Each Act

Assert value, visibility, URL, or download after each step.

Fail fast with artifacts at the true step.

Log state transitions.

## Phase 4 — Librarize

Extract repeated flows into helpers.

Document with examples.

Test helpers in isolation.

## Examples

### Example 1: Wizard flow

User says: "5-step application wizard."

Actions:

1. Mapped 40 controls
2. Verified per step
3. Branches covered
4. 100 clean runs

Result: Trusted wizard suite.

### Example 2: Export flow

User says: "Export CSV then validate."

Actions:

1. Download event awaited
2. Checksum verified
3. Content parsed
4. Stable nightly

Result: Deterministic export test.

## Troubleshooting

### Upload silently fails

Cause: Hidden input or chooser timing

Fix:

1. Set files on input directly
2. Await chooser event properly
3. Verify file appears
4. Log input state

### Download never arrives

Cause: Path config or dialog dismissal

Fix:

1. Configure download path
2. Await download event
3. Check browser prefs
4. Verify bytes on disk

### Frame locator misses

Cause: Frame reload or wrong scope

Fix:

1. Re-resolve frame locators
2. Assert frame URL
3. Wait for frame load
4. Scope strictly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Script.
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

Avoid unverified chains; OS-dialog dependence; frame guessing; gesture without assertions; one-off unshared flows; cross-browser assumed.

## Bundled References

Read `references/interaction-recipes.md` when scripting specific controls.
Run `scripts/interactions_snippets.py` as copy-paste Playwright patterns (requires playwright to run).
Copy `assets/checklists.md` into every delivery.
