# Vitals and Budgets

Metric meanings: LCP marks when the largest content paints and should beat 2.5s; INP measures worst interaction latency and should beat 200ms; CLS sums unexpected layout shift and should stay under 0.1. Lab tools approximate; field data (CrUX or RUM) decides user impact. Always state which you report.

Chain thinking: every LCP has a chain of navigation, redirects, HTML, critical CSS or JS, hero fetch, render. Cost each hop and assign an owner. Fix hops in chain order; parallel wishes do not shorten chains.

Budget starters per template: JS under 300KB transfer on content pages, images under 500KB above fold, webfonts under 100KB with two families max, third-party blocking JS zero by default, request counts under 60 critical. Tune to your field data within one quarter.

Guard design: fail builds on budget breach with asset name, bytes over, and owner. Allow explicit waivers with expiry dates. Review waivers weekly until field confirms.
