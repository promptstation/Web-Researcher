# Signal Layers

Layer inventory: network covers IP reputation, ASN, geo, velocity; TLS covers versions, ciphers, extensions, ALPN, handshake shape; HTTP covers method semantics, header presence and order, cookie behavior, HTTP version; browser covers navigator, rendering, fonts, storage, permissions; behavior covers rate, paths, timing entropy, mouse and scroll for interactive sessions.

Audit practice: record your exact emissions with echo endpoints and handshake dumps; store user agent strings, header orders, TLS profiles, and rate shapes per client version. Diff after every dependency upgrade.

Honesty rules: user agents name the operator with contact URL; purpose pages explain scope; rates stay human-scale unless allowlisted higher; patterns avoid bursts and off-hours floods. Imitating browsers or users to mislead scoring is out of scope.

Allowlist packs: operator name, purpose, scope (hosts, paths, volume), rate, schedule, retention, abuse contact, and opt-out handling. Track request, response, renewal.
