# Proxy Types

Types: datacenter (cheap, fast, low trust — APIs, bulk, tolerant targets); ISP/static residential (mid cost, stable, higher trust — sessions, accounts); residential rotating (expensive, high trust, variable — sensitive geo); mobile (priciest, highest trust — app-like flows). Match type to target class; never residential-by-default.

Protocols: HTTP(S) simplest; SOCKS5 for non-HTTP and UDP-ish needs; auth via user:pass (rotate) or IP allowlist (prefer); sticky sessions by TTL or session ID. Client must support your auth plus rotation mode.

Trials: identical URL sets, volumes, schedules; blind provider labels; 1-2 weeks; metrics success rate, p95 latency, IP churn, ban rate, support responsiveness. Score weighted: success 35, cost 25, stability 15, ethics 15, support 10. Adjust weights per use.

Ethics: require written consent chain for residential/mobile supply; reject botnetted or opaque sourcing; document chain; re-vet yearly. Exit: second source warm at 10 percent; failover tested; contract exit under 30 days.
