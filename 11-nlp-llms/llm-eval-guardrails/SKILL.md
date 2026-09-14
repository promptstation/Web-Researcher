---
name: llm-eval-guardrails
description: Ship LLM features with red-teaming, PII scrubbing, and layered guardrails. Use when the user asks to red-team an LLM feature; scrub PII from text; prevent prompt injection; validate LLM outputs; check model outputs for toxicity.
compatibility: Adversarial suites; PII patterns per locale; human review for high-stakes.
metadata:
  author: Promptstation
  version: 1.0.0
  category: nlp
---

# LLM Eval Guardrails

Ship LLMs without surprises. You red-team adversarially, scrub PII both directions, check toxicity and bias, bound tools against injection, validate every output, and drill incidents before they happen.

Optimize simultaneously for:

- tested attacks
- scrubbed PII
- checked outputs
- bounded tools
- drilled teams

High-stakes outputs get human review; PII never trains or leaks; incidents disclosed.

## Use Cases

### Feature launch

Trigger: user says 'ship chatbot' or 'launch LLM feature'

Steps:

1. Red-team suite
2. Scrub + validate
3. Review band
4. Launch gated

Result: Safe launch.

### Injection scare

Trigger: user says 'prompt injection' or 'jailbreak found'

Steps:

1. Reproduce
2. Bound tools
3. Validate in/out
4. Re-test suite

Result: Hardened feature.

### PII audit

Trigger: user says 'leak check' or 'PII in outputs'

Steps:

1. Scan both ways
2. Fix gaps
3. Verify clean
4. Monitor live

Result: Clean pipeline.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Threat model
- Adversarial suite
- PII pattern set
- Scrub reports
- Validation rules
- Review SLA
- Drill log
- Incident runbook

Never connect LLMs to privileged tools without boundaries or skip human review for high-stakes.

## Phase 1 — Threat-Model

Attackers, assets, abuse cases.

Risk-tier the feature.

Scope the suite.

## Phase 2 — Scrub PII

Run `scripts/pii_redact_text.py --in sample.txt` to baseline.

Patterns per locale; verify with planted PII.

Scrub inputs and outputs; log counts.

## Phase 3 — Bound and Validate

Tools allowlisted, least-privilege, confirmable.

Outputs schema + policy checked.

Review band for risky.

## Phase 4 — Red-Team and Drill

Suite 100+ adversarial; fix all criticals.

Incident drill yearly.

Monitor live; re-test per release.

## Examples

### Example 1: Bot hardened

User says: "Launch support copilot."

Actions:

1. Red-teamed 150 attacks
2. Bounded tools
3. PII scrub live
4. Launched gated, clean

Result: Safe copilot.

### Example 2: Leak caught

User says: "Model echoed emails."

Actions:

1. Scrub gap found
2. Fixed + verified planted
3. Monitor added
4. Disclosed properly

Result: Closed leak.

## Troubleshooting

### Scrub over-redacts

Cause: Greedy patterns

Fix:

1. Tighten per locale
2. Context-aware rules
3. Review samples
4. Tune precision

### Jailbreaks persist

Cause: Single-layer defense

Fix:

1. Layer in+out checks
2. Bound tools harder
3. Update suite
4. Re-test

### Review floods

Cause: Threshold too low

Fix:

1. Risk-tier routing
2. Tune thresholds
3. Sample audits
4. Re-tune monthly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Model.
- Guard.
- Prove.

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

Avoid suite-free launches; scrub-free pipelines; boundary-free tools; validate-free outputs; review-free stakes; drill-free teams.

## Bundled References

Read `references/llm-safety.md` when guarding LLM features.
Run `scripts/pii_redact_text.py` to baseline PII scrubbing.
Copy `assets/checklists.md` into every delivery.
