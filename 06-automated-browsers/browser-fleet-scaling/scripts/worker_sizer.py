#!/usr/bin/env python3
"""Size browser workers from host RAM (stdlib only)."""
import argparse, os

def host_ram_mb():
    try:
        with open("/proc/meminfo") as fh:
            for line in fh:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1]) // 1024
    except Exception:
        pass
    try:
        pages = os.sysconf("SC_PHYS_PAGES")
        size = os.sysconf("SC_PAGE_SIZE")
        return pages * size // (1024 * 1024)
    except Exception:
        return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--headroom", type=float, default=0.25)
    ap.add_argument("--context-mb", type=int, default=400)
    ap.add_argument("--browser-mb", type=int, default=300)
    args = ap.parse_args()
    ram = host_ram_mb()
    if not ram:
        print("cannot read host RAM; pass numbers manually")
        return
    usable = ram * (1 - args.headroom)
    per_browser = args.browser_mb + args.context_mb
    n = max(1, int(usable // per_browser))
    print("host_ram_mb=%d usable=%.0f context_mb=%d" % (ram, usable, args.context_mb))
    print("suggested browser workers: %d (1 context each, recycle every 100 jobs)" % n)
    print("measure real RSS on targets, then re-run with --context-mb set.")

if __name__ == "__main__":
    main()
