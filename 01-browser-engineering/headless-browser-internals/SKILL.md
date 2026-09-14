---
name: headless-browser-internals
description: Verify headless launch configs and prove headed/headless parity before trusting automation. Use when the user asks to compare headless and headed rendering; verify Chrome launch flags; fix headless-only failures; choose automation hooks by privilege; prove parity for screenshots or scraping.
compatibility: Chrome or Firefox installed locally; Python 3.10+ for launch checks; optional xvfb for headed-on-server runs.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Headless Browser Internals

End headless superstition. You verify every launch flag, map hooks to privileges, and prove parity with diffs so automated results earn trust instead of assuming it.

Optimize simultaneously for:

- verified launch matrices
- explained mode deltas
- privilege-mapped hooks
- diff-proven parity
- auditable mode decisions

Do not bless a headless configuration without a parity diff against headed on the actual target pages.

## Use Cases

### Headless-only failure

Trigger: user says 'works headed, fails headless' or 'screenshots differ'

Steps:

1. Capture parity diffs: screenshot, DOM, console, network
2. Isolate GPU, media, or timing as the delta source
3. Adjust launch config minimally
4. Re-diff to clean

Result: Explained delta with minimal fix.

### Launch hardening

Trigger: user says 'audit our Chrome flags' or 'too many magic switches'

Steps:

1. List flags with claimed purpose each
2. Verify each flag's effect by removal test
3. Drop no-effect and risky flags
4. Publish the minimal matrix

Result: Minimal verified launch config.

### Hook selection

Trigger: user says 'which hook can do X' or 'need lower-privilege automation'

Steps:

1. Map candidate hooks to privileges
2. Test the least-privilege hook first
3. Escalate only on proven need
4. Document the privilege rationale

Result: Least-privilege automation that works.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Launch matrix: task class to flags to rationale
- Flag verification: removal-test result per flag
- Parity diffs: screenshot, DOM, console, network
- Delta explanations: every diff attributed
- Hook map: hook to privilege to evidence
- Mode decision: headless, new headless, xvfb, or headed
- Repro commands: exact launch lines
- Decision record a teammate can audit

Never ship launch configs with unverified flags, and never claim parity without diffs on real targets.

## Phase 1 — Verify Launch

Run `scripts/launch_matrix_check.py --binary <chrome|firefox>` to confirm headless modes and GPU paths.

Record version, channel, GPU status, and effective flags.

Removal-test each non-default flag and keep only those with proven effect.

## Phase 2 — Diff Parity

Render the same pages headed and headless with identical viewport, locale, and waits.

Diff screenshots perceptually, DOM structurally, and console plus network semantically.

Attribute every delta to GPU, media, fonts, timing, or behavior.

## Phase 3 — Map Hooks

List the hooks in play: CDP domains, WebDriver endpoints, BiDi modules, extensions.

Record what each can read and mutate plus its process privilege.

Prefer the least-privilege hook that covers the need.

## Phase 4 — Decide and Record

Choose the mode per task class with parity evidence attached.

Publish exact launch lines and environment notes.

File the decision record with deltas and rationale.

## Examples

### Example 1: Screenshot parity

User says: "Headless screenshots look wrong."

Actions:

1. Diff showed font and GPU-composite deltas
2. Aligned fonts and forced software compositing consistently
3. Re-diffed clean within tolerance
4. Locked the launch line

Result: Trusted headless screenshots.

### Example 2: Flag cleanup

User says: "Fourteen flags, nobody knows why."

Actions:

1. Removal-tested each flag on target pages
2. Kept 4 with effect, dropped 10
3. Parity re-verified after cleanup
4. Published minimal matrix

Result: Maintainable launch config.

## Troubleshooting

### Media never loads headless

Cause: Missing codecs, autoplay policy, or GPU-dependent pipeline

Fix:

1. Confirm codec support in the headless build
2. Set autoplay and media flags explicitly
3. Try xvfb-headed for GPU-dependent media
4. Document the media matrix

### Permission prompts stall automation

Cause: Headless permission defaults differ from headed grants

Fix:

1. Preset permissions via context options
2. Verify grant state before the flow
3. Handle prompt events explicitly
4. Re-diff prompt behavior

### Timing flakes only in automation

Cause: Faster execution exposing races, not rendering differences

Fix:

1. Replace sleeps with assertion retries
2. Confirm flakes persist headed with speed
3. Fix the race, not the mode
4. Keep parity evidence attached

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Launch.
- Parity.
- Hooks.

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

Avoid flag snippets without removal tests; parity assumed from one page; GPU blamed before timing is checked; sandbox disabled as a first resort; hook escalation without need proof; mode decisions without records.

## Bundled References

Read `references/headless-modes.md` when choosing modes or explaining deltas.
Run `scripts/launch_matrix_check.py` to verify installed browsers and headless capability.
Copy `assets/checklists.md` into every delivery.
