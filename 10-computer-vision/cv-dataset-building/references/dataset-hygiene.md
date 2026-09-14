# Dataset Hygiene

Licenses: per-source table (source, license, commercial-ok, attribution, expiry); robots/ToS checked; personal images need consent or exclusion; re-verify yearly. No license, no ingest — quarantine by default.

Provenance per image: source URL or id, license, fetched_at, hash (sha256), near-hash (aHash/dHash), split assignment. Manifest per version with counts and hashes; changelog for every change.

Dedupe: exact sha256 at ingest (zero tolerance); near via aHash Hamming <= 5 or dHash <= 8, cluster-reviewed; ALWAYS dedupe before splitting; verify zero cross-split near-dupes. Corrupt: verify (PIL verify + load) at ingest; quarantine failures with reasons.

Bias scouting: sample 500+ for source, geography, skin tone, gender, object size, lighting skews; document gaps; plan collection to fill. Splits: stratified, seeded, recorded; test set locked and touched only for final eval.
