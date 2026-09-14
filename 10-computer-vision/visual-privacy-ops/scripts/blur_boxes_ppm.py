#!/usr/bin/env python3
"""Blackout boxes in PPM P6 (redaction mechanics demo, stdlib only)."""
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--boxes", required=True, help="JSON [[x,y,w,h],...] + gray 0-255")
    ap.add_argument("--gray", type=int, default=0)
    args = ap.parse_args()
    parts = open(args.inp, "rb").read().split(b"\n", 3)
    w, h = map(int, parts[1].split()[:2])
    px = bytearray(parts[3][:w * h * 3])
    for x, y, bw, bh in json.loads(open(args.boxes).read()):
        for j in range(max(0, y), min(h, y + bh)):
            for i in range(max(0, x), min(w, x + bw)):
                o = (j * w + i) * 3
                px[o:o + 3] = bytes((args.gray,) * 3)
    open(args.out, "wb").write(b"P6\n%d %d\n255\n" % (w, h) + bytes(px))
    print("redacted %s -> %s (verify by eye + re-detect)" % (args.inp, args.out))

if __name__ == "__main__":
    main()
