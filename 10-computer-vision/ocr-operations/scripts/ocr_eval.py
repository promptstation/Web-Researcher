#!/usr/bin/env python3
"""Score CER/WER between reference and hypothesis texts (stdlib only)."""
import argparse, difflib

def er(ref, hyp):
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    dist = sum(max(i2 - i1, j2 - j1) for o, i1, i2, j1, j2 in sm.get_opcodes() if o != "equal")
    return dist / max(1, len(ref))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True)
    ap.add_argument("--hyp", required=True)
    args = ap.parse_args()
    ref = open(args.ref, encoding="utf-8").read()
    hyp = open(args.hyp, encoding="utf-8").read()
    print("CER=%.2f%% WER=%.2f%% (chars=%d words=%d)" % (
        100 * er(ref, hyp), 100 * er(ref.split(), hyp.split()), len(ref), len(ref.split())))
    print("report by bucket; never single-number OCR claims.")

if __name__ == "__main__":
    main()
