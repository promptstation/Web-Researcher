// Fingerprint signal probe. Paste in DevTools console, save the JSON.
// Measurement and defense only.
(async () => {
  const out = {};
  const nav = navigator;
  ["userAgent","platform","hardwareConcurrency","deviceMemory","language","languages",
   "webdriver","cookieEnabled","onLine","maxTouchPoints","pdfViewerEnabled"].forEach(k => {
    try { out[k] = nav[k]; } catch (e) { out[k] = "error"; }
  });
  out.screen = [screen.width, screen.height, screen.colorDepth, devicePixelRatio];
  out.viewport = [innerWidth, innerHeight];
  out.timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  try {
    const c = document.createElement("canvas");
    c.width = 256; c.height = 64;
    const x = c.getContext("2d");
    x.fillText("probe-text-42", 8, 32);
    x.strokeRect(4, 4, 248, 56);
    const d = c.toDataURL();
    let h = 0;
    for (let i = 0; i < d.length; i++) h = (h * 31 + d.charCodeAt(i)) >>> 0;
    out.canvasHash = h.toString(16);
  } catch (e) { out.canvasHash = "error"; }
  try {
    const gl = document.createElement("canvas").getContext("webgl");
    const dbg = gl.getExtension("WEBGL_debug_renderer_info");
    out.webgl = dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : "masked";
  } catch (e) { out.webgl = "error"; }
  console.log(JSON.stringify(out, null, 2));
  return out;
})();
