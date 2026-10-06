"""Turn downloaded photos (12_assets/downloaded) into slide-ready images (12_assets/processed).

Driven by _build/image_manifest.py:
    MANIFEST = { key: dict(src="file.jpg", treat="sepia|duotone|warm|none", box=(w_in, h_in),
                           focus=(fx, fy), fade=("left", 0.0, 0.35, "5B0808") | None,
                           caption="…", credit="…") }
    MOSAIC   = [ ("file.jpg", (fx, fy)), ... ]   # tiles for the "ĐẠI" photo mosaic (slide 5)
Never stretches: every output is a cover-crop at the target box ratio.
Writes 12_assets/processed/captions.py for the deck builder.
"""
import sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import imgfx as fx
from image_manifest import MANIFEST, MOSAIC, MOSAIC_CAPTION

ROOT = Path(__file__).resolve().parents[1]
DL = ROOT / "12_assets" / "downloaded"
OUT = ROOT / "12_assets" / "processed"
OUT.mkdir(parents=True, exist_ok=True)
PPI = 220  # output pixels per inch of slide box (enough for 1080p projection, sharp in PDF)


def process(key, spec):
    im = fx.load(DL / spec["src"])
    if spec.get("precrop"):
        l, t, r, b = spec["precrop"]
        im = im.crop((int(im.width * l), int(im.height * t), int(im.width * (1 - r)), int(im.height * (1 - b))))
    bw, bh = spec["box"]
    tw, th = int(bw * PPI), int(bh * PPI)
    # upscale guard: never upscale beyond 1.15x of the source's useful size
    scale_need = max(tw / im.width, th / im.height)
    if scale_need > 1.15:
        tw, th = int(tw / scale_need * 1.15), int(th / scale_need * 1.15)
    out = fx.cover(im, tw, th, spec.get("focus", (0.5, 0.5)))
    t = spec.get("treat", "none")
    if t == "sepia":
        out = fx.sepia(out)
    elif t == "duotone":
        out = fx.duotone(out, dark=spec.get("dark", "#2A0303"), mid=spec.get("mid", "#8E1A16"), light=spec.get("light", "#F6E7CF"),
                         contrast=spec.get("contrast", 1.12))
    elif t == "warm":
        out = fx.warm_grade(out, amount=spec.get("amount", 0.16))
    if spec.get("vignette"):
        out = fx.vignette(out, spec["vignette"])
    if spec.get("brightness"):
        from PIL import ImageEnhance
        out = ImageEnhance.Brightness(out).enhance(spec["brightness"])
    if spec.get("fade"):
        side, a, b, col = spec["fade"]
        out = fx.fade_edge(out, side, a, b, "#" + col)
    if spec.get("alpha_fade"):  # transparent edge -> PNG, so motifs behind show through without a seam
        out = fx.alpha_fade(out, *spec["alpha_fade"])
        out.save(OUT / f"{key}.png", optimize=True)
        (OUT / f"{key}.jpg").unlink(missing_ok=True)
    else:
        out.save(OUT / f"{key}.jpg", quality=90, optimize=True)
        (OUT / f"{key}.png").unlink(missing_ok=True)
    print(f"{key:12s} {spec['src'][:48]:48s} -> {out.size} ({t})")


def mosaic():
    """Per-letter photo tiling of "ĐẠI": Đ 2x2, Ạ 2x2 (+ its dot), I 1x3 — each tile cover-cropped to its cell."""
    from PIL import ImageFont, ImageDraw, ImageFilter
    text, fsize = "ĐẠI", 1420
    font = ImageFont.truetype(str(Path(__file__).resolve().parents[1] / "12_assets/fonts/src/Phudu-w900.ttf"), fsize)  # same face as the slide titles
    W_, H_ = 2700, 1500
    tmp = Image.new("L", (W_, H_), 0)
    d = ImageDraw.Draw(tmp)
    bb = d.textbbox((0, 0), text, font=font)
    ox, oy = (W_ - (bb[2] - bb[0])) / 2 - bb[0], (H_ - (bb[3] - bb[1])) / 2 - bb[1]
    mask = Image.new("L", (W_, H_), 0)
    ImageDraw.Draw(mask).text((ox, oy), text, font=font, fill=255)
    ascent = font.getmetrics()[0]
    baseline = oy + ascent
    def _tile(entry):
        f, foc = entry[0], entry[1]
        im = fx.load(DL / f, max_side=2400)
        if len(entry) > 2:
            l, t, r, b = entry[2]
            im = im.crop((int(im.width * l), int(im.height * t), int(im.width * r), int(im.height * b)))
        return im, foc
    tiles = [_tile(e) for e in MOSAIC]
    coll = Image.new("RGB", (W_, H_), (60, 10, 10))
    k = 0
    layout = {0: (2, 2), 1: (2, 2), 2: (3, 1)}  # rows, cols per letter
    for i, ch in enumerate(text):
        x0 = ox + font.getlength(text[:i])
        cb = ImageDraw.Draw(tmp).textbbox((x0, oy), ch, font=font)
        top, bottom = cb[1], min(cb[3], baseline + 8)
        rows, cols = layout[i]
        cw, chh = (cb[2] - cb[0]) / cols, (bottom - top) / rows
        for r in range(rows):
            for c in range(cols):
                im, foc = tiles[k]; k += 1
                w, h = int(cw) + 2, int(chh) + 2
                coll.paste(fx.cover(im, w, h, foc), (int(cb[0] + c * cw), int(top + r * chh)))
        if ch == "Ạ":  # dot below the A
            im, foc = tiles[k]; k += 1
            dot_top = baseline + 8
            db = mask.crop((int(cb[0]), int(dot_top), int(cb[2]), int(cb[3]) + 4)).getbbox()
            dx0, dy0 = int(cb[0]) + db[0] - 2, int(dot_top) + db[1] - 2
            coll.paste(fx.cover(im, db[2] - db[0] + 4, db[3] - db[1] + 4, foc), (dx0, dy0))
    coll = Image.blend(coll, fx.ImageChops.soft_light(coll, Image.new("RGB", coll.size, (122, 11, 12))), 0.3)
    out = Image.new("RGBA", (W_, H_), (0, 0, 0, 0))
    out.paste(coll, (0, 0), mask)
    edge = mask.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(5))
    out.paste(Image.new("RGBA", (W_, H_), (210, 170, 80, 255)), (0, 0), edge)
    out = out.crop(out.getbbox())
    out.save(OUT / "mosaic.png", optimize=True)
    print("mosaic", out.size, "tiles used", k)


def phone():
    shot = ROOT / "_build" / "shots" / "00_home.png"
    if shot.exists():
        m = fx.phone_mockup(Image.open(shot))
        m.save(OUT / "s11_phone.png", optimize=True)
        print("phone mockup", m.size)


if __name__ == "__main__":
    for k, spec in MANIFEST.items():
        process(k, spec)
    if MOSAIC:
        mosaic()
    phone()
    caps = {k: v.get("caption", "") for k, v in MANIFEST.items()}
    caps["mosaic"] = MOSAIC_CAPTION
    (OUT / "captions.py").write_text("CAPTIONS = " + repr(caps) + "\n", encoding="utf-8")
    print("captions written")
