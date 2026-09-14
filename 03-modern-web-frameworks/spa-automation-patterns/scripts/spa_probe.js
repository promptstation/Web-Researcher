// SPA state probe. Paste in DevTools console on the page under test.
(() => {
  const out = {};
  out.url = location.href;
  out.readyState = document.readyState;
  out.roots = ["#__next", "#root", "#app", "[data-hydrated]"].map(s => [s, !!document.querySelector(s)]);
  out.nextData = !!document.getElementById("__NEXT_DATA__");
  out.nuxt = !!(window.__NUXT__ || document.getElementById("__NUXT_DATA__"));
  out.ng = !!document.querySelector("[ng-version]");
  const res = performance.getEntriesByType("resource");
  out.resources = res.length;
  out.pendingHints = res.filter(r => r.responseEnd === 0).length;
  out.scripts = [...document.scripts].length;
  console.log(JSON.stringify(out, null, 2));
  return out;
})();
