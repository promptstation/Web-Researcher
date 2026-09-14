#!/usr/bin/env python3
"""Score request pacing from JSONL logs with ts field (stdlib only)."""
import argparse, json, statistics, sys
from collections import defaultdict
from datetime import datetime

def ts(v):
    try:
        return datetime.fromisoformat(str(v).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True)
    args = ap.parse_args()
    by_host = defaultdict(list)
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        t = ts(r.get("ts"))
        if t and r.get("host"):
            by_host[r["host"]].append(t)
    for host, times in sorted(by_host.items()):
        times.sort()
        gaps = [b - a for a, b in zip(times, times[1:])]
        if not gaps:
            print("%s: n=1 SKIP" % host)
            continue
        mean = statistics.mean(gaps)
        cv = (statistics.pstdev(gaps) / mean) if mean else 0
        zeros = sum(1 for g in gaps if g < 0.1)
        print("%s: n=%d gap_med=%.2fs gap_p95=%.2fs zero_runs=%d cv=%.2f" % (
            host, len(times), statistics.median(gaps),
            statistics.quantiles(sorted(gaps), n=100)[94] if len(gaps) >= 10 else max(gaps), zeros, cv))
        flags = []
        if statistics.median(gaps) < 1.0: flags.append("FAST-MEDIAN")
        if zeros > 5: flags.append("BURSTY")
        if cv < 0.2: flags.append("METRONOME")
        if flags: print("  FLAGS: %s" % ", ".join(flags))

if __name__ == "__main__":
    main()
