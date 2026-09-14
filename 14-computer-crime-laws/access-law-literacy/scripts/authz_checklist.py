#!/usr/bin/env python3
"""Authorization briefing + grant checklist (stdlib only)."""
import argparse

ITEMS = ["system named", "actions listed", "data classes", "time window", "purpose stated",
         "exclusions listed", "granter signed", "expiry set", "logs planned", "counsel gray cleared"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief", action="store_true")
    ap.add_argument("--check", default="", help="comma: item=ok,...")
    args = ap.parse_args()
    if args.brief:
        print("Access rule: written scope before touch. Gates, not vibes.")
        for i, it in enumerate(ITEMS, 1):
            print("%2d. %s" % (i, it))
    if args.check:
        have = dict(x.split("=") for x in args.check.split(",") if "=" in x)
        missing = [it for it in ITEMS if have.get(it) != "ok"]
        print("missing=%s" % (missing or "none - access permitted"))

if __name__ == "__main__":
    main()
