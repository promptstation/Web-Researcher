# Incident Signatures

Ban wave: success rate cliff, 403/challenge spike, often pool or subnet scoped, latency flat or falling. Respond: quarantine egress, halve concurrency, park domain, verify with canary before resuming.

Layout drift: validation and null rates move while HTTP stays green; field-level first. Respond: pin change time, fix extractor, bump version, backfill window, add field alerts.

Proxy decay: gradual success erosion with latency rise and mixed errors across domains sharing a pool. Respond: score and quarantine egress, shift pools, rehab off-peak.

Cost spike: cost per 1k jumps from retries, rotations, or premium-pool overflow. Respond: attribute by pool and domain, cap retries, fix the underlying failure class, restore budget.

Capacity fault: queue growth with flat worker output, timeouts rising. Respond: add workers or cut scope, never just raise timeouts. Verify recovery on all signals for one full cycle before closing.
