#!/usr/bin/env python3
"""Probe + decode base64/hex/XOR blobs (stdlib only)."""
import argparse, base64, re, string, sys

def score_text(b):
    try:
        t = b.decode("utf-8")
    except Exception:
        return -1
    if not t:
        return -1
    ok = sum(1 for c in t if c in string.printable or c in "\n\t")
    return ok / len(t)

def xor_crack(data):
    best = (0, None, b"")
    for k in range(256):
        out = bytes(x ^ k for x in data)
        s = score_text(out)
        if s > best[0]:
            best = (s, k, out)
    return best

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", default="", help="blob string")
    ap.add_argument("--file", default="")
    args = ap.parse_args()
    blob = args.probe or (open(args.file, encoding="utf-8").read().strip() if args.file else "")
    if not blob:
        print("need --probe or --file", file=sys.stderr)
        sys.exit(2)
    print("len=%d b64shape=%s hexshape=%s" % (len(blob),
          bool(re.fullmatch(r"[A-Za-z0-9+/=\n\r]+", blob)), bool(re.fullmatch(r"[0-9a-fA-F\s]+", blob))))
    raw = blob.encode()
    try:
        raw = base64.b64decode(blob.strip() + "=" * (-len(blob.strip()) % 4))
        print("base64 decoded to %d bytes" % len(raw))
    except Exception:
        print("not base64; trying raw bytes")
    s, k, out = xor_crack(raw)
    print("xor_best key=0x%02x score=%.2f sample=%.160r" % (k, s, out[:160]))

if __name__ == "__main__":
    main()
