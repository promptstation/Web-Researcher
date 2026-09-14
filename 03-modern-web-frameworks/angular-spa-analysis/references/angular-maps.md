# Angular Maps

Fingerprints: ng-version attribute on app root; main/HASH.js plus polyfills and runtime chunks; 3rdpartylicenses and ngsw.json for PWA builds. Versions shape bundle layout; record full version always.

Route sources: router config in main chunk, lazy boundaries at import() splits, chunk manifest names hinting at modules. Verify by navigating authed, not by guessing URLs.

API sources: environment files compiled into main chunk as URL literals near endpoint paths; confirm each base with an authed request before building on it. Watch for per-tenant bases and gateway prefixes.

Enterprise rules: SSO via real login flows; MFA satisfied by the human owner, never automated around; tokens refreshed, never forged; every run logged with scope and counts; data minimized to the permission.
