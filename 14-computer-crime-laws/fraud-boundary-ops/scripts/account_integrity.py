#!/usr/bin/env python3
"""Audit account->human 1:1 maps (stdlib only)."""
import argparse, json
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", required=True, help="JSON {account:{human,purpose}}")
    args = ap.parse_args()
    m = json.load(open(args.map, encoding="utf-8"))
    humans = Counter(v.get("human", "?") for v in m.values())
    nopurpose = [a for a, v in m.items() if not v.get("purpose")]
    shared = {h: n for h, n in humans.items() if h != "service-owned" and n > 3}
    print("accounts=%d humans=%d no_purpose=%d" % (len(m), len(humans), len(nopurpose)))
    print("heavy_users=%s (review: 1:1 expected)" % (shared or "none"))
    print("missing_purpose=%s" % (nopurpose[:5] or "none"))
    print("service-owned accounts must be named, owned, vaulted, per-use logged.")

if __name__ == "__main__":
    main()
