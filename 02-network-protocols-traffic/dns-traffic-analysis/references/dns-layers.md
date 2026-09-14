# DNS Layers

Resolution path: stub asks recursive; recursive walks root to TLD to authoritative with referrals; answers cache by TTL at each layer plus OS and app caches. Query each layer directly to pin faults: authoritative for truth, recursive for policy, stub for local breakage.

Record reading: A and AAAA give addresses; CNAME aliases with chain cost; NS plus glue delegate; TXT carries verification and policy; MX routes mail. Long chains slow and fragilize; missing AAAA breaks IPv6-first clients; stale glue misroutes.

Encrypted DNS: DoH carries queries in HTTPS to named endpoints; DoT uses TLS on 853. Both hide queries from path snoopers but centralize trust in the endpoint. Debug with endpoint status pages plus parallel classic queries.

Change protocol: lower TTLs well before cutover, verify propagation from multiple resolvers and networks, then restore. Never assume global visibility in minutes.
