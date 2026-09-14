#!/usr/bin/env python3
"""Sanity-check pool size vs target rpm (stdlib only)."""
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--egress", type=int, default=50)
    ap.add_argument("--rpm", type=int, default=600)
    ap.add_argument("--per-egress-rpm", type=int, default=12)
    args = ap.parse_args()
    cap = args.egress * args.per_egress_rpm
    need = (args.rpm + args.per_egress_rpm - 1) // args.per_egress_rpm
    print("pool_cap_rpm=%d target_rpm=%d headroom=%.0f%%" % (cap, args.rpm, 100 * (cap - args.rpm) / max(1, args.rpm)))
    print("egress_needed=%d (at %d rpm each)" % (need, args.per_egress_rpm))
    print("rule: keep 30%%+ headroom; quarantine shrinks live pool fast.")

if __name__ == "__main__":
    main()
