---
name: devtools-cdp-reverse-engineering
description: Reverse-engineer page flows with DevTools panels and CDP to capture APIs and script repeatable observations. Use when the user asks to reverse-engineer a site's API calls; capture HAR and WebSocket traffic; override responses for testing; attach CDP to a browser target; turn manual findings into scripts.
compatibility: Chrome or Edge with DevTools; Python 3.10+ for target discovery; optional CDP client libraries for deep scripting.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# DevTools CDP Reverse Engineering

Turn opaque pages into documented systems. You walk panels methodically, capture the traffic that matters, prove hypotheses with overrides, and convert each finding into a script the team can rerun.

Optimize simultaneously for:

- complete flow maps
- captured API contracts
- proven override experiments
- scripted observations
- verifiable reports

Do not report behavior you only saw once; capture traffic, reproduce, then script before claiming the finding.

## Use Cases

### Hidden API discovery

Trigger: user says 'find the API behind this page' or 'scrape without the DOM'

Steps:

1. Record network with preserved logs through the flow
2. Isolate XHR/fetch calls returning structured data
3. Export curl and document params plus auth
4. Recommend API-first extraction with fallback

Result: Documented API contract with replay proof.

### Bug reproduction

Trigger: user says 'works for me but fails there' or 'need exact repro steps'

Steps:

1. Capture HAR plus console plus environment details
2. Bisect with request blocking to isolate the trigger
3. Write minimal repro script
4. Hand off with artifacts attached

Result: Minimal reproducible case with evidence.

### Override experiment

Trigger: user says 'what if the API returned X' or 'test empty state'

Steps:

1. Override the response in DevTools
2. Screenshot behavior deltas
3. Decide fix or handling from evidence
4. Script the override for regression tests

Result: Behavior decision from live experiment.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Flow map: steps, calls, and state changes
- Traffic artifacts: HAR plus WebSocket excerpts
- API contracts: endpoint, params, auth, sample payload
- Override log: what changed and what behavior resulted
- Repro script: runnable with waits and assertions
- Environment notes: browser, viewport, locale, flags
- Report: findings a second analyst can verify
- Cleanup: overrides removed, profile state restored

Never claim findings from unreproduced sessions, and never leave overrides or debug flags in shared profiles.

## Phase 1 — Walk the Flow

Disable cache, preserve logs, clear storage to the test baseline.

Step the flow once slowly, narrating which panel answers each question.

Mark the calls and state changes that define the flow contract.

## Phase 2 — Capture Traffic

Export the HAR and copy critical requests as curl.

Inspect WebSocket frames and event-stream messages where present.

Redact tokens before storing or sharing any artifact.

## Phase 3 — Prove with Overrides

Block or override one variable at a time; record behavior deltas with screenshots.

Use XHR and DOM breakpoints to catch dynamic triggers.

Keep an override log with hypothesis, change, and verdict per row.

## Phase 4 — Script the Finding

Run `scripts/cdp_targets.py --port 9222` to verify protocol attachability for scripted follow-up.

Convert selectors, waits, and assertions into a runnable script.

Have the script assert the finding, not merely replay clicks.

## Examples

### Example 1: Pricing API capture

User says: "Extract prices without brittle DOM parsing."

Actions:

1. Captured product API with pagination params
2. Documented auth header lifetime
3. Built API-first extractor with DOM fallback
4. Cut breakage to near zero

Result: Stable extraction from contract, not markup.

### Example 2: Flaky checkout repro

User says: "Checkout fails only sometimes."

Actions:

1. HAR showed race between coupon validate and submit
2. Blocked validate to force the losing order
3. Wrote repro asserting the error state
4. Fix verified by the same script

Result: Race proven and regression-guarded.

## Troubleshooting

### HAR misses early requests

Cause: Recording started after navigation or cache served silently

Fix:

1. Enable preserve log and disable cache first
2. Reload and re-walk from a clean state
3. Check service-worker cache hits
4. Re-export and confirm coverage

### CDP endpoint refuses connection

Cause: Browser not launched with remote debugging or wrong port/profile

Fix:

1. Launch with --remote-debugging-port and a temp profile
2. Query /json/version to confirm
3. Check firewall and port conflicts
4. Never expose the port beyond localhost

### Override has no effect

Cause: Wrong URL pattern, cached response, or worker bypass

Fix:

1. Match exact URL with query handling
2. Disable cache and unregister workers for the test
3. Confirm override hit in network panel
4. Re-run with logging on the handler

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Walk.
- Capture.
- Proof.

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

Avoid single-sighting findings; HARs shared with live tokens; debug ports on shared hosts; overrides left in team profiles; replay scripts without assertions; protocol automation before UI proof.

## Bundled References

Read `references/cdp-domains.md` when choosing protocol domains for scripted observation.
Run `scripts/cdp_targets.py` to verify a debugging endpoint and list attachable targets.
Copy `assets/checklists.md` into every delivery.
