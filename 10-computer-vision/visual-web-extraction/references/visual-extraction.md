# Visual Extraction

Capture: fixed viewport/devicePixelRatio, pinned fonts, timezone/locale, prefers-reduced-motion, hide carets/cursors; wait fonts + network-stable + animations-settled; full-page for layout, element for widgets, viewport for above-fold. Deterministic or it is not a signal.

Reading: template match for icons/badges; OCR for canvas text (upscaled element shots); layout models/VLM for tables/forms; always verify against DOM/API where any overlap exists; gallery of examples per locator with failure modes.

Goldens: baseline per page per viewport; mask dates/times, ads, avatars, A/B regions; per-page thresholds; diff triage daily (real vs flake vs intended); updates deliberate with before/after review. Never auto-accept.

Fusion: DOM primary + visual check, or visual primary + DOM check; divergence alerts with both artifacts; either channel alone must validate. Flake budget (e.g., under 1 percent); flakes fixed or masked, never tolerated.
