---
name: packet-capture-analysis
description: Plan minimal captures and extract stream evidence with tshark and Wireshark discipline. Use when the user asks to capture traffic for one flow; write a BPF filter; follow a TLS or HTTP/2 stream; prove retransmission from a capture; extract evidence from a pcap.
compatibility: Any OS with tcpdump or Wireshark/tshark installed; capture needs local admin or owned test traffic.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# Packet Capture Analysis

Capture less, prove more. You plan minimal filters, record with rotation discipline, analyze through statistics and stream views, and extract redacted evidence that stands up in review.

Optimize simultaneously for:

- minimal complete captures
- filter precision
- stream-level verdicts
- redacted evidence
- repeatable recipes

Capture only traffic you own or are authorized to inspect; minimize collection and redact before sharing.

## Use Cases

### Flow debug

Trigger: user says 'prove what the client sent' or 'server claims X'

Steps:

1. Plan filter for the flow
2. Capture with rotation
3. Follow the stream to verdict
4. Extract redacted transcript

Result: Packet-level truth, minimal bytes.

### Loss proof

Trigger: user says 'prove packet loss' or 'retransmission suspected'

Steps:

1. Capture both ends if possible
2. Graph sequence and ACK behavior
3. Quantify retransmit rate
4. Hand off with IO graph

Result: Quantified loss evidence.

### Protocol study

Trigger: user says 'map this handshake' or 'decode this stream'

Steps:

1. Capture with full snaplen
2. Dissect layers in order
3. Annotate the handshake or framing
4. Publish the annotated flow

Result: Readable protocol map.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Capture plan: target, filter, duration, size cap
- BPF filter with rationale per clause
- Recording setup: snaplen, rotation, interface
- Analysis path: filters and statistics used
- Stream evidence: followed transcript or graph
- Redaction log: what was removed and why
- Retention note: storage and deletion date
- Re-capture commands

Never capture broadly without filters, and never share payloads with credentials or PII intact.

## Phase 1 — Plan the Capture

Run `scripts/capture_plan.py --host <h> --port 443 --task tls-debug` to generate filter and commands.

Confirm authorization, interface, and size caps in writing.

Set snaplen: full for analysis, trimmed only for header-only stats.

## Phase 2 — Record Cleanly

Use ring buffers and file rotation; never one giant file.

Timestamp with the flow's wall clock; note timezone.

Stop on evidence, not on schedule overrun.

## Phase 3 — Analyze by Streams

Start with conversations and protocol hierarchy, not packet lists.

Follow the suspect stream; read handshakes and framing in order.

Graph IO and RTT where timing is the question.

## Phase 4 — Extract and Redact

Export the stream transcript and key frames with hashes.

Redact auth, cookies, tokens, and PII; log each redaction.

Set deletion date and store securely until then.

## Examples

### Example 1: Auth header dispute

User says: "Server says we never sent the token."

Actions:

1. Captured the flow at 2MB
2. Followed TLS with key log on test client
3. Transcript showed header present
4. Server team found their parser bug

Result: Dispute settled by transcript.

### Example 2: Retransmit proof

User says: "Path blamed for slow uploads."

Actions:

1. IO graph showed 8 percent retransmits
2. Quantified per-minute with tshark stats
3. Network team rerouted
4. Re-capture clean

Result: Reroute from quantified loss.

## Troubleshooting

### Capture misses packets

Cause: Snaplen trimming, buffer drops, or Wi-Fi monitor gaps

Fix:

1. Raise buffer and snaplen
2. Capture on wired path
3. Check dropped-packet counters
4. Re-capture with tighter filter

### TLS indecipherable

Cause: No key log or forward-secret session without keys

Fix:

1. Use test client with SSLKEYLOGFILE
2. Capture from session start
3. Confirm key log matches
4. Analyze metadata if keys unavailable

### Filter catches nothing

Cause: Wrong interface, VLAN tags, or tunnel encapsulation

Fix:

1. Verify interface traffic first
2. Account for VLAN and tunnels
3. Broaden one clause at a time
4. Confirm with unfiltered sample briefly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Plan.
- Record.
- Share.

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

Avoid unfiltered captures; giant single pcaps; payload sharing without redaction; packet scrolling instead of statistics; decryption of traffic you do not own; captures kept past retention.

## Bundled References

Read `references/capture-filters.md` when writing BPF or display filters.
Run `scripts/capture_plan.py` to generate precise capture commands per task.
Copy `assets/checklists.md` into every delivery.
