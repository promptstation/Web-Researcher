#!/usr/bin/env python3
"""Score control posture from checklist JSON (stdlib only)."""
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--controls", required=True, help="JSON list {id,design,operating}")
    args = ap.parse_args()
    cs = json.load(open(args.controls, encoding="utf-8"))
    de = sum(1 for c in cs if c.get("design") == "ok")
    op = sum(1 for c in cs if c.get("operating") == "ok")
    print("controls=%d design_ok=%d operating_ok=%d" % (len(cs), de, op))
    for c in cs:
        if c.get("design") != "ok" or c.get("operating") != "ok":
            print("  GAP %s design=%s operating=%s" % (c.get("id"), c.get("design"), c.get("operating")))
    print("close gaps owned+dated; verify operating, not just designed.")

if __name__ == "__main__":
    main()
