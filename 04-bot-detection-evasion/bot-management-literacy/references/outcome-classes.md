# Outcome Classes

Class guide: allow serves content with normal headers; managed challenge serves interactive verification with vendor markers; rate limit returns 429 or 403 with Retry-After or shaping headers; hard block serves denial with reference IDs; auth wall redirects to login; geo wall localizes or denies by region; capacity errors show 502/503 without vendor markers.

Reading rules: quote URL, status, title, body markers, and headers per verdict; never verdict from status alone; separate vendor markers from generic CDN text. New or generic pages default to backoff plus human review.

Routing: challenge -> backoff, park, human review where permitted; rate -> honor Retry-After, cut concurrency; hard block -> stop, seek permission or API; auth/geo -> respect scope; capacity -> retry with jitter later.

Logging: timestamp, URL pattern, class, evidence hash, action taken, approver for exceptions. Review weekly; catalogs rot fast.
