---
name: tcp-ip-flow-fundamentals
description: Attribute connection cost to DNS, TCP, and TLS phases and set timeouts from measured reality. Use when the user asks to explain slow connects to a host; set timeouts from measurements; separate network from app failures; tune keep-alive and reuse; baseline path latency for scraping.
compatibility: Any OS with Python 3.10+ and outbound TCP; no root or capture tools required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# TCP IP Flow Fundamentals

Ground every timeout and retry in transport evidence. You split connection cost by phase, baseline paths with percentiles, and eliminate fault layers in order so fixes land on the true cause.

Optimize simultaneously for:

- attributed connection cost
- measured timeout tables
- correct fault layering
- tuned reuse
- recorded baselines

Do not set timeouts or blame the network without phased timings from the affected path.

## Use Cases

### Slow host triage

Trigger: user says 'one host is slow' or 'connects time out'

Steps:

1. Probe DNS, connect, and TLS splits repeatedly
2. Compare against baseline percentiles
3. Name the inflated phase
4. Fix routing, timeout, or target handling accordingly

Result: Phase-named fix with splits.

### Timeout policy

Trigger: user says 'set timeouts for the fleet' or 'too many false timeouts'

Steps:

1. Sample each host class at production hours
2. Derive connect, read, and total from percentiles
3. Roll out per-host tables
4. Watch timeout-rate deltas

Result: Timeouts matched to reality.

### Fault separation

Trigger: user says 'is it us or them' or 'app versus network'

Steps:

1. Walk the elimination order with live probes
2. Pin transport, TLS, HTTP, or app
3. Hand off with phase evidence
4. Record the verdict pattern

Result: Correct owner with proof.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Phase splits: DNS, connect, TLS, first byte
- Percentile baselines per host class
- Timeout table with derivation notes
- Elimination walk with verdict
- Reuse and keep-alive settings
- Before/after timeout-rate deltas
- Probe commands with exact flags
- Baseline record with date and path notes

Never tune timeouts from single samples, and never conflate application slowness with transport faults.

## Phase 1 — Split the Connection

Run `scripts/connectivity_probe.py --host <h> --port 443 --samples 20` and save the JSON.

Record DNS, TCP connect, TLS handshake, and time-to-first-byte medians and p95s.

Flag any phase exceeding its baseline by 2x as the suspect.

## Phase 2 — Baseline the Path

Sample at production hours across two days minimum.

Store percentiles per host class: APIs, listings, media, auth.

Note routing, proxy egress, and geography per baseline.

## Phase 3 — Derive Timeouts

Set connect to p95 plus 50 percent margin, capped sanely per class.

Set read from TTFB p95 plus body scaling; set totals from end-to-end p99.

Publish the table with derivation math visible.

## Phase 4 — Eliminate and Verify

Walk DNS, transport, TLS, HTTP, app in order on each new failure.

Stop at the first phase that reproduces abnormally and fix there.

Re-probe after fixes and confirm the timeout rate fell.

## Examples

### Example 1: One slow API

User says: "API calls randomly take 10 seconds."

Actions:

1. Splits showed TLS p95 at 8s on one egress
2. Traced to proxy TLS interception on that pool
3. Moved API traffic to direct egress
4. p95 back under 800ms

Result: Egress fix from phase evidence.

### Example 2: Timeout tuning

User says: "False timeouts killing good jobs."

Actions:

1. Sampled 200 fetches per class
2. Raised read timeout for media, lowered for APIs
3. Timeout rate fell 6 percent to 0.4 percent
4. Table published with math

Result: Calibrated timeouts, fewer false kills.

## Troubleshooting

### Connect hangs then succeeds in bursts

Cause: DNS stalls or SYN throttling on the path

Fix:

1. Split DNS from connect over time
2. Try alternate resolvers and compare
3. Check SYN retry patterns
4. Pin resolver or route fix

### High latency only through proxy

Cause: Egress congestion or distant exit nodes

Fix:

1. Compare direct versus proxy splits
2. Test alternate exits and pools
3. Quarantine slow egress
4. Route latency-sensitive hosts direct

### Timeouts cluster at one hour

Cause: Target deploy windows or rate shaping by time

Fix:

1. Correlate with target status signals
2. Shift load away from the window
3. Widen totals only for that window
4. Document the shaping pattern

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Splits.
- Timeouts.
- Faults.

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

Avoid single-sample timeout tuning; blaming the network without splits; identical timeouts for all host classes; retries on non-idempotent posts; ignoring DNS as a phase; fixing app code for transport faults.

## Bundled References

Read `references/transport-signals.md` when reading timings or setting timeouts.
Run `scripts/connectivity_probe.py` to capture phased timings per host.
Copy `assets/checklists.md` into every delivery.
