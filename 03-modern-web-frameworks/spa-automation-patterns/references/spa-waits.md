# SPA Waits

Wait ladder: URL assertions for navigation; locator assertions for data; response waits scoped to exact URLs for APIs; route events where exposed. Sleeps are never the fix; longer auto-retry usually is. Global networkidle deadlocks on polling, streams, analytics, and sockets.

Selector ladder: getByRole plus accessible name first; test-id second for dynamic content; visible text third; CSS and XPath last with comments. Prefer user-facing semantics; verify strict uniqueness; scope lists to containers.

Hydration gates: wait for framework markers (__NEXT_DATA__ consumed, app mounted, loading spinners gone) plus content assertions before interacting. CI runners are slower; raise timeouts, not sleeps.

Flake taxonomy: timing (fix waits), selector (fix ladder), data (fix fixtures), environment (fix runners), product bug (file it). Every flake gets a trace, a class, and a fix.
