"""Walk through Unity Lab headlessly (system Edge) and screenshot every screen.

Usage: python _build/shoot_unitylab.py [outdir] [--choices 1,2,0]
Serves 03_UnityLab on a throwaway local port, so it works without any other server.
Also writes the phone-mockup source screenshot used on slide 11.
"""
import sys, threading, functools, http.server, socketserver
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "03_UnityLab"
out = Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else ROOT / "_build" / "shots"
out.mkdir(parents=True, exist_ok=True)
picks = [1, 2, 0]
if "--choices" in sys.argv:
    picks = [int(x) for x in sys.argv[sys.argv.index("--choices") + 1].split(",")]

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
Handler.log_message = lambda *a, **k: None
httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), Handler)
port = httpd.server_address[1]
threading.Thread(target=httpd.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}/index.html"

errors = []
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=3, is_mobile=True, has_touch=True)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.set_default_timeout(90000)
    pg.goto(base)
    pg.wait_for_function("document.fonts.status === 'loaded'")
    pg.wait_for_timeout(3500)  # hero entrance animation
    pg.screenshot(path=str(out / "00_home.png"))
    pg.click("#start"); pg.wait_for_timeout(2000)  # wipe transition + entrance
    pg.screenshot(path=str(out / "01_warmup.png"), full_page=True)
    pg.click('.poll .choice[data-k="A"]'); pg.wait_for_timeout(2000)
    for n, pick in enumerate(picks, 1):
        pg.screenshot(path=str(out / f"{n:02d}a_case.png"), full_page=True)
        pg.click(f'.choices .choice[data-i="{pick}"]'); pg.wait_for_timeout(2000)
        print(f"case {n}: scrollY after answering = {pg.evaluate('window.scrollY')}")  # must be 0 (screen starts at top)
        pg.click("details.others summary"); pg.wait_for_timeout(200)
        pg.evaluate("window.scrollTo(0, 0)"); pg.wait_for_timeout(150)  # clicking the summary scrolled the page; reset for the capture
        pg.screenshot(path=str(out / f"{n:02d}b_feedback.png"), full_page=True)
        pg.click("#next"); pg.wait_for_timeout(2000)
    pg.wait_for_timeout(2500)  # badge + confetti
    pg.screenshot(path=str(out / "04_result.png"), full_page=True)
    pg.click('#poll2 .choice[data-k="B"]'); pg.wait_for_timeout(800)
    pg.screenshot(path=str(out / "04_result_after_poll.png"), full_page=True)
    # presenter mode (needs Internet for the QR library)
    pg2 = b.new_page(viewport={"width": 1440, "height": 900})
    pg2.on("pageerror", lambda e: errors.append(str(e)))
    pg2.set_default_timeout(90000)
    pg2.goto(base + "?present")
    pg2.wait_for_timeout(3500)
    pg2.screenshot(path=str(out / "05_presenter.png"))
    b.close()
httpd.shutdown()
print("screens ->", out)
print("errors:", errors or "none")
