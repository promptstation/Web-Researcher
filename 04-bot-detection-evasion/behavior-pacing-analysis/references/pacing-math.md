# Pacing Math

Gap math: collect inter-request gaps per host; report median, p95, min, and zero-gap runs. Healthy polite crawlers show medians above 1s on small sites, no zero-gap runs over 5, and burst factors (peak-minute rate over mean) under 3. Metronome check: coefficient of variation under 0.2 means suspiciously regular.

Pacing design: base gap from politeness budget (small sites 2-5s, large APIs per quota); full jitter uniform(0, 2x base); startup ramp from 1 worker adding one per 30s; per-host concurrency 1-2 default. Honors Retry-After and crawl-delay above all local math.

Scheduling: learn target business hours per timezone; bulk at night, priority trickle by day; pause during incident windows and launches. Publish the calendar to stakeholders.

Verification: re-run identical analysis post-change; require burst factor under threshold for a full week before closing. Pacing proves politeness; permission still governs volume.
