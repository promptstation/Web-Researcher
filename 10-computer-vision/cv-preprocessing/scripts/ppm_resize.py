#!/usr/bin/env python3
"""Nearest-neighbor resize + letterbox pad for PPM P6 (stdlib only)."""
import argparse, struct

def read_ppm(path):
    data = open(path, "rb").read().split(b"\n", 3)
    assert data[0] == b"P6", "need binary P6 PPM"
    w, h = map(int, data[1].split()[:2])
    px = data[3][:w * h * 3]
    return w, h, px

def resize_letterbox(w, h, px, size):
    s = min(size / w, size / h)
    nw, nh = max(1, int(w * s)), max(1, int(h * s))
    out = bytearray(b"\x80" * size * size * 3)
    ox, oy = (size - nw) // 2, (size - nh) // 2
    for y in range(nh):
        sy = int(y / s)
        for x in range(nw):
            sx = int(x / s)
            src = (sy * w + sx) * 3
            dst = ((oy + y) * size + (ox + x)) * 3
            out[dst:dst + 3] = px[src:src + 3]
    return size, size, bytes(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", type=int, default=224)
    args = ap.parse_args()
    w, h, px = read_ppm(args.inp)
    W, H, out = resize_letterbox(w, h, px, args.size)
    open(args.out, "wb").write(b"P6\n%d %d\n255\n" % (W, H) + out)
    print("%dx%d -> %dx%d letterboxed (aspect preserved)" % (w, h, W, H))

if __name__ == "__main__":
    main()
