#!/usr/bin/env python3
"""List CDP targets from a debugging endpoint (stdlib only)."""
import argparse, json, sys, urllib.request

def get(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--timeout", type=int, default=10)
    args = ap.parse_args()
    base = "http://%s:%d" % (args.host, args.port)
    try:
        ver = get(base + "/json/version", args.timeout)
        print("browser: %s" % ver.get("Browser", "?"))
        print("protocol: %s" % ver.get("Protocol-Version", "?"))
        targets = get(base + "/json/list", args.timeout)
    except Exception as e:
        print("endpoint unreachable: %s" % e, file=sys.stderr)
        print("Launch with: chrome --remote-debugging-port=%d --user-data-dir=/tmp/cdp-profile" % args.port)
        sys.exit(2)
    for t in targets:
        print("- %s | %s | %s" % (t.get("type"), (t.get("title") or "")[:60], (t.get("url") or "")[:100]))

if __name__ == "__main__":
    main()
