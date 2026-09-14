#!/usr/bin/env python3
"""Deterministically rename _0x identifiers by role hints (stdlib only)."""
import argparse, re

def role(name, src):
    uses = len(re.findall(r"\b%s\b" % re.escape(name), src))
    if re.search(r"%s\s*\(\s*0x" % re.escape(name), src):
        return "decode"
    if re.search(r"var\s+%s\s*=\s*\[" % re.escape(name), src):
        return "strtab"
    if uses < 5:
        return "tmp"
    return "v"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    names = sorted(set(re.findall(r"_0x[a-f0-9]+", src)))
    table, counters = {}, {}
    for n in names:
        r = role(n, src)
        counters[r] = counters.get(r, 0) + 1
        table[n] = "%s%d" % (r, counters[r])
    out = src
    for old in sorted(table, key=len, reverse=True):
        out = re.sub(r"\b%s\b" % re.escape(old), table[old], out)
    if args.out:
        open(args.out, "w").write(out)
    print("renamed: %d" % len(table))
    for old in sorted(table)[:20]:
        print("  %s -> %s" % (old, table[old]))

if __name__ == "__main__":
    main()
