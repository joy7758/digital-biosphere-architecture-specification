---
document_id: DBA-FINAL-RELEASE-DECISION-PACKET-0.1
title: Trusted Multi-Agent Infrastructure Developer Preview v0.1 Final Release Decision Packet
title_zh: 可信多智能体基础设施开发者预览版 v0.1 最终发布决策包
status: ready-for-human-decisions-not-release-authorized
release_authorized: false
developer_preview_cloud_release_authorized: false
website_candidate_deployment_authorized: true
website_candidate_deployed: true
website_candidate_github_prerelease_published: true
license_selected: false
last_reviewed: 2026-07-21
---

# Final Release Decision Packet v0.1（最终发布决策包 v0.1）

## 1. Current Proven State（当前已证明状态）

| Surface（表面） | Current evidence（当前证据） | 状态 |
|---|---|---|
| DBA GitHub | `origin/main@6793320`；公开网站源码、部署报告与治理入口 | `REMOTE_WEBSITE_CANDIDATE_BASELINE_PASS` |
| DBOS GitHub | `origin/main@b4e3cbe`；fresh install、331 tests、34 validators、两个 Demo | `REMOTE_CLEAN_CLONE_PASS_PRIVATE_REPO` |
| SAEE GitHub public layer | `origin/main@e503c22`；public smoke/demo 通过 | `PUBLIC_LAYER_PASS_ADAPTER_MISSING` |
| Cross-project Clean Clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `FAIL_REQUIRED_SAEE_ADAPTER_MISSING` |
| Baidu website | `https://redcrag.cn/` 中英文候选网站；健康、安全头和回滚通过 | `CANDIDATE_DEPLOYED_NOT_RELEASED` |
| External trial | 参与者 0，`DQ-010` 未授权 | `NOT_STARTED` |
| GitHub website artifact | `v0.1-public-website-candidate`；`prerelease=true` | `WEBSITE_CANDIDATE_PRERELEASED` |
| DBOS repository visibility | GitHub API 返回 `PRIVATE` | `PUBLIC_ACCESS_NOT_ESTABLISHED` |

## 2. DQ-011 — SAEE Adapter Publication Boundary（SAEE 适配器公开边界）

精确技术清单和隔离复验见
[`SAEE-PUBLIC-SAFE-EXTRACTION-REVIEW.md`](SAEE-PUBLIC-SAFE-EXTRACTION-REVIEW.md)。
现有候选在隔离目录中 8/8 tests 通过并能消费冻结 DBOS 演示输出，但最小闭包为
19 个文件，且 8 个 Python 实现／测试路径全部不在 SAEE public `main`。这使公开
边界修订成为真实 Decision，而不是缺少一次复制命令。

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

Human Owner 随后明确旧 SAEE 与 Agent Evidence Receipt 应用资产已经过期，授权在
保留系统、证书和安全配置的前提下完整清理，并要求建立中英文新网站。原独立路径问题
因此由 `ADR-019` 标记为 `SUPERSEDED`。

当前已执行：

```text
release_directory=/srv/tmai/releases/<source-revision>
public_path=https://redcrag.cn/
website_candidate_deployed=true
atomic_rollback_required=true
atomic_rollback_validated=true
developer_preview_released=false
```

网站候选与相同工件的 GitHub prerelease 已完成。该动作不授权正式 Developer Preview、
DBOS 公开、SAEE Adapter 迁移、许可证选择或外部试用。

## 5. DQ-014 — DBOS Repository Visibility（DBOS 仓库可见性）

只读预检见
[`DBOS-PUBLIC-VISIBILITY-PREFLIGHT.md`](DBOS-PUBLIC-VISIBILITY-PREFLIGHT.md)。
当前 457 个 tracked files（已跟踪文件）中未发现高置信度密钥模式、敏感文件名或
超过 5 MiB 的历史 blob；但 GitHub Secret Scanning 与 Dependabot Alerts 均禁用，
根许可证缺失，完整历史安全审查仍未完成。

DBOS `b4e3cbe` 的 clean clone 使用当前 GitHub 凭据完成；这不是 anonymous clone
（匿名检出）证据。仓库当前为 `PRIVATE`，因此 3–5 名陌生开发者和正式公开用户默认
无法获取 SDK、Quick Start 或 Demo。

推荐在许可证、SAEE public-safe extraction、最终 clean clone 和外部试用修正完成后，
由 Owner 将 DBOS 切换为 `PUBLIC`；切换前必须再次扫描 secret、private material 和
历史 Evidence 边界。试用阶段可以用受控 collaborator access（协作者访问），但不能
据此声称 public release（公开发布）。

```text
DBOS_REPOSITORY_VISIBILITY=PRIVATE
ANONYMOUS_CLONE_VALIDATED=false
DBOS_PUBLICATION_AUTHORIZED=false
```

## 6. Required Human Decision Record（所需人工决定记录）

```text
decided_by_ref=
dq_011_saee_public_safe_extraction=approved|rejected
dq_012_license=Apache-2.0|other|withheld
dq_013_baidu_isolated_path=superseded_by_ADR-019
dq_014_dbos_visibility=public_after_trial|private_collaborator_trial|rejected
decision_timestamp=
```

其余决定完成后仍需：实现/审计 SAEE public-safe extraction、重跑 Clean Clone、处理
`DQ-010`、完成 3–5 人试用，再由 `DQ-009` 决定 tag、GitHub Release 和百度正式部署。

本决策包不是 Decision、Authorization、Release 或 Deployment。
