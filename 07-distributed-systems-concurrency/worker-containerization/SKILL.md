---
name: worker-containerization
description: Containerize scraping workers reproducibly and roll out with canaries. Use when the user asks to dockerize Playwright workers; write docker-compose for scrapers; manage secrets in containers; canary-deploy workers; pin browser versions in Docker.
compatibility: Docker 24+ and compose v2; registry access; vault or env-file secrets.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Worker Containerization

Ship fleets that reproduce exactly. You pin every layer, compose whole stacks from one file, vault every secret, canary every update, and gate rollouts on health — with rollback always one command away.

Optimize simultaneously for:

- pinned images
- reproducible stacks
- vaulted secrets
- canaried updates
- gated rollouts

No latest tags and no baked-in secrets; every rollout reversible in minutes.

## Use Cases

### First container

Trigger: user says 'works on my machine' or 'dockerize this'

Steps:

1. Pin image fully
2. Compose the stack
3. Verify parity
4. Document ops

Result: Reproducible fleet.

### Safe update

Trigger: user says 'new browser version' or 'deploy workers'

Steps:

1. Build canary image
2. Run canary workers
3. Gate on metrics
4. Roll or back

Result: Verified rollout.

### Secret cleanup

Trigger: user says 'secrets in images' or 'audit containers'

Steps:

1. Scan images
2. Move to vault
3. Rotate exposed
4. Verify clean

Result: Secret-free images.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Dockerfile pinned
- Compose file
- Secret map
- Volume policy
- Health checks
- Canary procedure
- Rollback command
- Parity evidence

Never ship latest tags or baked-in secrets, and never roll out without canary and rollback.

## Phase 1 — Pin Images

Digest-pin base; version-pin browsers and libs.

Scan for secrets and CVEs.

Record SBOM-lite.

## Phase 2 — Compose Stacks

Generate starters with `scripts/compose_gen.py --workers 4`.

One file: queue, workers, storage, observability.

Parity-test vs bare metal.

## Phase 3 — Vault Secrets

Inject at runtime; never bake.

Least-privilege mounts.

Rotate on exposure.

## Phase 4 — Canary Rollouts

One canary worker first; smoke jobs green.

Metrics gate before fleet.

Rollback one command, drilled.

## Examples

### Example 1: Parity win

User says: "CI differs from laptops."

Actions:

1. Same image everywhere
2. Diffs vanished
3. Onboarding to minutes
4. Pinned forever

Result: Uniform fleet.

### Example 2: Bad browser caught

User says: "New Chromium broke selectors."

Actions:

1. Canary caught in smoke
2. Rolled back in 2 min
3. Pinned previous
4. Postmortem filed

Result: Safe failure.

## Troubleshooting

### Image bloat

Cause: Caches and dev deps in final

Fix:

1. Multi-stage builds
2. Slim bases
3. Prune caches
4. Measure layers

### Browser crashes in container

Cause: Missing shm or deps

Fix:

1. Size /dev/shm
2. Install OS deps
3. Cap contexts
4. Verify flags

### Canary blind

Cause: No smoke jobs or metrics gate

Fix:

1. Add smoke suite
2. Gate on RED
3. Auto-rollback
4. Verify drill

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Pin.
- Stack.
- Roll.

## Decision Heuristic

Before adding complexity, ask:

1. What outcome requires this step?
2. What evidence justifies it?
3. What happens when it fails?
4. What is the cheaper alternative?
5. What proves quality did not regress?
6. What must be logged for audit?
7. What is the rollback plan?

If the main justification is "more", prove the outcome needs it first.

## Anti-Patterns

Avoid latest tags; baked secrets; unlimited containers; canary-free rollouts; rollback-free deploys; parity-assumed fleets.

## Bundled References

Read `references/container-ops.md` when containerizing or rolling out workers.
Run `scripts/compose_gen.py` to scaffold a worker fleet compose file.
Copy `assets/checklists.md` into every delivery.
