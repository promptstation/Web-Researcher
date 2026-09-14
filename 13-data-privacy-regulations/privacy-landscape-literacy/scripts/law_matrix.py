#!/usr/bin/env python3
"""Generate a privacy regime comparison matrix (stdlib only)."""
import argparse

ROWS = [
    ("Scope test", "establishment+targeting", "thresholds+residents", "processing in/on CN", "processing in BR"),
    ("Lawful basis", "6 bases, doc'd", "notice+opt-outs", "consent-forward", "10 bases"),
    ("Key rights", "access/erase/port/object", "delete/correct/opt-out", "access/correct/erase/explain", "GDPR-like"),
    ("High-risk review", "DPIA mandatory", "risk assessment", "PIA + security assess", "DPIA (ANPD rules)"),
    ("Breach notice", "72h authority", "without delay", "prompt + assess", "reasonable time"),
    ("Transfers", "adequacy/SCCs", "contract terms", "security assess/cert", "adequacy/SCCs"),
    ("Response SLA", "1 month", "45 days", "prompt (15d-ish)", "15 days"),
    ("Teeth", "4% turnover", "$7.5k/violation+", "5% turnover", "2% turnover"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    head = "| Duty | GDPR | CCPA/CPRA | PIPL | LGPD |\n|---|---|---|---|---|\n"
    body = "".join("| %s | %s | %s | %s | %s |\n" % r for r in ROWS)
    text = "# Regime Matrix (operational sketch — counsel confirms)\n\n" + head + body
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s" % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
