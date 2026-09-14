#!/usr/bin/env python3
"""Validate cron specs and preview next runs (stdlib only, UTC)."""
import argparse
from datetime import datetime, timedelta

def parse_field(f, lo, hi):
    if f == "*":
        return set(range(lo, hi + 1))
    out = set()
    for part in f.split(","):
        step = 1
        if "/" in part:
            part, step = part.split("/")
            step = int(step)
        if part == "*":
            a, b = lo, hi
        elif "-" in part:
            a, b = map(int, part.split("-"))
        else:
            a = b = int(part)
        out.update(range(a, b + 1, step))
    if not out or min(out) < lo or max(out) > hi:
        raise ValueError("out of range")
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True, help="'min hour dom mon dow'")
    ap.add_argument("--count", type=int, default=5)
    args = ap.parse_args()
    try:
        mi, hr, dm, mo, dw = args.spec.split()
        M = parse_field(mi, 0, 59); H = parse_field(hr, 0, 23)
        DM = parse_field(dm, 1, 31); MO = parse_field(mo, 1, 12); DW = parse_field(dw, 0, 6)
    except Exception as e:
        print("INVALID: %s" % e)
        return
    print("VALID (UTC). Next runs:")
    t = datetime.utcnow().replace(second=0, microsecond=0)
    shown = 0
    while shown < args.count and t < datetime.utcnow() + timedelta(days=370):
        t += timedelta(minutes=1)
        if t.minute in M and t.hour in H and t.day in DM and t.month in MO and t.weekday() in DW:
            print("  " + t.strftime("%Y-%m-%d %H:%M UTC"))
            shown += 1

if __name__ == "__main__":
    main()
