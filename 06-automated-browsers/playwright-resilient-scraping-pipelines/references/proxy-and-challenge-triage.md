# Proxy and Challenge Triage

Use this reference when choosing proxy pools, hardening browser contexts, detecting challenges, or handling authenticated flows.

## Proxy pools

| Pool | Use when | Cautions |
|---|---|---|
| Direct (no proxy) | <500 pages, tolerant target, own IP is clean | Easiest to debug. Stop at first 429 wave. |
| Datacenter rotating | High volume, tolerant targets | Cheap, fast, easily fingerprinted. Quarantine subnets on 403 spikes. |
| Residential rotating | Sensitive or geo-locked targets | Expensive. Rotate per job or per N requests. Track cost per 1k pages. |
| Residential sticky | Logins, carts, multi-step flows | Pin IP per account/context for session lifetime. Never rotate mid-flow. |
| Mobile | Last resort for hardened targets | Highest cost. Require explicit approval and tight scope. |

Rules:

- One pool per sensitivity tier. Never mix login traffic with bulk crawl traffic on the same egress.
- Isolate by domain and account: `pool_key = f"{pool}:{domain}:{account}"`.
- Quarantine egress after 5 consecutive 403/challenge outcomes or p95 latency 3x baseline. Probe with a known-easy URL before return.
- Record `proxy_pool` and anonymized egress ID (hash, not raw IP) in every job log.

## Context hardening baseline

Apply in order. Stop when success rate meets SLA. Each layer adds maintenance cost.

1. Align identity: user-agent, viewport (e.g. 1366x768 or 1920x1080), locale, timezone, geolocation, `colorScheme`, `deviceScaleFactor`.
2. Remove automation tells: launch with `--disable-blink-features=AutomationControlled`, set `navigator.webdriver=false` via init script only for research targets where permitted, use headed or `headless=new` / xvfb for hardened targets.
3. Spoof sparingly: plugins, languages, permissions, WebGL vendor/renderer. Prefer `playwright-stealth`-style init scripts over hand-rolled patches.
4. Humanize behavior: randomized delays 800-2500ms between actions, curved mouse moves, typing with 40-120ms key variance, scroll-by-viewport with pauses.
5. Escalate only with evidence: Patchright/Rebrowser patched builds, Camoufox, or managed anti-detect browsers for Turnstile/DataDome/PerimeterX persistence. Document why baseline failed with artifact links.

Validate hardening against `https://bot.sannysoft.com` and `https://creepjs.github.io` on staging, never against production targets during tuning.

## Challenge detectors

Check after navigation and after extraction wait. Classify on first hit:

```python
CHALLENGE_MARKERS = [
    "just a moment", "verify you are human", "checking your browser",
    "captcha", "turnstile", "datadome", "perimeterx", "px-captcha",
    "request blocked", "access denied", "unusual traffic",
]
```

Signals:

- URL contains `challenge`, `captcha`, `turnstile`, `datadome`, `perimeterx`.
- Title/body matches any marker (case-insensitive).
- Status 403 with marker, or 429 with marker.
- Known selector present: `iframe[src*="turnstile"]`, `iframe[src*="captcha"]`, `#px-captcha`.

Log `challenge_class` as `turnstile`, `captcha-generic`, `datadome`, `perimeterx`, `rate-limit-page`, or `unknown-block`.

## Triage flow

1. First hit: close context, rotate egress (unless sticky login), back off domain with jitter, requeue job with `attempts+1`.
2. Second hit: recycle browser, double delay, capture HAR for analysis.
3. Third hit: park job to `review_queue.jsonl` with screenshot path, HAR path, HTML hash, and classifier evidence. Do not burn more egress.
4. Domain-wide spike: open circuit breaker, park new leases, notify owner with ban-wave summary.
5. Human review: reviewer decides solve-where-permitted, reduce scope, switch to API capture, or stop. Record decision and rationale.

Never auto-solve CAPTCHAs on targets where it violates Terms of Service or access controls. When in doubt, stop and recommend the official API.

## Authenticated flows

- Login once per account, save `storage_state.json`, reuse across workers.
- Pin each account to one sticky proxy + one context at a time.
- Refresh tokens proactively at 80% lifetime. On 401, re-login once, then park on repeat.
- Store secrets in env vars or a secret manager. Never commit `storage_state.json` or screenshots containing session tokens.
- Separate pools and throttles for authed vs anon traffic; authed bans cost accounts, not just IPs.
