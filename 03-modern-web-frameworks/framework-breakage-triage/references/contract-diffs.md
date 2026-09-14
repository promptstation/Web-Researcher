# Contract Diffs

Snapshot content: URL, fetch time, buildId, chunk list, payload keys, data-region HTML (normalized), record sample with IDs. Store per template per day minimum; git works for small estates.

Normalization: strip timestamps, nonces, ad slots, and session tokens before diffing. Scope diffs to data regions; cosmetic churn outside regions is noise. Report changed region plus sample lines.

Scope classes: deploy-wide (buildId rotated everywhere), template (one layout), route (one path pattern), locale (one region), variant (A/B split). Classify before fixing; scope sets the fix shape.

Recovery: version every fix; dual-read old and new shapes during transitions; backfill by window with idempotent IDs; verify counts and null rates match pre-break baselines.
