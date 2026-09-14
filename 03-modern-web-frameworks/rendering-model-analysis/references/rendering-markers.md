# Rendering Markers

Marker guide: __NEXT_DATA__ plus _next/static means Next.js; __NUXT__ or __NUXT_DATA__ means Nuxt; ng-version means Angular; sveltekit:data or sveltekit:body means SvelteKit; astro- islands mean Astro; data-hydrated or data-reactroot mean generic hydration. Empty #root or #app with large JS bundles means CSR. Full article text in HTML means SSR or SSG.

Completeness scoring: text over 2k chars with target entities present is complete; empty root with payload scripts is payload-backed; empty root without data is browser-required pending API mapping. Always check two routes minimum per template.

Header hints: x-nextjs-cache HIT/MISS, x-nuxt-cache, age headers, and CDN cache statuses reveal SSG/ISR. Vary and cache-control shape revalidation.

Decision tree: complete HTML -> parse; payload-backed -> parse payload; JSON APIs found -> API-first; else browser with selector waits. Re-verify after deploys.
