# OCR Eval

Metrics: CER (char error rate) primary, WER secondary; score on 100+ stratified pages; report by bucket (clean, skew, faint, table, handwriting). Targets: printed clean CER under 2 percent; mixed under 5; handwriting stated separately (often 10-30).

Preprocessing: deskew first (biggest cheap win), denoise, 300 DPI minimum, contrast normalize, binarize gently (Otsu/Sauvola); ablate each on CER; lock winners per source type. Never upscale garbage expecting miracles.

Engines: Tesseract (free, solid printed), PaddleOCR (multilingual, tables), cloud (best handwriting/complex, costly); bake off on YOUR pages with cost per 1k. Hybrid common: cheap engine first, expensive on low-confidence.

Routing: word/field confidence thresholds tuned per value; critical fields (totals, IDs, dates) human-verified to precision target; review SLA tracked; reprocess loop for systematic errors. State limits in writing.
