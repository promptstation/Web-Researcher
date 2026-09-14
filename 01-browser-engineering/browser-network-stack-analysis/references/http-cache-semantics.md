# HTTP Cache Semantics

Directives: immutable means never revalidate during max-age; no-cache means store but revalidate; no-store means never store; private restricts to single-user caches; must-revalidate forbids stale use after expiry. HTML entry points usually no-cache; hashed static assets immutable with long max-age; APIs private or no-store unless explicitly cacheable.

Validators: ETag plus If-None-Match and Last-Modified plus If-Modified-Since enable 304 revalidation. Weak etags suit byte-varying content; strong etags suit exact bytes. Vary keys cache by header; normalize or avoid Vary on high-cardinality headers.

Protocol notes: HTTP/2 multiplexes streams over one TCP connection with prioritization; HTTP/3 runs QUIC over UDP with per-stream loss isolation and faster handshakes. ALPN negotiates the version during TLS. Sharding across many origins defeats multiplexing; consolidate or preconnect.

Security baseline: TLS 1.2 minimum, 1.3 preferred; HSTS with long max-age and includeSubDomains once HTTPS is total; upgrade-insecure-requests during migration; no mixed active content.
