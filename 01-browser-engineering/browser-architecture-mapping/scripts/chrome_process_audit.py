#!/usr/bin/env python3
"""Audit local browser processes into a JSON inventory.

Reads `ps` output for chrome/firefox process types and summarizes
counts plus RSS per type. No dependencies beyond the standard library.
"""
import argparse, json, re, shutil, subprocess, sys

TYPE_RE = re.compile(r"--type=([a-z-]+)")

def collect(binary):
    if not shutil.which("ps"):
        return {"error": "ps not available on this host"}
    try:
        out = subprocess.run(["ps", "-ax", "-o", "pid=,rss=,args="],
                             capture_output=True, text=True, timeout=15)
    except Exception as e:
        return {"error": str(e)}
    procs = []
    for line in out.stdout.splitlines():
        if binary not in line:
            continue
        parts = line.strip().split(None, 2)
        if len(parts) < 3:
            continue
        pid, rss, args = parts
        m = TYPE_RE.search(args)
        ptype = m.group(1) if m else ("browser" if " --type=" not in args else "unknown")
        try:
            rss_mb = int(rss) // 1024
        except ValueError:
            rss_mb = 0
        procs.append({"pid": pid, "type": ptype, "rss_mb": rss_mb})
    by_type = {}
    for p in procs:
        d = by_type.setdefault(p["type"], {"count": 0, "rss_mb": 0})
        d["count"] += 1
        d["rss_mb"] += p["rss_mb"]
    return {"binary": binary, "processes": len(procs), "by_type": by_type,
            "sample": procs[:25]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser", default="chrome", choices=["chrome", "firefox"])
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    binary = "chrome" if args.browser == "chrome" else "firefox"
    data = collect(binary)
    text = json.dumps(data, indent=2)
    if args.out:
        open(args.out, "w").write(text)
    print(text)
    if not data.get("processes"):
        print("No %s processes found. Start the browser or record topology as unmeasured." % binary, file=sys.stderr)

if __name__ == "__main__":
    main()
