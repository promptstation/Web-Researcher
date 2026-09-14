# Good Citizen

Budgets: requests/day + bytes/day + est. server cost per target; small sites get tiny budgets (dozens/day); approve overages explicitly with operator contact preferred. Start 1 req/2-5s per host; raise only on clean signals with caps.

Adaptation: slow 2x on p95 doubling, 429s, or 5xx; pause on 503 waves or webmaster contact; honor Retry-After exactly; backoff with jitter; never crawl through distress. Off-peak per target timezone; maintenance windows respected; conditional GET + sitemaps + caches minimize load.

Identity: UA names operator + purpose + contact URL; abuse@ monitored with hours-SLA; public crawler page (who, why, rates, opt-out). Complaints: pause target instantly, acknowledge same-day, fix root, compensate considerationately, resume only agreed.

Reports: quarterly footprint (targets, requests, bytes, complaints, pauses) published; zero-complaint goal tracked; postmortem every complaint into prevention. Politeness is competitive advantage: access preserved, reputation earned.
