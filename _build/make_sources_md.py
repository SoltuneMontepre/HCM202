"""Generate 04_sources.md from curated claim→source rows + the research record of opened pages + image manifest."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# research log of every page opened during source verification (URL -> tier, org, title, date, claim ids)
opened = json.load(open(ROOT / "_build" / "sources_opened.json", encoding="utf-8"))
manifest = json.load(open(ROOT / "_build" / "download_manifest.json", encoding="utf-8"))

U = {
    "NXB": "https://www.nxbctqg.org.vn/giao-trinh-tu-tuong-ho-chi-minh-danh-cho-bac-dai-hoc-he-khong-chuyen-ly-luan-chinh-tri-.html",
    "FPTLIB": "https://library.fpt.edu.vn/SearchBook/Detail?detail_id=19303",
    "HUIT": "https://foodtech.huit.edu.vn/Upload/file/Chuong%20trinh%20dao%20tao/CNTP%202024/4_%202024-T%C6%B0%20t%C6%B0%E1%BB%9Fng%20HCM-%C4%90%E1%BB%81%20c%C6%B0%C6%A1ng%20HP.pdf",
    "VNUF": "https://daotao.vnuf.edu.vn/documents/94121951/106165782/3.%C4%90CCT-%20T%C6%B0%20t%C6%B0%E1%BB%9Fng%20H%E1%BB%93%20Ch%C3%AD%20Minh%202022.pdf",
    "HUB": "https://clc.hub.edu.vn/DATA/CHUONGTRINH.DTCLC/DOCUMENT/2023/07/19/PDF%20Dai%20cuong%20TCNH/5.%20TTHCM.pdf",
    "TMU": "https://tmu-moodle.tmu.edu.vn/moodledata/filedir/e0/40/e04043a58ba0c05e1e103c4b03845935ae153100.pdf",
    "PTTC1": "https://qldt.pttc1.edu.vn/slides/bas1122-tx-8365",
    "SAODO": "https://saodo.edu.vn/uploads/about/ctdt2019-may/ctri201.pdf",
    "TCCS17": "https://tapchicongsan.org.vn/web/guest/hoat-ong-cua-lanh-ao-ang-nha-nuoc/-/2018/44966/tu-tuong-ho-chi-minh-ve-dai-doan-ket-dan-toc-va-su-tham-nhuan,-van-dung-cua-dang-ta-trong-su-nghiep-doi-moi.aspx",
    "LLCT21": "https://lyluanchinhtri.vn/tang-cuong-khoi-dai-doan-ket-toan-dan-toc-theo-tu-tuong-ho-chi-minh-279.html",
    "DBND23": "https://daibieunhandan.vn/print/10316356.html",
    "TCNN24": "https://tcnnld.vn/news/detail/66662/Tiep-tuc-xay-dung-khoi-dai-doan-ket-toan-dan-toc-theo-di-nguyen-cua-Chu-tich-Ho-Chi-Minh.html",
    "TCNN25": "https://tcnnld.vn/news/detail/69703/Van-dung-tu-tuong-Ho-Chi-Minh-ve-dai-doan-ket-trong-xay-dung-khoi-dai-doan-ket-toan-dan-toc.html",
    "TT4": "https://hochiminh.vn/upload/3000001/20251024/786ba6cbfbb9aa4c66f7e55c826dce2bHO_CHI_MINH_TOAN_TAP_-_TAP_4.pdf",
    "TT5": "https://hochiminh.vn/upload/3000001/20251024/3a93cdbc9f4e465ad1603967610eb969HO_CHI_MINH_TOAN_TAP_-_TAP_5.pdf",
    "TT6": "https://hochiminh.vn/book/tac-pham-cua-ho-chi-minh/ho-chi-minh-toan-tap/ho-chi-minh-toan-tap-tap-6-273",
    "TT7": "https://hochiminh.vn/upload/3000001/20251024/a80af28feed0cde322ca24207165ae3dHO_CHI_MINH_TOAN_TAP_-_TAP_7.pdf",
    "TT9": "https://hochiminh.vn/upload/3000001/20251024/76482ff84eaa210c1480acd63f4c4c05HO_CHI_MINH_TOAN_TAP_-_TAP_9.pdf",
    "TT10": "https://hochiminh.vn/upload/3000001/20251024/df463c14188e86ed7d763e4a7c35b591HO_CHI_MINH_TOAN_TAP_-_TAP_10.pdf",
    "TT11": "https://hochiminh.vn/upload/3000001/20251024/6983eb5d88e228251dc2d61cfa18c5faHO_CHI_MINH_TOAN_TAP_-_TAP_11.pdf",
    "TT13": "https://hochiminh.vn/upload/3000001/20251024/bc4c76d39913c96671fec9bef96e417fHO_CHI_MINH_TOAN_TAP_-_TAP_13.pdf",
    "TT15": "https://hochiminh.vn/upload/3000001/20251024/13d6ae293a3e275ef22285a179a20ed4HO_CHI_MINH_TOAN_TAP_-_TAP_15.pdf",
    "MTTQ61": "https://mattran.org.vn/hoat-dong/ngay-2541961-tai-dai-hoi-dai-bieu-mat-tran-to-quoc-viet-nam-lan-thu-ii-bac-ho-can-dan-doan-ket-doan-ket-dai-doan-ket-thanh-cong-thanh-cong-dai-thanh-cong-3.html",
}

theory = [
    ("T-01 Danh tính giáo trình 2021 (Bộ GD&ĐT; chủ biên Mạch Quang Thắng; NXB CTQG Sự thật, 6/2021, 272 tr., ISBN 9786045765920)", "NXB CTQG Sự thật (trang sách); Thư viện ĐH FPT", f"{U['NXB']} · {U['FPTLIB']}", "T1 + T2", "HIGH", "Bản tái bản 2024: ISBN 9786045798102."),
    ("T-02 Chương 5: Tư tưởng HCM về đại đoàn kết toàn dân tộc và đoàn kết quốc tế", "NXB (mô tả); đề cương HUIT 2024, HUB 2023; bài giảng TMU", f"{U['NXB']} · {U['HUIT']} · {U['HUB']}", "T1 + T2", "HIGH", "Exact page in the 2021 textbook was not independently verified."),
    ("T-03 Khung trên slide theo bài giảng của lớp, mục II: Vai trò; Nội dung (đoàn kết toàn dân; 3 điều kiện); Hình thức tổ chức (MTDTTN; 4 nguyên tắc)", "Bài giảng Chương 5 của lớp — TS. Hà Triệu Huy, ĐH KHXH&NV – ĐHQG TP.HCM; đối chiếu đề cương VNUF 2022, HUIT 2024, bài giảng TMU", "12_assets/ref/Chapter 5 HCM-Ideology.pdf (tệp do nhóm cung cấp, không có URL công khai) · " + U["VNUF"] + " · " + U["HUIT"] + " · " + U["TMU"], "T2", "HIGH", "Khung giáo trình 2021 theo các đề cương: 5 mục (thêm Phương thức; lợi ích chung là điều kiện)."),
    ("T-05 ĐĐK toàn dân tộc là vấn đề có ý nghĩa chiến lược, quyết định thành công của cách mạng", "Đề cương HUIT, VNUF, TMU, PTTC1; Báo Đại biểu Nhân dân 2023; Tạp chí Cộng sản 2017", f"{U['HUIT']} · {U['DBND23']} · {U['TCCS17']}", "T2 + T1", "HIGH", "Exact page in the 2021 textbook was not independently verified."),
    ("T-06 ĐĐK dân tộc là mục tiêu, nhiệm vụ hàng đầu của Đảng, của dân tộc", "Bài giảng của lớp, mục II.1.b; đề cương HUIT, VNUF, TMU ('…của cách mạng Việt Nam'); Đại biểu Nhân dân 2023", "12_assets/ref/Chapter 5 HCM-Ideology.pdf (tệp do nhóm cung cấp, không có URL công khai) · " + U["VNUF"] + " · " + U["DBND23"], "T2 + T1", "HIGH", "Slide dùng cách diễn đạt của bài giảng của lớp."),
    ("T-07 Chủ thể: toàn thể nhân dân, không phân biệt dân tộc, tôn giáo, đảng phái, giai cấp…", "Bài giảng TMU; LLCT 7-2021; Đại biểu Nhân dân 2023; TCNN&LĐ 2024", f"{U['TMU']} · {U['LLCT21']} · {U['DBND23']}", "T2 + T1", "HIGH", "Câu 'con Rồng cháu Tiên… quý, tiện' là diễn giải, không phải nguyên văn HCM."),
    ("T-08 Nền tảng: công nhân, nông dân và trí thức (liên minh công – nông – trí)", "Bài giảng TMU; LLCT 7-2021; Toàn tập t.9 tr.244, t.10 tr.376, t.12 tr.417", f"{U['TMU']} · {U['LLCT21']} · {U['TT9']}", "T2 + T1", "HIGH", "Cụm 'liên minh công – nông – trí' là cách diễn đạt của văn kiện/giáo trình."),
    ("T-09 Ba điều kiện: truyền thống yêu nước – nhân nghĩa – đoàn kết; khoan dung, độ lượng; niềm tin vào nhân dân", "Bài giảng của lớp, mục II.2.b; bài giảng TMU; Tạp chí Cộng sản 2017; LLCT 7-2021", "12_assets/ref/Chapter 5 HCM-Ideology.pdf (tệp do nhóm cung cấp, không có URL công khai) · " + U["TMU"] + " · " + U["TCCS17"], "T2 + T1", "HIGH", "—"),
    ("T-10 Lợi ích: Mặt trận hoạt động trên cơ sở bảo đảm lợi ích tối cao của dân tộc, quyền lợi cơ bản của các tầng lớp nhân dân (nguyên tắc 2)", "Bài giảng của lớp, mục II.3.b; Tạp chí Cộng sản 2017; bài giảng TMU xếp 'lấy lợi ích chung làm điểm quy tụ' vào điều kiện", "12_assets/ref/Chapter 5 HCM-Ideology.pdf (tệp do nhóm cung cấp, không có URL công khai) · " + U["TCCS17"] + " · " + U["TMU"], "T2 + T1", "HIGH", "Khác cách xếp giữa các trường; nội dung tương đương."),
    ("T-11/T-12 Mặt trận dân tộc thống nhất; 4 nguyên tắc: liên minh công – nông – trí dưới sự lãnh đạo của Đảng; lợi ích tối cao của dân tộc; hiệp thương dân chủ (bàn bạc công khai, đi đến nhất trí, loại trừ áp đặt); đoàn kết chặt chẽ, lâu dài, thật sự, chân thành, thân ái", "Bài giảng của lớp, mục II.3; Tạp chí Cộng sản 2017; bài giảng TMU; TCNN&LĐ 2025", "12_assets/ref/Chapter 5 HCM-Ideology.pdf (tệp do nhóm cung cấp, không có URL công khai) · " + U["TCCS17"] + " · " + U["TCNN25"], "T2 + T1", "HIGH", "'Hiệp thương dân chủ' là thuật ngữ giáo trình/Đảng, không phải nguyên văn HCM."),
    ("T-13 Phương thức: dân vận; đoàn thể, tổ chức quần chúng; tập hợp trong Mặt trận (không có trong bài giảng của lớp — không dùng trên slide)", "Bài giảng TMU; Toàn tập t.6 tr.232–234", f"{U['TMU']} · {U['TT6']}", "T2 + T1", "MEDIUM", "—"),
]

quotes = [
    ("Q-01 'Đoàn kết, đoàn kết, đại đoàn kết, Thành công, thành công, đại thành công.' (25-4-1961)", "Toàn tập t.13 tr.119–120; mattran.org.vn", f"{U['TT13']} · {U['MTTQ61']}", "T1 (sơ cấp)", "HIGH", "S12"),
    ("Q-02 'Đoàn kết của ta không những rộng rãi mà còn đoàn kết lâu dài. Đoàn kết là một chính sách dân tộc, không phải là một thủ đoạn chính trị.' (10-1-1955)", "Toàn tập t.9 tr.244", U["TT9"], "T1 (sơ cấp)", "HIGH", "S4"),
    ("Q-04/05/18 'nền gốc' · 'Bất kỳ ai mà thật thà tán thành…' · 'cô độc hẹp hòi và đoàn kết vô nguyên tắc' (10-1-1955)", "Toàn tập t.9 tr.244", U["TT9"], "T1 (sơ cấp)", "HIGH", "S5, S12 (ghi chú), Q&A"),
    ("Q-06 Lời kêu gọi toàn quốc kháng chiến (19-12-1946)", "Toàn tập t.4 tr.534; scov.gov.vn", U["TT4"], "T1 (sơ cấp)", "HIGH", "S5, S12"),
    ("Q-07 'Năm ngón tay cũng có ngón vắn ngón dài…' (Thư gửi đồng bào Nam Bộ, 1-6-1946)", "Toàn tập t.4 tr.280–281", U["TT4"], "T1 (sơ cấp)", "HIGH", "S7, S12"),
    ("Q-08 'Đoàn kết thực sự nghĩa là mục đích phải nhất trí và lập trường cũng phải nhất trí…' (19-3-1958)", "Toàn tập t.11 tr.362", U["TT11"], "T1 (sơ cấp)", "HIGH", "S12, Unity Lab"),
    ("Q-09 'Tuy khác nhau nhưng cùng chung một mục đích.' (Báo Nhân dân 24-12-1954)", "Toàn tập t.9 tr.203", U["TT9"], "T1 (sơ cấp)", "MEDIUM (1 nguồn)", "S6"),
    ("Q-10 'Dân vận kém thì việc gì cũng kém…' (Sự thật, 15-10-1949)", "Toàn tập t.6 tr.234", U["TT6"], "T1 (sơ cấp)", "HIGH", "Q&A"),
    ("Q-12 '…So đi sánh lại, sẽ lòi ra một ý kiến mà mọi người đều tán thành, hoặc số đông người tán thành.' (Sửa đổi lối làm việc, 10-1947)", "Toàn tập t.5 tr.336 (mục Cách lãnh đạo)", U["TT5"], "T1 (sơ cấp)", "HIGH (nguyên văn) / MEDIUM (khi làm cơ sở cho hiệp thương dân chủ)", "S8, Unity Lab"),
    ("Q-13 '…tuy khác nhau nơi việc làm, nhưng đều giống nhau nơi lòng nồng nàn yêu nước.' (2-1951)", "Toàn tập t.7 tr.38", U["TT7"], "T1 (sơ cấp)", "HIGH", "ghi chú S7"),
    ("Q-16 'Mục đích của Đảng Lao động Việt Nam có thể gồm trong 8 chữ là: ĐOÀN KẾT TOÀN DÂN, PHỤNG SỰ TỔ QUỐC.' (3-3-1951)", "Toàn tập t.7 tr.49", U["TT7"], "T1 (sơ cấp)", "HIGH", "ghi chú S4"),
    ("X-01 'Đoàn kết là sức mạnh, đoàn kết là thắng lợi' — có nguyên văn ở t.14 (3-2-1963), mạch đoàn kết quốc tế; hay bị dẫn sai trang", "Toàn tập t.14 tr.27", "Toàn tập t.14 (hochiminh.vn)", "T1 (sơ cấp)", "—", "Không dùng làm luận cứ; Q&A #14"),
]

contemporary = [
    ("C-01 NQ 23-NQ/TW (12/3/2003) về phát huy sức mạnh đại đoàn kết toàn dân tộc; NQ 43-NQ/TW (24/11/2023)", "tulieuvankien.dangcongsan.vn; mattran.org.vn", "https://tulieuvankien.dangcongsan.vn/van-kien-tu-lieu-ve-dang/hoi-nghi-bch-trung-uong/khoa-ix/nghi-quyet-so-23-nqtw-ngay-1232003-hoi-nghi-lan-thu-bay-ban-chap-hanh-trung-uong-dang-khoa-ix-ve-phat-huy-suc-manh-dai-doan-ket-toan-dan-toc-vi-dan-giau-nuoc-manh-xa-hoi-cong-bang-dan-chu-van-minh-2846", "T1", "HIGH", "Văn bản gốc NQ 43 chưa mở trực tiếp; số hiệu/ngày xác nhận qua 3 trang T1."),
    ("C-02 Đại hội XIII (2021): '…phát huy ý chí, sức mạnh đại đoàn kết toàn dân tộc kết hợp với sức mạnh thời đại'", "tulieuvankien.dangcongsan.vn (Báo cáo chính trị)", "https://tulieuvankien.dangcongsan.vn/ban-chap-hanh-trung-uong-dang/dai-hoi-dang/lan-thu-xiii", "T1", "HIGH", "—"),
    ("C-03 Đại hội XIV (19–23/01/2026): 'Xây dựng và triển khai Chiến lược đại đoàn kết toàn dân tộc đến năm 2035, tầm nhìn đến năm 2045'", "Báo cáo chính trị & Nghị quyết Đại hội XIV", "https://tulieuvankien.dangcongsan.vn/upload/2006988/fck/phuongdt/nq_Daihoi14_(CT).pdf", "T1", "HIGH", "S9"),
    ("C-04 Ngày hội Đại đoàn kết toàn dân tộc 18/11 (NQ 04/NQ/ĐCT-MTTW, 1/8/2003); 2025: 95 năm Mặt trận", "mattran.org.vn", "https://mattran.org.vn/gioi-thieu/lich-su-mat-tran-dan-toc-thong-nhat-32563.html", "T1", "HIGH", "ghi chú"),
    ("C-05 Bão Yagi (2024): Ban Vận động Cứu trợ TW tiếp nhận trên 2.200 tỷ đồng (đến 29/11/2024)", "mattran.org.vn", "https://mattran.org.vn/hoat-dong/them-nguon-luc-giup-nguoi-dan-vung-lu-tai-thiet-cuoc-song-57988.html", "T1", "HIGH", "S9"),
    ("C-06 Xóa nhà tạm, nhà dột nát: 334.234 căn, gần 24.762 tỷ đồng; hoàn thành 9/2025", "mattran.org.vn (10 sự kiện nổi bật 2025); Báo cáo chính trị Đại hội XIV", "https://mattran.org.vn/hoat-dong/10-hoat-dong-va-su-kien-noi-bat-cua-cong-tac-mat-tran-nam-2025-68666.html", "T1", "HIGH", "S9"),
    ("C-07 Quỹ vắc-xin COVID-19: 8.794,6 tỷ đồng (sơ bộ, đến 3/11/2021)", "mattran.org.vn", "https://mattran.org.vn/hoat-dong/hon-21188-ty-dong-ung-ho-cong-tac-phong-chong-dich-covid19-41124.html", "T1", "MEDIUM", "Không dùng trên slide."),
    ("C-08 Sửa đổi Hiến pháp 2025 (NQ 203/2025/QH15, 16/6/2025), Điều 9: 5 tổ chức chính trị – xã hội trực thuộc MTTQ Việt Nam", "mattran.org.vn (toàn văn NQ 203)", "https://mattran.org.vn/tin-tuc/nghi-quyet-so-2032025qh15-cua-quoc-hoi-ve-sua-doi-bo-sung-mot-so-dieu-cua-hien-phap-nuoc-cong-hoa-xa-hoi-chu-nghia-viet-nam-nam-2013-64107.html", "T1", "HIGH", "Q&A / bối cảnh"),
    ("C-09 Khoảng 110 triệu tài khoản người Việt trên MXH trong nước, khoảng 203 triệu trên MXH nước ngoài (Bộ TT&TT, 11/2024)", "mst.gov.vn", "https://mst.gov.vn/mang-xa-hoi-nao-duoc-nhieu-nguoi-dung-nhat-tai-viet-nam-197250107160615446.htm", "T1", "MEDIUM (là số tài khoản, không phải số người)", "S10"),
    ("C-10 Phát biểu của Tổng Bí thư Tô Lâm tại Ngày hội Đại đoàn kết toàn dân tộc (14/11/2025)", "mattran.org.vn (theo TTXVN)", "https://mattran.org.vn/tin-tuc/phat-bieu-cua-tong-bi-thu-to-lam-tai-ngay-hoi-dai-doan-ket-toan-dan-toc-nam-2025-phuong-thuong-cat-thanh-pho-ha-noi-67539.html", "T1", "HIGH", "S8, S10"),
]


def table(rows, head):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        out.append("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
    return out


img_rows = []
slide_of = {"H1-a": "S1", "H1-b": "S12", "H2-a": "S15", "H2-b": "S4", "H2-c": "S5", "H2-d": "S3"}
for m in manifest:
    sl = slide_of.get(m["id"], m["use"].split()[0])
    lic = m.get("license") or ""
    mod = "cắt khung, chỉnh tông màu (duotone/sepia hoặc ấm nhẹ)"
    if m["id"].startswith("C1"):
        mod = "cắt vừa ô chữ trong ảnh ghép “ĐẠI”, chỉnh tông"
    if m["id"] in ("C2-d",):
        sl = "S9"
    if m["id"] == "C3-d":
        continue
    img_rows.append((sl, m["desc"][:110], f"{m.get('org') or ''} — {(m.get('author') or '')[:50]}", m["page"], f"{lic}; {mod}"))
img_rows += [
    ("S1, S6, S11, S15…", "Hoa văn lấy cảm hứng trống đồng Đông Sơn, dải lụa đỏ, hoa sen nét vàng, nền giấy, sơ đồ hội tụ, bàn tay", "Nhóm tự vẽ bằng mã (`_build/make_motifs.py`, `_build/make_hands.py`)", "—", "Tác phẩm gốc của nhóm"),
    ("S1", "Logo Trường Đại học FPT", "Tệp do nhóm cung cấp", "—", "Nhận diện trường, dùng trong bài học tập"),
    ("S11", "Ảnh chụp màn hình Unity Lab trong khung điện thoại", "Nhóm (03_UnityLab)", "—", "Tác phẩm của nhóm"),
]

md = [
    "# 04 — Sources (nguồn tham khảo)",
    "",
    "Phân cấp nguồn: **T1** chính thống/sơ cấp (NXB CTQG Sự thật, hochiminh.vn, tulieuvankien.dangcongsan.vn, mattran.org.vn, Tạp chí Cộng sản, Lý luận chính trị, Đại biểu Nhân dân, cơ quan nhà nước) · **T2** học thuật thể chế (đề cương, bài giảng, tạp chí của trường/bộ) · **T3** chỉ dùng để đối chiếu.",
    "",
    "**Giáo trình 2021:** Exact page in the 2021 textbook was not independently verified (cho mọi mục). Nhóm cần đối chiếu bản in và bổ sung số trang.",
    "",
    "## A. Lý luận (khung giáo trình)",
    "",
    *table(theory, ["Claim", "Source", "URL", "Source type", "Confidence", "Notes"]),
    "",
    "## B. Trích dẫn Hồ Chí Minh — đối chiếu nguyên văn với *Hồ Chí Minh Toàn tập*, xuất bản lần thứ ba, NXB CTQG Sự thật, 2011",
    "",
    *table(quotes, ["Claim", "Source", "URL", "Source type", "Confidence", "Slide"]),
    "",
    "## C. Số liệu & văn kiện đương đại",
    "",
    *table(contemporary, ["Claim", "Source", "URL", "Source type", "Confidence", "Notes / slide"]),
    "",
    "## D. Ảnh",
    "",
    "Tất cả ảnh lịch sử là ảnh tư liệu thật (không dùng ảnh tạo bằng AI). Ảnh Unsplash/Pexels dùng theo giấy phép của nền tảng (không bắt buộc ghi công — nhóm vẫn ghi). Ảnh CC BY-SA được ghi công, ghi giấy phép và nêu rõ phần chỉnh sửa. Danh sách tải về đầy đủ (tên tệp, dung lượng): `12_assets/DOWNLOAD_LIST.md`.",
    "",
    *table(img_rows, ["Slide", "Image description", "Source organization — author", "URL", "Usage (license; modification)"]),
    "",
    "## E. Toàn bộ trang đã mở trong quá trình kiểm chứng (tự động từ nhật ký nghiên cứu)",
    "",
]
for tier in ("T1", "T2", "T3"):
    md.append(f"### {tier}")
    md.append("")
    for u, m in opened.items():
        if m.get("tier") != tier:
            continue
        t = (m.get("title") or "").strip()
        org = (m.get("org") or "").strip()
        md.append(f"- {org}{(' — ' + t) if t else ''}{(' (' + m['date'] + ')') if m.get('date') else ''}: {u}")
    md.append("")
md.append("*Ghi chú: một bản thảo giáo trình 8/2019 do bên thứ ba đăng tải chỉ được dùng để đối chiếu cấu trúc, không trích dẫn và không ghi đường dẫn tại đây.*")
md = [l for l in md if "baitaptracnghiem" not in l]
(ROOT / "04_sources.md").write_text("\n".join(md), encoding="utf-8")
print("04_sources.md written", len(md), "lines")
