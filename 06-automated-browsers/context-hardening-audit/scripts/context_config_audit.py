#!/usr/bin/env python3
"""Audit browser context configs for tuple coherence (stdlib only)."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="JSON list of context dicts")
    args = ap.parse_args()
    try:
        cfgs = json.load(open(args.config, encoding="utf-8"))
    except Exception as e:
        print("parse failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    bad = 0
    for i, c in enumerate(cfgs):
        issues = []
        ua, plat = c.get("user_agent", ""), c.get("platform", "")
        if plat and plat.lower() not in ua.lower():
            issues.append("platform-vs-ua")
        loc, tz = c.get("locale", ""), c.get("timezone", "")
        if loc and tz and loc.split("-")[-1].lower() not in tz.lower().replace("_", " "):
            issues.append("locale-vs-timezone?(verify)")
        vp = c.get("viewport", {})
        if vp and (vp.get("width", 0) < 300 or vp.get("height", 0) < 300):
            issues.append("tiny-viewport")
        if c.get("is_mobile") and not c.get("has_touch"):
            issues.append("mobile-without-touch")
        print("context %d (%s): %s" % (i, c.get("name", "?"), issues or ["OK"]))
        bad += bool(issues)
    print("mismatched: %d/%d" % (bad, len(cfgs)))

if __name__ == "__main__":
    main()
