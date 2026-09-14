#!/usr/bin/env python3
"""Compare sequential/threads/asyncio/processes on simulated IO (stdlib only)."""
import argparse, asyncio, concurrent.futures, time

def job(_):
    time.sleep(0.01)
    return 1

async def ajob(_):
    await asyncio.sleep(0.01)
    return 1

async def run_async(n):
    return sum(await asyncio.gather(*[ajob(i) for i in range(n)]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=200)
    ap.add_argument("--workers", type=int, default=20)
    args = ap.parse_args()
    n, w = args.jobs, args.workers
    t = time.perf_counter()
    r = sum(job(i) for i in range(n))
    print("sequential: %.2fs (%d)" % (time.perf_counter() - t, r))
    t = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(w) as ex:
        r = sum(ex.map(job, range(n)))
    print("threads-%d: %.2fs (%d)" % (w, time.perf_counter() - t, r))
    t = time.perf_counter()
    r = asyncio.run(run_async(n))
    print("asyncio: %.2fs (%d)" % (time.perf_counter() - t, r))
    t = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(4) as ex:
        r = sum(ex.map(job, range(n)))
    print("processes-4: %.2fs (%d)" % (time.perf_counter() - t, r))
    print("rerun on YOUR workload; this shapes intuition only.")

if __name__ == "__main__":
    main()
