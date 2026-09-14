# Transport Signals

Phase map: DNS resolves names to addresses; TCP SYN/SYN-ACK/ACK opens the channel; TLS negotiates security inside it; HTTP runs on top; TTFB adds server thinking. Measure each separately or misattribute everything.

Healthy shapes: DNS under 100ms cached, single-digit ms on repeat; connect near RTT; TLS adds 1-2 RTT on 1.3, more on 1.2 full handshakes; TTFB stable per route. Warning shapes: connect multiples of RTT suggest loss; TLS seconds suggest interception or overload; TTFB variance suggests server or shaping.

Timeout rules: connect short and strict; read scaled to body; totals guarding runaway jobs. Retries only for idempotent fetches with jitter. Keep-alive and connection reuse cut setup tax on chatty hosts.

Elimination order: resolver, route, transport, TLS, HTTP, application. Prove each layer healthy before moving up; fix at the first failing layer.
