#!/usr/bin/env python3
"""Classify JS obfuscation from static fingerprints (stdlib only)."""
import argparse, hashlib, math, re
from collections import Counter

def entropy(s):
    if not s:
        return 0.0
    c = Counter(s)
    return -sum((v / len(s)) * math.log2(v / len(s)) for v in c.values())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    src = open(args.file, encoding="utf-8", errors="replace").read()
    print("sha256: %s" % hashlib.sha256(src.encode()).hexdigest())
    print("bytes: %d entropy: %.2f" % (len(src), entropy(src)))
    ids = re.findall(r"[_$a-zA-Z][_$a-zA-Z0-9]*", src)
    hexids = [i for i in ids if re.fullmatch(r"_0x[a-f0-9]+", i)]
    print("identifiers: %d hex_like: %d (%.0f%%)" % (len(ids), len(hexids), 100 * len(hexids) / max(1, len(ids))))
    print("string_array: %s" % bool(re.search(r"var\s+_0x[a-f0-9]+\s*=\s*\[", src)))
    print("rotation_iife: %s" % bool(re.search(r"\(function\(_0x", src)))
    print("packer_eval: %s" % bool(re.search(r"eval\(function\(p,a,c,k,e", src)))
    print("debugger_stmts: %d" % len(re.findall(r"\bdebugger\b", src)))
    print("fromCharCode_chains: %d" % len(re.findall(r"fromCharCode", src)))
    print("verdict: %s" % ("string-array-obfuscated" if hexids and "var _0x" in src else
          "packed" if "eval(function(p,a,c,k,e" in src else
          "minified-or-plain" if len(hexids) < 20 else "suspicious-mangled"))

if __name__ == "__main__":
    main()
