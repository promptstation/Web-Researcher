#!/usr/bin/env python3
"""Audit JS bundles: weights, maps, secret patterns (stdlib only)."""
import argparse, re, sys, urllib.request

PATS = {"aws_key": r"AKIA[0-9A-Z]{16}", "stripe_live": r"sk_live_[0-9a-zA-Z]{16,}",
        "slack": r"xox[baprs]-[0-9a-zA-Z-]{10,}", "google_key": r"AIza[0-9A-Za-z_-]{20,}",
        "private_key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "pwd_literal": r"password\s*[:=]\s*\S{4,}"}

def fetch(url, timeout, cap=600000):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 bundle-audit"})
    r = urllib.request.urlopen(req, timeout=timeout)
    return r.read(cap).decode("utf-8", "replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--max-js", type=int, default=8)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    try:
        html = fetch(args.url, args.timeout)
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    scripts = re.findall(r'<script[^>]+src="([^"]+\.js[^"]*)"', html)[:args.max_js]
    print("chunks: %d" % len(scripts))
    for s in scripts:
        u = urllib.request.urljoin(args.url, s)
        try:
            js = fetch(u, args.timeout)
        except Exception as e:
            print("  FAIL %s (%s)" % (s, e))
            continue
        has_map = "sourceMappingURL" in js
        print("  %dB map=%s %s" % (len(js), has_map, s[:100]))
        for name, pat in PATS.items():
            hits = re.findall(pat, js)
            if hits:
                print("    SECRET? %s x%d e.g. %.24s (verify + disclose, never use)" % (name, len(hits), hits[0]))

if __name__ == "__main__":
    main()
