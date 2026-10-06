# 09 — QA report

Bốn vòng kiểm tra trước khi xuất file (theo yêu cầu §27):
**PASS 1** kiểm chứng nguồn/lý luận (10 tác tử tìm nguồn + 12 tác tử kiểm chứng đối kháng, đối chiếu toàn văn 15 tập *Hồ Chí Minh Toàn tập* 2011) ·
**PASS 2** đối chiếu rubric (`08_rubric-mapping.md`) ·
**PASS 3** bố cục/hình ảnh (render từng slide bằng PowerPoint ở 1920×1080, xem bảng tổng `10_slide-contact-sheet.png`, cộng 5 người rà soát độc lập) ·
**PASS 4** câu chuyện – thời lượng – ghi chú (`06_speaker-notes.md`: 11 phút 50 giây).

Bảng dưới là **các lỗi thật đã gặp** và cách xử lý. "S" = số slide.

## A. Nội dung & nguồn (PASS 1)

| Slide | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| S13 (ghi chú), 05, 11 | Vòng 1 ghi câu "Đoàn kết là sức mạnh, đoàn kết là thắng lợi" là **không có** trong Toàn tập. Vòng phản biện tìm thấy nguyên văn ở t.14 tr.27 (3-2-1963), cả tr.89 và t.15 tr.515 — mạch đoàn kết quốc tế | CRITICAL | Sửa ma trận X-01, Q&A #14, ghi chú S13; đổi ví dụ kiểm chứng sang câu "khó vạn lần" (sai nguyên văn thật) và ghi rõ đây là bài học "kết quả *không tìm thấy* cũng phải kiểm chứng" | Fixed |
| 05 (X-02) | "Đoàn kết là sức mạnh, là then chốt của thành công" bị ghi "chỉ có nguồn thứ cấp" — thực ra có ở t.14 tr.186 (Hà Bắc, 17-10-1963) | MAJOR | Sửa X-02, ghi bối cảnh đoàn kết trong Đảng | Fixed |
| S4 | Câu trích ban đầu viết "**Đại** đoàn kết là một chính sách dân tộc…" | MAJOR | Đúng nguyên văn: "**Đoàn kết** là một chính sách dân tộc, không phải là một thủ đoạn chính trị" (t.9 tr.244), trích cả câu "rộng rãi … lâu dài" | Fixed |
| S12 | "Đoàn kết, đoàn kết, đại đoàn kết. Thành công…" — dấu câu, trang và năm "lần đầu" chưa rõ | MINOR | Theo Toàn tập t.13 tr.119–120: dấu phẩy; chính HCM nói lần đầu nêu tại Đại hội hợp nhất Việt Minh – Liên Việt 1951 | Fixed |
| Q&A | "Dễ trăm lần … khó vạn lần" lưu truyền trên mạng | MAJOR | Nguyên văn t.15 tr.280: "Dễ mười lần … Khó **trăm** lần"; HCM *dẫn lại, tán thành* câu của cán bộ Quảng Bình | Fixed (không dùng trên slide) |
| Q&A | "Cầu đồng tồn dị" hay được gán là phương châm HCM | MAJOR | Trong Toàn tập chỉ có ở chú thích tên người về Chu Ân Lai → không gán cho HCM | Removed |
| S5 | Câu "mọi con dân nước Việt, con Rồng cháu Tiên … quý, tiện" định để trong ngoặc kép như lời HCM | MAJOR | Là diễn giải ghép → trình bày bằng lời nhóm, không ngoặc kép | Reclassified |
| S5 | "Liên minh công – nông – trí" có nguy cơ bị hiểu là nguyên văn HCM; lời nói gộp "nền gốc" thành "người lao động" | MINOR | Ghi rõ đây là cách diễn đạt của giáo trình/văn kiện; trích đúng "công nhân, nông dân và các tầng lớp nhân dân lao động khác … nền gốc" (t.9 tr.244) và "công, nông, trí…" (t.10 tr.376) | Fixed |
| S5 | Thiếu lưu ý về lập trường giai cấp công nhân và "hạt nhân" đoàn kết trong Đảng (có trong bài giảng khung 2021) | MAJOR | Bổ sung vào ghi chú S5 và Q&A #4 | Fixed |
| S5 | Câu trích Lời kêu gọi bị cắt mất vế mục đích "…để cứu Tổ quốc" | MINOR | Trích đủ câu | Fixed |
| S6 | Luận đề "≠ đồng nhất" thiếu ranh giới (HCM yêu cầu nhất trí mục đích **và lập trường**) | MINOR | Thêm ranh giới vào ghi chú S6; S12 có cột "CẦN NHẤT TRÍ"; ghi bối cảnh câu "Tuy khác nhau…" (nhà máy điện, 1954) | Fixed |
| S7 | Ngón "Mặt trận" bị gắn nhãn "nguyên tắc" (thực ra là **hình thức tổ chức**); lòng bàn tay (điều kiện 1) không được gọi là điều kiện | MAJOR | Nhãn mới: HÌNH THỨC / ĐIỀU KIỆN 1–4 / NGUYÊN TẮC; chú thích "chưa đối chiếu bản in" cho mục MEDIUM | Fixed |
| S7 | Câu "các luận điểm đã kiểm chứng" nói quá mức tin cậy | MAJOR | Đổi thành "cách nhóm sắp xếp…; *theo bài giảng Chương 5 (ĐH Thương mại), chưa đối chiếu bản in" | Fixed |
| S8, Unity Lab | Trích "Sửa đổi lối làm việc" được dẫn tr.336–337 và trình bày như HCM mô tả "hiệp thương dân chủ" | MAJOR | Trang đúng: tr.336; ghi rõ "Hồ Chí Minh bàn về cách lãnh đạo"; Unity Lab: "Tinh thần này gần với…" | Fixed |
| S8 | Số tiền 20 triệu và phương án "Góc đọc xanh" trình bày như thật / như lời giải | MINOR | Ghi "(giả định)", "(ví dụ)", nhãn GỢI Ý CỦA NHÓM + tag DIỄN GIẢI | Fixed |
| S9 | Hộp số liệu gộp hai nguồn, "hoàn thành 9/2025" diễn đạt chưa chính xác; nhầm nguồn "Nghị quyết" cho câu chỉ có ở Báo cáo chính trị | MINOR | Viết lại theo đúng nguồn (xây mới, sửa chữa 334.234 căn; "đến 9/2025"; Báo cáo chính trị ĐH XIV); dòng nguồn ghi ngày từng bài | Fixed |
| S9 | Ghi chú diễn ý công thức Nghị quyết Đại hội XIV, bỏ "sự lãnh đạo của Đảng" | MINOR | Trích nguyên công thức | Fixed |
| S9 | "Lợi ích chung làm điểm quy tụ" chỉ có 1 nguồn T2 | MAJOR | Bổ sung neo T1: NQ 23-NQ/TW (2003) "…làm điểm tương đồng, xoá bỏ mặc cảm, định kiến…" (đọc toàn văn) | Fixed |
| S10 | Tiêu đề khẳng định "thời đại mỗi người một feed" như sự thật; "ngày càng" không có nguồn | MINOR | Tiêu đề thành câu hỏi "…KHI MỖI NGƯỜI MỘT “FEED”?"; bỏ "ngày càng"; thêm tag DIỄN GIẢI | Fixed |
| S10 | Số liệu mạng xã hội: ghi chưa rõ cơ quan, mốc dữ liệu | MINOR | Cục PTTH&TTĐT – Bộ TT&TT, báo cáo 28/11/2024, số liệu trong nước tính đến 30/6/2024, TTXVN đăng mst.gov.vn 29/12/2024; "tài khoản, không phải số người" | Fixed |
| S10 | Trích phát biểu Tổng Bí thư bị cắt mất vế "lan tỏa hiểu biết, tinh thần cầu thị, tranh luận có văn hóa" | MINOR | Trích đủ câu; thói quen 2 đổi thành "Tranh luận có văn hóa" (không phải né tránh) | Fixed |
| S12 | Tóm tắt "A đúng một phần — nhất trí về mục đích" bỏ mất "lập trường" | MAJOR | "cần nhất trí về mục đích **và lập trường**" | Fixed |
| S12 | Gán "hiệp thương dân chủ" là điều **HCM nhấn mạnh** (thực ra là thuật ngữ giáo trình) và có thể bị hiểu là coi nhẹ biểu quyết | MAJOR | "với Mặt trận, **giáo trình** nêu nguyên tắc hiệp thương dân chủ"; C là cách ra quyết định hợp lệ — HCM: "thiểu số phải phục tùng đa số" (t.5 tr.276, đọc trực tiếp) | Fixed |
| S12 | "vì nước, vì dân" bị chuyển chỗ thành định nghĩa lập trường; "kể cả quá khứ" thiếu điều kiện | MINOR | "Mục đích và lập trường" + bối cảnh 1958; "…kể cả quá khứ, nếu nay thật thà tán thành mục tiêu chung" | Fixed |
| S13 | Cam kết viết như đã đối chiếu **bản in** giáo trình (thực tế chưa có) | MAJOR | "đối chiếu khung nội dung qua đề cương các trường dùng giáo trình 2021 (chưa đối chiếu bản in)…" | Fixed |
| S15 | Câu hỏi 1 để ngoặc kép một diễn ý và bỏ "lập trường" | MINOR | Trích đúng "mục đích phải nhất trí và lập trường cũng phải nhất trí" | Fixed |
| Unity Lab | Gọi mọi luận điểm là "nguyên tắc"; nguồn ghi như đã đọc giáo trình; phản hồi "bỏ phiếu" có thể bị hiểu là chê biểu quyết; tiêu đề "không hình thức" là lời nhóm | MINOR | Đổi thành "Luận điểm lý luận liên quan"; ghi mức tin cậy; nói rõ biểu quyết hợp lệ, rủi ro là bỏ qua bàn bạc; "Đoàn kết thực sự: vừa đoàn kết, vừa đấu tranh"; thêm câu HCM về vùng miền cho tình huống 3 | Fixed |
| S11 | Thời lượng: game 2 phút nhưng slot ghi 75 giây | MINOR | Slot 2:15, cắt bớt S2, S3, S8, S9, S10, S12, S13 → tổng 11:50 | Fixed |
| Tất cả | Số trang giáo trình 2021 | — | **Không thể kiểm chứng** (không có bản in). Không bịa số trang; ghi "Exact page … not independently verified" | Open — sinh viên đối chiếu |
| S3, S7, S8, S10, S12 | Số lượng "điều kiện" (3 hay 4) và vị trí mục "Phương thức" trong bản in | — | Trình bày thận trọng, gắn MEDIUM, ghi chú "cần đối chiếu bản in" | Open — sinh viên đối chiếu |

## B. Bố cục & hình ảnh (PASS 3)

| Slide | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| Toàn deck | File PPTX đầu tiên PowerPoint **không mở được** (2 thẻ `effectLst` trùng do helper đổ bóng) | CRITICAL | Sửa helper dùng lại `effectLst` có sẵn; mọi bản sau mở và xuất được | Fixed |
| Tất cả | Nhãn loại nội dung (pill) bị xuống dòng | MAJOR | Sửa công thức tính độ rộng | Fixed |
| S1 | Dòng nguồn ảnh chân dung tương phản thấp trên nền sepia | MAJOR | Chuyển lên góc trên, chữ nâu đậm | Fixed |
| S3 | Tiêu đề "KHÔNG HỌC LẠI —" gãy dòng ở dấu gạch; dòng nguồn đè số trang | MINOR | Đổi dấu, 30pt; thu hẹp dòng nguồn | Fixed |
| S3 | Ảnh nền tư liệu (Quốc hội khóa I) quá sáng, chữ ngà khó đọc | MAJOR | Duotone tối hơn + lớp phủ chuyển sắc | Fixed |
| S4 | Mệnh đề chính 30pt tràn dòng, đè dòng dưới | MAJOR | 27pt, dời vị trí | Fixed |
| S5 | Ảnh ghép chữ "ĐẠI" kiểu lưới đều cắt mặt người ở mép chữ, hàng dưới gần như không thấy | MAJOR | Ghép **theo từng chữ cái** (Đ 2×2, Ạ 2×2 + dấu, I 1×3), chỉnh tiêu điểm từng ảnh | Fixed |
| S5 | Hộp trích dẫn tràn sau khi trích đủ câu | MAJOR | Nới hộp, 13pt | Fixed |
| S6 | Tiêu đề chữ ký xuống 2 dòng; dòng trích HCM mồ côi số trang; câu hỏi xuống dòng | MAJOR | 66/80pt một dòng; tách trích dẫn 2 dòng có chủ đích; câu hỏi 19pt một dòng | Fixed |
| S7 | Chữ ngón tay chật; dòng "dưới sự lãnh đạo của Đảng" bị lòng bàn tay che; nhãn ngón xuống dòng đè tiêu đề | MAJOR | Ngón rộng hơn, rút gọn "nền tảng công – nông – trí; do Đảng lãnh đạo", nhãn ngắn | Fixed |
| S8 | Thẻ hé lộ che mất ảnh và nhãn 4 nhóm trong bản PDF tĩnh | MAJOR | Dời thẻ xuống dưới hàng ảnh | Fixed |
| S9 | Mô tả dưới ảnh đè khối phân tích | MAJOR | Giảm chiều cao dải ảnh | Fixed |
| S10 | Nhãn điện thoại đè trích dẫn; thói quen 2 xuống dòng đè thói quen 3 | MAJOR | Rút gọn, dời khối | Fixed |
| S11 | Hàng "chip" tràn sang ảnh điện thoại | MINOR | Gộp thành 1 dòng chữ | Fixed |
| S12 | Tiêu đề xuống dòng; nhãn đè ranh giới ảnh/nền; câu chốt 3 dòng đè nhãn | MAJOR | 25pt; nhãn xếp dọc trong vùng ảnh; câu chốt 15pt | Fixed |
| Unity Lab | Thanh trên hiện cả ở trang chủ (CSS `display:flex` đè `hidden`); nền trắng dưới trang dài; viền focus quanh khung chế độ trình chiếu | MAJOR | `[hidden]{display:none!important}`; nền html; tắt outline cho `main` | Fixed |

### B2. Vòng QA thị giác độc lập (5 người duyệt, render 1920×1080 + 6 màn hình Unity Lab), rồi sửa và render lại để kiểm tra

Cách làm: mỗi người duyệt xem ảnh render thật của 3 slide, phóng to từng vùng, ghi tọa độ lỗi; sau khi sửa, render lại toàn bộ (v11, v12) và tự kiểm tra từng slide đã sửa.

| Slide | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| S1 | Dấu nặng của "Ạ" (ĐẠI) nằm ngay trên dấu mũ của "Â" (DÂN) — tiêu đề đọc thành "DẬN" | CRITICAL | Giãn dòng tiêu đề 0,95 → 1,1; dời phụ đề và dòng học phần xuống | Fixed (v11) |
| S1 | Đường mép dọc cứng ở x≈1008 px: lớp chuyển sắc cắt ngang hoa văn trống đồng | MAJOR | Bỏ lớp chuyển sắc; ảnh chân dung xuất PNG có kênh trong suốt mờ dần sang trái, hoa văn hiện liền mạch phía sau | Fixed (v11) |
| S1, S15 | Dải lụa đỏ bị cắt phẳng (mép ngang cứng, đường vàng đứt), có vệt bóng kiểu mẫu có sẵn | MAJOR | Vẽ lại dải lụa: đường cong nằm trọn trong ảnh, trong suốt phía trên, không vệt bóng, thấp hơn | Fixed (v11) |
| S1 | Dòng nguồn ảnh xuống 2 dòng, chữ nâu trên tóc trong ảnh | MINOR | Rút gọn 1 dòng, chữ kem đặt trên dải lụa | Fixed (v11) |
| S1, S13 | Ô trống "Nhóm ___ · Lớp ___ · GVHD ___" | MAJOR | S13: thay bằng "Toàn bộ thành viên nhóm", bỏ dòng ký tên trên slide (chữ ký ở 07_AI-USAGE.md §9). S1: giữ ô trống — **nhóm điền tên thật** (AI không được tự đặt tên) | S13 Fixed · S1 Open (nhóm) |
| S2 | Phương án B dài nhất, "lộ" đáp án; chữ chỉ lấp nửa trên thẻ | MINOR | Cân độ dài 4 phương án (đồng bộ với Unity Lab); chữ 19pt; thẻ thấp hơn | Fixed (v11) |
| S2, S3, S7, S8, S12 | Từ ghép tiếng Việt bị tách dòng tự động (ngón / tay, mục / tiêu, tổ / chức, độ / lượng, nhân / dân, thống / nhất, quá / khứ…) | MAJOR | Ngắt dòng thủ công theo cụm nghĩa và dấu cách không ngắt (NBSP); helper chuyển "
" thành ngắt dòng thật `<a:br/>`. Vòng xác nhận (B4) còn thấy từ ghép bị tách ở S3, S5, S7–S10, S13 → xử lý **toàn deck** bằng `_build/vn_wrap.py` | Fixed (v17) |
| S3 | Chú thích cuối slide giống "việc cần làm" ("cần đối chiếu bản in"), sát mép dưới | MAJOR | Ghi nguồn gọn 2 dòng: khung giáo trình qua đề cương các trường; *theo bài giảng Ch.5 ĐH Thương mại (hạn chế "chưa đối chiếu bản in" vẫn ghi ở S13 và 05_theory-verification.md) | Fixed (v11) |
| S3 | Nhãn nút 4 sát mép panel trái; chữ trắng trên ảnh đám đông khó đọc | MAJOR | Thu hẹp, căn phải, dời nhãn; lớp phủ đậm hơn ở nửa dưới panel | Fixed (v11) |
| S3, S8, S9, S10 | Chữ số kiểu old-style của Constantia làm "20.000.000", "334.234", số thứ tự nhảy lên xuống | MINOR | Số dùng Segoe UI Semibold; tiêu đề S8 viết "BỐN NHÓM" | Fixed (v11–v12) |
| S4, S5 | Hộp trích dẫn đệm trên/dưới lệch; nguồn ngắt giữa "Toàn / tập" | MINOR–MAJOR | Thu hộp, cân lề; xuống dòng trước "Toàn tập" | Fixed (v11) |
| S5 | Ô ảnh giữa chữ "I": cây thánh giá chéo đọc thành dấu "X" đỏ (như ký hiệu loại trừ) | MAJOR | Cắt ảnh rước lễ lấy phần người mặc lễ phục (vẫn thể hiện đồng bào Công giáo), không còn thánh giá chéo | Fixed (v11) |
| S5 | Dấu nặng tròn cắt mất đầu người ("người không đầu") | MINOR | Ô ảnh dấu nặng cắt theo đúng khung tròn, giữ trọn dáng người lễ chùa | Fixed (v11) |
| S6 | Đường chia dọc chạm câu hỏi; hai vế so sánh không thẳng hàng; "điểm / chung" mồ côi | MAJOR | Rút đường chia; nhãn hai vế cùng một đường cơ sở; ngắt dòng thủ công | Fixed (v11) |
| S7 | Lòng bàn tay chữ lệch trên; ngón tay rời như viên nang; chú thích lộ "việc cần làm" | MAJOR | Căn giữa dọc; ngón kéo dài ra sau lòng bàn tay; chú thích chỉ ghi nguồn | Fixed (v11) |
| S8 | Nhãn vàng nằm trên vùng ảnh rối; câu hướng dẫn lệch đường cơ sở; mặt người bị cắt mép trên (ảnh 3) | MAJOR | Lớp phủ tối bắt đầu cao hơn; căn đường cơ sở; đổi tiêu điểm ảnh 3 | Fixed (v11) |
| S8 | Thẻ gợi ý hiện cùng lúc với câu hỏi 30 giây | MINOR | Đã là hiệu ứng **bấm mới hiện** trong PPTX; ảnh render/PDF hiển thị trạng thái cuối | No change needed |
| S9 | Dòng nguồn xuống 2 dòng, tách "NQ 23- / NQ/TW", sát mép dưới; thẻ số liệu 3 chật | MAJOR | Nguồn 1 dòng; rút gọn mô tả thẻ; mũi tên to hơn; ảnh "Quốc gia" sáng hơn 28% | Fixed (v11–v12) |
| S10 | Trích dẫn kết thúc bằng 1 từ mồ côi; khoảng trống lệch | MAJOR | 12,5pt, cân lại vị trí trích dẫn – nguồn – lưu ý | Fixed (v12) |
| S11 | Hai lời kêu gọi trùng nhau; mũi tên chỉ vào ảnh điện thoại; "màu." mồ côi | MAJOR | Nút: "QUÉT MÃ BÊN PHẢI →"; dưới QR: "Mở camera điện thoại để quét"; ngắt dòng thủ công | Fixed (v11) |
| S11 | Chưa có mã QR thật | CRITICAL (theo người duyệt) | **Cố ý**: chưa có URL triển khai thật nên không tạo QR giả; ô ghi "QR PLACEHOLDER — UPDATE AFTER DEPLOYMENT". Sau khi triển khai: `python _build/make_qr.py <URL>` | Fixed — triển khai 2/10/2026, QR thật (B5) |
| S12 | Thẻ trái trống nửa dưới; câu chốt sát thẻ; đoạn "Nhìn lại 4 đáp án" 4 dòng tràn lề phải; câu HCM ngắt "đại / thành công"; nhãn B trùng | MAJOR | Căn giữa dọc 2 thẻ; giãn khoảng; tóm 2 dòng trong lề thẻ (chi tiết chuyển sang ghi chú); ngắt câu theo nhịp "Đoàn kết, đoàn kết, / đại đoàn kết, / Thành công, thành công, / đại thành công"; bỏ nhãn B góc trên | Fixed (v11–v12) |
| S13 | Ghi chú "điền trung thực trước khi nộp" như việc cần làm; dòng gạch dưới chữ ký; câu cam kết dài; gạch đầu dòng không thụt treo | MAJOR | Thay bằng trỏ tới nhật ký chỉnh sửa (07_AI-USAGE.md §5); cam kết gọn 2–3 dòng; thụt treo cho dòng xuống | Fixed (v11–v12) |
| S14 | Khoảng trống giữa trang; tên riêng/giấy phép bị tách ("Ph. / Devillers", "CC / BY-SA") | MINOR | Dời hàng dưới lên; NBSP trong tên và giấy phép | Fixed (v11) |
| S15 | Câu hỏi 1 dài 5 dòng; "ví / dụ" tách | MINOR | Rút gọn câu hỏi 1; NBSP | Fixed (v11) |
| Toàn deck | Số trang (folio) lệch lề trái 14 px so với nội dung | MINOR | Folio x = 0,6 in, thẳng lề nội dung | Fixed (v11) |
| Unity Lab | Màn hình phản hồi mở giữa trang (thanh trên nằm giữa) | MAJOR | Kiểm tra lại: do kịch bản chụp màn hình bấm phần tử cuối trang trước khi chụp. Mã vẫn đặt lại cuộn về đầu (đã thêm `behavior:"instant"` + lần gọi sau khung hình); đo `scrollY = 0` sau khi trả lời ở cả 3 tình huống | Fixed / verified |
| Unity Lab | Tiêu đề luận điểm lặp lại nguyên văn ở đầu đoạn (2 mục) | MAJOR | Viết lại phần thân của 2 mục | Fixed |
| Unity Lab | Vùng yên tĩnh của QR ≈ 1,5 mô-đun (cần 4); lời kêu gọi ở chế độ trình chiếu quá nhỏ; URL nhỏ, có "/index.html" | MAJOR | Lề QR 32 px = 4 mô-đun; "Quét mã để tham gia" 26–38 px; URL 18–28 px, bỏ "index.html" | Fixed (đo lại trên ảnh chụp) |
| Unity Lab | URL trong ảnh chụp là 127.0.0.1 | CRITICAL (theo người duyệt) | Đúng hành vi khi chạy thử trên máy: chế độ `?present` luôn mã hóa địa chỉ đang mở. Khi trình chiếu phải mở từ URL đã triển khai (03_UnityLab/README.md) | Fixed — địa chỉ thật (B5) |
| Unity Lab | Trang kết quả rất dài; huy hiệu "Người kết / nối"; chữ in đậm giãn chữ; từ mồ côi trong lựa chọn | MINOR | 5 luận điểm thu gọn dạng chạm-để-mở; NBSP trong tên phong cách; bỏ giãn chữ; `text-wrap: pretty`; hàng lựa chọn căn giữa với chữ cái | Fixed |

### B3. Vòng kiểm tra độc lập cuối cùng (3 người duyệt: thị giác · độ chính xác học thuật · nhất quán giữa các tệp; mỗi phát hiện được 1 người khác kiểm chứng phản biện)

29 phát hiện → 23 được xác nhận, 6 bị bác. Tất cả 23 đã xử lý; deck được render lại (v13–v15) và kiểm tra bằng mắt các slide bị ảnh hưởng.

| Slide / tệp | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| Unity Lab (tình huống 3) | Trích "Đồng bào Nam Bộ là dân nước Việt Nam. Sông có thể cạn…" chưa có trong ma trận; lời dẫn "Về khác biệt vùng miền, Hồ Chí Minh viết" gán cách đọc của nhóm cho Hồ Chí Minh | MAJOR | Đối chiếu trực tiếp: **đúng nguyên văn**, Toàn tập t.4, tr.280 (Thư gửi đồng bào Nam Bộ, 1-6-1946) → thêm dòng Q-21 vào ma trận; viết lại lời dẫn theo đúng bối cảnh (khẳng định Nam Bộ là một phần không thể tách rời của nước Việt Nam) và ghi rõ liên hệ với khác biệt vùng miền là vận dụng của nhóm | Fixed |
| Ghi chú S12, Q&A #3 | Câu "Muốn tiến lên chủ nghĩa xã hội, mọi người cần đoàn kết thực sự…" đặt trong ngoặc kép nhưng chưa có trong ma trận | MINOR | Đối chiếu trực tiếp t.11, tr.362: nguyên văn "…cần đoàn kết thực sự và giúp nhau cùng tiến bộ." → trích đủ câu, ghi vào dòng Q-08 | Fixed |
| S9 | Thẻ "2035" bỏ mất ý "xây dựng và triển khai" (dễ hiểu là Chiến lược đã có sẵn) | MINOR | "Đại hội XIV (1/2026): xây dựng, triển khai Chiến lược đại đoàn kết toàn dân tộc đến 2035" (tầm nhìn 2045 giữ trong lời nói và nguồn) | Fixed |
| Ghi chú S10 | Số tài khoản mạng xã hội ghi độ tin cậy HIGH, trong khi 04_sources ghi MEDIUM | MINOR | MEDIUM (T1; là số tài khoản, không phải số người dùng) | Fixed |
| S14 | Thiếu t.5, tr.276 (trích "thiểu số phải phục tùng đa số" dùng ở S12) | MINOR | "t.5 (tr.276, 336)" | Fixed |
| Ghi chú S13 | Lời nói nói sinh viên **đã** kiểm tra từng trích dẫn, trong khi phần kiểm chứng do AI làm và checklist của nhóm chưa đánh dấu; không nói ví dụ "AI tự sai" đang hiện trên slide | MINOR | Nói đúng ai làm gì (AI đối chiếu; nhóm kiểm tra lại theo checklist) và đọc ví dụ AI tự sai (t.14, tr.27); README thêm bước tự kiểm tra trích dẫn trước khi nộp | Fixed |
| S4, S7, S9, S10, S15 | Từ ghép bị tách dòng trong trích dẫn và thẻ số liệu (lâu / dài, trung / thực, ngón / dài, Chiến / lược, mục / đích…) | MINOR | NBSP và ngắt dòng có chủ đích; S10 trích dẫn 4 dòng theo cụm, nguồn dời xuống | Fixed (v15) |
| Unity Lab | Số thứ tự trong danh sách luận điểm dùng chữ số old-style, lệch tâm vòng tròn | MINOR | `font-variant-numeric: lining-nums` (cả đồng hồ đếm giờ) | Fixed |
| README | Checklist còn bảo điền tên ở slide 13 (đã bỏ); thiếu Author PPTX và 07 §9; bước dựng lại không tạo lại 06/04/10; không cảnh báo build_deck.py xóa QR thật | MAJOR | Sửa checklist; thêm lệnh export_notes_md / make_sources_md / contact_sheet; cảnh báo chạy lại make_qr.py (cần `pip install segno`) sau mỗi lần dựng | Fixed |
| 08_rubric-mapping | Rủi ro 1.1 nói slide "không gắn số mục" (thực tế có đánh số 1–5 và điều kiện 1–4); rủi ro 1.2 lỗi thời; danh sách slide có nhãn DIỄN GIẢI thiếu S8, S10; phương án dự phòng mô tả khác ghi chú | MAJOR/MINOR | Viết lại đúng hiện trạng | Fixed |
| 06, 11, 03_UnityLab/README | Còn gọi khối lý luận là "nguyên tắc liên quan" (game đã đổi thành "Luận điểm lý luận liên quan"); tiêu đề S8, S10 cũ; S3 ghi "40 giây" nhưng thời lượng 0:35; bảng phân công ghi S15 cho Thành viên 5 trong khi ghi chú ghi "Cả nhóm" | MINOR | Đồng bộ thuật ngữ, tiêu đề, thời lượng, phân công; tạo lại 06 | Fixed |
| 07_AI-USAGE | Tham chiếu "xem mục 7" sai (đúng là mục 8) | MINOR | Sửa | Fixed |

### B4. Vòng xác nhận sau sửa (3 người duyệt + kiểm chứng phản biện từng phát hiện)

Kiểm tra lại 23 phát hiện của B3 trên file và ảnh render mới: 19 phát hiện → 15 xác nhận, 4 bị bác. Đã xử lý cả 15 và render lại (v16–v17), xem lại cả 15 slide.

| Slide / tệp | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| Toàn deck (S3, S5, S7, S8, S9, S10, S13) | Vẫn còn từ ghép bị tách dòng (trả / lời, công / thức, dân / chủ, tài / khoản, đảng / phái, đề / cương, hình / thức…); báo cáo B2 ghi "Fixed" là chưa đúng | MAJOR | `_build/vn_wrap.py`: danh sách ~190 từ ghép hai âm tiết; `deck_lib.text()` tự nối bằng NBSP cho mọi chữ ≤ 24pt. Ba đoạn bị đổi dòng xấu sau đó (S5 "Chủ thể", S9 phân tích, S10 câu hỏi) được ngắt dòng thủ công | Fixed (v17) |
| Ghi chú S13 | Câu lặp "lập ma trận kiểm chứng"; lời nói ~230 âm tiết cho 0:30 | MINOR | Viết lại gọn (~140 âm tiết), giữ ví dụ "AI tự sai" khớp với slide; bỏ ví dụ "Dễ trăm lần…" (vẫn ghi ở 05 mục D, X-04) | Fixed |
| Ghi chú S11, 05 | Danh sách luận điểm Unity Lab còn Q-06 (không dùng), thiếu Q-21, T-15; Q-21 đứng trước Q-20 | MINOR | Sửa danh sách; bỏ ghi chú "dùng trong Unity Lab" ở Q-06; xếp lại thứ tự | Fixed |
| 05 | 8 dòng ma trận ghi "dùng ở ghi chú/Q&A" nhưng thực tế không dùng (T-04, Q-03, Q-10, Q-11, Q-13, Q-14, Q-15, Q-17); S14 vì thế liệt kê t.7 tr.38, t.10 tr.453 | MINOR | Đánh dấu "dự phòng; chưa dùng" (Q-10: chỉ diễn ý ở S3); danh mục trang S14 chỉ còn các trang thực sự được trích | Fixed |
| Q&A #3, #4 | Hai câu trích chưa có dòng trong ma trận | MINOR | Đối chiếu trực tiếp Toàn tập: "ưa ai thì kéo vào, không ưa thì tìm cách tẩy ra" — t.5, tr.276 (ghi vào Q-20); "liên minh công nông là nền tảng của Mặt trận dân tộc thống nhất" — t.12, tr.417, bài "Ba mươi năm hoạt động của Đảng" (Nhân dân, 6-1-1960) → dòng Q-22; thêm t.12 tr.417 vào S14 | Fixed |
| 08, 11 | Nói mọi câu Q&A đều gắn nhãn TEXTBOOK-SUPPORTED / APPLICATION, nhưng 5 câu dùng nhãn khác | MINOR | Ghi đúng: chủ yếu hai nhãn đó, một số câu dùng nhãn Phương pháp / Trả lời thật / Kết quả kiểm chứng | Fixed |
| Ghi chú S8, 04 | Loại nội dung thiếu "Diễn giải của nhóm"; trích phát biểu Tổng Bí thư không có nguồn ở S8 | MINOR | Bổ sung loại nội dung và nguồn C-10; 04 ghi C-10 dùng ở S8, S10 | Fixed |
| S9 | Mũi tên nối ảnh gần chạm ảnh kế tiếp | MINOR | Rãnh giữa ảnh 0,27 in, mũi tên căn giữa | Fixed (v16) |
| Unity Lab | Đáp án A, D tách "quan / điểm", "hòa / khí"; câu "quay lại câu hỏi này ở slide cuối" sai (thực tế là slide tiếp theo, S12) | MINOR | NBSP; sửa thành "ngay ở slide tiếp theo" | Fixed |
| README / `_build/make_sources_md.py` | Bước dựng lại `04_sources.md` đọc tệp từ thư mục tạm của phiên AI → không chạy được trên máy nhóm | MINOR | Chép `sources_opened.json` (nhật ký các trang nguồn đã mở) vào `_build/`, sửa đường dẫn | Fixed |

### B5. Triển khai Unity Lab và QR thật (2/10/2026)

| Slide / tệp | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| Netlify | Sau lần đăng đầu, mọi địa chỉ trả về **401 "Login Redirect"**: nhóm Netlify bật sẵn bảo vệ truy cập (chỉ thành viên đăng nhập mới xem được) → điện thoại của lớp sẽ gặp trang đăng nhập | CRITICAL | Được người dùng đồng ý: đặt bảo vệ cho bản thử (non-production) thôi; bản chính công khai. Kiểm tra lại: `/`, `index.html`, `style.css`, `script.js`, `assets/*` đều 200; `README.md`, `netlify.toml` 404 | Fixed |
| Netlify | Gói miễn phí tự chèn nút "Powered by Netlify" cố định ở góc dưới, có lúc che dòng chữ cuối trên điện thoại | MINOR | Thêm khoảng trống cuối trang (`padding-bottom` 96px + safe-area), đăng lại | Fixed |
| Netlify | CLI tự tạo `netlify.toml` (ghi đường dẫn thư mục trên máy) và gửi kèm khi đăng | MINOR | Kiểm tra: tệp không được phục vụ công khai (404) | No change needed |
| S11 | Thay khung QR PLACEHOLDER bằng QR thật | — | `make_qr.py`: QR mức sửa lỗi H, vùng yên tĩnh 4 mô-đun; giải mã thử bằng jsQR trên ảnh render: ảnh QR 470px, thu nhỏ còn 160px và 110px, và cả slide thu còn 960px → cả 4 đều ra đúng `https://unitylab-hcm202.netlify.app/`. `build_deck.py` tự dùng lại QR này khi dựng lại | Fixed |
| Unity Lab (bản trên mạng) | Chơi thử trên trình duyệt di động (390×844): đủ 3 tình huống tới màn hình kết quả, không lỗi console; `?present` hiện đúng địa chỉ và QR | — | — | Verified |

### B6. Đổi phông chữ và làm lại trang giới thiệu Unity Lab (3/10/2026)

| Slide / tệp | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| Toàn deck | Phudu hẹp hơn Constantia (chữ hoa ~77% bề rộng) và không có chữ nghiêng; Be Vietnam Pro rộng hơn Segoe UI ~8% | MAJOR | Helper tự xử lý: tiêu đề ≥ 20pt to thêm 10%, chữ đậm dùng bản Phudu ExtraBold (không đậm giả), chữ nghiêng chuyển sang Be Vietnam Pro Italic, chữ thân thu 7% để giữ nguyên chỗ xuống dòng | Fixed (v20) |
| S1, S2, S5, S11 | Tiêu đề to hơn chạm dòng dưới; trích dẫn S5 tràn khung | MAJOR | Chỉnh giãn dòng và vị trí; khung trích dẫn S5 cao hơn | Fixed (v21) |
| S12 | Câu dài đặt bằng Phudu (chỉ có chữ hoa) khó đọc | MINOR | Câu dài chuyển sang Be Vietnam Pro | Fixed (v20) |
| S5 | Chữ ĐẠI ghép ảnh vẽ lại bằng Phudu Black cho đồng bộ; khung cao hơn | MINOR | Đặt vừa khung, căn giữa | Fixed (v20) |
| S10–S13 | Be Vietnam Pro không có ký tự mũi tên (→, ↔): PowerPoint tự thay bằng Times New Roman | MINOR | Chỉ các mũi tên đặt bằng Segoe UI; kiểm tra danh sách phông trong PDF | Fixed (v23) |
| Unity Lab | Ảnh trong lưới bị kéo theo thuộc tính width/height; thẻ tình huống trên máy tính dừng ở tư thế nghiêng 75° (CSS transition và GSAP cùng điều khiển transform) | MAJOR | `img { height: auto }`; bỏ transition transform khi có GSAP, hiệu ứng nghiêng khi rê chuột làm bằng GSAP | Fixed |
| Unity Lab | Chữ trắng của dòng giới thiệu chìm trên ảnh nền; nút "Bắt đầu" và dòng "Khám phá" chồng nhau trên điện thoại; tiêu đề bị ngắt giữa cụm | MINOR | Lớp phủ tối hơn; xếp dọc trên điện thoại; tiêu đề ngắt theo cụm | Fixed |
| Unity Lab | Kiểm tra: điện thoại 390×844, máy tính 1440×900, chế độ giảm chuyển động; chơi hết 3 tình huống trên bản đã đăng | — | Không lỗi JavaScript; đủ 5 thư viện; bản giảm chuyển động hiện đầy đủ nội dung | Verified |

### B7. Bám khung bài giảng Chương 5 của lớp (4/10/2026)

Người dùng cung cấp bài giảng Chương 5 (TS. Hà Triệu Huy, ĐH KHXH&NV – ĐHQG TP.HCM) và xác nhận đây là bài giảng của lớp.

| Slide / tệp | Issue | Severity | Correction | Status |
|---|---|---|---|---|
| S3 | Khung 5 mục (có "Phương thức") khác bài giảng của lớp (mục II: Vai trò · Nội dung: đoàn kết toàn dân, điều kiện · Hình thức tổ chức) | MAJOR | Sơ đồ 4 mảnh đánh số theo bài giảng (1 · 2a · 2b · 3); nguồn ghi bài giảng của lớp | Fixed |
| S7 | 4 điều kiện (có "lợi ích chung") khác bài giảng (3 điều kiện + 4 nguyên tắc Mặt trận) | MAJOR | Ngón tay: điều kiện 1–3, nguyên tắc 1 và 3; lòng bàn tay: nguyên tắc 2 "Bảo đảm lợi ích tối cao của dân tộc…"; nguyên tắc 4 ghi ở chú thích | Fixed |
| S4, S5 | Diễn đạt và đánh số khác bài giảng ("…của cách mạng Việt Nam"; "2 · Lực lượng") | MINOR | "…của Đảng, của dân tộc"; "2a · Nội dung" | Fixed |
| S8, S10, Unity Lab | Còn dùng cụm "lấy lợi ích chung làm điểm quy tụ" (theo ĐH Thương mại) | MINOR | Dùng cách nói của bài giảng: thống nhất mục tiêu và lợi ích; nguồn trong Unity Lab ghi mục của bài giảng | Fixed |
| Bài giảng | Một số câu bài giảng ghi là lời HCM khác nguyên văn ("đồng tâm" thay "đồng minh"; "ngón ngắn… thuộc về một bàn tay"; "thật sự… học hỏi"); "cầu đồng tồn dị" chỉ có ở chú thích về Chu Ân Lai | — | Ghi vào `05` mục G; slide giữ nguyên văn Toàn tập; chuẩn bị Q&A #8, #13, #17 | Recorded |
| Render | PowerPoint không thấy phông Phudu/Be Vietnam Pro trong phiên mới (phông cài cho người dùng chưa được nạp), tiêu đề rơi về phông mặc định | MAJOR | `render.ps1` tự nạp phông từ `12_assets/fonts/src` cho phiên làm việc trước khi mở PowerPoint | Fixed |

## C. Kiểm tra cuối (định dạng file)

- PPTX mở và xuất PDF/PNG bằng Microsoft PowerPoint (Office 16) không lỗi; phông Phudu ExtraBold, Be Vietnam Pro, Be Vietnam Pro SemiBold và Segoe UI (chỉ cho các mũi tên) được **nhúng** vào file; PDF không còn phông thay thế.
- Quét tự động toàn bộ chữ trên slide và ghi chú: chỉ còn 1 chỗ giữ chỗ **có chủ đích** — ô "Nhóm ___ · Lớp ___ · GVHD: ___" ở S1 để nhóm tự điền. Khung QR PLACEHOLDER ở S11 đã được thay bằng QR thật của https://unitylab-hcm202.netlify.app/.
- 3 slide có hiệu ứng bấm-để-hiện (S5, S8, S12); bản PDF thể hiện trạng thái cuối của mỗi slide.
- Ghi chú thuyết trình có ở cả 15 slide.
