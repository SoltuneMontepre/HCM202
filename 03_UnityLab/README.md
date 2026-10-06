# Unity Lab — hướng dẫn chạy & triển khai

Mini-game 3 tình huống cho slide 11 ("UNITY LAB — Bạn xử lý khác biệt như thế nào?").
Trang tĩnh thuần HTML/CSS/JS, **không có backend, không thu thập dữ liệu**: lựa chọn của người chơi chỉ nằm trong trình duyệt của họ.

```
03_UnityLab/
  index.html     khung trang
  style.css      giao diện (burgundy / cream / gold, ưu tiên điện thoại)
  script.js      nội dung tình huống + logic (sửa nội dung ở đầu file)
  assets/        drum.svg (hoa văn nền, do nhóm tự vẽ), favicon.svg
```

## Chạy thử trên máy

Mở `index.html` bằng trình duyệt là chạy được. Nếu trình duyệt chặn file cục bộ, chạy một server tĩnh trong thư mục cha:

```bash
python -m http.server 8765 --directory 03_UnityLab
```

rồi mở `http://localhost:8765`.

## Bản đang chạy trên mạng

- Địa chỉ: **https://unitylab-hcm202.netlify.app/** — chế độ trình chiếu: `https://unitylab-hcm202.netlify.app/?present`
- Triển khai ngày 2/10/2026 lên Netlify, dưới tài khoản Netlify của nhóm (người dùng tự đăng nhập và cấp quyền cho Netlify CLI).
- Chỉ 5 tệp công khai: `index.html`, `style.css`, `script.js`, `assets/drum.svg`, `assets/favicon.svg` (README này không đăng). Trang có `noindex` để không lên kết quả tìm kiếm.
- Truy cập: bản chính (production) công khai; các bản thử (deploy preview, branch deploy) vẫn yêu cầu đăng nhập Netlify của nhóm.
- Gói miễn phí của Netlify tự chèn nút "Powered by Netlify" ở góc dưới phải; trang đã chừa khoảng trống phía dưới để nút này không che chữ.
- Cập nhật: `python _build/stage_unitylab.py` rồi `netlify deploy --prod --dir _build/site_unitylab --site unitylab-hcm202`.

## Trang giới thiệu (landing page)

Mở trang là thấy phần giới thiệu cuộn dọc, nút **Bắt đầu** vào thẳng game:

1. Mở đầu: chữ UNITY LAB bay vào, nền là 3 cột ảnh gương mặt Việt Nam chạy liên tục, pháo giấy vàng.
2. ĐOÀN KẾT ≠ ĐỒNG NHẤT: khi cuộn, một hàng chấm giống hệt nhau tách ra thành nhiều hình, nhiều màu và cùng xoay quanh "điểm chung" (diễn giải của nhóm).
3. AI NẰM TRONG CHỮ "ĐẠI"?: chữ ĐẠI ghép ảnh mở ra như ống kính, 16 gương mặt bay vào lưới.
4. 1945 – 1946: bộ sưu tập ảnh tư liệu cuộn ngang (được ghim khi cuộn dọc).
5. Từ một lớp học đến cả quốc gia; 3 thẻ tình huống lật lên; nút bắt đầu cuối trang.

Giữa các màn hình game có hiệu ứng màn đỏ quét qua; chọn đáp án có gợn sóng và pháo giấy nhỏ; màn kết quả có huy hiệu xoay vào và pháo giấy theo màu thẻ.

- Thư viện (tải từ jsDelivr): GSAP 3.15 + ScrollTrigger + SplitText (giấy phép miễn phí của GSAP), Lenis 1.3 (MIT, cuộn mượt trên máy tính), canvas-confetti 1.9 (ISC). Nếu không tải được, trang vẫn chạy đầy đủ, chỉ không có hiệu ứng.
- Người dùng bật "giảm chuyển động" trong hệ điều hành sẽ thấy bản tĩnh (không chạy ảnh, không pháo giấy).
- Phông: Phudu (tiêu đề) + Be Vietnam Pro (chữ), qua Google Fonts.
- Ảnh: 29 ảnh WebP (~1,9 MB) do `_build/prepare_web_images.py` tạo từ ảnh gốc có giấy phép trong `12_assets/downloaded/`; nguồn và giấy phép từng ảnh hiện ở mục **Nguồn ảnh & phông chữ** cuối trang (dữ liệu trong `assets/media.js`).

## Cách khác để đưa lên Internet (nếu cần)

1. **Netlify Drop** — vào <https://app.netlify.com/drop>, kéo thả cả thư mục `03_UnityLab`. Nhận ngay một địa chỉ dạng `https://ten-ngau-nhien.netlify.app`.
2. **GitHub Pages** — tạo repository, tải 4 mục trên lên nhánh `main`, vào *Settings → Pages → Deploy from branch*.
3. **Vercel** — `npx vercel deploy 03_UnityLab` (cần tài khoản).

Việc đăng trang công khai là quyết định của nhóm; hãy kiểm tra nội dung trước khi đăng.

## Sau khi có địa chỉ thật

1. (Đã làm cho địa chỉ ở trên.) Nếu đổi địa chỉ: tạo QR mới và chèn vào slide 11:

   ```bash
   pip install segno
   python _build/make_qr.py https://dia-chi-that-cua-nhom/
   ```

2. Xuất lại PDF từ PowerPoint (hoặc `_build/render.ps1`).

## Chế độ trình chiếu (QR lớn trên máy chiếu)

Mở `https://dia-chi-that-cua-nhom/?present` trên máy chiếu: trang tự tạo **mã QR thật của chính địa chỉ đang mở** (cần Internet để tải thư viện QR `qrcode-generator` từ cdnjs/jsDelivr) và có đồng hồ đếm ngược 2 phút.

## Kịch bản tương tác trong lớp (gợi ý)

1. Slide 11: chiếu QR → "Quét để tham gia" → đếm 2 phút.
2. Mỗi bạn kết thúc với một **thẻ màu**: VÀNG (Người kết nối), ĐỎ (Người quyết đoán), KEM (Người giữ hòa khí), NHIỀU MÀU (Người linh hoạt).
3. Người dẫn hỏi: "Ai thẻ vàng giơ tay? Thẻ đỏ? Thẻ kem?" → cả lớp cùng tham gia, kể cả bạn không có điện thoại (ngồi chung với bạn bên cạnh).
4. Nối sang slide 12: quay lại câu hỏi mở đầu.

## Phân loại nội dung

- Tình huống, lựa chọn, "phong cách" → **VẬN DỤNG ĐƯƠNG ĐẠI / DIỄN GIẢI CỦA NHÓM** (không phải nội dung giáo trình).
- Mục "Luận điểm lý luận liên quan" → diễn đạt lại từ các luận điểm đã đối chiếu trong `05_theory-verification.md`.
