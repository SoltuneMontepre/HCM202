---
name: deployment
description: Ship MediLab or work on its delivery pipeline — GitHub Actions, Docker image builds, GitOps via FluxCD reconciling this repo's own infra/clusters/ tree, Terraform in infra/, Doppler secrets, Cloudflare DNS, rollback. Use when the user says deploy, release, ship, pipeline, CI, CD, GitOps, Flux, Terraform, infra, secrets, or rollback. Index skill — loads the reference docs the task actually needs.
---

# Deployment

**Index skill.** Dẫn tới đúng doc task cần; đừng nạp trước mọi thứ.

Push lên `main` → Actions build và push image → commit tag vào cây `infra/clusters/` của chính repo
này → FluxCD reconcile lên cluster. Không bước nào ở đây nói chuyện trực tiếp với cluster, nên một
deploy bị kẹt luôn là câu hỏi *chặng nào* đã dừng. Ngoại lệ duy nhất là `cd.reset.yml` (reset tay môi
trường lims, dùng `kubectl` qua environment `lims-reset`).

| Việc                                          | Đọc                                                              |
| --------------------------------------------- | ------------------------------------------------------------------ |
| Build, workflow, hoặc pin action                | [cicd.md](../../../docs/infrastructure/cicd.md)          |
| Thay đổi tới cluster bằng cách nào; deploy bị kẹt | [gitops.md](../../../docs/infrastructure/gitops.md)      |
| Một namespace không đọc được secret của nó             | [gitops.md](../../../docs/infrastructure/gitops.md#how-dopplersecret-is-wired-and-why-theres-only-one-token) |
| DNS, Terraform, HCP state                      | [terraform.md](../../../docs/infrastructure/terraform.md) |
| Credential nằm ở đâu; xoay vòng             | [secrets.md](../../../docs/infrastructure/secrets.md)    |
| `odoo.conf` local / kết nối DB bất thường    | [local-stack.md](../../../docs/infrastructure/local-stack.md#do-not-put-db-credentials-in-odooconf) |
| Rollback                                       | [runbooks/rollback.md](../../../docs/infrastructure/runbooks/rollback.md) |
| Bootstrap cluster từ đầu         | [runbooks/cluster-bootstrap.md](../../../docs/infrastructure/runbooks/cluster-bootstrap.md) |
| Đổi **giá trị** của secret                    | Doppler — không phải repo này, không phải Terraform state                      |
| Đổi thứ chạy trên cluster                | `infra/clusters/` trong repo này, Flux reconcile                |
| Vì sao pipeline có hình dạng này            | Một spec dưới [docs/superpowers/specs/](../../../docs/superpowers/specs/) |

## Shipping

1. Kiểm local — `task restart`/`upgrade`, chạy thử, kiểm `docker compose logs -f odoo`
   sạch lỗi ([workflow.md](../../../src/modules/docs/workflow.md)).
2. Kiểm CD sẽ chạy: `cd.core.yml` cần push lên `main` đụng `src/**` hoặc chính workflow.
   Mọi trường hợp khác cần `workflow_dispatch`.
3. **Thay đổi schema và module không đi theo image.** Cài hoặc upgrade module trên cluster là một
   bước riêng — nói rõ điều đó thay vì để việc deploy ngầm hiểu là đã làm.
4. Push, theo dõi run, rồi xác nhận tag đã đổi trong `infra/clusters/environments/lims/apps/medilab/`
   *và* Flux đã reconcile. Một run Actions xanh chỉ chứng minh hai chặng đầu.

## Rules

- Không bao giờ commit secret. Repo này giữ tham chiếu; Doppler giữ giá trị.
- `task infra:apply` và push lên `main` có tác động ra ngoài — xác nhận trước, trừ khi đã được bảo
  cứ làm.
- Plan trước khi apply, cho xem plan, lấy xác nhận tường minh. `terraform apply` đụng DNS và secret
  đang chạy thật.
- Đừng sửa tay state của cluster để lách pipeline — Flux sẽ hoàn tác.
- Báo tình trạng theo những gì bạn quan sát được ở từng chặng, không theo việc bạn đã push.
