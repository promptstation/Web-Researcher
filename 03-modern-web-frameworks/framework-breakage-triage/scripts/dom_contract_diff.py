#!/usr/bin/env python3
"""Diff normalized data regions between two HTML snapshots (stdlib only)."""
import argparse, difflib, re, sys

def normalize(html):
    html = re.sub(r"<script.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}\S*", "TS", html)
    html = re.sub(r"(nonce|csrf|token)\W+\S+", "TOK", html, flags=re.I)
    lines = [re.sub(r"\s+", " ", l).strip() for l in re.split(r"[<>]", html)]
    return [l for l in lines if len(l) > 3][:3000]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--context", type=int, default=2)
    args = ap.parse_args()
    a = normalize(open(args.old, encoding="utf-8", errors="replace").read())
    b = normalize(open(args.new, encoding="utf-8", errors="replace").read())
    diff = list(difflib.unified_diff(a, b, lineterm="", n=args.context))
    added = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    print("added=%d removed=%d ratio=%.1f%%" % (added, removed, 100 * (added + removed) / max(1, len(a))))
    for l in diff[:120]:
        print(l[:200])

if __name__ == "__main__":
    main()
