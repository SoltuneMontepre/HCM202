"""Screenshot the Unity Lab landing page while scrolling (phone + desktop) and play the game once.

    python _build/shoot_landing.py [URL] [OUTDIR]

Default URL: http://localhost:8765/ (start it with: python -m http.server 8765 --directory 03_UnityLab).
Prints any JavaScript errors; exits 1 if there were some.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8765/"
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else Path(__file__).resolve().parent / "shots_landing")
OUT.mkdir(parents=True, exist_ok=True)
errors = []


def frames(pg, prefix, step, count, wait=900):
    h = pg.evaluate("document.documentElement.scrollHeight")
    print(f"{prefix}: page height {h}px")
    for k in range(count):
        y = k * step
        if y > h:
            break
        pg.mouse.wheel(0, step if k else 0)
        pg.wait_for_timeout(wait)
        pg.screenshot(path=str(OUT / f"{prefix}_{k:02d}.png"))


with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    # ---- phone
    ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(f"phone: {e}"))
    pg.on("console", lambda m: errors.append(f"phone console: {m.text}") if m.type == "error" else None)
    pg.goto(URL, wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(600)
    pg.screenshot(path=str(OUT / "phone_intro_mid.png"))
    pg.wait_for_timeout(2600)
    pg.screenshot(path=str(OUT / "phone_hero.png"))
    print("libs:", pg.evaluate("({gsap: !!window.gsap, st: !!window.ScrollTrigger, split: !!window.SplitText, lenis: !!window.Lenis, confetti: !!window.confetti, anim: document.documentElement.classList.contains('anim')})"))
    # scroll with touch-like wheel steps
    for k in range(1, 26):
        pg.evaluate("window.scrollBy(0, 560)")
        pg.wait_for_timeout(750)
        pg.screenshot(path=str(OUT / f"phone_scroll_{k:02d}.png"))
    print("phone scrollHeight:", pg.evaluate("document.documentElement.scrollHeight"))
    # play the game
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(500)
    pg.click("#start"); pg.wait_for_timeout(250)
    pg.screenshot(path=str(OUT / "phone_wipe.png"))
    pg.wait_for_timeout(1400)
    pg.screenshot(path=str(OUT / "phone_warmup.png"))
    pg.click('.poll .choice[data-k="B"]'); pg.wait_for_timeout(1800)
    for n in range(3):
        pg.screenshot(path=str(OUT / f"phone_case{n+1}.png"))
        pg.click(f'.choices .choice[data-i="{(n + 1) % 3}"]'); pg.wait_for_timeout(1800)
        pg.screenshot(path=str(OUT / f"phone_feedback{n+1}.png"))
        pg.click("#next"); pg.wait_for_timeout(1900)
    pg.wait_for_timeout(1500)
    pg.screenshot(path=str(OUT / "phone_result.png"))
    pg.screenshot(path=str(OUT / "phone_result_full.png"), full_page=True)
    ctx.close()
    # ---- desktop
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(f"desktop: {e}"))
    pg.on("console", lambda m: errors.append(f"desktop console: {m.text}") if m.type == "error" else None)
    pg.goto(URL, wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(3200)
    pg.screenshot(path=str(OUT / "desk_hero.png"))
    for k in range(1, 22):
        pg.mouse.wheel(0, 700)
        pg.wait_for_timeout(900)
        pg.screenshot(path=str(OUT / f"desk_scroll_{k:02d}.png"))
    pg.goto(URL + "?present", wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(3000)
    pg.screenshot(path=str(OUT / "desk_present.png"))
    ctx.close()
    # ---- reduced motion (phone): everything must be visible without animation
    ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=1, reduced_motion="reduce")
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(f"reduced: {e}"))
    pg.goto(URL, wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(800)
    pg.screenshot(path=str(OUT / "reduced_full.png"), full_page=True)
    ctx.close()
    b.close()

print("screens ->", OUT)
print("errors:", errors or "none")
sys.exit(1 if errors else 0)
