# Origin Controls

Same-origin policy: scheme plus host plus port define origin. DOM access and storage reads require same origin; embedding allows display with restrictions; network reads across origins need CORS. Origin inheritance covers about:blank and data: quirks; test embeds explicitly.

CORS essentials: simple requests skip preflight; others send OPTIONS first. Response needs Access-Control-Allow-Origin matching the Origin (or * only without credentials), Allow-Methods and Allow-Headers covering the request, and Allow-Credentials true for cookies or Authorization. Vary: Origin when ACAO is dynamic.

CSP essentials: default-src fallback, script-src with nonces or hashes, style-src, img-src, connect-src for APIs, frame-src and frame-ancestors for embedding, worker-src for workers, object-src none, base-uri self, form-action scoped. Report with report-uri or report-to; roll out report-only first.

Isolation set: Cross-Origin-Opener-Policy, Cross-Origin-Embedder-Policy, and Cross-Origin-Resource-Policy combine for cross-origin isolation; X-Content-Type-Options nosniff stops MIME sniffing; frame-ancestors replaces X-Frame-Options.
