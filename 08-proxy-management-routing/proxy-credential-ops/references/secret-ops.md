# Secret Ops

Inventory: every proxy user, password, token, allowlist entry with scope, owner, and expiry. Vault: one manager, least-privilege paths, audit logging, break-glass documented. Injection: env or socket at runtime; never disk, never logs, never images.

Rotation: cadence 90 days or on trigger; dual-validity window 24-48h; rolling cutover with auth-failure monitoring; revoke old only at zero failures for 24h. Emergency: revoke first, rotate all, purge exposures, postmortem.

Allowlists: prefer over passwords for static egress; /32 entries with owner and review date; automate provider updates; quarterly prune. Credentials where dynamic: long random, unique per scope, rotated on schedule.

Audits: scan code, images, tickets, and artifacts in CI for secret patterns; drill emergency rotation yearly; review vault access quarterly; log every rotation with before/after verification.
