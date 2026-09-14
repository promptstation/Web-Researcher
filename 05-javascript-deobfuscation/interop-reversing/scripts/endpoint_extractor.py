#!/usr/bin/env python3
"""Extract endpoint candidates + context from bundles (stdlib only)."""
import argparse, re

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    found = {}
    for m in re.finditer(r'["\']((?:/[A-Za-z0-9._-]+)+(?:/[A-Za-z0-9._:{}$-]+)*)["\']', src):
        ep = m.group(1)
        if len(ep) < 5 or "." in ep.split("/")[-1]:
            continue
        ctx = src[max(0, m.start()-60):m.end()+40].replace("\n", " ")
        found.setdefault(ep, ctx)
        if len(found) >= args.limit * 2:
            break
    print("candidates: %d" % len(found))
    for ep, ctx in sorted(found.items())[:args.limit]:
        print("- %s" % ep)
        print("    ...%.150s" % ctx)
    print("confirm each against lawful traffic before specifying.")

if __name__ == "__main__":
    main()
