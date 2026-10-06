# Tư tưởng Hồ Chí Minh về đại đoàn kết dân tộc — bộ thuyết trình (HCM202)

| Tệp | Nội dung |
|---|---|
| `01_Tu_tuong_HCM_Dai_doan_ket.pptx` | Bộ slide 15 trang (13 slide chính + phụ lục nguồn + kết), chữ chỉnh sửa được, có ghi chú thuyết trình, hiệu ứng hé lộ ở S5, S8, S12; phông Phudu (tiêu đề) + Be Vietnam Pro (chữ) đã nhúng vào file |
| `02_Tu_tuong_HCM_Dai_doan_ket.pdf` | Bản PDF (trạng thái cuối của mọi hiệu ứng) |
| `03_UnityLab/` | Trang giới thiệu + mini-game 3 tình huống (HTML/CSS/JS, không backend; hiệu ứng GSAP), đang chạy tại https://unitylab-hcm202.netlify.app/ — xem `03_UnityLab/README.md` |
| `04_sources.md` | Nguồn cho từng luận điểm, trích dẫn, số liệu, ảnh (URL, loại nguồn, mức tin cậy) |
| `05_theory-verification.md` | Ma trận kiểm chứng lý luận — slide được viết **từ** ma trận này |
| `06_speaker-notes.md` | Lời nói gợi ý, chuyển tiếp, loại nội dung, nguồn, độ tin cậy, thời lượng (tổng 11:50), phân công |
| `07_AI-USAGE.md` | Phụ lục AI Usage + cam kết liêm chính (có phần **nhóm tự điền**) |
| `08_rubric-mapping.md` | Đối chiếu từng tiêu chí rubric ↔ slide ↔ bằng chứng ↔ rủi ro |
| `09_QA-report.md` | Các lỗi thật đã phát hiện và cách sửa |
| `10_slide-contact-sheet.png` | Bảng tổng 15 slide |
| `11_Q&A-preparation.md` | 16 câu hỏi phản biện khó + gợi ý đặt câu hỏi cho nhóm khác |
| `12_assets/` | Ảnh đã tải (kèm `DOWNLOAD_LIST.md`), ảnh đã xử lý, đồ họa nhóm tự vẽ |
| `_build/` | Mã dựng lại toàn bộ (python-pptx, Pillow, Playwright; render bằng PowerPoint) |

## Việc nhóm PHẢI làm trước khi thuyết trình

1. Điền tên nhóm / lớp / GVHD ở slide 1; điền tên nhóm ở `07_AI-USAGE.md` §9 và thuộc tính Author của file PPTX (File › Info) — hoặc sửa `prs.core_properties.author` trong `_build/build_deck.py` rồi dựng lại.
2. Khung lý luận trên slide đã theo **bài giảng Chương 5 của lớp** (bản sao ở `12_assets/ref/`). Nếu có bản in giáo trình 2021, ghi số trang vào `05_theory-verification.md`; khác biệt "3 hay 4 điều kiện" giữa các trường đã có câu trả lời ở `11_Q&A-preparation.md` #8.
3. ✅ Unity Lab đã lên mạng: **https://unitylab-hcm202.netlify.app/** (Netlify, tài khoản của nhóm; chế độ trình chiếu: `https://unitylab-hcm202.netlify.app/?present`). QR thật đã nằm ở slide 11 và trong PDF. Trước buổi học: mở thử bằng 4G trên 1–2 điện thoại.
4. Điền bảng "phần sinh viên chỉnh sửa" và ký cam kết trong `07_AI-USAGE.md`; chép LO của HCM202 vào `08_rubric-mapping.md`.
5. Mở lại Toàn tập để tự kiểm tra các trích dẫn trong `05_theory-verification.md` mục C (checklist ở `07_AI-USAGE.md` §6).
6. Tập dượt bấm giờ (mục tiêu 10–12 phút).

## Dựng lại

Phông chữ: cài các tệp trong `12_assets/fonts/src/` (Phudu, Be Vietnam Pro — SIL OFL) trước khi dựng lại hoặc sửa slide trong PowerPoint. Máy chỉ để trình chiếu thì không cần cài: phông đã nhúng trong .pptx.

```bash
python _build/make_motifs.py && python _build/make_hands.py
python _build/prepare_images.py
python _build/prepare_web_images.py
python _build/build_deck.py
powershell -ExecutionPolicy Bypass -File _build/render.ps1 -Pptx 01_Tu_tuong_HCM_Dai_doan_ket.pptx -Pdf 02_Tu_tuong_HCM_Dai_doan_ket.pdf -PngDir _build/render -Embed
python _build/export_notes_md.py
python _build/make_sources_md.py
python _build/contact_sheet.py _build/render 10_slide-contact-sheet.png 3 600
```

QR: `build_deck.py` tự dùng QR thật khi có `12_assets/created/qr_unitylab.png` và `_build/unitylab_url.txt` (do `make_qr.py` tạo); nếu xóa hai tệp này, slide 11 quay về khung QR PLACEHOLDER. Đổi địa chỉ: `pip install segno` rồi `python _build/make_qr.py <URL mới>`.

Cập nhật Unity Lab trên mạng (cần `npm install -g netlify-cli` và `netlify login` bằng tài khoản của nhóm):

```bash
python _build/stage_unitylab.py
python _build/shoot_landing.py http://localhost:8765/   # tùy chọn: chụp thử trang (cần chạy python -m http.server 8765 --directory 03_UnityLab)
netlify deploy --prod --dir _build/site_unitylab --site unitylab-hcm202
```
