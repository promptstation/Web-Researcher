# Nextjs Channels

Channel map: SSR HTML carries rendered text; __NEXT_DATA__ carries propsQuery, pageProps, and buildId; /_next/data/<buildId>/<route>.json mirrors props per route; server components stream flight data; underlying REST/GraphQL APIs feed all of the above. Prefer props, then data routes, then APIs, then HTML, then browsers.

URL rules: buildId from fresh HTML each run; locale prefix from detected locales; trailing-slash behavior from config; rewrites resolved by testing, not reading config. ISR pages carry revalidate hints; treat cached JSON as possibly stale and stamp fetch time.

Schema discipline: version every payload shape; validate types and required keys; dual-read during transitions; alert on unknown keys rather than silently dropping.

Fallback ladder: data route 404 -> refresh buildId; props renamed -> schema v+1; channel gone -> underlying API; API gated -> permission request, not evasion.
