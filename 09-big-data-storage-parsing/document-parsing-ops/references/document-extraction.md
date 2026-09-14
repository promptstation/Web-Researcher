# Document Extraction

Tools: PDF native pypdf (fast) then pdfplumber (layout/tables); scanned OCR via ocrmypdf/tesseract at 300dpi; DOCX python-docx; XLSX openpyxl (values plus formatting notes); PPTX python-pptx; legacy .doc via antiword/libreoffice. Pin versions; fixtures per template.

Triage signals: file size, page count, embedded text length (native vs scanned), image DPI, table hints, corruption. Buckets: native-easy, native-hard (layout), scanned-worthy, scanned-skip, corrupt-quarantine. Always rank by value x feasibility.

OCR: sample 50+ pages across buckets; score character error roughly plus table usability; cost = pages x sec/page x compute; pilot 5 percent; proceed only if value beats cost with margin. Preprocess: deskew, denoise, 300dpi.

Tables: bordered lattice first, stream fallback; verify with row counts, header match, numeric totals; store cells with coordinates and confidence; quarantine ambiguous. Layout: preserve headings, lists, reading order; downstream specifies what matters before you flatten.
