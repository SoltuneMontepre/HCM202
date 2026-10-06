"""Contact sheet of rendered slides: python _build/contact_sheet.py <png_dir> <out.png> [cols] [thumb_w]"""
import sys, glob, os
from PIL import Image, ImageDraw, ImageFont

src, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
tw = int(sys.argv[4]) if len(sys.argv) > 4 else 640
files = sorted(glob.glob(os.path.join(src, "slide-*.png")))
th = int(tw * 9 / 16)
pad, lab = 24, 34
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + pad + lab) + pad), (32, 26, 26))
d = ImageDraw.Draw(sheet)
f = ImageFont.truetype(str(__import__("pathlib").Path(__file__).resolve().parents[1] / "12_assets/fonts/src/BeVietnamPro-Bold.ttf"), 20)
for i, fp in enumerate(files):
    im = Image.open(fp).convert("RGB").resize((tw, th), Image.LANCZOS)
    r, c = divmod(i, cols)
    x, y = pad + c * (tw + pad), pad + r * (th + pad + lab)
    d.text((x, y), f"{i + 1:02d}", font=f, fill=(210, 170, 80))
    sheet.paste(im, (x, y + lab))
sheet.save(out)
print(out, sheet.size)
