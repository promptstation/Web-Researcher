# Array Shapes

Shape guide: giant _0x array literal; rotation IIFE shifting until a parseInt checksum matches; decoder function indexing with offset; call sites as _0x(0x1a4) or aliased wrappers. Offsets shift per build; never assume constants.

Emulation: reimplement the rotation loop's arithmetic (shifts, checksum target) in analysis code; verify by matching known plaintext markers like 'log' or 'length'. Sandbox observation is the fallback when rotation reads environment.

Resolution: collect all decoder aliases via assignment tracing; rewrite calls to literals keeping original call in trailing comments; count coverage; list unresolved with reasons (computed indices, aliased imports).

Nesting: entries may hold base64, hex, or RC4 blobs; decode per entry with the codec toolkit; re-verify readability. Some builds re-encode per deploy; template the pipeline, not the constants.
