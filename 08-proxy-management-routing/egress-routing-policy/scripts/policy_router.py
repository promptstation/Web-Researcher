#!/usr/bin/env python3
"""Prototype ordered policy routing (stdlib only)."""
import argparse, json

def route(table, req):
    for rule in table["rules"]:
        m = rule.get("match", {})
        if all(req.get(k) == v for k, v in m.items()):
            return rule["pool"], rule.get("name", "?")
    return table.get("default", "none"), "default"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", required=True)
    ap.add_argument("--req", default='{"class":"bulk","geo":"any","sensitive":false}')
    args = ap.parse_args()
    table = json.load(open(args.table, encoding="utf-8"))
    req = json.loads(args.req)
    pool, rule = route(table, req)
    print("req=%s -> pool=%s via=%s" % (req, pool, rule))
    print("table rules=%d default=%s" % (len(table.get("rules", [])), table.get("default")))

if __name__ == "__main__":
    main()
