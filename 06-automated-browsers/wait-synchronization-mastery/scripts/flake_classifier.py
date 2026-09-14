#!/usr/bin/env python3
"""Classify automation failures from JSONL logs (stdlib only)."""
import argparse, json, re
from collections import Counter

RULES = [
    ("timing", r"timeout|waiting for|exceeded|not stable|did not appear"),
    ("selector", r"strict mode|resolved to \d+|no element|locator"),
    ("network", r"net::|navigation|networkidle|abort|connection"),
    ("data", r"fixture|seed|already exists|not found in db|unique"),
    ("environment", r"browser.*crash|launch|executable|permission|disk|memory"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True)
    args = ap.parse_args()
    counts, examples = Counter(), {}
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        msg = (str(r.get("error", "")) + " " + str(r.get("message", ""))).lower()
        if not msg.strip():
            continue
        cls = "product-or-unknown"
        for name, pat in RULES:
            if re.search(pat, msg):
                cls = name
                break
        counts[cls] += 1
        examples.setdefault(cls, msg[:140])
    for cls, n in counts.most_common():
        print("%-18s %d  e.g. %.120s" % (cls, n, examples[cls]))
    print("total: %d — fix top class first, prove with repeats." % sum(counts.values()))

if __name__ == "__main__":
    main()
