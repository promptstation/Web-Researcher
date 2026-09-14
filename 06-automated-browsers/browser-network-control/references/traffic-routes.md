# Traffic Routes

Route order: log everything first; classify first-party data, first-party chrome, third-party functional, third-party tracking; block only the last class plus proven-dead first-party weight. Log every rule with rationale and date.

Mocking: capture real responses as fixtures; serve by URL plus method matching; version fixtures with API dates; contract-test mocks against live staging weekly. Test-only scope enforced by config.

HAR mining: filter to XHR/fetch, first-party hosts, JSON content; rank by response data value; extract params, paging, auth; verify live before documenting. Ignore beacons, pixels, and polling noise.

Dual channels: API primary with DOM fallback, or DOM primary with API cross-check; alert on sustained divergence; either channel alone must produce valid records.
