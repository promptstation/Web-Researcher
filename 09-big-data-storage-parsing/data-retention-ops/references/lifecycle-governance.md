# Lifecycle Governance

Schedules: per dataset hot (days), warm (months), cold (years), delete (date); from legal holds, contracts, and business need; legal sign-off; yearly review; exceptions dated with owners. Automate sweeps; dry-run before every delete.

Archival: cold copy with manifest (files, hashes, schema, restore steps); checksums verified at write; restore-tested quarterly (sample + full yearly); retrieval cost tracked. One tested restore beats ten assumed archives.

Deletion: partition drops preferred (whole-unit, provable); manifest diff before/after as proof; verify absence via search plus random sampling; include backups (next cycle purge or crypto-shredding); file proof with timestamps and actor.

DSARs: intake log with SLA clock (statutory); search raw+clean+serve+backups+logs; delete and verify; respond with what was found, deleted, and kept (with basis); postmortem misses into prevention.
