"""Web images + credits for the Unity Lab landing page.

    python _build/prepare_web_images.py

Reads the licensed originals in 12_assets/downloaded (see 12_assets/DOWNLOAD_LIST.md) and writes
03_UnityLab/assets/img/*.webp plus 03_UnityLab/assets/media.js (captions, credits, licences).
Historical photos get the same sepia/duotone treatment as the slides; contemporary photos a light warm grade.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import imgfx as fx  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DL = ROOT / "12_assets" / "downloaded"
OUT = ROOT / "03_UnityLab" / "assets" / "img"
MEDIA_JS = ROOT / "03_UnityLab" / "assets" / "media.js"
MANIFEST = json.load(open(ROOT / "_build" / "download_manifest.json", encoding="utf-8"))
BY_FILE = {m["file"]: m for m in MANIFEST}

# key: (source file, size (w, h), focus, treatment, optional crop box l,t,r,b as fractions, short Vietnamese description)
FACES = [  # 3:4 portraits for the hero marquee and the faces grid
    ("f01", "c1m_hmong_woman_laocai.jpg", (0.55, 0.35), None, "Người phụ nữ H'Mông, Lào Cai"),
    ("f02", "c1a_farmer_hoian.jpg", (0.45, 0.4), None, "Nông dân, Hội An"),
    ("f03", "c1q_elderly_vendor_hanoi.jpg", (0.62, 0.42), None, "Bà bán hàng ở chợ, Hà Nội"),
    ("f04", "c1e_workshop_hcmc.jpg", (0.5, 0.5), None, "Công nhân xưởng cơ khí, TP.HCM"),
    ("f05", "c1g_teacher_chalkboard.jpg", (0.5, 0.4), (0.2, 0.0, 0.62, 0.7), "Giáo viên trên bục giảng"),
    ("f06", "c1j_graduates_hanoi_law.jpg", (0.56, 0.2), None, "Tân cử nhân, Hà Nội"),
    ("f07", "c1i_health_worker_2021.jpg", (0.5, 0.35), None, "Nhân viên y tế, 2021"),
    ("f08", "c1z_fisherman_namdinh.jpg", (0.55, 0.4), None, "Ngư dân, Nam Định"),
    ("f09", "c1s_devotee_danang.jpg", (0.5, 0.6), (0.3, 0.05, 0.7, 0.8), "Người lễ chùa, Đà Nẵng"),
    ("f10", "c1n_gong_kontum.jpg", (0.45, 0.5), None, "Diễn tấu cồng chiêng, Kon Tum"),
    ("f11", "c1u_easter_procession_thaibinh.jpg", (0.5, 0.5), (0.45, 0.62, 1.0, 1.0), "Giáo dân trong lễ rước, Thái Bình"),
    ("f12", "c1d_construction_cantho.jpg", (0.5, 0.45), (0.28, 0.32, 0.84, 0.7), "Công nhân xây dựng, Cần Thơ"),
    ("f13", "c2e_child_gift_village.jpg", (0.5, 0.42), None, "Em nhỏ nhận quà ở vùng quê"),
    ("f14", "c2c_volunteer_elderly_binhphuoc.jpg", (0.55, 0.6), None, "Tình nguyện viên với người cao tuổi, Bình Phước"),
    ("f15", "c3a_classroom_hanoi.jpg", (0.62, 0.5), None, "Học sinh trong lớp học, Hà Nội"),
    ("f16", "c3c_usth_students.jpg", (0.5, 0.45), None, "Sinh viên USTH"),
]
WIDE = [  # landscape images for the story sections
    ("w_trees", "c2a_tree_planting_phanthiet.jpg", (1280, 800), (0.55, 0.55), "warm", None, "Trồng cây ở Phan Thiết"),
    ("w_bookbus", "c2f_book_bus.jpg", (1280, 800), (0.5, 0.45), "warm", None, "Xe buýt sách"),
    ("w_tractor", "c2d_children_volunteers_binhphuoc.jpg", (1280, 800), (0.55, 0.45), "warm", None, "Các em nhỏ và tình nguyện viên, Bình Phước"),
    ("w_class", "c3a_classroom_hanoi.jpg", (1280, 800), (0.62, 0.5), "warm", None, "Lớp học, Hà Nội"),
    ("w_usth", "c3c_usth_students.jpg", (1280, 800), (0.5, 0.55), "warm", None, "Sinh viên USTH"),
    ("w_flags", "c3f_flags_dusk_hcmc.jpg", (1280, 800), (0.6, 0.55), "warm_bright", None, "Cờ Tổ quốc lúc hoàng hôn, TP.HCM"),
    ("w_laocai", "c3d_gathering_laocai_aerial.jpg", (1280, 800), (0.6, 0.65), "warm", None, "Một buổi sinh hoạt cộng đồng ở Lào Cai, nhìn từ trên cao"),
    ("h_badinh", "h2b_ba_dinh_1945-09-02.jpg", (1280, 860), (0.48, 0.55), "sepia", None, "Lễ đài Quảng trường Ba Đình, Hà Nội, 2/9/1945"),
    ("h_congiao", "h2c_cong_giao_ngay_doc_lap_1945.jpg", (1280, 860), (0.45, 0.4), "sepia", None, "2/9/1945: khối Trường Thần học Công giáo trong đoàn mít tinh Ngày Độc lập"),
    ("h_quochoi", "h2d_quoc_hoi_khoa_I_1946-03-02.jpg", (1280, 860), (0.5, 0.5), "sepia", (0.0, 0.0, 1.0, 0.94), "Đại biểu Quốc hội khóa I, 2/3/1946"),
    ("h_ledai", "h2a_ba_dinh_le_dai_1945-09-02.jpg", (1280, 860), (0.5, 0.5), "sepia", (0.0, 0.0, 0.97, 0.73), "Toàn cảnh lễ đài Ba Đình, 2/9/1945"),
    ("h_portrait", "h1a_hcm_portrait_c1946.jpg", (900, 1125), (0.5, 0.36), "duotone", None, "Chủ tịch Hồ Chí Minh, khoảng 1946"),
]


def crop_box(im, box):
    l, t, r, b = box
    return im.crop((int(im.width * l), int(im.height * t), int(im.width * r), int(im.height * b)))


def treat(im, kind):
    if kind == "sepia":
        return fx.sepia(im)
    if kind == "duotone":
        return fx.duotone(im, dark="#24060A", mid="#7E3A2A", light="#F2DDBB", contrast=1.08)
    if kind == "warm_bright":
        from PIL import ImageEnhance
        return ImageEnhance.Brightness(fx.warm_grade(im, amount=0.1)).enhance(1.28)
    if kind == "warm":
        return fx.warm_grade(im, amount=0.12)
    return im


def credit(src):
    m = BY_FILE[src]
    lic = m["license"]
    short = ("Phạm vi công cộng" if lic.lower().startswith("public domain") else lic.split(".")[0])
    return {"author": m["author"].split(" (")[0] if not lic.lower().startswith("public domain") else m["author"],
            "license": short, "page": m["page"]}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    media = {"faces": [], "wide": {}, "mosaic": "assets/img/mosaic.webp", "credits": []}
    seen = set()
    for key, src, focus, box, desc in FACES:
        im = fx.load(DL / src, max_side=2400)
        if box:
            im = crop_box(im, box)
        im = fx.warm_grade(fx.cover(im, 480, 640, focus), amount=0.08)
        im.save(OUT / f"{key}.webp", "WEBP", quality=74, method=6)
        media["faces"].append({"src": f"assets/img/{key}.webp", "alt": desc})
        if src not in seen:
            seen.add(src); media["credits"].append(dict(credit(src), what=desc))
    for key, src, size, focus, kind, box, desc in WIDE:
        im = fx.load(DL / src, max_side=2600)
        if box:
            im = crop_box(im, box)
        w, h = size
        scale_need = max(w / im.width, h / im.height)
        if scale_need > 1.0:  # never upscale: shrink the target instead
            w, h = int(w / scale_need), int(h / scale_need)
        im = treat(fx.cover(im, w, h, focus), kind)
        im.save(OUT / f"{key}.webp", "WEBP", quality=74, method=6)
        media["wide"][key] = {"src": f"assets/img/{key}.webp", "alt": desc, "w": im.width, "h": im.height}
        if src not in seen:
            seen.add(src); media["credits"].append(dict(credit(src), what=desc))
    # the "ĐẠI" photo collage from the slides (same 12 photos, already credited above or in the deck)
    from PIL import Image
    mo = Image.open(ROOT / "12_assets" / "processed" / "mosaic.png")
    mo.thumbnail((1400, 1400))
    mo.save(OUT / "mosaic.webp", "WEBP", quality=78, method=6)
    js = ("/* Generated by _build/prepare_web_images.py — do not edit by hand. */\n"
          "window.UL_MEDIA = " + json.dumps(media, ensure_ascii=False, indent=1) + ";\n")
    MEDIA_JS.write_text(js, encoding="utf-8")
    total = sum(p.stat().st_size for p in OUT.glob("*.webp"))
    print(f"{len(list(OUT.glob('*.webp')))} webp files, {total/1024:.0f} KB total; credits: {len(media['credits'])}")


if __name__ == "__main__":
    main()
