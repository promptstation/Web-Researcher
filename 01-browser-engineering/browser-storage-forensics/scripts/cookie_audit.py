#!/usr/bin/env python3
"""Audit Set-Cookie flags for a URL using only the standard library."""
import argparse, sys, urllib.request
from http.cookies import SimpleCookie

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 cookie-audit"})
    try:
        r = urllib.request.urlopen(req, timeout=args.timeout)
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    raw = r.headers.get_all("Set-Cookie") or []
    if not raw:
        print("no Set-Cookie headers on %s (final %s)" % (args.url, r.geturl()))
        return
    for h in raw:
        c = SimpleCookie()
        try:
            c.load(h)
        except Exception:
            print("UNPARSEABLE %s" % h)
            continue
        for name, m in c.items():
            flags = {"secure": bool(m.get("secure")), "httponly": bool(m.get("httponly")),
                     "samesite": m.get("samesite") or "unset",
                     "max-age": m.get("max-age") or m.get("expires") or "session",
                     "path": m.get("path") or "/", "domain": m.get("domain") or "host-only"}
            verdict = "OK" if (flags["secure"] or args.url.startswith("http://localhost")) and flags["httponly"] and flags["samesite"] != "unset" else "REVIEW"
            print("%s %s %s" % (verdict, name, flags))

if __name__ == "__main__":
    main()
