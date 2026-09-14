#!/usr/bin/env python3
"""Grade browser security headers for one route (stdlib only)."""
import argparse, sys, urllib.request

CHECKS = ["Content-Security-Policy", "Strict-Transport-Security",
          "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy",
          "Cross-Origin-Opener-Policy", "Cross-Origin-Resource-Policy",
          "Access-Control-Allow-Origin"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 sec-audit"})
    try:
        r = urllib.request.urlopen(req, timeout=args.timeout)
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    h = dict(r.headers.items())
    print("final: %s status: %s" % (r.geturl(), r.status))
    for c in CHECKS:
        v = h.get(c)
        print("%s %s: %s" % ("OK " if v else "MISS", c, (v or "")[:160]))
    csp = h.get("Content-Security-Policy", "")
    if "'unsafe-inline'" in csp and "nonce-" not in csp:
        print("WARN CSP allows unsafe-inline without nonces")
    if h.get("Access-Control-Allow-Origin") == "*" and h.get("Access-Control-Allow-Credentials") == "true":
        print("WARN wildcard ACAO combined with credentials will fail")

if __name__ == "__main__":
    main()
