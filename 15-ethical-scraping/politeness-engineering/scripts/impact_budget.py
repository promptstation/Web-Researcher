#!/usr/bin/env python3
"""Estimate crawl impact budgets (stdlib only)."""
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rpm", type=float, default=60)
    ap.add_argument("--kb-per-req", type=float, default=120)
    ap.add_argument("--hours", type=float, default=24)
    args = ap.parse_args()
    reqs = args.rpm * 60 * args.hours
    gb = reqs * args.kb_per_req / 1e6
    print("reqs/day=%.0f bandwidth~=%.1fGB/day rps=%.2f" % (reqs, gb, args.rpm / 60))
    print("small-site rule: <=1 rps AND <=5k req/day unless agreed; big only with contact.")
    print("file budget + approval; adapt live; report actuals.")

if __name__ == "__main__":
    main()
