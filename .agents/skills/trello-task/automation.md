# Trello automation

Cách board medilab giữ trạng thái card con và epic khớp nhau, và phần việc connector MCP không làm được.

## Parent–child link

- Epic (`[[MILESTONE]]`) có checklist `Deliverables`, mỗi item là URL ngắn của một card con
  (`https://trello.com/c/<short>`). Trello hiện item thành tên card kèm badge list.
- Mỗi card con có **attachment** trỏ về URL epic cha. Butler tìm card cha qua attachment này; thiếu
  attachment thì rule 1 và 2 không chạy.
- Không link bằng comment: khó đọc và không có tiến độ.
- Trello **không** tự đồng bộ item link card với trạng thái card con. Đã thử cả hai chiều ngày
  18-09-2026 (đổi `dueComplete` của card con, tick item bên epic): không bên nào kéo theo bên kia.

## Butler rules

Butler không có API, connector cũng không tạo rule được: người dùng tạo tay ở
`Automation → Rules → Create a Rule`. Rule 1 và 2 phải bật **Advanced** để dán nguyên văn.

| # | Rule (nguyên văn) | Tác dụng |
| - | ----------------- | -------- |
| 1 | `when a card is moved into list "Done", find the first card linked in the attachments, and check item "{triggercardlink}{*}" in checklist "Deliverables"` | Card con vào Done → tick item bên epic |
| 2 | `when a card is moved out of list "Done", find the first card linked in the attachments, and uncheck item "{triggercardlink}{*}" in checklist "Deliverables"` | Card con ra khỏi Done → bỏ tick item bên epic |
| 3 | `when a card is moved out of list "Done", mark the card as incomplete` | Ra khỏi Done → bỏ nút complete trên card con |
| 4 | `when the card is marked as complete in a card not in list "Done", mark the card as incomplete` | Chặn đánh complete khi card chưa ở Done |
| 5 | `when the card is marked as incomplete in a card in list "Done", mark the card as complete` | Chặn bỏ complete khi card đang ở Done |
| 6 | `when a card is added to list "Done", mark the card as complete` | Vào Done → tự đánh complete |

- Dùng `{triggercardlink}{*}`, không dùng `{triggercardname}`: item là link nên Trello lưu nó dưới dạng
  link, không phải tên card.
- Action đặt **sau** bước `find` chạy trên card epic, không phải card con. Vì vậy việc đánh complete
  cho card con nằm ở rule riêng (3 và 6), không gộp vào rule 1 và 2.
- Filter `in list` / `not in list` của rule 4 và 5 chọn bằng icon phễu ở bước **Select trigger**, không có
  ở bước action. Hai rule dùng filter ngược nhau nên không tạo vòng lặp.
- Butler chỉ chạy khi có sự kiện. Card đã lệch từ trước thì chạy `sync-deliverables` một lần.

Đã test ngày 18-09-2026 trên card `OO5HF08H`: vào Done → item tick và card complete (rule 1, 6); về To Do →
item bỏ tick và card incomplete (rule 2, 3); đánh complete khi ở To Do → tự bỏ sau khoảng 1 giây (rule 4).
Rule 5 chưa test vì connector không có lệnh bỏ complete.

## REST helper

`tools/scripts/trello_api.py` làm phần connector thiếu: `comment`, `delete-comment`, `delete-item`,
`tick-item`, `add-checklist`, `attach-url`, `sync-deliverables`.

```bash
doppler run --project medilab --config tf -- python tools/scripts/trello_api.py sync-deliverables mk5Pnyu3 Done
```

- `sync-deliverables` đồng bộ hai chiều mọi checklist `Deliverables` trên board theo list của card con;
  chạy lại bao nhiêu lần cũng được. Dùng để dọn lệch hoặc thay Butler khi rule hỏng.
- Khi tạo epic mới: `add-checklist <epic> "Deliverables" <url con>...` rồi `attach-url <card con> <url epic>`
  cho từng card con.

## Credentials

- `TRELLO_API_KEY` và `TRELLO_TOKEN` nằm ở Doppler project `medilab`, config `tf`. Config `tf` là nơi người
  nhập secret gốc; các config `production_*` được Doppler operator đồng bộ vào cluster nên không đặt ở đó.
- Token phải có scope `read,write`. Token trong `.env` của repo skyhook chỉ có quyền đọc: mọi lệnh ghi trả
  `401 unauthorized card permission requested`.
- Cấp token mới: `https://trello.com/1/authorize?expiration=never&scope=read,write&response_type=token&name=medilab-scripts&key=<TRELLO_API_KEY>`,
  rồi `doppler secrets set TRELLO_TOKEN=<token> --project medilab --config tf`.
