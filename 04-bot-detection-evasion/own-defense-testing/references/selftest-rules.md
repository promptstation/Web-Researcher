# Selftest Rules

Authorization: written scope naming hosts, paths, accounts, windows, and stop conditions; signed by the system owner; production only with explicit production clause. No letter, no probes.

Probe discipline: staging first; single-digit rates; business-hours windows; stop on errors, latency spikes, or user impact; log target, time, action, and result per probe. Treat staging data as production for handling.

Grading: severity from exploitability times business impact; UX harm counts as impact; every finding needs reproduction, evidence, and fix advice. Retest with identical probes; compare artifacts side by side.

Records: authorization, scope, logs, reports, retests, sign-off filed together with retention dates. Never reuse findings against other systems.
