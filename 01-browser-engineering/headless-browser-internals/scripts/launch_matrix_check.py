#!/usr/bin/env python3
"""Verify browser binaries and headless render capability (stdlib only)."""
import argparse, shutil, subprocess, sys

CANDIDATES = {
    "chrome": ["google-chrome", "chrome", "chromium", "chromium-browser"],
    "firefox": ["firefox"],
}

def run(cmd, timeout=60):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout + r.stderr)[:2000]
    except Exception as e:
        return -1, str(e)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--binary", default="chrome", choices=["chrome", "firefox"])
    args = ap.parse_args()
    exe = next((c for c in CANDIDATES[args.binary] if shutil.which(c)), None)
    if not exe:
        print("no %s binary found in PATH" % args.binary, file=sys.stderr)
        sys.exit(2)
    print("binary: %s (%s)" % (exe, shutil.which(exe)))
    code, out = run([exe, "--version"])
    print("version_rc=%s %s" % (code, out.strip().splitlines()[0] if out.strip() else ""))
    if args.binary == "chrome":
        code, out = run([exe, "--headless=new", "--disable-gpu", "--dump-dom", "about:blank"])
        print("headless_new_dump_dom_rc=%s bytes=%d" % (code, len(out)))
        code2, out2 = run([exe, "--headless=new", "--dump-dom", "about:blank"])
        print("headless_new_gl_rc=%s bytes=%d" % (code2, len(out2)))
    else:
        code, out = run([exe, "--headless", "--screenshot", "/tmp/firefox-probe.png", "about:blank"])
        print("headless_screenshot_rc=%s" % code)
    print("done. Record these lines in the launch matrix.")

if __name__ == "__main__":
    main()
