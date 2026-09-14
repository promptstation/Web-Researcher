# Storage Tiers

Tier guide: cookies travel on every request, cap near 4KB each, and suit session IDs with Secure plus HttpOnly plus SameSite; localStorage persists per origin near 5-10MB and suits preferences, never secrets; sessionStorage lasts one tab lifetime and suits wizard state; IndexedDB holds structured offline data with versioned schemas; Cache Storage holds request/response pairs for service workers.

Lifetimes: session cookies die with the session unless Max-Age set; persistent cookies honor Max-Age or Expires; localStorage and IndexedDB persist until cleared or evicted under pressure; service-worker caches persist by version until deleted. Partitioned third-party storage isolates embedded origins per top site.

Quota: navigator.storage.estimate reports usage and quota; persistence via navigator.storage.persist reduces eviction risk. Evict by cache version and LRU; never wipe session cookies as a cache fix.

Automation: export session cookies plus localStorage essentials only; keep one state file per account; redact values in logs; refresh before expiry; test restore in an isolated context before fleet rollout.
