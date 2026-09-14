#!/usr/bin/env python3
"""Stop/pause/continue decision aid (stdlib only)."""
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--signals", default="", help="comma: pii_spill,auth_breach,harm_report,distress,red_flag")
    args = ap.parse_args()
    sigs = set(x for x in args.signals.split(",") if x)
    hard = {"pii_spill", "auth_breach", "red_flag"}
    soft = {"harm_report", "distress"}
    if sigs & hard:
        print("STOP: halt scope now, quarantine, notify chain, memo 24h.")
    elif sigs & soft:
        print("PAUSE: freeze scope, triage in hours, disclose per findings.")
    elif not sigs:
        print("no signals passed - drill with --signals pii_spill,distress etc.")
    else:
        print("unknown signals %s - treat as PAUSE + review." % sigs)

if __name__ == "__main__":
    main()
