#!/usr/bin/env python3
"""Token bucket limiter demo (stdlib only)."""
import argparse, time

class Bucket:
    def __init__(self, rate, capacity):
        self.rate, self.cap = rate, capacity
        self.tokens, self.t = capacity, time.monotonic()
    def take(self, n=1):
        now = time.monotonic()
        self.tokens = min(self.cap, self.tokens + (now - self.t) * self.rate)
        self.t = now
        if self.tokens >= n:
            self.tokens -= n
            return 0.0
        wait = (n - self.tokens) / self.rate
        return wait

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rate", type=float, default=5)
    ap.add_argument("--burst", type=float, default=10)
    ap.add_argument("--takes", type=int, default=20)
    args = ap.parse_args()
    b = Bucket(args.rate, args.burst)
    waits = 0
    for _ in range(args.takes):
        w = b.take()
        if w > 0:
            waits += 1
            time.sleep(w)
    print("takes=%d rate=%.1f burst=%.0f waited=%d" % (args.takes, args.rate, args.burst, waits))
    print("shape: burst instant, then sustained rate; copy this class into clients.")

if __name__ == "__main__":
    main()
