---
name: malicious-js-triage
description: Risk-score suspicious JS, extract IOCs safely, and disclose with evidence. Use when the user asks to triage a suspicious script; score JS malware risk; extract IOCs from JavaScript; report a skimmer; handle a malicious redirect.
compatibility: Any OS with Python 3.10+; isolated lab for detonation; disclosure contacts per case.
metadata:
  author: Promptstation
  version: 1.0.0
  category: js-analysis
---

# Malicious JS Triage

Move suspicious scripts from alarm to action. You score risk statically, detonate only when needed and isolated, extract IOCs without live-touching them, and disclose with defanged evidence packs.

Optimize simultaneously for:

- scored risk
- justified detonations
- safe IOCs
- deployed blocks
- closed disclosures

Never visit live malicious URLs from analyst hosts, and never publish live IOCs undefanged.

## Use Cases

### Skimmer alert

Trigger: user says 'possible skimmer' or 'card theft script'

Steps:

1. Score statically
2. Sandbox-detonate isolated
3. Extract exfil IOCs
4. Block and disclose

Result: Contained skimmer, filed case.

### Redirect chain

Trigger: user says 'malicious redirect' or 'injected script'

Steps:

1. Trace chain statically
2. Score each hop
3. Extract final IOCs
4. Disclose per hop owner

Result: Chain mapped and reported.

### Supply scare

Trigger: user says 'vendor script suspicious' or 'compromised tag'

Steps:

1. Score and detonate
2. Confirm or clear
3. Notify vendor
4. Pin or remove

Result: Verdict with evidence.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Risk scores with rubric
- Detonation decision plus logs
- IOC list defanged
- Block receipts
- Disclosure drafts
- Evidence pack
- Victim notes
- Closure record

Never live-touch malicious infrastructure from analyst systems, and never skip defanging in shared reports.

## Phase 1 — Score Static

Run `scripts/js_triage.py --file sample.js` for the risk score.

Grade eval, network, obfuscation, exfil signals.

Decide clear, monitor, or detonate.

## Phase 2 — Detonate Isolated

Sandbox only, no host shares, no real data.

Capture transcripts and payloads.

Hash everything.

## Phase 3 — Extract IOCs

List URLs, IPs, emails, wallets with context.

Defang for sharing (hxxp, dots).

Never fetch live from lab.

## Phase 4 — Block and Disclose

Deploy blocks with receipts.

Disclose to owners and registries.

Track to closure.

## Examples

### Example 1: Checkout skimmer

User says: "Odd script on checkout."

Actions:

1. Scored 92/100, detonated
2. Exfil endpoint captured
3. Blocked, vendor notified
4. Removed same day

Result: Skimmer killed fast.

### Example 2: False alarm

User says: "Obfuscated analytics looks evil."

Actions:

1. Scored 18/100, no network
2. Cleared as minified tracker
3. Documented verdict
4. Monitoring kept light

Result: Cleared with evidence.

## Troubleshooting

### Score borderline

Cause: Mixed benign and suspicious signals

Fix:

1. Weight network-plus-obfuscation highest
2. Detonate to break ties
3. Document the call
4. Re-score post-detonation

### IOCs rotate fast

Cause: DGA or fresh infrastructure

Fix:

1. Extract generation logic
2. Predict and pre-block
3. Share patterns
4. Monitor continuously

### Disclosure ignored

Cause: Wrong contact or abuse-desks flooded

Fix:

1. Escalate via registrar and host
2. Add evidence weight
3. Loop in affected brand
4. Track persistently

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Score.
- Detonate.
- Close.

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

Avoid live IOC visits; undefanged sharing; host detonation; score-free verdicts; disclosure skipping; victim silence.

## Bundled References

Read `references/triage-rubric.md` when scoring samples or deciding detonation.
Run `scripts/js_triage.py` to risk-score samples statically.
Copy `assets/checklists.md` into every delivery.
