#!/usr/bin/env python3
"""TPM decision-tree walk (stdlib only)."""
import argparse

Q = ["gate_identified", "authority_to_pass", "method_is_ordinary_use",
     "exemption_fits_all_factors", "counsel_written_go"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--answers", default="", help="comma k=yes,...")
    args = ap.parse_args()
    ans = dict(x.split("=") for x in args.answers.split(",") if "=" in x)
    print("TPM decision walk (default NO at every unsure):")
    for q in Q:
        v = ans.get(q, "unsure")
        print("  %-28s %s" % (q, v))
        if q == "gate_identified" and v != "yes":
            print("=> no gate identified: document + proceed with normal authz checks")
            return
        if q != "gate_identified" and v != "yes":
            print("=> STOP: counsel gate before any code. Log + seek alt path.")
            return
    print("=> all yes with written counsel go: file + scope tightly + proceed")

if __name__ == "__main__":
    main()
