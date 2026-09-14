# Transform Policy

Geometry: pad (letterbox) preserves aspect; stretch only when aspect is noise; random-crop must keep labels valid (boxes clipped, OCR text intact); rotation limited by task (documents +-5, products +-30, aerial free). Test extremes by eye.

Photometric: brightness/contrast mild; color jitter only when color is not signal; noise/blur matched to deployment conditions; never invent conditions the camera never sees. Normalize exactly per model card (mean/std, scale); wrong norms silently cost points.

Inspection: 100+ augmented samples with labels overlaid before every training run; check 10 edge cases (small objects, dense text, dark images); ablation one-op-off to keep winners. Seeds recorded; eval path deterministic and versioned with the model.

Eval: resize-shortest + center-crop (or pad) + normalize, no randomness; TTA only as separate reported experiment. Document policy with examples; review on data change.
