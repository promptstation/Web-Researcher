# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 10 Computer Vision (CV) → Section: Object Detection Operations

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Object Detection Operations”** as part of an advanced course in computer vision, image datasets, and visual extraction. How to annotate boxes consistently, validate COCO datasets, train detectors, read mAP honestly, and handle small, dense, and overlapping objects.

The material should teach how to operate object detection end to end. Go beyond surface-level tips and examine vision operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong visual quality balances **accuracy, speed, cost, privacy, and fairness**. Show how these principles apply differently to sample images, labeled datasets, and production inference. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to write box guidelines (tightness, occlusion, truncation, groups) annotators follow

Teach how to validate COCO annotations for bounds, areas, duplicates, and splits

Teach how to train detectors with anchor/box priors and schedules that converge

Teach how to read mAP by size and class instead of single numbers

Teach how to handle small, dense, and overlapping objects with targeted fixes

Include practical methods for real projects. Cover:

* Guideline authoring
* Annotator agreement
* COCO validation
* Detector baselines
* mAP slicing
* Small-object toolkit
* NMS tuning
* Ship criteria

Explain how practitioners can avoid map plateaus low (noisy boxes or wrong priors).
Explain how practitioners can avoid dense crowds merge (nms too aggressive).
Explain how practitioners can avoid val/test gap (scene leakage across splits).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , p, h, o, t, o, s, ,,  , d, o, c, u, m, e, n, t,  , s, c, a, n, s, ,,  , s, c, r, e, e, n, s, h, o, t, s, ,,  , s, h, e, l, f,  , i, m, a, g, e, s, ,,  , a, n, d,  , s, a, t, e, l, l, i, t, e,  , t, i, l, e, s. Keep examples focused on visual quality rather than generic advice.

Include practical exercises that require the learner to:

1. Write one box guideline.
2. Measure annotator agreement.
3. Validate one COCO set.
4. Train one baseline.
5. Slice one mAP.
6. Fix one small-object gap.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from datasets, annotation, detection, OCR, and evaluation where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize OpenCV and PyTorch docs, COCO and ImageNet practices, OCR literature, and fairness references. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **guideline-live checklist**, a **agreement-ok checklist**, a **coco-clean checklist**, a **baseline-1 checklist**, a **sliced-map checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
