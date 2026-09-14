# Mitm Modes

Modes: regular proxies explicit client traffic; reverse fronts a fixed upstream; transparent intercepts routed flows withiptables or PF; upstream chains through another proxy; WireGuard and local redirect modes cover mobile and desktop apps. Pick the least invasive mode that observes the flow.

Addon anatomy: request handlers see and mutate outgoing flows; response handlers see and mutate replies; blocklists drop out-of-scope hosts first; logging writers emit JSONL with redacted headers. Review every mutation rule for scope before enabling.

CA facts: mitmproxy generates its own CA; install mitm.it certs on test devices only; verify fingerprints; remove or scope-limit after testing. Certificate-pinned apps will and should refuse interception; use debuggable builds.

Evidence: log URL, method, status, timing, and hashes by default; bodies only when the question needs them; redact Authorization, Cookie, tokens, and PII at write time; pack scope sheet with logs; delete on schedule.
