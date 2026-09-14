# API Discovery

Mining: fetch page HTML plus top JS chunks with byte caps; regex for /api/, /graphql, fetch(, axios., open(, and URL literals; rank by co-occurrence with entity names and paging params (cursor, page, limit, offset). Verify live before documenting.

Well-known paths: /openapi.json, /swagger.json, /api/docs, /.well-known/*, /graphql with GET query={__typename} only where permitted. Developer portals and status pages often link canonical docs; prefer them over reverse engineering.

Contracts: method, path, auth (none, key, cookie, OAuth), required headers, params with types, paging mechanics, error shapes, rate limits with headers (RateLimit-*, Retry-After). Stamp discovery date and response samples.

Ladder: official documented API first; permitted undocumented endpoint second with care; DOM scraping last. Request access in writing before leaning on undocumented endpoints at scale.
