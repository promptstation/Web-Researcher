# Stack Setup

Playwright: pip install playwright==X plus playwright install chromium (and firefox/webkit as needed); pytest-playwright for suites. Puppeteer: npm i puppeteer@X with bundled Chrome; set PUPPETEER_SKIP_DOWNLOAD only with system Chrome pinned. Selenium: selenium==X plus matching chromedriver/geckodriver via webdriver-manager pinned.

Verification: launch headed and headless, print versions, screenshot blank, read console, close cleanly. Save transcripts per machine. Container images pin OS plus browser plus driver together.

Lifecycle template: try/finally around everything; timeouts on every wait; screenshot plus HTML on failure; trace on flake; close contexts then browsers. Teach this before any framework features.

Upgrades: branch, bump one component, run parity suite, compare artifacts, roll out or revert. Never upgrade browsers and libraries in one blind step.
