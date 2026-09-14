#!/usr/bin/env python3
"""Scan files for confidential markers (stdlib only)."""
import argparse, os, re

PATS = [r"confidential", r"internal[- ]only", r"do not distribute", r"attorney", r"privileged",
        r"api[_-]?key", r"secret[_-]?key", r"password\s*[:=]"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    args = ap.parse_args()
    rx = re.compile("|".join(PATS), re.I)
    hits, files = [], 0
    for root, _, fs in os.walk(args.root):
        for f in fs:
            p = os.path.join(root, f)
            files += 1
            try:
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    for i, line in enumerate(fh, 1):
                        if rx.search(line):
                            hits.append("%s:%d" % (p, i))
                            break
            except OSError:
                pass
    print("scanned=%d flagged=%d" % (files, len(hits)))
    for h in hits[:15]:
        print("  FLAG " + h[-120:])
    print("review flags: quarantine real secrets, counsel same-day.")

if __name__ == "__main__":
    main()
