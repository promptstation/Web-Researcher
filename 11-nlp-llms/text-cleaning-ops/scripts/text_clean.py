#!/usr/bin/env python3
"""Clean text: unicode, whitespace, boilerplate lines, dedupe (stdlib only)."""
import argparse, re, unicodedata

BOILER = re.compile(r"cookie|subscribe|newsletter|all rights reserved|click here|sign up", re.I)

def clean(text):
    text = unicodedata.normalize("NFKC", text)
    lines, seen, out = text.splitlines(), set(), []
    for ln in lines:
        ln = re.sub(r"\s+", " ", ln).strip()
        if not ln or BOILER.search(ln):
            continue
        if ln in seen:
            continue
        seen.add(ln)
        out.append(ln)
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()
    raw = open(args.inp, encoding="utf-8", errors="replace").read()
    done = clean(raw)
    if args.report:
        print("chars %d -> %d (%.0f%% kept)" % (len(raw), len(done), 100 * len(done) / max(1, len(raw))))
    if args.out:
        open(args.out, "w", encoding="utf-8").write(done)
        print("wrote %s" % args.out)
    else:
        print(done[:2000])

if __name__ == "__main__":
    main()
