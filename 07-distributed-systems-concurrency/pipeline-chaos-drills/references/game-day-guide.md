# Game Day Guide

Plan: one-page hypothesis (system survives X with loss under Y in under Z minutes); scope and blast radius with explicit excludes; observers with abort authority; comms channel; rollback ready. Sign-off required for shared staging, mandatory for prod.

Runbook: order injections latency -> errors -> kills -> partitions; one fault at a time first, combined later; record detection, mitigation, and full-recovery timestamps; reconcile inputs vs outputs vs DLQ after each. Abort on radius breach, customer impact, or observer call — no debate.

Postmortem: within 48h, blameless, timeline-first; five-whys on surprises; actions with owners and dates; publish to the team. Track action aging; re-drill the same fault after fixes ship.

Cadence: kill tests per release; game days quarterly; partition drills yearly; chaos suites in CI for unit-level faults. Maturity = smaller surprises per drill over time.
