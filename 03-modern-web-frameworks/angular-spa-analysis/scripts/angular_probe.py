#!/usr/bin/env python3
"""Fingerprint Angular apps + surface API base hints (stdlib only)."""
import argparse, re, sys, urllib.request

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 ng-probe"})
    try:
        html = urllib.request.urlopen(req, timeout=args.timeout).read().decode("utf-8", "replace")
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    m = re.search(r'ng-version="([^"]+)"', html)
    print("ng_version: %s" % (m.group(1) if m else "not-angular-or-hidden"))
    scripts = re.findall(r'<script[^>]+src="([^"]+)"', html)
    print("scripts: %d" % len(scripts))
    for s in scripts[:15]:
        print("  %s" % s)
    apis = sorted(set(re.findall(r'https?://[A-Za-z0-9._:-]+/(?:api|gateway|v\d+)[A-Za-z0-9._/:-]*', html)))
    print("api_hints_in_html: %d" % len(apis))
    for a in apis[:15]:
        print("  %s" % a)
    print("next: fetch main chunk, grep api/gateway literals, confirm authed.")

if __name__ == "__main__":
    main()
