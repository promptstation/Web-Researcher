#!/usr/bin/env python3
"""Dump obfuscator string arrays + decode entry encodings (stdlib only)."""
import argparse, base64, json, re, sys

def try_b64(s):
    try:
        raw = base64.b64decode(s.strip() + "=" * (-len(s.strip()) % 4))
        txt = raw.decode("utf-8", "strict")
        if all(32 <= ord(c) < 127 or c in "\n\t" for c in txt[:200]):
            return txt[:200]
    except Exception:
        pass
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--dump", action="store_true")
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    m = re.search(r"var\s+(_0x[a-f0-9]+)\s*=\s*\[(.*?)\];", src, re.S)
    if not m:
        print("no _0x array found")
        sys.exit(0)
    name, body = m.group(1), m.group(2)
    entries = re.findall(r"'((?:[^'\\]|\\.)*)'|\"((?:[^\"\\]|\\.)*)\"", body)
    flat = [a or b for a, b in entries]
    print("array: %s entries: %d" % (name, len(flat)))
    print("rotation_iife: %s" % bool(re.search(r"\(function\(_0x", src)))
    decoders = sorted(set(re.findall(r"function\s+(_0x[a-f0-9]+)\s*\(", src)))
    print("decoder_fns: %s" % (decoders[:10] or ["?"]))
    if args.dump:
        for i, e in enumerate(flat[:args.limit]):
            d = try_b64(e)
            print("%d %s%s" % (i, e[:90], ("  ->B64-> " + d[:90]) if d else ""))

if __name__ == "__main__":
    main()
