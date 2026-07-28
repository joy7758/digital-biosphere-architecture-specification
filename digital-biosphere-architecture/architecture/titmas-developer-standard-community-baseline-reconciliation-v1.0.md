---
document_id: DBA-TITMAS-DEVELOPER-STANDARD-COMMUNITY-BASELINE-1.0
title: TITMAS Developer Standards Community Baseline Reconciliation v1.0
title_zh: TITMAS 开发者标准社区基线核对 v1.0
status: reconciled-development-baseline
maturity: Development
owner_ref: zhangbin
decision_reference: USER_GOAL_2026-07-28
observed_at: 2026-07-28
source_branch: codex/commercial-standard-next-human-decision-packet
source_commit: 8d79c3a7e50d0477e1dd7da855e82b9e659a550b
public_launch_authorized: false
community_established: false
---

# TITMAS Developer Standards Community Baseline Reconciliation v1.0

## 1. Reconciliation rule

本记录只陈述在 `2026-07-28` 直接读取到的工作区、Git 和文件事实。历史聊天、模型输出、
路线图和文件数量均不能替代实现证据。

状态词：

- `IMPLEMENTED`：存在可运行代码或机器验证；
- `DOCUMENTED_CANDIDATE`：有文档或 Schema 候选但无已证明实现；
- `PROPOSED`：只有建议或规划；
- `AUTHORIZED_NOT_IMPLEMENTED`：有明确授权但尚无实现；
- `REFERENCE_ONLY`：仅作为外部或相邻资料引用；
- `UNKNOWN`：证据不足；
- `CONFLICT`：两个来源对同一状态给出不兼容陈述。

## 2. Repository baseline

| Surface | Observed state | Classification | Evidence / limitation |
|---|---|---|---|
| TITMAS community direction | 已由 `ADR-029` 采纳 | `DOCUMENTED_CANDIDATE` | Contributor Entry 已准备；公共贡献、社区、Maintainer 均未建立 |
| Canonical TITMAS layout | 不存在统一 `TITMAS/` 开发者目录 | `PROPOSED` | 社区、规范、商业和实验材料分散在根目录与 `architecture/` |
| Canonical Charter | 远端分支只有 v0.1；本地有未跟踪 v0.2 候选 | `CONFLICT` | v0.2 把免疫身份置于互操作基础设施之上，与本 Goal 冲突；不导入为事实 |
| Community governance | 有 Contributor Guide、角色、成熟度和模板候选 | `DOCUMENTED_CANDIDATE` | 没有真实 Maintainer、Reviewer、成员或公共贡献授权 |
| Code of Conduct | 只有 candidate | `DOCUMENTED_CANDIDATE` | `TITMAS_CODE_OF_CONDUCT_ADOPTED=false` |
| Security disclosure | 没有已激活的安全接收路径 | `UNKNOWN` | 不得公开提交漏洞详情；公共接收仍需 Human Gate |
| Specification registry | 没有唯一机器注册表 | `PROPOSED` | 现有编号和成熟度散落在多个文件 |
| Conformance harness | 没有 TITMAS 社区级一键工具 | `PROPOSED` | 商业评估工具不能替代开发者规范符合性工具 |
| Reference implementation | 无最小 TITMAS 互操作参考实现 | `PROPOSED` | DBOS wheel 或商业评估不能写成 TITMAS 标准实现 |
| Public launch | 未授权 | `DOCUMENTED_CANDIDATE` | `PUBLIC_LAUNCH_AUTHORIZED=false` |

## 3. Adjacent repository facts

| Repository / surface | Observed ref | Classification | Bounded current role |
|---|---|---|---|
| `agent-health` | `main@6c7937f7...`, dirty worktree | `IMPLEMENTED` | 本地单仓库静态健康探针、趋势、报告和 AEO 自完整性；不是自动修复器 |
| `titmas-health` | `main@55181024...`, clean | `DOCUMENTED_CANDIDATE` | README、health-report Schema 和示例；没有运行引擎 |
| Agent Evidence | `revision/softwarex-v2-grounding-fix@1b692de...`, dirty | `IMPLEMENTED` with bounded public surface | 本地 Evidence 记录、导出、验证和适配；不是 canonical Truth |
| DBOS | `main@0caa2c45...`, dirty | `IMPLEMENTED` with source drift caveat | 存在治理和记录基础设施；不由 DBA 复制事实 |
| SAEE | `feat/canonical-capability-inventory-routing-v1@697ae208...`, dirty | `IMPLEMENTED` with branch caveat | 只读评价和建议；不是执行器或 Permission Authority |
| ARO | `audit-scope-alignment-v1@74a7f584...`, dirty | `REFERENCE_ONLY` | 有界 receipt verification；不是生产 audit control plane |
| AVH | DBA architecture assessment | `DOCUMENTED_CANDIDATE` | validation-execution Profile 候选；未采纳、未实现 |
| EEOAP / VEAP | Agent Evidence public profile + DBA VEAP draft | `DOCUMENTED_CANDIDATE` and bounded implementation surfaces | 必须复用对象所有权；不得创建第二套 Evidence |

## 4. Conflict findings

1. TITMAS 在部分材料中被写成商业评估入口、审批表面或数字免疫中心；这与开放互操作
   基础设施核心定位冲突。
2. 数字免疫模型应降为 explanatory layer，不得覆盖开发者接口。
3. `agent-health` 当前代码不是自动修复器。
4. `Health Check Alpha` 精确搜索只命中 OpenTelemetry Collector `health_check`
   extension 的 Alpha maturity；没有发现同名 TITMAS 实现或分支。
5. 社区、规范、商业和 Foundation Freeze 文件存在大量相邻材料，但没有唯一入口、唯一
   注册表或一键符合性工具。
6. 当前 README 主要引导 Commercial Evaluation Pack，不是从零开始的规范社区入口。
7. CS-G0、CS-G1 和 VEAP review package 仍未通过；本 Goal 不修改其范围或状态。

## 5. Pre-development agent recommendation gate

`qwen3.7-max` advisory review 结果：

```text
AGENT_RECOMMENDATION=NOT_RECOMMENDED
MODEL=qwen3.7-max
AUTHORITY_EFFECT=none
```

主要原因：缺失远端 canonical Charter、Conformance Harness、最小参考实现、清晰维护入口，
且治理材料多于可运行开发者表面。

本 Goal 分解：

- 修复：唯一入口、Charter、注册表、Harness、Reference 和模板；
- 保留阻塞：真实 Maintainer、Reviewer、公共贡献授权、社区成立、外部采用；
- 停止条件：需要创建新 Truth、Authority、Runtime、第二套 Evidence 或修改冻结 VEAP；
- 后续人工决定：公共贡献、Maintainer、Reviewer、公告、Release 和标签。

```text
BASELINE_RECONCILIATION_COMPLETE=true
MAJOR_CONFLICT_FOUND=true
MAJOR_CONFLICT_BOUNDED=true
CS_G0_PASS=false
CS_G1_PASS=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
```
