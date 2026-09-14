# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 10 Computer Vision (CV) → Section: Image Classification Operations

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Image Classification Operations”** as part of an advanced course in computer vision, image datasets, and visual extraction. How to run transfer-learning classification: stratified splits, fine-tuning schedules, class imbalance handling, calibration, and error analysis that ships.

The material should teach how to operate image classification end to end. Go beyond surface-level tips and examine vision operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong visual quality balances **accuracy, speed, cost, privacy, and fairness**. Show how these principles apply differently to sample images, labeled datasets, and production inference. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to split stratified with locked test sets

Teach how to fine-tune pretrained backbones with schedules that converge

Teach how to handle imbalance with sampling, weights, and focal options

Teach how to calibrate probabilities for threshold decisions

Teach how to analyze errors by slice and turn them into data fixes

Include practical methods for real projects. Cover:

* Stratified splitting
* Transfer schedules
* Imbalance toolkit
* Calibration checks
* Slice analysis
* Threshold tuning
* Experiment tracking
* Ship criteria

Explain how practitioners can avoid val oscillates (lr too high or tiny val).
Explain how practitioners can avoid overfits fast (small data or huge head).
Explain how practitioners can avoid calibrated on val, off live (distribution shift).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , p, h, o, t, o, s, ,,  , d, o, c, u, m, e, n, t,  , s, c, a, n, s, ,,  , s, c, r, e, e, n, s, h, o, t, s, ,,  , s, h, e, l, f,  , i, m, a, g, e, s, ,,  , a, n, d,  , s, a, t, e, l, l, i, t, e,  , t, i, l, e, s. Keep examples focused on visual quality rather than generic advice.

Include practical exercises that require the learner to:

1. Split one dataset stratified.
2. Fine-tune one backbone.
3. Fix one imbalance.
4. Calibrate one model.
5. Analyze errors by slice.
6. Ship against criteria.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from datasets, annotation, detection, OCR, and evaluation where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize OpenCV and PyTorch docs, COCO and ImageNet practices, OCR literature, and fairness references. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **split-clean checklist**, a **converged-1 checklist**, a **balanced-ok checklist**, a **calibrated-1 checklist**, a **shipped-criteria checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
