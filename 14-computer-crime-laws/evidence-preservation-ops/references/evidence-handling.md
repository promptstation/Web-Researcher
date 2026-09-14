# Evidence Handling

Collection: counsel-directed for litigation; runbook per source (logs, captures, DBs, endpoints); method notes (tool, version, command, operator, time); write to sealed write-once store; work on copies, never originals. Hash sha256 at capture; manifest sealed; verify on every receipt/move.

Custody: append-only log (artifact, from, to, when, why, hash-check); least-privilege access, all logged; sealed storage with integrity monitoring; no silent copies — every copy logged. Timestamp: system + trusted (RFC3161/nTP-logged) where admissibility matters.

Forensic captures: full page + headers + TLS cert + URL + time + method; screenshot + HTML + HAR; hash all; notes affidavit-ready (who captured, how, when, unaltered statement). Screenshots alone are weak — corroborate.

Holds: written notice, narrow scope, custodian acks tracked, deletes suspended scoped-only, monthly review, loud release. Spoliation (lose/alter after duty) sanctions cases and careers — when in doubt, preserve and ask counsel.
