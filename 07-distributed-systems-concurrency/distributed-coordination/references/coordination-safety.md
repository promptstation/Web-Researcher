# Coordination Safety

Locks: acquire with TTL, work under TTL with heartbeats, release explicitly, fence guarded writes with monotonic tokens so stale holders cannot corrupt. Single host: flock; multi-host: Redis SET NX PX or Postgres pg_advisory with session discipline.

Leaders: lease 10-30s, heartbeat at 1/3 TTL, failover declared after missed 2x, new leader fenced-in before acting. Schedulers run only on leader; ledger slots (date+job) to survive failover without double-run.

Sharding: hash(canonical key) mod N with stable assignment; document map; rebalance on N change with dual-read windows; verify full coverage and zero overlap. Prefer sharding over locking for throughput.

Safety: fail closed on lease doubt; NTP everywhere with drift alerts; partition drills yearly; split-brain analysis per system with fencing proof.
