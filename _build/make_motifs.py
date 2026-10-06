"""Original vector motifs + textures for the deck (no third-party artwork).

Outputs to 12_assets/created/:
  drum_gold_{a}.png      Dong Son-inspired concentric line pattern (gold, baked alpha)
  ribbon_red.png         flowing silk-ribbon band (transparent PNG)
  lotus_gold.png         geometric lotus line art
  paper_cream.png        warm ivory paper texture (16:9)
  paper_cream_soft.png   lighter variant
  bg_burgundy.png        cinematic dark burgundy background w/ soft light
  bg_burgundy_left.png   same, light pool on the left
  convergence.png        many different shapes -> one ring (slide 6/12 motif)
"""
import math, random, atexit
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image, ImageFilter, ImageDraw, ImageChops

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "12_assets" / "created"
OUT.mkdir(parents=True, exist_ok=True)

BURG, CRIM, RED, WARM = "#5B0808", "#7A0B0C", "#9C1214", "#C33734"
IVORY, CREAM, GOLD, GOLD2, BROWN = "#FAF5E8", "#EFE3CE", "#B68A45", "#D2AA50", "#4C3026"

_pw = sync_playwright().start()
_browser = _pw.chromium.launch(channel="msedge")
atexit.register(lambda: (_browser.close(), _pw.stop()))


def svg_png(svg, name, w, h):
    """Rasterise an SVG string with headless Edge (transparent background)."""
    page = _browser.new_page(viewport={"width": w, "height": h})
    page.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
    page.locator("svg").screenshot(path=str(OUT / name), omit_background=True)
    page.close()


# ---------------------------------------------------------------- drum motif
def drum_svg(stroke, opacity):
    c = 1200
    parts = []
    add = parts.append
    sw = 3.2

    def ring(r, w=sw):
        add(f'<circle cx="{c}" cy="{c}" r="{r}" fill="none" stroke="{stroke}" stroke-width="{w}"/>')

    # central 14-point star
    pts = []
    for i in range(28):
        ang = math.pi * i / 14 - math.pi / 2
        r = 190 if i % 2 == 0 else 62
        pts.append(f"{c + r * math.cos(ang):.1f},{c + r * math.sin(ang):.1f}")
    add(f'<polygon points="{" ".join(pts)}" fill="{stroke}" fill-opacity="0.55" stroke="{stroke}" stroke-width="{sw}"/>')
    # teardrops between rays
    for i in range(14):
        ang = math.pi * (2 * i + 1) / 14 - math.pi / 2
        x, y = c + 150 * math.cos(ang), c + 150 * math.sin(ang)
        add(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="10" ry="26" transform="rotate({math.degrees(ang) + 90:.1f} {x:.1f} {y:.1f})" fill="none" stroke="{stroke}" stroke-width="2.4"/>')
    ring(225); ring(240)
    # tangent circles band
    def tangent_band(r, n, rr):
        for i in range(n):
            ang = 2 * math.pi * i / n
            x, y = c + r * math.cos(ang), c + r * math.sin(ang)
            add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr}" fill="none" stroke="{stroke}" stroke-width="2.4"/>')
            add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr * 0.28:.1f}" fill="{stroke}"/>')
    tangent_band(270, 36, 22)
    ring(300); ring(312)
    # radial hatches
    def hatch(r1, r2, n):
        for i in range(n):
            ang = 2 * math.pi * i / n
            add(f'<line x1="{c + r1 * math.cos(ang):.1f}" y1="{c + r1 * math.sin(ang):.1f}" x2="{c + r2 * math.cos(ang):.1f}" y2="{c + r2 * math.sin(ang):.1f}" stroke="{stroke}" stroke-width="2"/>')
    hatch(318, 352, 160)
    ring(358); ring(372)
    # zigzag band
    zz = []
    n = 72
    for i in range(n * 2 + 1):
        ang = math.pi * i / n
        r = 384 if i % 2 == 0 else 424
        zz.append(f"{c + r * math.cos(ang):.1f},{c + r * math.sin(ang):.1f}")
    add(f'<polyline points="{" ".join(zz)}" fill="none" stroke="{stroke}" stroke-width="2.4"/>')
    ring(436); ring(450)
    tangent_band(480, 50, 24)
    ring(510); ring(524)
    # flying birds band (stylised, original drawing)
    nb = 14
    for i in range(nb):
        ang = 2 * math.pi * i / nb
        deg = math.degrees(ang)
        bx, by = c + 640 * math.cos(ang), c + 640 * math.sin(ang)
        bird = (
            "M -70 0 C -40 -6 20 -8 70 -2 L 110 -14 L 74 4 C 30 12 -30 12 -70 0 Z "
            "M -10 -4 C 0 -60 30 -86 60 -96 C 40 -60 30 -30 22 -6 Z "
            "M -20 6 C -14 40 -34 62 -60 74 C -46 44 -40 24 -36 6 Z "
            "M -70 0 L -96 -18 L -88 2 L -100 16 Z"
        )
        add(f'<path d="{bird}" transform="translate({bx:.1f} {by:.1f}) rotate({deg + 90:.1f}) scale(1.05)" fill="{stroke}" fill-opacity="0.6" stroke="{stroke}" stroke-width="2"/>')
    ring(760); ring(774)
    hatch(780, 812, 220)
    ring(818); ring(832)
    tangent_band(862, 70, 26)
    ring(894); ring(908, 4)
    body = "".join(parts)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="2400" viewBox="0 0 2400 2400"><g opacity="{opacity}">{body}</g></svg>'


for a in (14, 22, 35, 60):
    svg_png(drum_svg(GOLD2, a / 100), f"drum_gold_{a}.png", 2400, 2400)

# ---------------------------------------------------------------- ribbon
def ribbon_svg():
    W, H = 3840, 1100
    defs = f'''<defs>
<linearGradient id="g1" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="{BURG}"/><stop offset="0.35" stop-color="{RED}"/>
 <stop offset="0.6" stop-color="{WARM}"/><stop offset="0.85" stop-color="{RED}"/><stop offset="1" stop-color="{CRIM}"/></linearGradient>
<linearGradient id="g2" x1="0" y1="0" x2="1" y2="0.3">
 <stop offset="0" stop-color="{CRIM}"/><stop offset="0.45" stop-color="#B0201E"/><stop offset="1" stop-color="{BURG}"/></linearGradient>
<linearGradient id="hl" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="0.5" stop-color="#FFD9C8" stop-opacity="0.45"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.35"/></linearGradient>
</defs>'''
    back = f'<path d="M0 760 C 700 520 1300 980 2050 760 C 2700 570 3200 640 3840 470 L 3840 1100 L 0 1100 Z" fill="url(#g2)"/>'
    front = f'<path d="M0 900 C 800 700 1400 1060 2200 860 C 2900 690 3300 820 3840 640 L 3840 1100 L 0 1100 Z" fill="url(#g1)"/>'
    fold = f'<path d="M0 900 C 800 700 1400 1060 2200 860 C 2900 690 3300 820 3840 640 L 3840 700 C 3300 880 2900 760 2200 930 C 1400 1120 800 770 0 960 Z" fill="url(#hl)"/>'
    goldline = f'<path d="M0 742 C 700 505 1300 965 2050 745 C 2700 555 3200 625 3840 455" fill="none" stroke="{GOLD2}" stroke-width="5" stroke-opacity="0.9"/>'
    shade = f'<rect x="0" y="980" width="3840" height="120" fill="url(#sh)"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{defs}{back}{goldline}{front}{fold}{shade}</svg>'


svg_png(ribbon_svg(), "ribbon_red.png", 3840, 1100)

# ---------------------------------------------------------------- lotus
def lotus_svg(stroke):
    p = []
    sw = 7
    # centre petal
    p.append(f'<path d="M500 140 C 590 260 600 420 500 560 C 400 420 410 260 500 140 Z"/>')
    # inner side petals
    p.append(f'<path d="M500 560 C 470 420 380 300 250 250 C 250 400 330 520 500 560 Z"/>')
    p.append(f'<path d="M500 560 C 530 420 620 300 750 250 C 750 400 670 520 500 560 Z"/>')
    # outer petals
    p.append(f'<path d="M500 568 C 380 520 230 470 90 470 C 170 580 330 610 500 568 Z"/>')
    p.append(f'<path d="M500 568 C 620 520 770 470 910 470 C 830 580 670 610 500 568 Z"/>')
    # petal veins
    p.append(f'<path d="M500 200 L 500 520" />')
    p.append(f'<path d="M300 300 C 380 380 440 470 492 548" />')
    p.append(f'<path d="M700 300 C 620 380 560 470 508 548" />')
    # water lines
    p.append(f'<path d="M200 650 C 350 620 650 620 800 650" />')
    p.append(f'<path d="M300 700 C 420 680 580 680 700 700" />')
    body = "".join(x.replace("/>", f' fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>') for x in p)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="760" viewBox="0 0 1000 760">{body}</svg>'


svg_png(lotus_svg(GOLD2), "lotus_gold.png", 1000, 760)
svg_png(lotus_svg(GOLD), "lotus_antique.png", 1000, 760)

# ---------------------------------------------------------------- textures
W, H = 2400, 1350
random.seed(7)


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def noise_layer(w, h, amp, blur=0.6, seed=1):
    random.seed(seed)
    n = Image.effect_noise((w, h), amp).filter(ImageFilter.GaussianBlur(blur))
    return n


def paper(base, edge, name, fibers=True, amp=18):
    img = Image.new("RGB", (W, H), hex2rgb(base))
    # vignette toward edge colour
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((-W * 0.25, -H * 0.35, W * 1.25, H * 1.35), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(220))
    edge_img = Image.new("RGB", (W, H), hex2rgb(edge))
    img = Image.composite(img, edge_img, mask)
    # grain
    n = noise_layer(W, H, amp).convert("L")
    grain = Image.merge("RGB", (n, n, n))
    img = ImageChops.overlay(img, Image.blend(Image.new("RGB", (W, H), (128, 128, 128)), grain, 0.10))
    if fibers:
        fl = Image.new("L", (W, H), 0)
        fd = ImageDraw.Draw(fl)
        for _ in range(900):
            x, y = random.randint(0, W), random.randint(0, H)
            L = random.randint(10, 46)
            a = random.uniform(0, math.pi)
            fd.line((x, y, x + L * math.cos(a), y + L * math.sin(a)), fill=random.randint(10, 26), width=1)
        fl = fl.filter(ImageFilter.GaussianBlur(0.7))
        tint = Image.new("RGB", (W, H), hex2rgb(BROWN))
        img = Image.composite(tint, img, fl)
    img.save(OUT / name, quality=95)


paper(IVORY, CREAM, "paper_cream.png")
paper("#FCF9F1", IVORY, "paper_cream_soft.png", fibers=True, amp=12)


def dark_bg(name, cx, cy, light=CRIM, base=BURG, deep="#3A0405"):
    img = Image.new("RGB", (W, H), hex2rgb(deep))
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    r = 1500
    d.ellipse((cx - r, cy - r * 0.8, cx + r, cy + r * 0.8), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(380))
    img = Image.composite(Image.new("RGB", (W, H), hex2rgb(base)), img, m)
    m2 = Image.new("L", (W, H), 0)
    d2 = ImageDraw.Draw(m2)
    r2 = 700
    d2.ellipse((cx - r2, cy - r2 * 0.75, cx + r2, cy + r2 * 0.75), fill=200)
    m2 = m2.filter(ImageFilter.GaussianBlur(300))
    img = Image.composite(Image.new("RGB", (W, H), hex2rgb(light)), img, m2)
    n = noise_layer(W, H, 22).convert("L")
    grain = Image.merge("RGB", (n, n, n))
    img = ImageChops.overlay(img, Image.blend(Image.new("RGB", (W, H), (128, 128, 128)), grain, 0.08))
    img.save(OUT / name, quality=95)


dark_bg("bg_burgundy.png", int(W * 0.68), int(H * 0.45))
dark_bg("bg_burgundy_left.png", int(W * 0.28), int(H * 0.5))
dark_bg("bg_burgundy_center.png", int(W * 0.5), int(H * 0.42))

# ---------------------------------------------------------------- convergence motif
def convergence_svg():
    Wc, Hc = 1800, 1200
    cx, cy = 900, 600
    random.seed(11)
    cols = [IVORY, GOLD2, WARM, "#E8C9A0", "#F2D9D0", GOLD, "#D9826B"]
    els, lines = [], []
    n = 26
    for i in range(n):
        ang = 2 * math.pi * i / n + random.uniform(-0.08, 0.08)
        r = random.uniform(430, 560)
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang) * 0.82
        lines.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{cx + 150 * math.cos(ang):.0f}" y2="{cy + 150 * math.sin(ang):.0f}" stroke="{GOLD2}" stroke-width="2.4" stroke-opacity="0.75"/>')
        col = cols[i % len(cols)]
        s = random.uniform(20, 34)
        kind = i % 4
        if kind == 0:
            els.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s:.0f}" fill="{col}"/>')
        elif kind == 1:
            els.append(f'<rect x="{x - s:.0f}" y="{y - s:.0f}" width="{2 * s:.0f}" height="{2 * s:.0f}" rx="6" fill="{col}" transform="rotate({random.randint(0, 45)} {x:.0f} {y:.0f})"/>')
        elif kind == 2:
            els.append(f'<polygon points="{x:.0f},{y - s * 1.1:.0f} {x + s:.0f},{y + s * 0.8:.0f} {x - s:.0f},{y + s * 0.8:.0f}" fill="{col}"/>')
        else:
            els.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{s * 1.3:.0f}" ry="{s * 0.75:.0f}" fill="{col}"/>')
    ring = f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="{GOLD2}" stroke-width="10"/><circle cx="{cx}" cy="{cy}" r="118" fill="{GOLD2}" fill-opacity="0.18"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wc}" height="{Hc}" viewBox="0 0 {Wc} {Hc}">{"".join(lines)}{"".join(els)}{ring}</svg>'


svg_png(convergence_svg(), "convergence.png", 1800, 1200)
# ---------------------------------------------------------------- ribbon band (whole curve inside the image: no clipping edges)
def ribbon_band_svg():
    W_, H_ = 3840, 520
    defs = f'''<defs>
<linearGradient id="b1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BURG}"/><stop offset="0.5" stop-color="{CRIM}"/><stop offset="1" stop-color="{BURG}"/></linearGradient>
<linearGradient id="b2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CRIM}"/><stop offset="0.45" stop-color="{RED}"/><stop offset="0.8" stop-color="#A51A18"/><stop offset="1" stop-color="{CRIM}"/></linearGradient>
</defs>'''
    back = '<path d="M0 300 C 900 150 1700 410 2600 250 C 3200 150 3550 220 3840 140 L 3840 520 L 0 520 Z" fill="url(#b1)"/>'
    gold = f'<path d="M0 292 C 900 142 1700 402 2600 242 C 3200 142 3550 212 3840 132" fill="none" stroke="{GOLD2}" stroke-width="5"/>'
    front = '<path d="M0 390 C 1000 260 1800 470 2700 330 C 3300 240 3600 300 3840 250 L 3840 520 L 0 520 Z" fill="url(#b2)"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W_}" height="{H_}" viewBox="0 0 {W_} {H_}">{defs}{back}{gold}{front}</svg>'


svg_png(ribbon_band_svg(), "ribbon_band.png", 3840, 520)
print("motifs written")
