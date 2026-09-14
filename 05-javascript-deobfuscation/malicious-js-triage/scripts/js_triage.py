#!/usr/bin/env python3
"""Risk-score suspicious JS statically (stdlib only)."""
import argparse, re

SIGNS = [
    ("eval_dynamic", 20, r"\beval\b|new\s+Function|setTimeout\("),
    ("net_exfil", 20, r"fetch\(|XMLHttpRequest|navigator\.sendBeacon|WebSocket\("),
    ("obfuscation", 20, r"_0x[a-f0-9]{4,}|fromCharCode.*,.*,"),
    ("form_cookie_read", 15, r"document\.cookie|querySelector.*(card|cvv|pass)|getElementById.*(card|pass)"),
    ("exfil_post", 15, r"\.open\([^)]{0,30}POST|method[^\n]{0,20}POST"),
    ("traps", 10, r"\bdebugger\b|outerWidth"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    score, hits = 0, []
    for name, pts, pat in SIGNS:
        n = len(re.findall(pat, src))
        if n:
            score += pts
            hits.append("%s x%d +%d" % (name, n, pts))
    print("score: %d/100" % min(100, score))
    for h in hits:
        print("  %s" % h)
    urls = sorted(set(re.findall(r"https?://[A-Za-z0-9._:-]+(?:/[A-Za-z0-9._/=?&%-]*)?", src)))[:15]
    print("urls_seen: %d (do not visit live)" % len(urls))
    for u in urls:
        print("  hxxp" + u[4:])
    print("call: %s" % ("DETONATE-URGENT" if score >= 60 else "DETONATE" if score >= 25 else "MONITOR"))

if __name__ == "__main__":
    main()
