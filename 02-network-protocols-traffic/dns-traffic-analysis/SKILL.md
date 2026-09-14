---
name: dns-traffic-analysis
description: Trace DNS resolution, audit records and TTLs, and fix resolver faults. Use when the user asks to trace why a domain fails to resolve; audit DNS records and TTLs; compare DNS resolvers; verify DNS-over-HTTPS behavior; fix fleet-wide resolution faults.
compatibility: Any OS with Python 3.10+; outbound UDP/53 or HTTPS for DoH checks; no root required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# DNS Traffic Analysis

Make name resolution boring and reliable. You trace delegations, audit records and TTLs, compare resolvers with data, and pin faults to resolver, delegation, or path with reproducible queries.

Optimize simultaneously for:

- traced delegations
- audited records
- compared resolvers
- pinned faults
- fleet policy

Do not change resolvers or TTLs without query transcripts showing current behavior.

## Use Cases

### Resolution failure

Trigger: user says 'domain does not resolve' or 'DNS flaky on workers'

Steps:

1. Query authoritative directly, then recursive, then stub
2. Pin the failing layer
3. Fix delegation, resolver, or path
4. Verify fleet-wide

Result: Layer-pinned DNS fix.

### Record audit

Trigger: user says 'audit our DNS' or 'migration checklist'

Steps:

1. Inventory records and TTLs
2. Flag chains, glue, and gaps
3. Lower TTLs before cutover
4. Verify propagation after

Result: Safe migration with proof.

### Resolver policy

Trigger: user says 'pick fleet resolvers' or 'DoH or classic'

Steps:

1. Benchmark candidates on latency and correctness
2. Test DoH endpoints
3. Publish primary plus fallback
4. Monitor resolver errors

Result: Evidence-backed resolver policy.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Query transcripts per layer
- Delegation diagram
- Record inventory with TTLs
- Resolver comparison table
- DoH verification where used
- Fault verdict with layer
- Policy: primary plus fallback
- Re-query commands

Never blame targets for resolver faults, and never cut over DNS without TTL planning and propagation checks.

## Phase 1 — Query Layer by Layer

Run `scripts/dns_audit.py --domain <d> --resolver 1.1.1.1` and save transcripts.

Query authoritative, recursive, and local stub separately.

Record answers, TTLs, and response times per layer.

## Phase 2 — Audit Records

Inventory A, AAAA, CNAME, NS, MX, TXT for the domain.

Flag long CNAME chains, missing AAAA, and stale glue.

Check TTLs against change plans.

## Phase 3 — Compare Resolvers

Benchmark latency and correctness across candidates.

Verify DoH endpoints with HTTPS queries.

Score privacy, speed, and reliability together.

## Phase 4 — Fix and Verify

Fix at the pinned layer only.

Verify from multiple networks and resolvers.

Publish policy and monitor error rates.

## Examples

### Example 1: Fleet DNS stall

User says: "Workers hang on DNS every morning."

Actions:

1. Transcripts showed one resolver timing out
2. Secondary healthy; primary overloaded
3. Swapped order plus added DoH fallback
4. Stalls gone, policy published

Result: Resolver fix from transcripts.

### Example 2: Migration safety

User says: "Moving origins next week."

Actions:

1. Lowered TTLs 48h ahead
2. Inventoried every record
3. Cut over and verified propagation
4. Restored TTLs after settle

Result: Clean cutover, no stale fleet.

## Troubleshooting

### SERVFAIL on one resolver only

Cause: DNSSEC validation or lame delegation visible there

Fix:

1. Query authoritative directly
2. Check DS and DNSKEY chains
3. Compare validating vs non-validating
4. Fix delegation or validation path

### Stale answers after change

Cause: Long TTLs cached at recursive or app level

Fix:

1. Confirm TTL on authoritative
2. Wait out or flush documented caches
3. Fix app-level caching next
4. Plan TTL windows for future cuts

### DoH works, classic fails

Cause: Port 53 blocked or hijacked on path

Fix:

1. Prove with parallel queries
2. Route via DoH where policy allows
3. Document the path interference
4. Monitor classic restoration

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Query.
- Audit.
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

Avoid single-resolver verdicts; cutovers without TTL windows; app caches forgotten; DoH assumed without endpoint checks; lame delegations patched with retries; fleet resolvers unmonitored.

## Bundled References

Read `references/dns-layers.md` when tracing queries or planning changes.
Run `scripts/dns_audit.py` to query records across resolvers with transcripts.
Copy `assets/checklists.md` into every delivery.
