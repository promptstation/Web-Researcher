#!/usr/bin/env python3
"""Plan frame sampling: counts + storage estimate (stdlib only)."""
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=60)
    ap.add_argument("--fps", type=float, default=1)
    ap.add_argument("--kb-per-frame", type=float, default=150)
    args = ap.parse_args()
    frames = int(args.minutes * 60 * args.fps)
    print("frames=%d fps=%.2f storage~=%.1fGB" % (frames, args.fps, frames * args.kb_per_frame / 1e6))
    print("ffmpeg: -ss 0 -i in.mp4 -vf fps=%.2f,scale=1280:-2 out/%%06d.jpg" % args.fps)
    print("dedupe after extract; annotate the lean set only.")

if __name__ == "__main__":
    main()
