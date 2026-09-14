#!/usr/bin/env python3
"""Manage golden screenshot sets by hash (stdlib only)."""
import argparse, hashlib, json, os

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--record", default="")
    ap.add_argument("--check", default="")
    args = ap.parse_args()
    if args.record:
        m = {}
        for f in sorted(os.listdir(args.dir)):
            if f.endswith((".png", ".jpg")):
                m[f] = sha(os.path.join(args.dir, f))
        json.dump(m, open(args.record, "w"), indent=1)
        print("recorded %d goldens -> %s" % (len(m), args.record))
    if args.check:
        m = json.load(open(args.check, encoding="utf-8"))
        bad = 0
        for f, h in sorted(m.items()):
            p = os.path.join(args.dir, f)
            cur = sha(p) if os.path.exists(p) else "MISSING"
            if cur != h:
                bad += 1
                print("DIFF %s (triage: real/flake/intended)" % f)
        print("checked=%d diffs=%d" % (len(m), bad))

if __name__ == "__main__":
    main()
