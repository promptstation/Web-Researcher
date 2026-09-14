#!/usr/bin/env python3
"""Inventory anti-debug/anti-tamper traps (stdlib only)."""
import argparse, re

PATS = {
    "debugger_stmt": r"\bdebugger\b",
    "console_timing": r"console\.(time|table|clear)",
    "devtools_size": r"outerWidth|outerHeight|innerWidth.*innerHeight",
    "domain_lock": r"location\.host(name)?",
    "integrity": r"toString\(\)\.length|Function\.prototype\.toString",
    "infinite_loop": r"while\s*\(\s*true\s*\)|for\s*\(\s*;\s*;\s*\)",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    for name, pat in PATS.items():
        hits = [m.start() for m in re.finditer(pat, src)]
        print("%s: %d" % (name, len(hits)))
        lines = src.splitlines()
        for h in hits[:5]:
            ln = src.count("\n", 0, h) + 1
            print("  L%d %.120s" % (ln, lines[ln-1].strip() if ln <= len(lines) else ""))
    print("patch lab copies only; keep originals hashed.")

if __name__ == "__main__":
    main()
