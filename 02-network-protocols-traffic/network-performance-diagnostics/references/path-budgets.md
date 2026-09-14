# Path Budgets

Measurement: sample 30+ per path at production hours; report p50/p95 for RTT and TTFB plus loss hints from retries and timeouts. Compare across egress, region, and hour before concluding. Single samples convict no one.

Bandwidth honesty: estimate from paced known-size transfers with margins; sustained rates beat peaks; server pacing and congestion windows cap single flows; parallelism multiplies only to the knee. Never flood shared or target paths for measurement.

Ceiling order: client limits, egress contention, transit loss, server capacity, shaping policy. Ladder one variable at a time and watch latency plus errors together. The tighter of path budget and politeness budget always wins.

Shaping signatures: time-of-day cliffs, size-dependent slowdowns, protocol-specific gaps. Adapt with scheduling, chunking, and pacing; document patterns for planning.
