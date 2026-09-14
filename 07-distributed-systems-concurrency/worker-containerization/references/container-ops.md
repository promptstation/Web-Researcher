# Container Ops

Images: digest-pinned base (bookworm-slim class); pinned browser plus deps; multi-stage (build then runtime); non-root user; HEALTHCHECK per worker; no secrets, no caches, no dev tools in final. Rebuild weekly for patches.

Compose: services for queue, workers (scaled), storage, and optional exporter; resource limits per worker (cpus, mem); restart policies; named volumes for data; env files git-ignored with vault source. One command brings the fleet.

Rollouts: build tagged image; canary one worker with smoke suite; gate on error rate and p95 for 30 min; fleet rollout in halves; auto-rollback on gate breach; rollback is previous tag redeploy. Drill quarterly.

Browser specifics: /dev/shm sized 1-2GB; --no-sandbox only with user namespaces understood; cap contexts per container; recycle browsers on schedule; log browser versions per run.
