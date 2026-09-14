---
name: websocket-stream-analysis
description: Debug WebSocket upgrades, frames, and reconnects from handshake evidence. Use when the user asks to debug a WebSocket disconnect; explain close codes; compare WebSocket and SSE; fix reconnect storms; parse WebSocket frames.
compatibility: Any OS with Python 3.10+; test endpoints you own; no special libraries.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# WebSocket Stream Analysis

Make streams observable and polite. You verify handshakes, parse frames to verdicts, read close codes literally, and design reconnects that recover without hammering servers.

Optimize simultaneously for:

- verified handshakes
- parsed frames
- read close codes
- calm reconnects
- watched streams

Do not tune reconnects or blame servers without handshake transcripts and close-code evidence.

## Use Cases

### Drop diagnosis

Trigger: user says 'socket drops randomly' or 'code 1006'

Steps:

1. Capture handshake and close sequence
2. Read close code and ping gaps
3. Pin network, server, or client cause
4. Fix with evidence

Result: Pinned cause, targeted fix.

### Transport choice

Trigger: user says 'WebSocket or SSE' or 'polling versus streams'

Steps:

1. Map direction, scale, and infra
2. Score options on ops cost
3. Prototype the winner
4. Measure under load

Result: Justified transport pick.

### Storm control

Trigger: user says 'reconnects DDoS us' or 'thundering herd'

Steps:

1. Add backoff with jitter and caps
2. Stagger fleet restarts
3. Add resume tokens
4. Storm-test before deploy

Result: Calm recovery at scale.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Handshake transcript
- Frame evidence for claims
- Close-code table with meanings
- Ping and lag measurements
- Transport comparison
- Reconnect policy with caps
- Storm-test results
- Monitoring with alerts

Never ship reconnects without backoff caps, and never ignore close codes in favor of blind retries.

## Phase 1 — Verify Handshake

Run `scripts/ws_handshake_check.py --url <ws-url>` and save the transcript.

Confirm 101, Upgrade, Connection, and Sec-WebSocket-Accept correctness.

Record subprotocol and extension negotiation.

## Phase 2 — Parse Frames

Decode opcodes, lengths, and masking for the suspect sequence.

Reassemble fragments before judging content.

Log ping/pong gaps as health signal.

## Phase 3 — Read Closes

Map every close code to its RFC meaning plus server custom codes.

Correlate closes with deploys, idles, and load.

Separate clean closes from abnormal drops.

## Phase 4 — Engineer Reconnects

Set base, cap, jitter, max attempts, and resume behavior.

Stagger fleets and honor Retry-After style signals.

Storm-test with simulated outage and confirm calm.

## Examples

### Example 1: Nightly 1006s

User says: "Sockets die nightly at 3am."

Actions:

1. Closes correlated with proxy idle timeout
2. Added 25s pings under the 30s idle
3. 1006s stopped entirely
4. Alert set on ping gaps

Result: Idle-timeout fix with proof.

### Example 2: Herd on deploy

User says: "Deploys cause reconnect floods."

Actions:

1. Added jittered backoff plus stagger
2. Server drains before close
3. Flood became trickle
4. Storm drill recorded

Result: Calm deploys.

## Troubleshooting

### Handshake 400s on one path

Cause: Missing headers, bad key, or proxy stripping Upgrade

Fix:

1. Diff working vs failing transcripts
2. Check proxy Upgrade passthrough
3. Fix client headers
4. Re-verify 101

### Messages delayed in bursts

Cause: Nagle, buffering proxies, or slow consumer

Fix:

1. Disable needless buffering
2. Measure consumer lag
3. Add backpressure signals
4. Confirm smooth delivery

### Resume duplicates data

Cause: No idempotency on replayed messages

Fix:

1. Add message IDs server-side
2. Dedupe client-side on resume
3. Test kill-and-resume
4. Monitor duplicate rate

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Handshake.
- Frames.
- Reconnect.

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

Avoid blind retries on closes; reconnects without jitter; handshake guesses without transcripts; masked-frame confusion; resume without idempotency; storm-untested deploy plans.

## Bundled References

Read `references/stream-transports.md` when choosing or debugging streaming.
Run `scripts/ws_handshake_check.py` to verify upgrade handshakes verbosely.
Copy `assets/checklists.md` into every delivery.
