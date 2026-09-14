# Classifier Ops

Splits: stratified 70/15/15-ish by class with seed recorded; dedupe across splits first; test locked — touch once for ship/no-ship. Report accuracy plus macro-F1 plus per-class P/R always.

Training: ImageNet-pretrained backbone; freeze-then-unfreeze; LR finder then cosine with warmup; early stop patience 5-10 on val macro-F1; batch largest stable; reproduce best run twice with different seeds. Track configs, metrics, and artifacts.

Imbalance: weighted sampling first, class weights second, focal/gather-hard third, targeted collection always in parallel. Never accuracy-only on skewed data. Slices: per class, per source, per lighting/size buckets.

Calibration: ECE on val; temperature scaling; threshold from cost matrix (FP vs FN cost), verified on test once; monitor live ECE and slice metrics; recalibrate on shift. Ship criteria: test macro-F1 floor, worst-class floor, ECE ceiling, latency budget — all met.
