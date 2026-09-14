#!/usr/bin/env python3
"""Score competitive-collection fair play (stdlib only)."""
import argparse

ITEMS = ["license_considered", "terms_respected", "rates_polite", "identity_honest",
         "attribution_given", "value_compensated", "no_dark_acts", "exit_ready"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yes", default="")
    args = ap.parse_args()
    done = set(x for x in args.yes.split(",") if x)
    print("fairplay=%d/%d" % (sum(1 for i in ITEMS if i in done), len(ITEMS)))
    for i in ITEMS:
        print("  [%s] %s" % ("x" if i in done else " ", i))
    print("ship only at 8/8; dark acts = stop + report.")

if __name__ == "__main__":
    main()
