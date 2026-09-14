# Parse and Paint Rules

Parser rules: classic scripts without defer or async block parsing; deferred scripts run in order after parsing; async scripts run whenever fetched. Stylesheets block rendering and block scripts that follow them. Fonts block text paint unless display=swap or optional. Preload fetches early at high priority but does not execute; preconnect warms DNS plus TLS only.

Tree facts: DOM comes from HTML; CSSOM from stylesheets; the render tree joins visible DOM with computed style; layout assigns geometry; paint records draw calls; composite draws layers. Display:none nodes skip render and layout but still parse. Content-visibility skips rendering work for offscreen subtrees.

Budgets that catch trouble: nodes above ~3,000 deserve review, depth above ~30 deserves review, blocking JS above ~200KB deserves splitting, unused CSS above 50% deserves delivery changes. Always confirm with traces; budgets triage, they do not convict.

Scraper corollary: extraction needs the subtree containing data plus its scripts, not the whole page at full fidelity. Block third parties, skip below-fold hydration, and wait on data selectors.
