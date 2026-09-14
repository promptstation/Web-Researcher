# Stream Transports

WebSocket: HTTP upgrade to 101, then bidirectional frames with opcodes (text, binary, close, ping, pong, continuation), client-masked payloads, 64-bit lengths for large messages. Close frames carry codes: 1000 clean, 1001 going away, 1006 abnormal (never sent, locally observed), 1011 server error, 4000-4999 application use. Ping every 20-30s under idle timeouts.

SSE: unidirectional text/event-stream over HTTP with automatic browser reconnect and Last-Event-ID resume; simpler ops, no binary, proxy-friendly. Chunked responses stream bodies without framing. Polling suits rare updates with caching. Choose by direction, scale, and existing infra.

Reconnect policy: exponential backoff with full jitter, cap near 60s, max attempts or indefinite with circuit breaking, resume tokens where supported, stagger across fleets, honor server backoff hints. Storm-test by killing the endpoint and watching reconnect shape.

Debug order: handshake transcript, then frames, then closes, then timing. Never tune reconnects before reading close codes.
