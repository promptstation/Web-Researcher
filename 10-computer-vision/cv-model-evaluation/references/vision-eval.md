# Vision Eval

Slices: class, object size, source/domain, lighting/quality, geography, and (with care) demographics. Report headline plus every slice with n and CI; gate on worst-slice floors, not means. Slice metadata collected at eval design, not after.

Calibration: ECE overall and per slice for thresholded uses; reliability diagrams; temperature scaling; recheck on shift. Robustness: 5+ corruptions (blur, noise, JPEG, brightness, occlusion) at 3 severities; report drop curves; shift sets (new camera, season, site) where available.

Fairness: consented attributes only; gaps with uncertainty; data-first mitigation (collect, balance, augment carefully); model fixes second; external review for high-stakes. Document limits and residual gaps honestly.

Galleries: 100 errors clustered by cause, reviewed weekly with domain eyes; top-3 clusters become data fixes with verified lift; fix backlog tracked; gate ships on: headline floor, worst-slice floor, ECE ceiling, robustness floor, fairness review done.
