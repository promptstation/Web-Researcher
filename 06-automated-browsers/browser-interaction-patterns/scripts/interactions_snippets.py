"""Playwright interaction patterns (copy-paste; needs playwright to run)."""
# Upload without dialogs:
#   page.set_input_files("#file-input", "/tmp/a.csv")
#   assert page.locator("#file-input").evaluate("el => el.files.length") == 1
# Download with event:
#   with page.expect_download() as dl:
#       page.click("#export")
#   path = dl.value.path()
# Frame-scoped action:
#   frame = page.frame_locator("iframe#pay").locator("#card")
#   frame.fill("4111111111111111")
# Popup handling:
#   with page.expect_popup() as pop:
#       page.click("#open-help")
#   assert "help" in pop.value.url
# Dialog handling:
#   page.on("dialog", lambda d: d.accept())
# Verified typing:
#   box = page.get_by_label("Email")
#   box.fill("a@b.co")
#   assert box.input_value() == "a@b.co"
PATTERNS = ["upload", "download", "frame", "popup", "dialog", "verified-fill"]
