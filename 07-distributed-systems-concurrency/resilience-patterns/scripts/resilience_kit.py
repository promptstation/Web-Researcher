#!/usr/bin/env python3
"""Retry-with-jitter + deadline + circuit breaker mini-kit (stdlib only)."""
import random, time

class Breaker:
    def __init__(self, fails=5, cool=30):
        self.fails, self.cool = fails, cool
        self.n, self.open_until = 0, 0
    def allow(self):
        return time.monotonic() >= self.open_until
    def ok(self):
        self.n, self.open_until = 0, 0
    def fail(self):
        self.n += 1
        if self.n >= self.fails:
            self.open_until = time.monotonic() + self.cool

def call_with_retry(fn, attempts=4, base=0.5, cap=30, deadline=60, breaker=None):
    start = time.monotonic()
    last = None
    for i in range(attempts):
        if breaker and not breaker.allow():
            raise RuntimeError("breaker-open")
        if time.monotonic() - start > deadline:
            raise TimeoutError("deadline-exceeded")
        try:
            out = fn()
            if breaker:
                breaker.ok()
            return out
        except Exception as e:
            last = e
            if breaker:
                breaker.fail()
            wait = min(cap, base * 2 ** i) * random.random()
            time.sleep(wait)
    raise last

def main():
    state = {"n": 0}
    def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise ConnectionError("blip")
        return "ok"
    print(call_with_retry(flaky, breaker=Breaker()))
    print("patterns: copy Breaker + call_with_retry into clients; tune per dependency.")

if __name__ == "__main__":
    main()
