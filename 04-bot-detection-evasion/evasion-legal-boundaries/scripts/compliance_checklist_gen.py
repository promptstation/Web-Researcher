#!/usr/bin/env python3
"""Scaffold a scraping compliance review from a plan file (stdlib only)."""
import argparse, datetime, re

FLAGS = ["login", "paywall", "captcha", "block", "ban", "api key", "account",
         "terms", "personal data", "email", "phone", "price", "copyright"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = open(args.plan, encoding="utf-8", errors="replace").read()
    low = text.lower()
    hits = sorted(set(f for f in FLAGS if f in low))
    sources = sorted(set(re.findall(r"https?://[A-Za-z0-9._-]+", text)))[:20]
    doc = []
    doc.append("# Compliance review %s" % datetime.date.today().isoformat())
    doc.append("")
    doc.append("## Flags found: %s" % (hits or ["none"]))
    doc.append("")
    doc.append("## Sources: %s" % (sources or ["none listed"]))
    doc.append("")
    doc.append("## Per-source grades (fill in)")
    for s in sources or ["source-1"]:
        doc.append("- %s : GREEN/AMBER/RED + terms quote + decision" % s)
    doc.append("")
    doc.append("## Counsel brief needed if any AMBER/RED. Stop-work triggers defined: YES/NO")
    doc.append("")
    doc.append("_Informational only, not legal advice._")
    out = "\n".join(doc) + "\n"
    if args.out:
        open(args.out, "w").write(out)
    print(out)

if __name__ == "__main__":
    main()
