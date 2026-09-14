# HTML Parsing

Selection: lxml.html (fastest, strict-ish); BeautifulSoup+lxml (tolerant, slower); stdlib html.parser (zero-dep, manual). Benchmark pages/sec on YOUR corpus; 10-100x gaps are normal. Regex only for already-extracted text, never structure.

Robustness: detect encoding (headers, meta, chardet fallback); normalize to UTF-8 with replacement logging; cap document size (5-20MB) with streaming above; tolerant fallback chain (lxml -> bs4 -> stdlib -> quarantine).

Boilerplate: score blocks by text density, link ratio, and tag class signals; drop nav/header/footer/aside/ads by role and class; verify on 100+ samples with rough precision/recall; extractor-specific tuning beats generic.

Scale: one document per task; processes for CPU-bound; stream lists (iterparse patterns); release DOMs promptly; golden fixtures (50+ pages) gate every change; field-fill rates monitored in prod.
