#!/usr/bin/env python3
"""Adaptive throttle demo + importable controller (stdlib only)."""
import argparse, random, time

class Throttle:
    def __init__(self, rate=10.0):
        self.rate = rate
        self.min_gap = 1.0 / rate
        self.next_at = 0.0
    def wait(self):
        now = time.monotonic()
        gap = random.uniform(0, 2 * self.min_gap)
        at = max(now, self.next_at)
        time.sleep(max(0, at - now + gap * 0.1))
        self.next_at = max(now, self.next_at) + self.min_gap
    def on_success(self):
        self.min_gap = max(0.05, self.min_gap * 0.99)
    def on_throttle(self, retry_after=0.0):
        self.min_gap = min(60.0, self.min_gap * 2 + (retry_after or 0))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()
    t = Throttle(rate=5)
    for i in range(8):
        t.wait()
        if i == 4:
            t.on_throttle(retry_after=2)
            print("got-429 -> gap now %.2fs" % t.min_gap)
        else:
            t.on_success()
    print("final gap %.2fs (import Throttle in your client)" % t.min_gap)

if __name__ == "__main__":
    main()
