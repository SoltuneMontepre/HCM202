---
name: resolve-issue
description: Take open GitHub issues from the medilab repo through to stacked pull requests — pull the issues, implement each one, verify with a cloned dev database and non-admin users, raise Trello tasks for anything BA must confirm, and open one PR per issue as a GitHub stack. Use when the user says "resolve issue", "handle issues", "pull down the issues and implement", "do the next issues", or names issue numbers.
---

# Resolve issues

Luồng đã chạy cho #150–#153, xếp thành một stack PR. Mỗi bước trỏ tới skill hoặc doc làm phần việc
thật; skill này chỉ giữ thứ tự và các bẫy.

## 1. Lấy issue

```bash
gh issue list --state open --limit 50 --json number,title,labels
gh issue view <n> --json title,body,comments -q '.title, .body, (.comments[]|.body)'
```

- Nhiều issue mở thì hỏi user chọn (AskUserQuestion, multiSelect), đừng tự chọn.
- Đọc hết body và comment của issue đã chọn: Description, Acceptance criteria, References.
- Đọc doc trong `References` và mục `Known pitfalls` của addon trước khi sửa.
- Mơ hồ về luật nghiệp vụ thì đi bước 2, đừng đoán.

## 2. BA cần chốt thì tạo task Trello

Issue có dòng kiểu "BA to confirm", "chờ stakeholders", hoặc câu hỏi nghiệp vụ chưa có đáp án:

- Dùng skill `trello-task`, loại **Task**, đọc lại template `[Task] tên task` mỗi lần, list `To Do`.
- Description tiếng Việt: Purpose, Description (các câu hỏi cần chốt), Expected Outcome, Source of
  information (link issue, PR, doc).
- Comment `@hoanganh` và `@nnh53` ở card để tag. Username thật trên board: tra
  `trelloReadMember list_by_board` (`nnh53work` là Hoàng Nguyễn Nam, `lenguyenhoanganhk18hcm` là Hoàng
  Anh); xác nhận với user nếu không chắc.
- Connector không thêm được member vào card. Nói rõ phần "gán người phụ trách" chưa làm, đừng tick
  item đó.
- Phần code không phụ thuộc câu trả lời vẫn làm; ghi trong PR và card phần còn chờ.

## 3. Tách worktree riêng

Nhiều session Claude có thể dùng chung worktree chính: session khác đổi branch và commit lên branch
của bạn (đã xảy ra với #147–149). Trước khi sửa:

```bash
git worktree list && git status --short && git branch --show-current
git worktree add ../medilab-<slug> --detach <base>
```

- `<base>` là trunk của stack: `origin/main`, hoặc branch của PR chưa merge mà issue phụ thuộc.
- Sửa và commit trong worktree riêng. Không để thay đổi chưa commit của mình nằm trong worktree chung.
- Cuối việc, xóa bản sao thay đổi của mình ở worktree chung bằng `git checkout -- <file>` chỉ trên
  file của mình; file của session khác giữ nguyên.

## 4. Hiện thực

Theo skill `implement-feature` và [conventions](../../../src/modules/docs/conventions.md). Nhắc lại
các luật hay bị quên:

- Code trỏ về doc luật (`Luật nghiệp vụ: docs/business/<file>.md#<anchor>`); thêm section tương ứng vào
  doc nghiệp vụ trong cùng change. `task docs:check` kiểm anchor.
- Phân quyền chặn ở server, không chỉ `groups=`/`invisible=`.
- Copy bản ghi dưới quyền Sales có thể vỡ vì field many2one/many2many tới `hr.employee`; bỏ field đó
  khỏi dữ liệu copy thay vì `sudo()` (mất người tạo).
- Bump version manifest chỉ khi chưa ai bump trong stack.
- Viết file bằng script Python: chuỗi `\n` trong heredoc dễ thành xuống dòng thật; chạy
  `python -m py_compile` trên mọi file `.py` đã sửa.

## 5. Kiểm thật

Mục tiêu: chạy code của worktree, không dùng container dev chung (session khác có thể đang upgrade
hoặc dùng nó).

```bash
# nhân bản DB dev (nhỏ, vài chục MB)
docker exec medilab-postgres psql -U root -d postgres -c "create database medilab_stack"
docker exec medilab-postgres sh -c "pg_dump -U root medilab | psql -U root -q -d medilab_stack"
```

Chạy Odoo trên worktree với cùng image, mount `src/config`, `src/modules`, `src/templates` của
worktree, `--env-file src/.env.local` (thiếu thì lỗi "Bucket storage is not fully configured"), cổng
`18069`, rồi `-u <addon>` với `--stop-after-init`, sau đó chạy server.

- **Shell (`odoo shell -d medilab_stack --no-http --db_host=postgres --db_user=root --db_password=root`)**:
  thử từng guard bằng `env(user=<id>)` của người dùng thật. Superuser bỏ qua mọi check vai trò. Chọn bản
  ghi bằng `env(user=...).search(...)`, vì record rule làm bản ghi admin thấy mà Sales không thấy.
  Kết thúc bằng `env.cr.rollback()`.
- **User demo** mật khẩu `demo` (`nhanvienkinhdoanh`, `truongphongkinhdoanh`, `giaonhanmau`,
  `quanlychatluong`, `truonglab`, `kiemnghiemvien1`). DB clone có thể thiếu nhóm: gán bằng
  `user.write({"group_ids": [(4, env.ref(xmlid).id)]})` rồi `commit()`; seed thêm bản ghi ở trạng thái
  cần thử (ví dụ mẫu `cho_phe_duyet`).
- **UI**: dùng trình duyệt tích hợp ở `http://127.0.0.1:18069` (không dùng `localhost`: cookie dùng
  chung giữa các cổng nên Odoo :8069 đá session ra). Đăng nhập bằng JS đặt `login`/`password` rồi
  `form.submit()`. Đợi form render (hàm `setTimeout` dừng khi pane ẩn; chụp screenshot để đánh thức).
  Thử từng vai trò: field hiện/ẩn, nút hiện/ẩn, bấm nút thật, xem thông báo lỗi.
- Trang cổng khách hàng: `curl` `/my/orders/<id>?access_token=...` rồi tìm đoạn HTML mong đợi.
- Dọn xong: `docker rm -f medilab-stack-odoo`, `drop database medilab_stack`.

Báo đúng những gì đã chạy và chưa chạy (lint, `task format-check`, test module, đường tích cực,
vai trò nào).

## 6. Commit: một commit một issue

- Conventional Commits, scope là addon, kết bằng số issue: `feat(tpc_thu_nghiem): ... (#150)`.
- **Không** thêm `Co-Authored-By:` hay dòng "Generated with" vào commit và mô tả PR
  ([repo-convention](../../../docs/repo-convention.md#commit)); luật repo thắng mặc định của harness.
- Thay đổi dồn trong một worktree mà cần tách theo issue thì chọn hunk theo từ khoá:
  `git diff -U0` → lọc hunk → `git apply --cached --unidiff-zero -`, sinh lại diff sau mỗi commit vì số
  dòng đổi. File lẫn hai issue trong một hunk thì dựng bản một-issue trước rồi `git add`.
- File trong index là LF, worktree Windows là CRLF nên `git status` hiện `M` giả. `git checkout -- .`
  trước `rebase`/`filter-branch`.
- Sửa message cả stack: `git filter-branch -f --msg-filter '...' -- ^<base> <branch>...` (rebase
  `--update-refs` kẹt vì CRLF giả), rồi `git push --force-with-lease`.

## 7. Stack PR

```bash
gh extension install github/gh-stack        # một lần
gh stack init --base <trunk> <branch1> <branch2> ...   # dưới lên trên
gh stack submit --auto                      # đẩy branch, tạo PR, tạo stack
gh stack push                               # đẩy lại sau khi thêm commit
```

- Đặt tên branch `feat/<issue>-<slug>`, đặt branch các issue phụ thuộc nhau ở dưới.
- Sau `submit`, sửa mô tả từng PR: một câu nói PR làm gì, `Closes #<n>`, một câu nói đây là stack.
  `gh pr edit <n> --body "..."`.
- Sau khi nhận xét, đẩy commit sửa lên branch đúng tầng rồi `gh stack push`.

## 8. Báo lại

Liệt kê PR, việc Trello đã tạo, phần chưa kiểm, và mọi việc chạm vào worktree hay branch của người
khác. Gọn, không kể lại từng lệnh.
