# Queue Ladder

Ladder: file/SQLite queue under 10k jobs and one host; Redis (RQ/BullMQ) to ~500k with one team; RabbitMQ/Celery for routing, priorities, and multi-team; managed (SQS) when ops time costs more than fees. Graduate on measured pain, not ambition.

Lease rules: timeout 2-3x p99 job time; extend heartbeats for long jobs; redeliver on expiry; ack only after durable output write; idempotent handlers everywhere. Visibility math: redelivery rate under 1 percent is healthy.

Priorities: bands (urgent, fresh, bulk) with weights; age alerts per band; starvation test with bulk flood. DLQ: cap attempts (5-10), capture error plus payload, review daily, requeue only with fixed code.

Proofs: kill -9 a worker mid-batch and show zero loss and bounded duplicates; drain procedure tested quarterly; depth and age dashboards always on.
