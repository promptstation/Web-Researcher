# Framework Layout

Layout: tests by user flow; fixtures central with documented lifetimes; page objects per flow (not per component); helpers versioned with docs; config per environment with secrets vaulted. One-page map mandatory.

CI: shard by measured time across N workers; fence retries (max 2, flagged); upload traces/videos on failure only; retain 14-30 days; gate merges on green; nightly full plus per-PR affected. Report links to artifacts.

Ownership: every directory has an owner team; CODEOWNERS enforced; stale areas reassigned quarterly; helper usage audited semiannually; deprecations get migration windows plus removal dates.

Health: runtime trend, flake rate, skip count, helper usage, artifact bytes, owner coverage. Review monthly; red metrics get dated fixes.
