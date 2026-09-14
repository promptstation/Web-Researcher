# Challenge Playbook

Detection: status plus markers plus timing from responses you already hold; no extra probes to classify. Thresholds: challenge rate over 10 percent pages, over 30 percent trips breaker; single-job third strike parks the job.

Parking: job id, URL pattern, class, evidence path, timestamps, owner. Bounded queues with aging; parks never auto-retry. Review only where terms permit manual access; log solve/skip/stop per item with rationale.

Resume: one canary per domain, then 1-5-25-100 percent stages on green windows of 10 clean minutes; abort to park on any re-trip. Storm guard: global lease cap during any open breaker.

Forbidden: automated CAPTCHA solving services against terms, credential stuffing past auth walls, IP rotation to defeat blocks. Back off, seek access, or stop.
