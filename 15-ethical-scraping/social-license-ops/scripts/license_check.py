#!/usr/bin/env python3
"""Score social-license readiness (stdlib only)."""
import argparse

ITEMS = ["norms_read", "introduced", "reciprocity_sized", "optout_easy", "optout_total",
         "transparency_page", "grievance_live", "liaison_named"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yes", default="", help="comma items done")
    args = ap.parse_args()
    done = set(x for x in args.yes.split(",") if x)
    score = sum(1 for i in ITEMS if i in done)
    print("license_readiness=%d/%d" % (score, len(ITEMS)))
    for i in ITEMS:
        print("  [%s] %s" % ("x" if i in done else " ", i))
    print("collect only at 7+: norms + reciprocity + real opt-out first.")

if __name__ == "__main__":
    main()
