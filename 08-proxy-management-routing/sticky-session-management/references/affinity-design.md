# Affinity Design

Affinity keys: account ID for logins, flow ID for anonymous multi-step; TTL = 2x p99 flow time, max 24h; scope documented (egress, UA, geo, jar). One map per environment; versioned; reviewed before changes.

Pin discipline: 1:1 account-to-egress always; no sharing, no borrowing; pinned egress excluded from rotation and rebalance; coherence check (egress + fingerprint tuple) at each step; drift aborts the flow safely.

Flow freeze: lock egress, UA, viewport, locale, timezone, jar for flow duration; queue config changes for between flows; checkout and payment flows get dedicated pins with extended TTLs.

Expiry: drain in-flight (no new steps, finish current), then release; re-auth path tested monthly; audit trail per pin lifecycle; leak tests (cross-account reads) in CI for shared code paths.
