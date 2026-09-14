# Multilingual Ops

Detection: script ratios (Latin/CJK/Arabic/Cyrillic/Devanagari) as priors + n-gram model (fasttext lid.176 class); confidence threshold 0.7+ for auto-route, quarantine below; short text (<30 chars) uses metadata + script only. Eval detection per language on 500+ docs.

Routing: per-language cleaning (quotes, segmentation), chunking (sentence rules), stopwords, and eval sets; mixed docs get multi-labels and a mixed pipeline; log every routing decision with confidence. Locale table: language -> configs, eval set, owner, quality floor.

CJK: no space segmentation (use proper tokenizers); width normalization careful; chunk by sentences not words. Arabic: RTL handling, diacritics policy. Code-switch: segment by script runs; evaluate mixed separately.

Fairness: report quality per language always; fix worst-first with care budget; low-resource languages get judged sets before scaling; never English-only eval for multilingual claims.
