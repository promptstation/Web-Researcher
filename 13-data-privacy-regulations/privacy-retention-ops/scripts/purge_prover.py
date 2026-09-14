#!/usr/bin/env python3
"""Verify subject-key absence across files (stdlib only)."""
import argparse, os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--subject", required=True, help="key/email/id to be absent")
    args = ap.parse_args()
    hits, files = [], 0
    for root, _, fs in os.walk(args.root):
        for f in fs:
            p = os.path.join(root, f)
            files += 1
            try:
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    for i, line in enumerate(fh, 1):
                        if args.subject in line:
                            hits.append("%s:%d" % (p, i))
                            break
            except OSError:
                pass
    print("scanned=%d hits=%d" % (files, len(hits)))
    for h in hits[:10]:
        print("  HIT " + h[-120:])
    print("absent-confirmed" if not hits else "NOT-CLEAN: remove + re-verify")

if __name__ == "__main__":
    main()
