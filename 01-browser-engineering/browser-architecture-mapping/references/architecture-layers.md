# Architecture Layers

Chromium topology: one browser process owns UI, navigation, and storage coordination; renderers run Blink plus V8 per site; the GPU process owns GL/Vulkan and compositing; the network service owns DNS, sockets, TLS, and cache; utility processes host audio, storage, and device work. Firefox: parent plus content, GPU, RDD, socket, and extension processes. WebKit/Safari: UI process plus web content, networking, GPU, and plugin processes.

Pipeline order: navigation request, network fetch, commit, HTML parse, CSS parse, style recalc, layout, paint record, composite, raster, display. Script can interleave at parse and after commit. First paint requires commit plus style plus one composite; interactivity requires main-thread availability.

Protocol homes: page lifecycle and rendering in CDP Page/Rendering or BiDi browsingContext; network in CDP Network/Fetch or BiDi network; input in CDP Input or BiDi input; storage in CDP Storage or BiDi storage; console and exceptions in Runtime/Log or BiDi log. WebDriver classic covers navigation plus element automation with weaker observation.

Sizing rules of thumb: measure, do not assume. Typical heavy renderers run 200-600MB; GPU 150-400MB with compositing; each idle context adds 20-60MB. Recycle browsers every 50-200 jobs depending on measured growth.
