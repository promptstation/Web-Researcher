#!/usr/bin/env python3
"""Mine API endpoints from page + JS chunks (stdlib only)."""
import argparse, re, sys, urllib.request

EP = re.compile(r'["\']((?:https?://[A-Za-z0-9._:-]+)?/(?:api|graphql|v\d+|rest)[A-Za-z0-9._/{}:?=&,%$-]*)["\']')

def fetch(url, timeout, cap=400000):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 api-mapper"})
    return urllib.request.urlopen(req, timeout=timeout).read(cap).decode("utf-8", "replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--max-js", type=int, default=6)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    try:
        html = fetch(args.url, args.timeout)
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    found = {}
    for m in EP.findall(html):
        found[m] = found.get(m, 0) + 2
    scripts = re.findall(r'<script[^>]+src="([^"]+\.js[^"]*)"', html)[:args.max_js]
    for s in scripts:
        u = urllib.request.urljoin(args.url, s)
        try:
            js = fetch(u, args.timeout)
        except Exception:
            continue
        for m in EP.findall(js):
            found[m] = found.get(m, 0) + 1
    for ep, score in sorted(found.items(), key=lambda kv: -kv[1])[:40]:
        print("%d %s" % (score, ep))
    print("candidates: %d (verify live before documenting)" % len(found))

if __name__ == "__main__":
    main()
