"""Original geometric hand icons: hand_1..hand_5 (raised finger count), burgundy + gold variants."""
from pathlib import Path
from playwright.sync_api import sync_playwright
OUT = Path(__file__).resolve().parents[1] / "12_assets" / "created"

def hand_svg(n, fill, stroke, thumb):
    fingers = [  # x, width, raised top y
        (46, 26, 34), (78, 26, 20), (110, 26, 32), (142, 22, 58)]
    parts = []
    for i, (x, w, top) in enumerate(fingers):
        up = i < min(n, 4)
        y = top if up else 112
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{150 - y}" rx="{w/2}" fill="{fill}"/>')
    # palm
    parts.append(f'<rect x="40" y="118" width="130" height="118" rx="34" fill="{fill}"/>')
    # thumb
    if n >= 5:
        parts.append(f'<rect x="14" y="128" width="26" height="92" rx="13" transform="rotate(-32 27 174)" fill="{fill}"/>')
    else:
        parts.append(f'<rect x="38" y="148" width="74" height="26" rx="13" fill="{thumb}"/>')
    # knuckle line accents

    return f'<svg xmlns="http://www.w3.org/2000/svg" width="210" height="250" viewBox="-10 0 200 250">{"".join(parts)}</svg>'

with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    for n in range(1, 6):
        for tag, fill, stroke, thumb in (("burg", "#5B0808", "#D2AA50", "#8E1A16"), ("gold", "#D2AA50", "#5B0808", "#B68A45")):
            pg = b.new_page(viewport={"width": 210, "height": 250}, device_scale_factor=4)
            pg.set_content(f'<html><body style="margin:0;background:transparent">{hand_svg(n, fill, stroke, thumb)}</body></html>')
            pg.locator("svg").screenshot(path=str(OUT / f"hand_{n}_{tag}.png"), omit_background=True)
            pg.close()
    b.close()
print("hands ok")
