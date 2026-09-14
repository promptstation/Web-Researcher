// First-observation JS sandbox (Node vm). Run in a disposable VM only:
// node scripts/sandbox_run.js --file sample.js --timeout 5000
const fs = require("fs");
const vm = require("vm");
const args = process.argv.slice(2);
const file = args[args.indexOf("--file") + 1];
const timeout = parseInt(args[args.indexOf("--timeout") + 1] || "5000", 10);
const log = [];
const sink = (name) => (...a) => {
  log.push([name, JSON.stringify(a).slice(0, 300)]);
  return undefined;
};
const sandbox = {
  console: { log: sink("console.log") },
  document: { cookie: "", write: sink("document.write"), createElement: () => ({}) },
  window: {}, navigator: { userAgent: "sandbox" },
  localStorage: { getItem: () => null, setItem: sink("localStorage.set") },
  fetch: sink("fetch"), XMLHttpRequest: function () {},
  setTimeout: (fn) => 0, setInterval: () => 0,
};
sandbox.window = sandbox;
sandbox.globalThis = sandbox;
try {
  vm.createContext(sandbox);
  vm.runInContext(fs.readFileSync(file, "utf8"), sandbox, { timeout, filename: "sample.js" });
  console.log(JSON.stringify({ status: "completed", calls: log.slice(0, 100) }, null, 2));
} catch (e) {
  console.log(JSON.stringify({ status: "threw", error: String(e).slice(0, 300), calls: log.slice(0, 100) }, null, 2));
}
