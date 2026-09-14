---
name: browser-automation-foundations
description: Install and verify automation stacks and write lifecycle-correct first scripts. Use when the user asks to set up Playwright from scratch; install Puppeteer and browsers; verify Selenium drivers; write my first automation script; compare headed and headless runs.
compatibility: Any OS with Python 3.10+ or Node.js 18+; 2GB free for browsers; no prior automation needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Browser Automation Foundations

Start every automation journey on solid ground. You install pinned stacks, verify launches in both modes, teach lifecycle-correct scripts, and make failure artifacts automatic from the very first run.

Optimize simultaneously for:

- verified installs
- pinned versions
- working first scripts
- automatic artifacts
- parity awareness

No automation without verified installs and lifecycle-correct templates; never debug without artifacts.

## Use Cases

### Fresh setup

Trigger: user says 'new to Playwright' or 'set up automation'

Steps:

1. Install pinned stack
2. Verify launches
3. Run first script
4. Review artifacts

Result: Working environment, first green run.

### Stack comparison

Trigger: user says 'Playwright or Puppeteer' or 'which tool'

Steps:

1. List needs per project
2. Trial both on one flow
3. Score reliability and fit
4. Recommend with evidence

Result: Evidence-backed tool pick.

### Upgrade safety

Trigger: user says 'update browsers' or 'new major version'

Steps:

1. Pin current working set
2. Upgrade in branch
3. Run parity suite
4. Roll out or roll back

Result: Safe upgrade with proof.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Install transcript
- Version pins
- Launch verification
- First-script template
- Artifact samples
- Parity smoke results
- Upgrade runbook
- Troubleshooting notes

Never run unpinned stacks in shared work, and never skip cleanup and artifacts.

## Phase 1 — Install Pinned

Install the chosen stack with locked versions.

Run `scripts/env_check.py` and save the report.

Record OS, browser, and driver versions.

## Phase 2 — Verify Launches

Launch headed and headless; screenshot about:blank both.

Confirm GPU path and console access.

File the verification log.

## Phase 3 — Write First Script

Use the lifecycle template: launch, act, assert, artifact, close.

Force one failure and inspect artifacts.

Review with a second pair of eyes.

## Phase 4 — Lock and Document

Pin versions in requirements.

Write the upgrade runbook.

Schedule quarterly re-verification.

## Examples

### Example 1: Team onboarding

User says: "Onboard five engineers to Playwright."

Actions:

1. Pinned stack doc plus env checks
2. First scripts green day one
3. Artifacts taught early
4. Zero setup drift

Result: Uniform ready team.

### Example 2: Headed mystery

User says: "Works headed, fails headless."

Actions:

1. Parity smoke isolated GPU path
2. Documented mode deltas
3. Chose xvfb for the suite
4. Flakes gone

Result: Mode decision with evidence.

## Troubleshooting

### Browser will not launch

Cause: Missing system deps or driver mismatch

Fix:

1. Read the exact launch error
2. Install OS deps per docs
3. Align driver and browser
4. Re-verify clean

### First script hangs

Cause: Missing waits or unclosed browser

Fix:

1. Add explicit timeouts
2. Ensure finally-close
3. Capture trace
4. Re-run to green

### Works for one engineer only

Cause: Unpinned versions or OS differences

Fix:

1. Diff env_check reports
2. Pin everything
3. Containerize the runner
4. Re-verify fleet-wide

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Install.
- First.
- Lock.

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

Avoid unpinned stacks; cleanup-free scripts; artifact-free debugging; mode blindness; blind upgrades; setup drift across team.

## Bundled References

Read `references/stack-setup.md` when installing or upgrading automation stacks.
Run `scripts/env_check.py` to verify automation environments.
Copy `assets/checklists.md` into every delivery.
