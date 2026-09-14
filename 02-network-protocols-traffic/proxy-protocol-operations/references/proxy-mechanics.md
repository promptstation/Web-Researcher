# Proxy Mechanics

HTTP forward: client sends absolute-URI requests; proxy fetches and returns. CONNECT: client asks for a TCP tunnel (CONNECT host:port), then TLS runs end to end inside; 200 means tunnel open, 407 means authenticate. SOCKS5: greeting with auth methods, method selection, auth if any, then CONNECT/BIND/UDP-ASSOCIATE requests with replies; supports remote DNS when the client sends domain names. SOCKS4: simpler, IPv4 only, no auth standard.

DNS rules: send domain names through SOCKS5 for remote resolution; verify HTTP proxies do not leak via local resolvers; test with resolver-identity endpoints. Header rules: strip or set X-Forwarded-For deliberately; never forward internal headers to targets; inspect Via and Forwarded additions.

Chain order: client to hop1 to hop2 to target, each hop needing its own auth and TLS decision. Test inside-out: target direct, then each added hop. Log hop receipts without credentials.

Selection: direct for owned tolerant hosts; datacenter for volume; residential for sensitive or geo-locked; sticky for sessions. Price per gigabyte against success rate, not sticker price.
