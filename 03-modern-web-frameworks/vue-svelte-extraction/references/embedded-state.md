# Embedded State

Island inventory: scan script[type=application/json] and known ids (__NEXT_DATA__, __NUXT__, __NUXT_DATA__, __PINIA__, __APOLLO_STATE__, sveltekit:data). Record id, byte size, and top-level keys. Anything over 5KB with entity keys is probably your data.

Nuxt notes: v2 __NUXT__ is plain JSON; v3 payloads use versioned reviver encoding for dates, regexps, and refs. Parse structurally; never eval. Pinia stores serialize under predictable keys; map store id to entity.

SvelteKit notes: data nodes pair with routes; __sveltekit manifest reveals route table; form actions need method plus body fidelity. Astro notes: static HTML plus island props; find islands by astro-island tags and their component-url props.

Safety: parse as data, never execute; cap payload sizes; validate schemas; version everything; re-census after upgrades.
