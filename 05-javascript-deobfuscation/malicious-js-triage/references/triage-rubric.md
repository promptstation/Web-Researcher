# Triage Rubric

Rubric (0-100): eval/Function plus dynamic code 20; network calls to non-vendor hosts 20; obfuscation depth (arrays, flattening, traps) 20; form/cookie/storage reads 15; exfil-shaped POSTs 15; recency and prevalence 10. Under 25 monitor; 25-60 detonate; over 60 detonate urgently and pre-draft disclosure.

Detonation bar: isolated VM, snapshots, no host shares, stubbed network sinks, budgets on. Static-only when score low or behavior already clear. Never live-fetch IOCs from analyst networks; use passive DNS and sandboxed sinks.

IOC handling: extract with surrounding context; defang dots and schemes for sharing; store live forms encrypted with access control; deploy blocks with change receipts.

Disclosure: site owner first, then vendor, host, registrar; include sample hash, behavior summary, IOCs defanged, transcripts excerpted, impact, and requested action. Track every disclosure to acknowledged or escalated.
