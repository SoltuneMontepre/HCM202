---
name: trello-task
description: Create or break down Trello cards on the medilab board following the board's card templates (Task, User Story, Milestone). Use whenever turning notes, a request, or a plan into Trello cards/tasks, splitting work into multiple cards, or rewriting an existing card to the template. Triggers on "Trello", "card", "task", "todo", "break task", "user story", "milestone".
---

# Trello task

Mọi card mới trên board medilab dựng theo template trong list **Draft**. Connector không copy được
card từ template, nên đọc template rồi dựng lại cấu trúc.

## Templates

Template là nguồn sự thật. Đọc lại mỗi lần tạo card (`trelloReadCard get` lấy description,
`trelloReadChecklist list_by_card` lấy checklist), đừng chép cấu trúc từ trí nhớ hay từ file này.

| Loại      | Template card                                      | Dùng khi                                                        |
| --------- | -------------------------------------------------- | --------------------------------------------------------------- |
| Task      | [[Task] tên task](https://trello.com/c/BCSUrPKC)    | Mặc định: việc kỹ thuật/nội bộ (review doc, kiểm tra, chore)    |
| US        | [[US] tiêu đề](https://trello.com/c/DAgUh6nV)       | Có hành vi người dùng thấy được, cần AC Given/When/Then để test |
| Milestone | [[[MILESTONE]] tên](https://trello.com/c/bZyS5t7r)  | User nói rõ, hoặc gom nhiều Task/US chung mục tiêu/deadline     |

Không rõ loại nào thì hỏi user.

## Prefixes

Tên card chỉ dùng các prefix sau, mỗi card một prefix loại (`[ASAP]` ghép thêm được):

| Prefix          | Template  | Nghĩa                                                           |
| --------------- | --------- | --------------------------------------------------------------- |
| `[Task]`        | Task      | Việc kỹ thuật/nội bộ                                            |
| `[Infra]`       | Task      | Việc hạ tầng (server, deploy, HA, compose…)                     |
| `[Req]`         | Task      | Yêu cầu từ bên ngoài mới xuất hiện hoặc sửa đổi                 |
| `[US]`          | US        | Hành vi người dùng thấy được                                    |
| `[[MILESTONE]]` | Milestone | Gom nhiều Task/US chung mục tiêu/deadline                       |
| `[ASAP]`        | —         | Gấp; đứng trước prefix loại                                     |

Prefix khác (`[Feature | customer-portal]`, `[Research]`…) không dùng: chuyển thông tin đó vào
`Purpose`.

## Rules

- **Tên card** theo bảng [Prefixes](#prefixes).
- **Description:** giữ nguyên heading tiếng Anh của template, điền nội dung tiếng Việt, bỏ hết chữ
  giữ chỗ `[…]` và phần `Ví dụ:`.
- **Checklist:** tên checklist giữ tiếng Anh (`Task creation`, `Story setup`, `Outcomes`,
  `Acceptance Criteria`, `Checklist`); mục bên trong viết tiếng Việt.
- **Checklist setup** (`Task creation`, `Story setup`, `Checklist` của Milestone): chép nguyên văn;
  mục agent đã tự làm (ví dụ điền description) thì tick luôn.
- **Checklist nội dung** (`Outcomes`, `Acceptance Criteria`): thay mục giữ chỗ bằng outcome/AC thật,
  khớp với description.
- **Label:** chép label của template (Milestone có `MANAGEMENT`, `Chiến lược`).
- **Thiếu thông tin** cho bất kỳ mục nào của template (ví dụ không biết doc/skill nào, không có
  Source of information): hỏi user trước khi tạo card, không điền "chưa rõ".
- **List đích:** `To Do` nếu user không chỉ định. Không tạo card trong `Draft` (chỉ chứa template).
- **Break task:** mặc định mỗi card độc lập. Chỉ tạo card cha khi các card cùng phục vụ một mục
  tiêu/deadline hoặc user yêu cầu; cha là Milestone thì link card con bằng checklist `Deliverables`
  trên card cha, mỗi item là URL một card con (Trello hiện tên card + list, tick item khi card con
  xong) và gắn attachment URL card cha lên từng card con (Butler tìm cha qua attachment). Không dùng
  comment. Việc connector không làm được (attachment, comment, xóa item) dùng
  `tools/scripts/trello_api.py`. Rule Butler, lệnh script và nơi để key: [automation.md](automation.md).
- **Sửa card cũ theo template:** connector không xoá được checklist; đổi tên checklist cũ thành
  checklist tương ứng của template thay vì tạo trùng.
