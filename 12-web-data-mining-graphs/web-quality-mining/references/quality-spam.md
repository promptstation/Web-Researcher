# Quality Spam

Signals: content (main-text length, uniqueness vs corpus, boilerplate ratio, readability, ad density); link (inlink trust, outlink spam ratio, farm membership); behavior (bounce-ish, freshness, update cadence). Catalog 15+ with coverage and cost.

Fusion: weighted sum or small model; threshold tuned on 200+ judged for precision target; borderline band (e.g., 0.4-0.6) to human review; version everything. Spam taxonomy: stuffing, cloaking, farms, scraped-dupe, thin-affiliate, hacked — each with detectors.

Enforcement: filter/demote/quarantine by band; log (page, score, signals, version); appeal path with SLA; restore + fix on valid appeals. Adversarial review quarterly: probe with crafted spam, add signals, re-tune.

Proof: precision sampled monthly (200+); false-positive log; corpus quality trend; decisions auditable. Filters serve users and corpus quality — never competitors or viewpoints.
