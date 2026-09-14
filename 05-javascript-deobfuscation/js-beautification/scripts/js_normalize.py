#!/usr/bin/env python3
"""Brace-aware JS formatter for review baselines (stdlib only)."""
import argparse

def fmt(src):
    out, ind, i, n = [], 0, 0, len(src)
    buf = ""
    S = None  # string delimiter state
    while i < n:
        ch = src[i]
        nxt = src[i:i+2]
        if S:
            buf += ch
            if ch == "\\":
                buf += src[i+1] if i + 1 < n else ""
                i += 2
                continue
            if ch == S:
                S = None
            i += 1
            continue
        if ch in "'\"`":
            S = ch
            buf += ch
            i += 1
            continue
        if nxt == "//":
            j = src.find("\n", i)
            buf += src[i:j if j > 0 else n]
            i = j if j > 0 else n
            continue
        if ch == "{":
            out.append("  " * ind + (buf.strip() + " {").strip())
            buf = ""
            ind += 1
            i += 1
            continue
        if ch == "}":
            if buf.strip():
                out.append("  " * ind + buf.strip())
                buf = ""
            ind = max(0, ind - 1)
            out.append("  " * ind + "}")
            i += 1
            continue
        if ch == ";":
            buf += ";"
            out.append("  " * ind + buf.strip())
            buf = ""
            i += 1
            continue
        buf += ch
        i += 1
    if buf.strip():
        out.append("  " * ind + buf.strip())
    return "\n".join(out) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    res = fmt(open(args.file, encoding="utf-8", errors="replace").read())
    if args.out:
        open(args.out, "w").write(res)
    else:
        print(res[:6000])

if __name__ == "__main__":
    main()
