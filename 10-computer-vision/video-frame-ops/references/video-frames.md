# Video Frames

Sampling: uniform 1fps for coverage baselines; keyframes for scene changes; motion/frame-diff for events; task-specific (entry zones, audio cues) for efficiency. Pilot 3 strategies; annotate the leanest sufficient set.

ffmpeg: input seeking (-ss before -i) for speed, output seeking for accuracy; scale once (e.g., 1280:-2); image2 with %06d names; version commands; checksums per batch. Test seeks land on intended timestamps.

Dedupe: hash consecutive frames, keep on change threshold; near-dedupe across clips; report keep rate; annotate deduped only. Tracking: detect-then-associate (ByteTrack/OC-SORT class); ID switches and fragmentation eval; handoff policy documented; count lines calibrated.

Storage: mezzanine masters for keepers, H.264 proxies for work, thumbnails for browse; purge raw after proxy verify; cost per hour tracked; retention scheduled. Never 30fps-annotate; never mezzanine-store everything.
