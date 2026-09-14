#!/usr/bin/env python3
"""Cross-process file lock demo, POSIX + Windows (stdlib only)."""
import argparse, os, sys, time

def locker(path, timeout):
    fh = open(path, "w")
    start = time.monotonic()
    while True:
        try:
            if sys.platform == "win32":
                import msvcrt
                msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return fh
        except OSError:
            if time.monotonic() - start > timeout:
                raise TimeoutError("lock-busy")
            time.sleep(0.1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="/tmp/coord.lock")
    ap.add_argument("--hold", type=float, default=2)
    ap.add_argument("--timeout", type=float, default=10)
    args = ap.parse_args()
    fh = locker(args.file, args.timeout)
    print("locked %s pid=%d" % (args.file, os.getpid()))
    try:
        time.sleep(args.hold)
    finally:
        fh.close()
    print("released; run twice concurrently to see mutual exclusion.")

if __name__ == "__main__":
    main()
