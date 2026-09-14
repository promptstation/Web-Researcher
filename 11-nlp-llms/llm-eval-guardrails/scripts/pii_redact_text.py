#!/usr/bin/env python3
"""Redact emails/phones/cards/SSN-ish patterns (stdlib only)."""
import argparse, re
from collections import Counter

PATS = {
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "phone": r"\+?\d[\d\s().-]{7,}\d",
    "card": r"\b(?:\d[ -]?){13,19}\b",
    "ssn_like": r"\b\d{3}-\d{2}-\d{4}\b",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = open(args.inp, encoding="utf-8").read()
    counts = Counter()
    for name, pat in PATS.items():
        text, n = re.subn(pat, "[%s]" % name.upper(), text)
        counts[name] = n
    print("redactions: %s" % dict(counts))
    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
        print("wrote %s — verify with planted PII + eye samples." % args.out)
    else:
        print(text[:2000])

if __name__ == "__main__":
    main()
