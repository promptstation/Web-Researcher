# Trap Patterns

Pattern catalog: bare debugger statements; setInterval-debugger loops; console timing (table/clear timing gaps); DevTools dimension and toString traps; domain locks comparing location.host to allowlists; integrity checks hashing own source; anti-breakpoint code randomizing paths under debugger.

Lab patching: nop debugger sites; stub Date for timing; fix innerWidth/Height for dimension traps; stub location.host for locks; neutralize integrity by patching the comparison, never by shipping weakened code. One class per patch revision.

Verification: run behavior samples pre/post on benign paths; confirm identical outputs minus trap firing; keep originals hashed and patches diffed. Mark every patched file LAB-ONLY in headers.

Boundaries: analyze to understand and report; do not redistribute deprotected commercial code; report findings to owners where security-relevant.
