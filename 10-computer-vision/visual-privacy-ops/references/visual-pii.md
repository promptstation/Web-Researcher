# Visual PII

PII types: faces (even partial/profile), plates, screens with text, badges/IDs, documents, distinctive tattoos, children (highest protection). Detect all at ingest; inventory per image; quarantine on detector failure.

Redaction: blackout for high-risk (children, IDs, plates in sensitive contexts); heavy pixelate (16px+) or strong blur for standard faces; expand boxes 10-20 percent; redact BEFORE thumbnails/crops/embeds derive. Originals encrypted, access-logged, purged on schedule.

Verification: eye-sample 5-10 percent; re-run detector over redacted output (must find ~zero); measure residual risk; fix detector gaps not just instances. Coverage report per release.

Governance: consent records (who, what, scope, expiry) or documented exclusion; retention minima with auto-purge; access least-privilege; exposure drill yearly (contain, scope, notify, harden). When unsure: redact or exclude.
