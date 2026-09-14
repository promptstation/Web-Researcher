# Fleet Math

Sizing: contexts_per_host = floor((RAM * (1 - headroom) - browser_overhead) / rss_per_context). Measure RSS on real targets over 100+ jobs; heavy pages 300-600MB per context; recycle browsers every 50-200 jobs. CPU: one worker per 2 cores for browser-heavy loads.

Queues: file or SQLite under 10k jobs; Redis/RQ to 500k; RabbitMQ/Celery beyond. Leases 5-15 min with redelivery; dead-letter after max attempts; shard by domain class with independent throttles.

Guards: pause leases above 80 percent RSS; cap contexts per worker; cap file handles; shed low priority first. Backpressure flows target -> queue -> workers -> producers; never buffer unbounded.

Ramps: 1x, 2x, 5x, 10x stages with 30 clean minutes between; stop at first ceiling signal; budget at 70 percent of knee. Load-test quarterly and after target changes.
