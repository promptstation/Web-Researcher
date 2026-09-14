---
name: browser-network-stack-analysis
description: Audit DNS, TLS, HTTP versions, and caching to cut connection cost and fix freshness bugs. Use when the user asks to audit TLS and certificate health; explain slow connection setup; fix redirect chains and HSTS; tune cache headers and revalidation; prove HTTP/2 or HTTP/3 behavior.
compatibility: Any OS with Python 3.10+ and outbound HTTPS; browser DevTools for waterfall confirmation; no special libraries.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Browser Network Stack Analysis

Make every connection explainable. You capture handshakes, map redirect and protocol behavior, audit cache semantics, and convert findings into header and origin fixes with timing proof.

Optimize simultaneously for:

- attributed connection cost
- verified protocol behavior
- correct cache semantics
- shorter redirect paths
- hardened TLS posture

Do not recommend protocol or cache changes without handshake output and header evidence from the affected origin.

## Use Cases

### Slow first fetch

Trigger: user says 'TTFB is high' or 'first request takes seconds'

Steps:

1. Measure DNS, connect, TLS, and wait splits
2. Map redirects and origin count
3. Audit handshake and protocol version
4. Fix the dominant phase with proof

Result: Named phase fix with split timings.

### Cache correctness

Trigger: user says 'users see stale JS' or 'APIs cache wrong'

Steps:

1. Audit headers per asset class
2. Separate immutable assets from revalidated HTML/APIs
3. Fix validators and Vary usage
4. Verify with conditional requests

Result: Freshness rules that behave as documented.

### Scraper connection triage

Trigger: user says 'TLS errors in automation' or 'proxy breaks HTTPS'

Steps:

1. Capture handshake through direct and proxy paths
2. Compare ALPN, SNI, and cert chains
3. Pin the diverging layer
4. Prescribe proxy or client fix

Result: Layer-pinned TLS diagnosis.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Handshake record: TLS version, cipher, ALPN, cert expiry
- Redirect map: hops, codes, and time per hop
- Protocol verdict: negotiated version with evidence
- Header table: cache directives per asset class
- HSTS and mixed-content review
- Fix list: header, value, scope, and rationale
- Before/after splits for the dominant phase
- Re-check steps with exact commands

Never prescribe cache or TLS changes without captured handshakes and current header dumps.

## Phase 1 — Capture Handshakes

Run `scripts/tls_http_audit.py --url <origin> --check-h2` and save the JSON.

Record TLS version, cipher, ALPN protocol, certificate subject, issuer, and expiry.

Flag TLS below 1.2, weak ciphers, expiring certs, and missing ALPN as findings.

## Phase 2 — Map Redirects and Origins

Follow the full redirect chain with per-hop codes and timings.

Count distinct origins and connection setups on the critical path.

Propose consolidation or preconnect for origins that repeat across pages.

## Phase 3 — Audit Cache Semantics

Dump response headers for HTML, JS, CSS, fonts, images, and one API route.

Classify each as immutable, revalidated, or private; fix mismatches with explicit directives.

Verify validators with conditional requests and confirm 304 behavior.

## Phase 4 — Fix and Re-measure

Apply header and redirect fixes in one reviewable change set.

Re-capture splits and confirm the dominant phase improved.

Leave the audit command and expected values in the runbook.

## Examples

### Example 1: Three-hop redirect tax

User says: "Homepage redirects feel slow."

Actions:

1. Mapped http to https to www: 3 hops, 600ms
2. Collapsed to one hop at the edge
3. Added HSTS with preload-ready max-age
4. Re-measured: redirect tax under 120ms

Result: Faster entry with hardened upgrades.

### Example 2: Stale bundle complaints

User says: "Users stuck on old JS after deploys."

Actions:

1. Found hashed bundles without immutable plus HTML cached too long
2. Set immutable on hashed assets, no-cache on HTML
3. Verified with conditional fetches
4. Complaints stopped on next deploy

Result: Correct freshness by asset class.

## Troubleshooting

### H2 shows no multiplexing win

Cause: Origin sharding, uncoalesced connections, or server without priorities

Fix:

1. Confirm ALPN h2 on each origin
2. Consolidate shards or enable connection coalescence
3. Check server push/priority settings
4. Re-measure with a multiplexed waterfall

### 304 storm on every navigation

Cause: Validators forced on non-cacheable or private responses

Fix:

1. Scope validators to cacheable classes
2. Add explicit max-age where safe
3. Fix Vary normalization
4. Confirm storm gone in waterfall

### TLS failure only through proxy

Cause: SNI alteration, cert replacement, or ALPN stripping by egress

Fix:

1. Diff direct vs proxy handshakes field by field
2. Check proxy CA trust and ALPN passthrough
3. Pin the diverging field before changing clients
4. Rotate or reconfigure the egress

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Handshake.
- Path.
- Cache.

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

Avoid cache advice without header dumps; immutable on unhashed assets; no-store used as a freshness strategy; redirect fixes without hop timings; protocol claims without ALPN evidence; proxy TLS blame before handshake diffs.

## Bundled References

Read `references/http-cache-semantics.md` when writing cache directives or diagnosing freshness.
Run `scripts/tls_http_audit.py` to capture handshake, redirect, and header evidence.
Copy `assets/checklists.md` into every delivery.
