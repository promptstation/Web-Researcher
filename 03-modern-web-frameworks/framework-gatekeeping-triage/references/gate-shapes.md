# Gate Shapes

Shape guide: middleware shows redirect chains with edge headers (x-middleware, x-vercel, cf-mitigated) and verification cookies; signed URLs carry exp, sig, token, or hash params with short lives; token walls 401/403 on data routes while HTML stays public; rate shapes throttle by IP with Retry-After; consent/geo walls localize content, not block identity.

Triage order: capture chain, read headers, compare authed versus anon, compare regions, then classify. Gating evidence beats rendering theories when redirects precede content.

Response ladder: stop pressure, map public surfaces, map official APIs, draft permission with purpose/scope/rate/retention, define reduced scope, set review date. Self-authorization is never an option.

Probe budget: single-digit requests, seconds apart, full logging. Gates are answers, not puzzles.
