# HTTP Versions

HTTP/1.1: one outstanding request per connection without pipelining; keep-alive reuses connections; browsers open around six per origin. Sharding multiplied connections historically. HTTP/2: binary framing, multiplexed streams over one TCP connection, header compression, server push now deprecated, stream priorities as hints. Head-of-line blocking survives at TCP loss level. HTTP/3: QUIC over UDP with per-stream loss isolation, 0-1 RTT handshakes, connection migration across networks. Alt-Svc advertises availability; ALPN confirms use.

Client rules: confirm version per origin before tuning; one connection per HTTP/2 origin usually suffices; ladder HTTP/1.1 connections conservatively; prioritize hero streams; respect server settings for max concurrent streams. Count 429s and latency together; either can mark the knee.

Fallback truths: middleboxes may strip ALPN or block UDP 443; servers may advertise h3 without capacity; proxies often terminate at h2. Keep graceful fallback and measure which version actually served each request class.
