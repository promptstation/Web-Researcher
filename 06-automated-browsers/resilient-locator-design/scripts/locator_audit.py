#!/usr/bin/env python3
"""Score locator health of saved HTML (stdlib only)."""
import argparse
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.n = {"elements": 0, "with_id": 0, "with_testid": 0, "buttons": 0,
                  "inputs": 0, "inputs_labeled": 0}
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.n["elements"] += 1
        if a.get("id"):
            self.n["with_id"] += 1
        if a.get("data-testid") or a.get("data-test"):
            self.n["with_testid"] += 1
        if tag == "button":
            self.n["buttons"] += 1
        if tag == "input":
            self.n["inputs"] += 1
            if a.get("id") or a.get("aria-label") or a.get("name"):
                self.n["inputs_labeled"] += 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    p = P()
    p.feed(open(args.file, encoding="utf-8", errors="replace").read())
    n = p.n
    print("elements: %d with_id: %d testid: %d" % (n["elements"], n["with_id"], n["with_testid"]))
    print("buttons: %d inputs: %d labeled_inputs: %d" % (n["buttons"], n["inputs"], n["inputs_labeled"]))
    cov = 100 * n["with_testid"] / max(1, n["elements"])
    print("testid_coverage: %.1f%% %s" % (cov, "HEALTHY" if cov > 3 else "ADD-HOOKS"))
    print("next: rewrite lowest-ladder selectors first; verify uniqueness live.")

if __name__ == "__main__":
    main()
