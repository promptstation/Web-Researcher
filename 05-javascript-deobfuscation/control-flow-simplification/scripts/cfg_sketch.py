#!/usr/bin/env python3
"""Inventory switch-dispatcher cases (stdlib only)."""
import argparse, re

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--fn", default="")
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    if args.fn:
        m = re.search(r"function\s+%s\b.*?(?=\nfunction\s|\Z)" % re.escape(args.fn), src, re.S)
        src = m.group(0) if m else src
    cases = re.findall(r"case\s+['\"]([^'\"]+)['\"]\s*:", src) or re.findall(r"case\s+(\d+)\s*:", src)
    print("cases: %d" % len(cases))
    print("labels: %s" % cases[:40])
    assigns = re.findall(r"(\w+)\s*=\s*['\"]([A-Za-z0-9_]+)['\"]\s*;", src)
    print("state_assignments_sample: %s" % assigns[:20])
    print("dispatcher: %s" % bool(re.search(r"while\s*\(\s*true\s*\)", src)))
    print("next: sketch transitions per case by hand; prove reachability from entry.")

if __name__ == "__main__":
    main()
