#!/usr/bin/env python3
"""Classify challenge/block samples from saved HTML (stdlib only)."""
import argparse, re, sys

RULES = [
    ("managed-challenge", ["just a moment", "verify you are human", "checking your browser", "turnstile"]),
    ("captcha", ["captcha", "recaptcha", "hcaptcha"]),
    ("rate-limit", ["too many requests", "rate limit", "slow down", "retry-after"]),
    ("hard-block", ["request blocked", "access denied", "forbidden", "reference id", "incident id"]),
    ("auth-wall", ["sign in to continue", "login required", "authenticate"]),
    ("geo-wall", ["not available in your region", "geoblocked", "restricted in your country"]),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--url", default="")
    args = ap.parse_args()
    html = open(args.file, encoding="utf-8", errors="replace").read().lower()
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    print("url: %s" % args.url)
    print("title: %.120s" % (title.group(1).strip() if title else "?"))
    hits = []
    for cls, markers in RULES:
        for m in markers:
            if m in html or m in args.url.lower():
                hits.append((cls, m))
                break
    if hits:
        for cls, m in hits:
            print("CLASS %s via %r" % (cls, m))
    else:
        print("CLASS unknown-block (default: backoff + human review)")
    print("bytes: %d" % len(html))

if __name__ == "__main__":
    main()
