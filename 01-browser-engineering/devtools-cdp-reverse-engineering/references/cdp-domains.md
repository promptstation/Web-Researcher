# CDP Domain Map

Discovery: launch with --remote-debugging-port=9222 and a dedicated profile, then GET /json/version and /json/list over HTTP to enumerate targets. Attach over WebSocket per target for commands and events. Keep the port on localhost only.

Core domains: Target for target lifecycle; Page for navigation, lifecycle events, and screenshots; Network plus Fetch for observation and interception; Runtime for evaluation; DOM and CSS for structure and style; Storage for cookies and caches; Performance for metrics; Log for console and violations. Fetch.authChallengeResponse and Fetch.fulfillRequest power overrides.

Session hygiene: one session per target, enable only needed domains, remove listeners on teardown, close pages and contexts explicitly. Log every command that mutates state.

UI-to-protocol bridge: Elements maps to DOM/CSS, Network to Network/Fetch, Sources breakpoints to Debugger, Performance to Profiler/Tracing, Application to Storage/CacheStorage/IndexedDB. Prove in UI first, then automate the proven path.
