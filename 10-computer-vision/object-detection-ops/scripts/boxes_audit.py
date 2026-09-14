#!/usr/bin/env python3
"""Validate COCO boxes: bounds, area, dupes, orphans (stdlib only)."""
import argparse, json
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--coco", required=True)
    args = ap.parse_args()
    d = json.load(open(args.coco, encoding="utf-8"))
    imgs = {i["id"]: (i.get("width", 0), i.get("height", 0)) for i in d.get("images", [])}
    cats = {c["id"] for c in d.get("categories", [])}
    bad, tiny, dupes, orphans = 0, 0, 0, 0
    seen = set()
    per = Counter()
    for a in d.get("annotations", []):
        iid = a.get("image_id")
        if iid not in imgs:
            orphans += 1
            continue
        W, H = imgs[iid]
        x, y, w, h = a.get("bbox", [0, 0, 0, 0])
        key = (iid, round(x), round(y), round(w), round(h), a.get("category_id"))
        if key in seen:
            dupes += 1
        seen.add(key)
        if a.get("category_id") not in cats or w <= 0 or h <= 0:
            bad += 1
            continue
        if x < 0 or y < 0 or x + w > W + 1 or y + h > H + 1:
            bad += 1
        if w * h < 100:
            tiny += 1
        per[a["category_id"]] += 1
    print("images=%d anns=%d bad=%d tiny=%d dupes=%d orphans=%d" % (
        len(imgs), len(d.get("annotations", [])), bad, tiny, dupes, orphans))
    print("per-class: %s" % dict(per))
    print("train only when bad=dupes=orphans=0.")

if __name__ == "__main__":
    main()
