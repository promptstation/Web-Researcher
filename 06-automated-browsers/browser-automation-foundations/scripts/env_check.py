#!/usr/bin/env python3
"""Verify Python automation stacks + browsers (stdlib only)."""
import shutil, subprocess, sys

def ver(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        line = (r.stdout + r.stderr).strip().splitlines()
        return line[0][:100] if line else "ok"
    except Exception as e:
        return "MISSING (%s)" % e

def mod(name):
    try:
        m = __import__(name)
        return getattr(m, "__version__", "installed")
    except Exception:
        return "missing"

def main():
    print("python: %s" % sys.version.split()[0])
    print("playwright: %s" % mod("playwright"))
    print("selenium: %s" % mod("selenium"))
    print("node: %s" % ("found" if shutil.which("node") else "missing"))
    for b in ["google-chrome", "chrome", "chromium", "firefox"]:
        print("%s: %s" % (b, shutil.which(b) or "missing"))
    print("pw_browsers: %s" % ver([sys.executable, "-m", "playwright", "--version"]))
    print("done. Green on your stack + one browser = ready.")

if __name__ == "__main__":
    main()
