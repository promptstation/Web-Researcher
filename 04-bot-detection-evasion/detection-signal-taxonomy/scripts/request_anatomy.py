#!/usr/bin/env python3
"""Record your HTTP client emission via echo endpoint (stdlib only)."""
import argparse, json, sys, urllib.request

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="https://postman-echo.com/headers")
    ap.add_argument("--ua", default="ResearchBot/1.0 (+https://example.com/bot)")
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": args.ua,
        "From": "bot-ops@example.com", "Accept": "application/json"})
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=args.timeout).read().decode())
    except Exception as e:
        print("echo failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    print("sent_user_agent: %s" % args.ua)
    print("echoed_headers:")
    for k, v in sorted((data.get("headers") or {}).items()):
        print("  %s: %.120s" % (k, v))
    print("record this output per client version; diff after upgrades.")

if __name__ == "__main__":
    main()
