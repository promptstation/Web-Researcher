#!/usr/bin/env python3
"""Walk proxy credential rotations step by step (stdlib only)."""
import argparse

STEPS = ["inventory", "issue-new", "dual-run", "cutover", "verify", "revoke-old", "postmortem"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", default="plan")
    args = ap.parse_args()
    if args.step == "plan":
        for i, s in enumerate(STEPS, 1):
            print("%d. %s" % (i, s))
        print("run each in order; verify zero auth failures before revoke-old.")
        return
    guide = {
        "inventory": "list scopes, workers, owners; confirm vault paths.",
        "issue-new": "create new creds; store in vault; do NOT deploy yet.",
        "dual-run": "enable both for 24-48h; monitor auth failures.",
        "cutover": "rolling deploy new; watch failure rate per worker.",
        "verify": "confirm 100% new-auth success for 24h.",
        "revoke-old": "revoke old; confirm zero old-auth attempts.",
        "postmortem": "file what worked, stragglers, next date.",
    }
    print("%s: %s" % (args.step, guide.get(args.step, "unknown step")))

if __name__ == "__main__":
    main()
