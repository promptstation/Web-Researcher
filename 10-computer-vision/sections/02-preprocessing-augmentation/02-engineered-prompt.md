# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 10 Computer Vision (CV) → Section: Preprocessing and Augmentation

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Preprocessing and Augmentation”** as part of an advanced course in computer vision, image datasets, and visual extraction. How resize, crop, normalize, color, and augmentation pipelines prepare images for models, with deterministic eval transforms and inspected training transforms.

The material should teach how to build preprocessing and augmentation pipelines. Go beyond surface-level tips and examine vision operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong visual quality balances **accuracy, speed, cost, privacy, and fairness**. Show how these principles apply differently to sample images, labeled datasets, and production inference. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to resize, crop, and pad without distorting task-critical features

Teach how to normalize with model-specific means and scales

Teach how to augment (flip, crop, color, noise) matched to task invariances

Teach how to inspect augmented samples visually before training

Teach how to freeze deterministic eval transforms separate from training

Include practical methods for real projects. Cover:

* Transform design
* Aspect handling
* Normalization tables
* Augmentation policy
* Visual inspection
* Seed discipline
* Eval freezing
* Ablation checks

Explain how practitioners can avoid train/val gap grows (augmentation too strong or eval leaks).
Explain how practitioners can avoid color aug harms (color is signal (ripeness, brand)).
Explain how practitioners can avoid slow pipeline (cpu-bound transforms).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , p, h, o, t, o, s, ,,  , d, o, c, u, m, e, n, t,  , s, c, a, n, s, ,,  , s, c, r, e, e, n, s, h, o, t, s, ,,  , s, h, e, l, f,  , i, m, a, g, e, s, ,,  , a, n, d,  , s, a, t, e, l, l, i, t, e,  , t, i, l, e, s. Keep examples focused on visual quality rather than generic advice.

Include practical exercises that require the learner to:

1. Design transforms for one task.
2. Handle aspect correctly.
3. Inspect 100 augmented.
4. Freeze one eval path.
5. Ablate one augmentation.
6. Document one policy.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from datasets, annotation, detection, OCR, and evaluation where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize OpenCV and PyTorch docs, COCO and ImageNet practices, OCR literature, and fairness references. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **designed-task checklist**, a **aspect-safe checklist**, a **inspected-100 checklist**, a **eval-frozen checklist**, a **ablated-1 checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
