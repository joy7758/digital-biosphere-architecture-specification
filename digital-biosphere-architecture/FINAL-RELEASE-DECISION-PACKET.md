---
document_id: DBA-FINAL-RELEASE-DECISION-PACKET-0.1
title: Trusted Multi-Agent Infrastructure Developer Preview v0.1 Final Release Decision Packet
title_zh: 可信多智能体基础设施开发者预览版 v0.1 最终发布决策包
status: ready-for-human-decisions-not-release-authorized
release_authorized: false
cloud_deployment_authorized: false
license_selected: false
last_reviewed: 2026-07-21
---

# Final Release Decision Packet v0.1（最终发布决策包 v0.1）

## 1. Current Proven State（当前已证明状态）

| Surface（表面） | Current evidence（当前证据） | 状态 |
|---|---|---|
| DBA GitHub | `origin/main@738a01d`；root README、root AGENTS、307 links | `REMOTE_CLEAN_CLONE_PASS` |
| DBOS GitHub | `origin/main@b4e3cbe`；fresh install、331 tests、34 validators、两个 Demo | `REMOTE_CLEAN_CLONE_PASS_PRIVATE_REPO` |
| SAEE GitHub public layer | `origin/main@e503c22`；public smoke/demo 通过 | `PUBLIC_LAYER_PASS_ADAPTER_MISSING` |
| Cross-project Clean Clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `FAIL_REQUIRED_SAEE_ADAPTER_MISSING` |
| Baidu mirror | `https://redcrag.cn/` HTTP/2 200；证书有效至 2026-10-09 | `EXISTING_SAEE_SITE_HEALTHY_NO_TMAI_PATH` |
| External trial | 参与者 0，`DQ-010` 未授权 | `NOT_STARTED` |
| GitHub Release | 没有本版本 tag / release | `NOT_CREATED` |

## 2. DQ-011 — SAEE Adapter Publication Boundary（SAEE 适配器公开边界）

### Dependency audit（依赖审计）

当前内部、只读 Adapter 的最小 Python 依赖闭包为：

1. `scripts/saee_evaluate_dbos_preview.py`；
2. `saee_backend/services/dbos_developer_preview_adapter.py`；
3. `saee_backend/services/baidu_agent_readiness_service.py`；
4. `saee_backend/services/reliability_framework/assessment_adapter.py`；
5. `saee_backend/services/reliability_framework/failure_classifier.py`；
6. `saee_backend/services/evidence_adequacy.py`；
7. `saee_backend/services/resource_resolution_receipt.py`。

它还需要 5 个 Qianfan request/response schemas、Evidence Adequacy schema、4 个
claim profiles 和 Resource Resolution Receipt schema。SAEE public `main` 的
`PUBLICATION_BOUNDARY.md` 当前排除 runtime implementation 和 scoring internals；
因此这些文件不能未经显式边界修订直接进入公开主线。

### Options（选项）

| Option | 说明 | 结论 |
|---|---|---|
| `A_PUBLIC_SAFE_EXTRACTION` | 以有来源、hash-bound（哈希绑定）的 public abstraction package（公共抽象包）迁移上述最小闭包；保留负向测试与非声明，不携带 kernel/selection/mutation/lineage/private backend | `CONDITIONALLY_RECOMMENDED` |
| `B_HOSTED_EVALUATION_API` | 在百度部署远程 SAEE service（服务），开发者只调用接口 | `NOT_RECOMMENDED_V0_1`：会新增 Runtime/API/Auth/运营边界 |
| `C_REMOVE_EXECUTABLE_SAEE_ADAPTER` | v0.1 只发布 SAEE 文档和 toy demo | `NOT_RECOMMENDED`：无法满足已冻结跨项目试用目标 |

推荐 `A_PUBLIC_SAFE_EXTRACTION`，但必须先由 Human Architecture Authority（人工架构权力）
明确批准 public boundary amendment（公开边界修订）和 exact manifest（精确清单）。
迁移必须是同一 evaluator 的可验证投影，不得手工重写为第二套算法。

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
SAEE_PUBLICATION_BOUNDARY_AMENDMENT_REQUIRED=true
PRIVATE_CORE_PUBLICATION_AUTHORIZED=false
PUBLIC_ADAPTER_MIGRATION_AUTHORIZED=false
```

## 3. DQ-012 — Public License（公开许可证）

GitHub 当前识别结果：DBA、DBOS、SAEE 均无根 `LICENSE`。正式开发者预览如果没有
许可证，外部开发者没有明确复制、修改或分发权利。

推荐统一使用 `Apache-2.0`：它适合基础设施与 SDK，包含明确 patent grant（专利授权）
和贡献边界。选择许可证是法律／Owner 决策，不能由 Codex 自动作出。

```text
RECOMMENDED_LICENSE=Apache-2.0
LICENSE_SELECTED=false
LICENSE_PUBLICATION_AUTHORIZED=false
```

## 4. DQ-013 — Baidu Deployment Target（百度部署目标）

已验证的正式域名是 `https://redcrag.cn/`，不是 `deep-evo.org`。现有 SAEE 页面与
历史 release directories（发布目录）必须保留。

推荐采用非破坏路径：

```text
release_directory=/srv/saee/releases/tmai-developer-preview-v0.1-<source-hash>
public_path=https://redcrag.cn/trusted-multi-agent-infrastructure/
replace_existing_saee=false
cloud_clear_required=false
atomic_rollback_required=true
```

该方案在独立目录部署，不清空 `/srv/saee/public/saee`，不修改历史 Evidence，且保留
原子回退。仍需 Human Deployment Authorization（人工部署授权）后才能修改 Nginx 或上传。

## 5. Required Human Decision Record（所需人工决定记录）

```text
decided_by_ref=
dq_011_saee_public_safe_extraction=approved|rejected
dq_012_license=Apache-2.0|other|withheld
dq_013_baidu_isolated_path=approved|rejected
decision_timestamp=
```

三个决定完成后仍需：实现/审计 SAEE public-safe extraction、重跑 Clean Clone、处理
`DQ-010`、完成 3–5 人试用，再由 `DQ-009` 决定 tag、GitHub Release 和百度正式部署。

本决策包不是 Decision、Authorization、Release 或 Deployment。
