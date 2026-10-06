"""Write 06_speaker-notes.md from _build/notes.py (the same text that is embedded in the PPTX notes)."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notes as N  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
TITLES = {
    1: "Hero cover — Tư tưởng Hồ Chí Minh về đại đoàn kết dân tộc",
    2: "Cold open — Đoàn kết là gì?",
    3: "Không học lại — mà nhìn lại sâu hơn",
    4: "Vai trò — không phải giải pháp tình thế",
    5: "Ai nằm trong chữ “Đại”?",
    6: "ĐOÀN KẾT ≠ ĐỒNG NHẤT",
    7: "Điều gì giữ những khác biệt ở cùng nhau? (mô hình bàn tay)",
    8: "Khi bốn nhóm đều có lý…",
    9: "Phóng to quy mô — từ lớp học đến quốc gia",
    10: "Đại đoàn kết khi mỗi người một “feed”?",
    11: "Unity Lab",
    12: "Quay lại câu hỏi ban đầu",
    13: "AI Usage · Liêm chính học thuật",
    14: "Phụ lục — Nguồn tham khảo & ảnh",
    15: "Xin cảm ơn — mời phản biện",
}


def secs(t):
    m = re.match(r"(\d+):(\d+)", t)
    return int(m.group(1)) * 60 + int(m.group(2)) if m else 0


rows, total = [], 0
for i in range(1, 16):
    t = re.search(r"THỜI GIAN: (.+)", N.S[i]).group(1)
    who = re.search(r"NGƯỜI TRÌNH BÀY \(gợi ý\): (.+)", N.S[i]).group(1)
    ctype = re.search(r"LOẠI NỘI DUNG: (.+)", N.S[i]).group(1)
    s = secs(t)
    total += s
    rows.append(f"| {i} | {TITLES[i]} | {ctype} | {t} | {total // 60}:{total % 60:02d} | {who} |")

out = [
    "# 06 — Speaker notes (ghi chú thuyết trình)",
    "",
    "Nội dung dưới đây **trùng khớp** với phần Notes trong `01_Tu_tuong_HCM_Dai_doan_ket.pptx` (cùng sinh ra từ `_build/notes.py`).",
    "Ghi chú là gợi ý để nói tự nhiên — **không đọc nguyên văn**, không đọc slide.",
    "",
    f"**Tổng thời lượng dự kiến: {total // 60} phút {total % 60:02d} giây** (mục tiêu 10–12 phút). Slide 14 là phụ lục, chỉ mở khi được hỏi.",
    "",
    "## Bảng thời gian",
    "",
    "| Slide | Nội dung | Loại nội dung | Thời lượng | Cộng dồn | Người trình bày (gợi ý) |",
    "|---|---|---|---|---|---|",
    *rows,
    "",
    "**Nếu bị trễ giờ:** rút S8 xuống 45 giây (bỏ phần mời 2–3 bạn nói, chỉ hỏi giơ tay); S9 chỉ nêu 1 con số; S10 bỏ đọc số liệu.",
    "**Nếu mất mạng ở S11:** chiếu tình huống 1 của Unity Lab (ảnh chụp trong `_build/shots/`), cả lớp giơ 1–2–3 ngón cho A–B–C.",
    "",
    "## Gợi ý phân công (nhóm 5 người — điều chỉnh theo số thành viên thật)",
    "",
    "| Thành viên | Slide | Ghi chú |",
    "|---|---|---|",
    "| Thành viên 1 | 1–3 | Mở màn, điều khiển khảo sát giơ tay |",
    "| Thành viên 2 | 4–5 | Lý luận cốt lõi: vai trò, lực lượng |",
    "| Thành viên 3 | 6–7 | Luận đề của nhóm + mô hình bàn tay |",
    "| Thành viên 4 | 8–10 | Thí nghiệm lớp học, quy mô, số liệu đương đại |",
    "| Thành viên 5 | 11–13 | Unity Lab, kết luận, AI usage |",
    "| Cả nhóm | 15 | Mời phản biện |",
    "",
    "Nhóm 4 người: gộp TV4 + TV5 phần S11. Nhóm 6 người: tách S13 cho TV6.",
    "",
]
for i in range(1, 16):
    out += [f"---", "", f"## Slide {i} — {TITLES[i]}", "", "```", N.S[i], "```", ""]
(ROOT / "06_speaker-notes.md").write_text("\n".join(out), encoding="utf-8")
print("06_speaker-notes.md written; total", f"{total // 60}:{total % 60:02d}")
