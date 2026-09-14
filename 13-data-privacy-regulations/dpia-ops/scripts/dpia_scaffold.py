#!/usr/bin/env python3
"""Scaffold DPIA documents (stdlib only)."""
import argparse
from datetime import date

TPL = """# DPIA: {name} ({today})
## 1. Describe processing
FILL: flows, data, subjects, retention, vendors.
## 2. Necessity vs purpose
FILL: why needed, milder alternatives considered.
## 3. Risks (likelihood x severity to rights)
R1 FILL | R2 FILL | R3 FILL
## 4. Mitigations (owner + date each)
M1 FILL | M2 FILL
## 5. Consultation
DPO: FILL | subjects/vendors: FILL
## 6. Residual + decision
FILL proceed/redesign/escalate | review_date=FILL
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(name=args.project, today=date.today())
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s — rigor in, launch gated on it." % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
