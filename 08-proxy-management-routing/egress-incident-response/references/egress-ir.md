# Egress IR

Severity: SEV-1 (all egress down, active leak/breach — page all, 15-min cadence); SEV-2 (major pool degraded, single-provider out — page on-call, 30-min); SEV-3 (elevated bans, minor drift — ticket, daily). Score from success drop, ban rate, scope, and compliance risk.

Roles: IC (decides), comms (updates), ops (acts), scribe (logs). Playbooks: ban wave (quarantine, slow, root-cause, canary); provider out (confirm, failover, ETA, return); leak (revoke, rotate, purge, disclose); breach (pause, preserve, legal, remediate).

Recovery ladders: verify fix in staging, canary 5 percent, graduate 25/100 with clean windows, full health check, close with report. Comms: acknowledge in 15 min, updates per cadence, all-clear with summary. Never speculate causes externally.

Learning: postmortem 48h blameless; five-whys; actions owned and dated; runbook updated same week; re-drill the class within a quarter. Track MTTD/MTTR trends; celebrate clean responses.
