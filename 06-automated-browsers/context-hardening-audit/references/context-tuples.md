# Context Tuples

Tuple coherence: platform matches UA OS; locale matches timezone city; viewport matches device class; touch matches mobile; language list starts with locale language; geolocation near timezone. Mismatches cause false failures and misleading measurements.

Standard tuples: desktop US (Win/Chrome, 1366x768, en-US, America/New_York), desktop EU (Win/Chrome, 1920x1080, de-DE, Europe/Berlin), mobile (Pixel-ish, 412x915, touch, en-US). Extend deliberately with docs.

Audit: schema-validate configs; cross-check tuple fields; flag drift from baselines; version every change. Staging tests use filed tuples only.

Boundaries: coherence serves correctness of your own testing. Imitating other clients to mislead third-party scoring is out of scope; see access negotiation for lawful paths.
