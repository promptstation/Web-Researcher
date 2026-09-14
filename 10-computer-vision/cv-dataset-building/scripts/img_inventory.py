#!/usr/bin/env python3
"""Inventory images: type, size, PNG dims, exact dupes (stdlib only)."""
import argparse, hashlib, os, struct
from collections import Counter

def kind(path):
    with open(path, "rb") as fh:
        head = fh.read(32)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", head[16:24])
        return "png", "%dx%d" % (w, h)
    if head[:2] == b"\xff\xd8":
        return "jpeg", "?"
    if head[:6] in (b"GIF87a", b"GIF89a"):
        w, h = struct.unpack("<HH", head[6:10])
        return "gif", "%dx%d" % (w, h)
    if head[:2] == b"BM":
        return "bmp", "?"
    if head[:4] == b"II*\x00" or head[:4] == b"MM\x00*":
        return "tiff", "?"
    return "unknown", "?"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()
    types, hashes, total = Counter(), {}, 0
    dupes = 0
    for root, _, files in os.walk(args.dir):
        for f in sorted(files):
            p = os.path.join(root, f)
            try:
                sz = os.path.getsize(p)
            except OSError:
                continue
            total += sz
            t, dims = kind(p)
            types[t] += 1
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
            if h in hashes:
                dupes += 1
            hashes.setdefault(h, p)
    print("files=%d bytes=%.1fMB dupes=%d" % (sum(types.values()), total / 1e6, dupes))
    for t, n in types.most_common():
        print("  %s: %d" % (t, n))
    print("next: perceptual near-dedupe + license log + manifest.")

if __name__ == "__main__":
    main()
