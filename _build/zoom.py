"""python _build/zoom.py <png_dir> <out.png> 9 10 12 14  -> 2-column sheet at half resolution"""
import sys, os
from PIL import Image
src, out, nums = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3:]]
W, H = 960, 540
cols = 2
rows = (len(nums) + 1) // 2
sheet = Image.new("RGB", (cols * (W + 10) + 10, rows * (H + 10) + 10), (30, 30, 30))
for k, n in enumerate(nums):
    im = Image.open(os.path.join(src, f"slide-{n:02d}.png")).resize((W, H), Image.LANCZOS)
    sheet.paste(im, ((k % cols) * (W + 10) + 10, (k // cols) * (H + 10) + 10))
sheet.save(out)
print(out)
