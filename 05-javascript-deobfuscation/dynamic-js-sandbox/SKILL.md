---
name: dynamic-js-sandbox
description: Observe suspicious JS in isolated sandboxes with logged stubs and hard budgets. Use when the user asks to run suspicious JS safely; sandbox obfuscated code; log what a script does; stub browser globals for analysis; capture JS exfil attempts.
compatibility: Node.js 18+ for vm sandboxes or a Linux VM; no network route for samples; host stays clean.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Dynamic JS Sandbox

Watch malware-adjacent code without becoming its victim. You isolate hard, stub convincingly, log everything, enforce budgets, and turn runtime behavior into hashed, documented evidence.

Optimize simultaneously for:

- hard isolation
- convincing stubs
- complete logs
- enforced budgets
- filed evidence

Isolated VMs or containers only, no host shares, no real network, no real credentials, budgets always on.

## Use Cases

### Payload reveal

Trigger: user says 'what does it do at runtime' or 'static dead end'

Steps:

1. Isolate and stub
2. Run with budgets
3. Capture transcript
4. Report behavior

Result: Observed intent, safe host.

### Exfil mapping

Trigger: user says 'where does it send data' or 'find C2'

Steps:

1. Stub network with logging
2. Run to exfil attempt
3. Record endpoints plus payloads
4. Block and disclose

Result: IOC list with proof.

### Environment keying

Trigger: user says 'behaves differently' or 'VM-aware?'

Steps:

1. Matrix environments
2. Diff behaviors
3. Name the keying signals
4. Document evasion

Result: Keying mapped honestly.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Isolation checklist signed
- Stub inventory
- Budget settings
- Full transcripts
- IOC lists
- Hashes of samples
- Environment notes
- Behavior report

Never run suspicious code on analyst hosts or connected networks, and never feed real credentials to samples.

## Phase 1 — Isolate Hard

Use a disposable VM or container without host shares.

Deny network except logged stub sinks.

Snapshot before first run.

## Phase 2 — Stub and Budget

Run `node scripts/sandbox_run.js --file sample.js --timeout 5000` for the first observation.

Stub missing globals from error messages iteratively.

Set time, loop, and memory budgets.

## Phase 3 — Capture Behavior

Log calls with arguments and order.

Record DOM, storage, and network attempts.

Hash all artifacts.

## Phase 4 — Report Evidence

Write behavior narrative with transcript excerpts.

List IOCs with context.

File with sample hashes.

## Examples

### Example 1: Skimmer run

User says: "Does it steal card fields?"

Actions:

1. Sandboxed with form stubs
2. Captured exfil POST shape
3. Blocked endpoint, disclosed
4. Report with transcript

Result: Confirmed and contained.

### Example 2: Keyed payload

User says: "Silent in our lab."

Actions:

1. Matrixed locales and referrers
2. Activated on one combo
3. Behavior captured
4. Keying documented

Result: Evasion mapped.

## Troubleshooting

### Sample exits silently

Cause: Missing stub or environment gate

Fix:

1. Read the guard conditions
2. Stub convincingly
3. Vary one signal at a time
4. Log the gating

### Infinite loop burns budget

Cause: Anti-analysis delay loops

Fix:

1. Shorten budgets
2. Stub Date for jumps
3. Cap iterations
4. Note the tactic

### Different behavior per run

Cause: Time, random, or remote keying

Fix:

1. Freeze time and random
2. Log remote fetches
3. Matrix variables
4. Report variance

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Isolate.
- Run.
- Report.

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

Avoid host execution; real network for samples; real credentials in stubs; budget-free runs; vm-as-security-boundary thinking; observed-vs-inferred blurring.

## Bundled References

Read `references/sandbox-ops.md` when running or reporting dynamic analysis.
Run `scripts/sandbox_run.js` for first-observation sandboxed runs.
Copy `assets/checklists.md` into every delivery.
