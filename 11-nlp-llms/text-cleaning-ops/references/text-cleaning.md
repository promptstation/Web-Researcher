# Text Cleaning

Order: detect true encoding -> repair mojibake (ftfy-class) -> unicode NFKC (careful with math/CJK) -> whitespace collapse (keep paragraph breaks) -> boilerplate strip (density/link signals) -> line/block dedupe -> trim. Each stage logged; raw kept immutable.

Boilerplate: drop cookie banners, nav, related-links, comments prompts by text signals + position; keep headings/lists/quotes; verify strip rate on 100 samples (target: boilerplate under 2 percent, content loss ~0). Syndication: normalized-hash dedupe, keep earliest/canonical, link copies.

Multilingual: detect per document; NFKC caution for CJK widths; keep original scripts (no romanization); normalize quotes/dashes per locale. Emojis: keep for social, drop for formal — decided per corpus, documented.

Verification: 100 before/after eye samples; fixtures 50+ gating changes; batch metrics (chars/doc, boilerplate rate, empty rate); alert on drift. Cleaning configs versioned with changelogs.
