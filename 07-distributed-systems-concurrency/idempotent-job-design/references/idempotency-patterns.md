# Idempotency Patterns

Keys: canonical URL + extractor version + scope, hashed; stable across retries and resumes; version bump reprocesses deliberately. Never include timestamps, randoms, or volatile DOM in keys.

Ledgers: seen-key store with atomic check-and-set; SQLite for single host, Redis SETNX or Postgres upsert for fleets; TTL by business retention; reconcile against outputs nightly.

Writes: upsert on keys; conditional puts with etags where supported; write output before ack; outbox pattern for side effects (insert intent in same transaction, relay async, dedupe downstream).

Proof: kill -9 workers at 30/60/90 percent; replay to completion; assert inputs == outputs + DLQ; residual dup rate under 0.01 percent or explained. Re-run proof after every storage change.
