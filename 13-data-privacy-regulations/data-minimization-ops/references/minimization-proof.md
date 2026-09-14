# Minimization Proof

Reviews: per flow, per field: purpose link, necessity (why less fails), sensitivity tier, decision (keep/drop/mask/aggregate), owner, date. 100 percent decided; undecided = dropped. Re-review on purpose change or yearly.

Guards: allowlisted fields in extractors (deny rest); PII detectors at ingest with quarantine; CI breaks on new PII-typed fields without review; production scans verify. Aggregation: k-anonymity-style floors, tested re-identification, residual risk stated; pseudonymization ≠ anonymization.

Defaults: TTL on every store; auto-delete jobs; holds dated with owners and monthly review; backups aligned. Metrics: PII fields per flow, PII bytes per store, hold count/age — all trending down. Audit yearly with evidence pack.

Anonymization honesty: test singling-out/linkability/inference; expert review for sensitive; state residual risk; treat as personal until proven otherwise. Minimization is a posture, not a project.
