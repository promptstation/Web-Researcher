# Wait Layers

Layer map: navigation -> URL assertion; content -> locator assertion with auto-retry; API-backed UI -> scoped response wait plus assertion; animations -> stable-state assertion, never fixed delays. Timeouts: action 5-15s, assertion 5-30s, navigation 30s, scaled 1.5x in CI.

Network scoping: wait for exact URL patterns with method filters; never global networkidle on polling, streams, or analytics pages; cap response waits and fall through to assertions. Deadlock check: if the wait can never settle by design, scope narrower.

Flake classes: timing (fix waits), selector (fix ladder), data (fix fixtures), environment (fix runners), product (file bug). Every flake: trace, class, fix, repeat proof. Quarantine max 7 days with owner.

Sleep hunt: grep for sleep/waitForTimeout monthly; each needs replacement plus proof; CI fails on new sleeps via lint.
