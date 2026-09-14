# Geo Testing

Tiers: country for pricing/currency QA; region/state for compliance messaging; city only for maps/logistics features. Justify each level; minimize by default. Targets must be owned or permitted; scope docs name every URL pattern.

Verification: exit IP via echo service; geo via two independent DBs/APIs; ASN via whois; rDNS via PTR; content locale via page signals. All five logged per egress per week minimum; per session for sensitive flows.

Drift: alert on country change, ASN change, or content-locale mismatch; quarantine immediately; canary before return. Provider SLA: 99 percent targeting accuracy or credits; escalate with dual-source evidence.

Boundaries: localization QA and compliance verification are legitimate; bypassing geo-blocks, licensing windows, or sanctions is prohibited. When in doubt, legal review before targeting.
