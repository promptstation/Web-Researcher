---
name: http-version-mechanics
description: Confirm negotiated HTTP versions and tune concurrency and priority per version. Use when the user asks to check which HTTP version a site uses; tune concurrency for HTTP/2 targets; diagnose HTTP/3 fallback problems; explain multiplexing behavior; set per-version client policy.
compatibility: Any OS with Python 3.10+ and outbound HTTPS; browser DevTools for waterfall confirmation.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# HTTP Version Mechanics

Make protocol behavior explicit per origin. You census versions, prove multiplexing where claimed, ladder concurrency to the knee, and publish per-version policies that balance speed with politeness.

Optimize simultaneously for:

- version census
- proven multiplexing
- knee-found concurrency
- explained fallbacks
- published policy

Do not set concurrency or priority policy without ALPN evidence and ladder measurements from the affected origins.

## Use Cases

### Slow multiplexed target

Trigger: user says 'HTTP/2 site still slow' or 'streams seem serial'

Steps:

1. Confirm ALPN and stream behavior
2. Check server priorities and flow windows
3. Ladder concurrency to the knee
4. Fix client or server setting with proof

Result: Real multiplexing gains, measured.

### Downgrade mystery

Trigger: user says 'HTTP/3 never negotiates' or 'QUIC blocked somewhere'

Steps:

1. Capture ALPN direct and per path
2. Test UDP reachability to 443
3. Pin the downgrading layer
4. Fix route, proxy, or client

Result: Named layer, restored version.

### Fleet policy

Trigger: user says 'one concurrency for all hosts' or 'getting 429s on new targets'

Steps:

1. Census versions fleet-wide
2. Ladder each class
3. Publish per-version caps
4. Watch 429 and latency deltas

Result: Polite, fast per-version policy.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- ALPN evidence per origin
- Version census table
- Multiplexing proof where claimed
- Ladder results with knee marked
- Priority assignments for heroes
- Fallback diagnosis with layer
- Policy table per version
- Re-check commands

Never copy concurrency numbers across versions, and never claim HTTP/3 wins without negotiation proof.

## Phase 1 — Census Versions

Run `scripts/protocol_negotiation_audit.py --targets targets.txt` and save the table.

Record ALPN, server header, and any version hints per origin.

Chart the fleet mix before tuning anything.

## Phase 2 — Prove Multiplexing

Waterfall one HTTP/2 origin and confirm overlapping streams on one connection.

Note server priority handling and any serial bottlenecks.

Repeat for HTTP/3 where negotiated.

## Phase 3 — Ladder Concurrency

Raise per-host concurrency stepwise while watching latency and 429s.

Mark the knee where gains flatten or errors rise.

Set caps at 70 percent of the knee for headroom.

## Phase 4 — Publish Policy

Write per-version caps, priorities, and fallback handling.

Attach evidence commands and expected outputs.

Schedule quarterly re-census.

## Examples

### Example 1: 429s on new target

User says: "New HTTP/2 target bans us fast."

Actions:

1. Census confirmed h2; ladder showed knee at 4
2. Cut cap from 16 to 3 with priorities
3. 429s stopped, throughput steady
4. Policy updated for the class

Result: Polite throughput with proof.

### Example 2: QUIC never negotiates

User says: "HTTP/3 configured but unused."

Actions:

1. ALPN showed h2; UDP 443 blocked at egress
2. Opened path for test pool
3. h3 negotiated, handshake faster
4. Rolled out with fallback intact

Result: Version restored at the true layer.

## Troubleshooting

### h2 waterfall looks serial

Cause: Server ignores priorities or client opens many connections

Fix:

1. Confirm single connection in net log
2. Check priority signals sent
3. Reduce connection count
4. Re-waterfall to verify overlap

### h3 works direct, fails via proxy

Cause: Proxy lacks UDP/QUIC support or strips Alt-Svc

Fix:

1. Diff ALPN and Alt-Svc per path
2. Test alternate egress
3. Route h3-capable hosts direct
4. Document proxy capability matrix

### Higher concurrency slows everything

Cause: Past the knee into loss or server queueing

Fix:

1. Re-ladder to find the true knee
2. Back off to 70 percent
3. Add jitter to starts
4. Watch p95, not mean

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Census.
- Tuning.
- Policy.

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

Avoid one concurrency for all versions; HTTP/3 claims without ALPN; priority hints treated as guarantees; sharding on HTTP/2 origins; knee ignored for round numbers; fallback paths untested.

## Bundled References

Read `references/http-versions.md` when reasoning about connections or setting concurrency.
Run `scripts/protocol_negotiation_audit.py` to census ALPN and version hints across targets.
Copy `assets/checklists.md` into every delivery.
