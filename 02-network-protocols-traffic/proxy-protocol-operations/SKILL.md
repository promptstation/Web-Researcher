---
name: proxy-protocol-operations
description: Verify HTTP and SOCKS chains hop by hop and select leak-free egress. Use when the user asks to explain SOCKS5 versus HTTP proxy; verify a proxy chain works; find DNS or header leaks; choose egress pools for scraping; test proxy auth safely.
compatibility: Any OS with Python 3.10+; test proxies and echo endpoints; no fleet tooling required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# Proxy Protocol Operations

Make every egress byte accountable. You map chains, verify each hop, sweep for leaks, and match pools to sensitivity so traffic exits where intended with nothing escaping around the proxy.

Optimize simultaneously for:

- mapped chains
- verified hops
- closed leaks
- matched pools
- scored egress

Do not route sensitive or authed traffic through unverified egress, and never log proxy credentials.

## Use Cases

### New pool onboarding

Trigger: user says 'test this proxy provider' or 'onboard new egress'

Steps:

1. Verify handshake and auth per protocol
2. Echo-test exit IP and geography
3. Sweep DNS, SNI, and header leaks
4. Score and admit or reject

Result: Evidence-backed admit decision.

### Leak hunt

Trigger: user says 'real IP leaked' or 'DNS bypasses proxy'

Steps:

1. Reproduce with echo and DNS endpoints
2. Pin the leaking layer
3. Fix client or chain config
4. Re-verify clean

Result: Closed leak with proof.

### Chain debug

Trigger: user says 'chain fails at second hop' or 'CONNECT rejected'

Steps:

1. Test each hop in isolation
2. Read status and auth responses
3. Fix creds, TLS, or routing per hop
4. Verify end to end

Result: Working chain, hop receipts.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Chain map: hops, protocols, auth, DNS path
- Hop receipts: status per hop
- Echo evidence: exit IP and geo
- Leak sweep: DNS, SNI, headers, WebRTC
- Credential handling: storage and rotation
- Pool matrix: sensitivity to pool mapping
- Health scores with thresholds
- Admit or quarantine verdict

Never trust egress without echo evidence, and never pass credentials in URLs or logs.

## Phase 1 — Map the Chain

Draw hops with protocol, auth method, TLS termination, and DNS resolution point each.

Run `scripts/proxy_chain_check.py --proxy <url> --target <https-url>` for handshake plus echo evidence.

Record exit IP, ASN, and geography from echo.

## Phase 2 — Verify Hop by Hop

Test each hop alone before testing the chain.

Read CONNECT statuses and SOCKS replies literally.

Confirm TLS reaches the target unbroken or terminates where intended.

## Phase 3 — Sweep Leaks

Check DNS path with resolver-identity endpoints.

Inspect forwarded headers and SNI visibility per hop.

Test WebRTC and fallback paths in browsers where relevant.

## Phase 4 — Select and Score

Map traffic classes to pools by sensitivity and cost.

Score latency, success, and leak status per egress.

Quarantine below threshold with cause and retest date.

## Examples

### Example 1: Provider shootout

User says: "Pick between two proxy vendors."

Actions:

1. Echo-tested 50 exits each
2. One leaked DNS on UDP
3. Scored success, latency, leaks
4. Admitted one, rejected one with cause

Result: Data-backed vendor pick.

### Example 2: Mystery direct connection

User says: "Some traffic bypasses the proxy."

Actions:

1. Found UDP DNS going direct
2. Forced remote resolution on the chain
3. Re-verified zero direct flows
4. Added leak check to onboarding

Result: Closed bypass, regression check added.

## Troubleshooting

### 407 despite correct password

Cause: Auth scheme mismatch or credential encoding

Fix:

1. Read Proxy-Authenticate schemes offered
2. Match Basic vs Digest handling
3. Check special-character encoding
4. Rotate creds if reused elsewhere

### SOCKS handshake hangs

Cause: Version or auth-method mismatch

Fix:

1. Offer methods the server lists
2. Confirm TCP reachability first
3. Read reply codes literally
4. Test with minimal client

### Geo wrong at exit

Cause: Stale GeoIP or anycast exit

Fix:

1. Confirm with two geo endpoints
2. Check ASN and rDNS
3. Request exit correction or swap
4. Pin sensitive geos explicitly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Verify.
- Leaks.

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

Avoid unverified egress for authed traffic; credentials in URLs or logs; local DNS with remote proxies; forwarded internal headers; single-hop tests for chains; price-only pool picks.

## Bundled References

Read `references/proxy-mechanics.md` when mapping chains or debugging handshakes.
Run `scripts/proxy_chain_check.py` to verify handshake, auth, and exit identity.
Copy `assets/checklists.md` into every delivery.
