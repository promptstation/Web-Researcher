#!/usr/bin/env python3
"""Coverage audit: known vs crawled URL sets (stdlib only)."""
import argparse

def load(p):
    return {l.strip() for l in open(p, encoding="utf-8") if l.strip()}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--known", required=True)
    ap.add_argument("--crawled", required=True)
    args = ap.parse_args()
    known, got = load(args.known), load(args.crawled)
    miss = known - got
    print("known=%d crawled=%d coverage=%.1f%% missing=%d" % (
        len(known), len(known & got), 100 * len(known & got) / max(1, len(known)), len(miss)))
    for u in sorted(miss)[:10]:
        print("  MISS %.120s" % u)
    print("explain every miss class; fix or disclose.")

if __name__ == "__main__":
    main()
