---
name: mitm-traffic-interception
description: Intercept owned test traffic with mitmproxy addons for logging, modification, and replay. Use when the user asks to inspect HTTPS from my test app; log API flows with mitmproxy; modify responses for testing; replay captured flows; debug mobile app traffic I own.
compatibility: Python 3.10+ with mitmproxy installed; test devices you own; never for third-party traffic.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# Mitm Traffic Interception

Make interception surgical and lawful. You scope traffic in writing, route only what is authorized, script addons that log and modify with guardrails, and package redacted evidence others can verify.

Optimize simultaneously for:

- written scope
- verified routing
- reviewed addons
- deterministic replays
- redacted evidence

Intercept only traffic you own or are explicitly authorized to inspect; block everything else at the proxy and document scope before capturing.

## Use Cases

### App API mapping

Trigger: user says 'map my test app API' or 'document staging calls'

Steps:

1. Scope hosts in writing
2. Route test device via mitm
3. Log flows with redaction addon
4. Publish contracts from logs

Result: Documented API from owned traffic.

### Fault injection

Trigger: user says 'test error handling' or 'simulate 500s'

Steps:

1. Write modifying addon with host guard
2. Inject faults per scenario
3. Record app behavior
4. Remove addon and verify clean

Result: Behavior proof per fault.

### Regression replay

Trigger: user says 'replay this sequence' or 'deterministic API test'

Steps:

1. Capture baseline flows
2. Script replay with assertions
3. Run on demand in CI
4. Alert on contract drift

Result: Living API contract test.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Scope sheet: hosts, devices, duration
- CA install proof on test devices
- Mode choice with rationale
- Addon code reviewed
- Flow logs in JSONL with schema
- Modification log per scenario
- Redaction pass documented
- Teardown: routes and certs restored

Never intercept traffic outside written scope, and never store unredacted credentials from flows.

## Phase 1 — Scope and Route

Write hosts, devices, accounts, and time window; get sign-off.

Install CA on test devices only; verify fingerprint matches.

Route in-scope traffic; blocklist everything else in the addon.

## Phase 2 — Log with Addons

Run `mitmdump -s scripts/mitm_flows_addon.py --set out=flows.jsonl` after reviewing the addon.

Confirm JSONL rows with redacted auth fields.

Sample-verify flows against app actions.

## Phase 3 — Modify and Replay

Enable modification rules one scenario at a time.

Record behavior deltas with screenshots or assertions.

Build replay scripts with contract assertions.

## Phase 4 — Package and Tear Down

Redact, hash, and pack evidence with the scope sheet.

Remove routes and test CA material per policy.

File retention and deletion dates.

## Examples

### Example 1: Staging contract

User says: "Document staging API before release."

Actions:

1. Scoped 3 hosts, logged 200 flows
2. Extracted 12 endpoint contracts
3. Redacted and published
4. Tore down same day

Result: Reviewed contract doc.

### Example 2: Offline behavior

User says: "Prove graceful offline mode."

Actions:

1. Injected failures per endpoint
2. App showed cached states correctly
3. Two gaps fixed and re-tested
4. Evidence pack filed

Result: Proven resilience, gaps closed.

## Troubleshooting

### App pins certs and refuses proxy

Cause: Certificate pinning on test builds

Fix:

1. Use debuggable builds with pinning disabled
2. Never bypass pins on production apps
3. Test at staging with consent
4. Document the pinning boundary

### Flows missing for one host

Cause: Out-of-scope block or direct connection

Fix:

1. Check allowlist first
2. Verify device proxy settings
3. Confirm no VPN bypass
4. Re-run with logging on blocks

### Replay nondeterministic

Cause: Timestamps, nonces, or ordering variance

Fix:

1. Normalize dynamic fields
2. Sequence with explicit waits
3. Assert contracts not bytes
4. Stabilize fixtures

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Scope.
- Run.
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

Avoid interception without scope sheets; production traffic through test proxies; pinning bypass attempts; unredacted flow archives; allowlist-free addons; certs left on shared devices.

## Bundled References

Read `references/mitm-modes.md` when choosing interception topology.
Run `scripts/mitm_flows_addon.py` as the reviewed starting addon for scoped logging.
Copy `assets/checklists.md` into every delivery.
