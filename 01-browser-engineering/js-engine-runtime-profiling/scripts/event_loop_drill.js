// Event-loop order drill. Run: node scripts/event_loop_drill.js
// Predict the print order first, then run and reconcile.
console.log("1 sync");
setTimeout(() => console.log("5 timeout-0"), 0);
Promise.resolve().then(() => console.log("3 microtask-1"));
queueMicrotask(() => console.log("4 microtask-2"));
(async () => {
  await Promise.resolve();
  console.log("3b async-resume");
})();
console.log("2 sync-end");
// Expected: 1, 2, 3, 4 (microtasks drain), 3b interleaved by enqueue order, then 5.
// Lesson: microtasks always beat timers; async resumes are microtasks.
