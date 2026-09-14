#!/usr/bin/env python3
"""Audit Playwright storageState: counts + expiries, values redacted (stdlib only)."""
import argparse, json, sys
from datetime import datetime, timezone

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    try:
        st = json.load(open(args.file, encoding="utf-8"))
    except Exception as e:
        print("parse failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    cookies = st.get("cookies", [])
    origins = st.get("origins", [])
    print("cookies: %d origins: %d" % (len(cookies), len(origins)))
    now = datetime.now(timezone.utc).timestamp()
    soon = 0
    for c in cookies:
        exp = c.get("expires", -1)
        name = c.get("name", "?")
        dom = c.get("domain", "?")
        if exp and exp > 0:
            left_h = (exp - now) / 3600
            if left_h < 24:
                soon += 1
            print("  cookie %s @%s expires_in=%.1fh %s" % (name, dom, left_h,
                  "REFRESH-SOON" if left_h < 24 else "ok"))
        else:
            print("  cookie %s @%s session-only" % (name, dom))
    for o in origins:
        print("  origin %s keys=%d" % (o.get("origin"), len(o.get("localStorage", []))))
    print("refresh_needed: %s (values never printed)" % (soon > 0))

if __name__ == "__main__":
    main()
