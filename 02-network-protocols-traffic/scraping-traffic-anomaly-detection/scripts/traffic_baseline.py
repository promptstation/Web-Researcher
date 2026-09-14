#!/usr/bin/env python3
"""Baseline JSONL job logs; flag rate/status/latency anomalies (stdlib only)."""
import argparse, json, statistics
from collections import Counter, defaultdict

def pct(xs, p):
    return statistics.quantiles(sorted(xs), n=100)[min(99, max(0, p - 1))] if xs else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", required=True, help="JSONL with domain/outcome/latency_ms")
    ap.add_argument("--min-n", type=int, default=50)
    args = ap.parse_args()
    by_domain = defaultdict(list)
    for line in open(args.logs, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("domain"):
            by_domain[r["domain"]].append(r)
    for dom, rows in sorted(by_domain.items()):
        if len(rows) < args.min_n:
            print("%s: n=%d SKIP (<%d)" % (dom, len(rows), args.min_n))
            continue
        outcomes = Counter(r.get("outcome", "?") for r in rows)
        lat = [r.get("latency_ms", 0) for r in rows if isinstance(r.get("latency_ms"), (int, float))]
        challenges = sum(1 for r in rows if r.get("challenge_class"))
        n = len(rows)
        ok = outcomes.get("success", 0) / n
        print("%s: n=%d success=%.1f%% challenge=%.1f%% lat_p50=%d lat_p95=%d" % (
            dom, n, ok * 100, challenges / n * 100, pct(lat, 50), pct(lat, 95)))
        flags = []
        if ok < 0.85: flags.append("LOW-SUCCESS")
        if challenges / n > 0.10: flags.append("HIGH-CHALLENGE")
        if outcomes.get("retriable", 0) / n > 0.25: flags.append("HIGH-RETRY")
        if flags: print("  FLAGS: %s" % ", ".join(flags))

if __name__ == "__main__":
    main()
