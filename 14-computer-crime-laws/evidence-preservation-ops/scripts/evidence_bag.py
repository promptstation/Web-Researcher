#!/usr/bin/env python3
"""Bag evidence: sha256 manifest + custody entry (stdlib only)."""
import argparse, hashlib, json, os, time

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(65536), b""):
            h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--case", required=True)
    ap.add_argument("--handler", required=True)
    args = ap.parse_args()
    files = {}
    for root, _, fs in os.walk(args.dir):
        for f in sorted(fs):
            p = os.path.join(root, f)
            if p.endswith("manifest.json"):
                continue
            try:
                files[os.path.relpath(p, args.dir)] = sha(p)
            except OSError:
                pass
    bag = {"case": args.case, "ts": time.time(), "handler": args.handler,
           "files": files, "custody": [{"to": args.handler, "ts": time.time(), "why": "collected"}]}
    mp = os.path.join(args.dir, "manifest.json")
    json.dump(bag, open(mp, "w"), indent=1)
    print("bagged %d files -> %s (seal + store write-once)" % (len(files), mp))

if __name__ == "__main__":
    main()
