#!/usr/bin/env python3
"""Rehearse failure scenarios against a simulated worker (stdlib only)."""
import argparse, random

def simulate(jobs, kill_at=None, err_rate=0.0, latency_ms=0):
    done, lost, retried = 0, 0, 0
    checkpoint = 0
    for i in range(1, jobs + 1):
        if kill_at and i == kill_at:
            lost = i - 1 - checkpoint
            checkpoint = 0
            continue
        if random.random() < err_rate:
            retried += 1
            continue
        done += 1
        if i % 10 == 0:
            checkpoint = done
    return done, lost, retried

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenario", default="kill", choices=["kill", "errors", "clean"])
    ap.add_argument("--jobs", type=int, default=100)
    args = ap.parse_args()
    kill = 55 if args.scenario == "kill" else None
    err = 0.1 if args.scenario == "errors" else 0.0
    done, lost, retried = simulate(args.jobs, kill, err)
    print("scenario=%s done=%d lost=%d retried=%d" % (args.scenario, done, lost, retried))
    print("lesson: checkpoint every success; resume loses at most one window.")

if __name__ == "__main__":
    main()
