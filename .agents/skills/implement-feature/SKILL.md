---
name: implement-feature
description: Implement or change a feature in MediLab — an Odoo 19 addon under src/modules/, or a client app under applications/. Use when adding a model, field, view, wizard, report, permission, or workflow step; when changing existing lab behaviour; or when the user says "implement", "add a feature", "build", or names a TPC flow. Index skill — loads the reference docs the task actually needs.
---

# Implement a feature

Đây là **index skill**: nó dẫn tới đúng doc tham chiếu thay vì nhắc lại nội dung.
Đọc thứ task cần, bỏ qua phần còn lại.

## Step 0 — always

Đọc [docs/repo-convention.md](../../../docs/repo-convention.md) nếu chưa đọc trong session này. File đó
chứa luật nền và bản đồ của mọi thứ bên dưới.

## Step 1 — locate

Xác định tính năng đụng tới phần nào, rồi nạp doc tương ứng:

| Phần bị đụng                          | Nạp                                                                    |
| -------------------------------- | ------------------------------------------------------------------------ |
| Bất kỳ module Odoo nào                  | [conventions.md](../../../src/modules/docs/conventions.md) — **luôn luôn**, trước khi viết code |
| Một module cụ thể                | `src/modules/<addon>/AGENTS.md` (mục đích 1 dòng + `## Docs`), rồi các trang nó link |
| Một luồng nghiệp vụ hoặc đổi tình trạng  | [business/](../../../docs/business/README.md)                            |
| Một lựa chọn cấu trúc / liên module | các spec dưới [docs/superpowers/specs/](../../../docs/superpowers/specs/) |
| Một client mobile hoặc bên ngoài      | `applications/<app>/AGENTS.md`                                           |
| Bất cứ gì đụng tới deploy         | skill `deployment`                                                   |

Rồi tìm code. Module có sẵn nằm trong `src/modules/` — `AGENTS.md` của mỗi addon nói nó sở hữu gì.
Ưu tiên mở rộng module đã sở hữu khái niệm đó thay vì tạo module mới; module mới cần một ranh giới
thật để biện minh.

## Step 2 — understand before changing

- **Đọc code có sẵn của module trước.** Cách đặt tên, cấu trúc và idiom trong codebase này là
  tiếng Việt và riêng theo module. Code mới phải không phân biệt được với code xung quanh.
- **Tra Odoo core, đừng nhớ lại.** `src/reference/` là core addon của container đang chạy
  (không gồm module của repo), nên mọi kết quả đều là Odoo 19 upstream. Grep ở đó trước khi giả định
  field của model gốc, chữ ký method hay cấu trúc view được kế thừa. Cũ hoặc rỗng?
  `task sync`.
- **Hỏi khi luật nghiệp vụ mơ hồ.** Đoán sai một chuyển tình trạng hay một ranh giới phân quyền
  tệ hơn một câu hỏi. Xem
  [business/](../../../docs/business/README.md) trước — có thể luật đã được ghi lại.

## Step 3 — implement

Theo [conventions.md](../../../src/modules/docs/conventions.md). Những phần hay sai
nhất:

- Cú pháp Odoo 19: `<list>` không phải `<tree>`; `invisible="expr"` không phải `attrs`; mọi field dùng
  trong biểu thức `readonly`/`invisible` phải có trong view (thêm nó với `invisible="1"`).
- `@api.model_create_multi`, `Command.*`, `_compute_display_name`.
- **Model mới cần một dòng `ir.model.access.csv`.** Thiếu dòng đó model sẽ vô hình và tính năng
  "không chạy".
- Thứ tự `data` trong manifest: security → views → data → menu.
- `groups=` và `invisible=` ở mức UI không phải bảo mật. Bắt buộc chặn cả phía server.
- Chuỗi mới hiện cho người dùng đi qua `_()` với tham số `%`, không dùng f-string.

## Step 4 — apply and verify

Chọn đúng lệnh — đây là nguyên nhân phổ biến nhất của lỗi giả:

| Đã đổi                                            | Chạy            |
| --------------------------------------------------- | --------------- |
| Python, hoặc XML view đã có trong `data`            | `task restart`  |
| `data` của manifest, file mới, CSV security, field/model mới | `task upgrade` |
| `requirements.txt` / dockerfile                     | `task rebuild`  |

Rồi kiểm thật — chi tiết trong
[workflow.md](../../../src/modules/docs/workflow.md):

1. `docker compose logs -f odoo` — lỗi XML và registry chỉ xuất hiện ở đây
2. UI tại http://localhost:8069 (`admin`/`admin`), bằng vai trò bị ảnh hưởng, không chỉ bằng admin
3. Dữ liệu qua CloudBeaver hoặc server `postgresql-mcp`, nếu thay đổi có ghi dữ liệu

## Step 5 — finish

- Chạy checklist trước khi commit trong
  [workflow.md](../../../src/modules/docs/workflow.md#before-committing).
- **Cập nhật doc trong cùng change.** Module mới → copy
  [khung doc](../../../src/modules/docs/_template/) vào `src/modules/<addon>/docs/` và link
  từ `AGENTS.md` của addon. Luồng nghiệp vụ mới hoặc đổi → một trang dưới
  [business/](../../../docs/business/README.md), link từ `## Docs` của mọi addon sở hữu.
  Quyết định cấu trúc → một spec dưới [docs/superpowers/specs/](../../../docs/superpowers/specs/).
- Conventional Commit, scope theo module:
  `feat(tpc_thu_nghiem): add subcontractor field to chỉ tiêu`.
- Báo những gì đã kiểm và chưa kiểm. Đường chưa test phải được gọi tên, không để ngầm hiểu.
