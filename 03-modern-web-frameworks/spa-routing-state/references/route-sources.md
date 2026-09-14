# Route Sources

Source ladder: sitemap.xml and sitemap indexes first; HTML nav and footer links second; framework manifests (__sveltekit manifest, Next.js routes-manifest, Nuxt payload paths) third; bundle-mined path literals fourth; CMS or search APIs fifth with permission. Reconcile all; no single source is complete.

Mining patterns: path:'/x', route:{path:}, '/x/:id', createRoute, files under pages/ or routes/ in maps. Verify mined paths by fetching; many are partials or examples.

Guard reading: 302 to /login means auth guard; 404 with app shell means client fallback; identical shell for all paths means catch-all routing. Classify before planning extraction.

Coverage math: report enumerated, fetchable, schema-valid, and excluded-with-reason separately. Never present enumerated as covered.
