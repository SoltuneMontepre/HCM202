"""Photographic treatments (Pillow) — duotone, sepia, edge fades, text mosaics, phone mockup.
All functions keep aspect ratio; nothing is stretched."""
import math
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFilter, ImageFont, ImageEnhance, ImageChops


def hx(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def load(path, max_side=None):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im).convert("RGB")
    if max_side and max(im.size) > max_side:
        im.thumbnail((max_side, max_side), Image.LANCZOS)
    return im


def _lut(stops):
    """stops: list of (pos 0..255, (r,g,b)) -> 3 x 256 LUT"""
    lut = [[], [], []]
    for v in range(256):
        for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
            if p0 <= v <= p1:
                t = (v - p0) / max(p1 - p0, 1)
                for k in range(3):
                    lut[k].append(int(c0[k] + (c1[k] - c0[k]) * t))
                break
    return lut


def duotone(im, dark="#2A0303", mid="#9C1214", light="#F6E7CF", contrast=1.15, brightness=1.0):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(contrast)
    if brightness != 1.0:
        g = ImageEnhance.Brightness(g).enhance(brightness)
    stops = [(0, hx(dark)), (128, hx(mid)), (255, hx(light))] if mid else [(0, hx(dark)), (255, hx(light))]
    lut = _lut(stops)
    return Image.merge("RGB", [g.point(lut[0]), g.point(lut[1]), g.point(lut[2])])


def sepia(im, dark="#2B1A12", light="#F3E6CC", contrast=1.08):
    return duotone(im, dark=dark, mid="#8A6A4A", light=light, contrast=contrast)


def warm_grade(im, amount=0.18, tint="#7A0B0C"):
    """Gentle warm/red grade for colour photos (keeps them natural)."""
    overlay = Image.new("RGB", im.size, hx(tint))
    return Image.blend(im, ImageChops.soft_light(im, overlay), amount)


def fade_edge(im, side="left", start=0.0, end=0.45, color="#5B0808", power=1.4):
    """Blend the image into a flat colour toward one side (soft mask baked in)."""
    mask = fade_mask(im.size, side, start, end, power)
    flat = Image.new("RGB", im.size, hx(color))
    return Image.composite(flat, im, mask)


def alpha_fade(im, side="left", start=0.0, end=0.4, power=1.4):
    """Return RGBA: fully transparent at `side`, opaque from `end` inward (no hard edge on the slide)."""
    from PIL import ImageChops
    mask = fade_mask(im.size, side, start, end, power)
    out = im.convert("RGBA")
    out.putalpha(ImageChops.invert(mask))
    return out


def fade_mask(size, side="left", start=0.0, end=0.45, power=1.4):
    w, h = size
    mask = Image.new("L", (w, h), 0)
    px = mask.load()
    n = w if side in ("left", "right") else h
    vals = []
    for i in range(n):
        t = i / (n - 1)
        if side in ("left", "top"):
            d = t
        else:
            d = 1 - t
        if d <= start:
            a = 255
        elif d >= end:
            a = 0
        else:
            a = int(255 * (1 - (d - start) / (end - start)) ** power)
        vals.append(a)
    row = Image.new("L", (n, 1))
    row.putdata(vals)
    if side in ("left", "right"):
        mask = row.resize((w, h))
    else:
        mask = row.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT).resize((w, h))
    return mask


def vignette(im, strength=0.45, color="#000000"):
    w, h = im.size
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    d.ellipse((-w * 0.2, -h * 0.25, w * 1.2, h * 1.25), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(min(w, h) * 0.18))
    m = ImageOps.invert(m).point(lambda v: int(v * strength))
    return Image.composite(Image.new("RGB", (w, h), hx(color)), im, m)


def cover(im, w, h, focus=(0.5, 0.5)):
    """Crop+scale to exactly w x h (object-fit: cover)."""
    iw, ih = im.size
    s = max(w / iw, h / ih)
    nw, nh = int(math.ceil(iw * s)), int(math.ceil(ih * s))
    im2 = im.resize((nw, nh), Image.LANCZOS)
    x = int(min(max(focus[0] * nw - w / 2, 0), nw - w))
    y = int(min(max(focus[1] * nh - h / 2, 0), nh - h))
    return im2.crop((x, y, x + w, y + h))


def text_mosaic(text, font_path, tiles, out_w, out_h, font_size=None, cols=4, gap=0, tint=None, bg=None, outline=None):
    """Fill the glyph shapes of `text` with a grid collage of photos (tiles: list of (PIL image, focus)).
    Returns RGBA image (transparent outside letters)."""
    font_size = font_size or int(out_h * 0.95)
    font = ImageFont.truetype(font_path, font_size)
    mask = Image.new("L", (out_w, out_h), 0)
    d = ImageDraw.Draw(mask)
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((out_w - tw) / 2 - bbox[0], (out_h - th) / 2 - bbox[1]), text, font=font, fill=255)
    # collage
    rows = math.ceil(len(tiles) / cols)
    cw, ch = out_w // cols, out_h // rows
    coll = Image.new("RGB", (out_w, out_h), (60, 10, 10))
    for i, (tile, focus) in enumerate(tiles):
        r, c = divmod(i, cols)
        t = cover(tile, cw - gap, ch - gap, focus)
        coll.paste(t, (c * cw + gap // 2, r * ch + gap // 2))
    if tint:
        coll = Image.blend(coll, ImageChops.soft_light(coll, Image.new("RGB", coll.size, hx(tint))), 0.35)
    out = Image.new("RGBA", (out_w, out_h), (0, 0, 0, 0))
    out.paste(coll, (0, 0), mask)
    if outline:
        edge = mask.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(5))
        ol = Image.new("RGBA", (out_w, out_h), hx(outline) + (255,))
        out.paste(ol, (0, 0), edge)
    return out, mask


def rounded(im, radius):
    im = im.convert("RGBA")
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), radius=radius, fill=255)
    im.putalpha(m)
    return im


def phone_mockup(screen, screen_w=1170, bezel=46, radius=150, color="#141011"):
    """Wrap a phone screenshot in a minimal device frame with soft shadow (RGBA)."""
    s = screen.convert("RGB")
    s = s.resize((screen_w, int(s.height * screen_w / s.width)), Image.LANCZOS)
    sw, sh = s.size
    W, Hh = sw + bezel * 2, sh + bezel * 2
    pad = 120
    canvas = Image.new("RGBA", (W + pad * 2, Hh + pad * 2), (0, 0, 0, 0))
    # shadow
    sh_m = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(sh_m).rounded_rectangle((pad, pad + 40, pad + W, pad + Hh + 40), radius=radius + bezel, fill=150)
    sh_m = sh_m.filter(ImageFilter.GaussianBlur(50))
    canvas.paste(Image.new("RGBA", canvas.size, (20, 0, 0, 255)), (0, 0), sh_m)
    body = Image.new("RGBA", (W, Hh), (0, 0, 0, 0))
    bd = ImageDraw.Draw(body)
    bd.rounded_rectangle((0, 0, W - 1, Hh - 1), radius=radius + bezel, fill=hx(color) + (255,))
    bd.rounded_rectangle((3, 3, W - 4, Hh - 4), radius=radius + bezel - 3, outline=(80, 70, 70, 255), width=3)
    body.paste(rounded(s, radius), (bezel, bezel), rounded(s, radius))
    # dynamic island
    iw, ih = int(sw * 0.3), int(sw * 0.085)
    bd.rounded_rectangle(((W - iw) // 2, bezel + 26, (W + iw) // 2, bezel + 26 + ih), radius=ih // 2, fill=(8, 8, 8, 255))
    canvas.alpha_composite(body, (pad, pad))
    return canvas
