---
document_id: DBA-DECISION-QUEUE-0.1
title: Digital Biosphere Program Decision Queue v0.1
title_zh: 数字生物圈项目群决策队列 v0.1
status: active-decision-register
decision_records_created: false
authority_assignments_created: false
last_reviewed: 2026-07-21
---

# Digital Biosphere Program Decision Queue v0.1（数字生物圈项目群决策队列 v0.1）

## 1. Queue Rule（队列规则）

本队列暴露需要人工决定的项目群事项。进入队列不等于批准；Priority（优先级）不等于 Authorization（授权）；关闭事项必须保留结果、理由、范围和 `decided_by_ref`。

合法状态：`OPEN`、`READY_FOR_REVIEW`、`BLOCKED_INPUT`、`DECIDED`、`DEFERRED`、`REJECTED`、`SUPERSEDED`。

## 2. Open Decisions（开放决策）

| decision_id | Priority | 决策问题 | 当前状态 | 所需输入 | 决策影响 | 禁止自动推断 |
|---|---|---|---|---|---|---|
| `DQ-001` | `P0` | 谁承担 Human Program Owner（人工项目群负责人）或最终项目群决策来源？ | `READY_FOR_REVIEW` | 角色范围、任期、替代/复核机制、`decided_by_ref` | 路线图优先级、项目准入、跨项目 gate 的人工关闭 | 仓库 Owner、Architecture Maintainer 或 Codex 自动成为 Program Owner |
| `DQ-002` | `P0` | DBA 是否应成为独立 Git root（Git 根目录），而不是父目录仓库中的子目录？ | `READY_FOR_REVIEW` | 当前本地/远端拓扑、历史保留方案、迁移风险 | 仓库边界、GitHub 根展示、后续自动化和发布 | 允许重写历史、删除父仓库或强制推送 |
| `DQ-003` | `P0` | DBOS、SAEE、Research Agent Pilot 各自哪个文件/manifest 是 canonical status source？ | `OPEN` | 各 Domain Owner 的来源确认、刷新频率、冲突规则 | 驾驶舱状态可信度和后续只读同步 | README、测试数量或 Git dirty 自动等于项目状态 |
| `DQ-004` | `P1` | 第一个跨项目里程碑是否选择 DBOS ↔ SAEE data contract conformance？ | `OPEN` | 字段映射、版本、现有实现审计、正负用例范围 | `M3` 的正式启动与 Owner 分派 | 已存在接口实现或允许直接调用 SAEE |
| `DQ-005` | `P1` | Research Agent Pilot 何时可以进入 Prototype Authorization Review（原型授权审查）？ | `BLOCKED_INPUT` | Human Review、approved sources、independent reviewer decision、protocol freeze | `M5` 是否进入人工授权 | `NOT_READY` 自动升级，或由 DBA 创建 Agent/Runtime |
| `DQ-006` | `P2` | POP、ARO、Agent Evidence、Token Governor、ACP 哪些进入正式 Portfolio？ | `OPEN` | 每个项目的目的、Owner、canonical source、重复能力和接口边界 | 项目组合与依赖范围 | 本地发现、历史关联或相邻角色等于正式准入 |
| `DQ-007` | `P2` | 驾驶舱状态采用人工周期刷新，还是未来建立只读 adapter（适配器）？ | `OPEN` | source contracts、安全边界、维护成本、staleness 需求 | 状态同步机制 | 允许 DBA 写入子仓库或自动改变项目状态 |
| `DQ-008` | `P0` | 当前 Program Governance Cockpit 与既有 Digital Biosphere public meaning layer 的 canonical relationship（规范关系）是什么？ | `READY_FOR_REVIEW` | 两个仓库的使命、受众、当前 URL、历史、重叠文件和迁移/引用方案 | 单一前门、规范优先级和避免双重 DBA 权威 | 当前驾驶舱自动覆盖、删除或合并既有 public meaning layer |
| `DQ-009` | `P0` | `Trusted Multi-Agent Infrastructure Developer Preview v0.1` 何时允许发布？ | `BLOCKED_INPUT` | 本地测试、Trial Plan、Guide 与已知限制已齐；仍缺冻结 source commits、clean-clone 复验、3–5 人 Trial Result 和 `released_by_ref` | `DP-R` 是否进入 `RELEASED` | ADR-017、测试通过、本地 Demo 或 Trial PASS 自动等于发布授权 |
| `DQ-010` | `P0` | 是否授权执行 External Developer Trial v0.1 并联系 3–5 名外部 Agent Developer？ | `BLOCKED_INPUT` | exact `trial_package_id`、DBA/DBOS/SAEE source commits、clean-clone result、trial coordinator、参与者画像、隐私说明和停止规则 | `DP-5B` 是否可进入 `AUTHORIZED/IN_PROGRESS`，并允许受限外部联系与反馈收集 | Trial Plan 或 ADR-018 自动授权外部联系、数据收集、发布或客户验证 |
| `DQ-011` | `P0` | SAEE DBOS Developer Preview Adapter 应如何安全提供给外部开发者？ | `READY_FOR_REVIEW` | public/private history 分离事实、Adapter 依赖、private-core 边界、避免重复 evaluator 的方案比较 | `DP-4` 是否能形成可干净检出的 SAEE 评价入口 | 将内部工程历史推入 public `main`、复制 evaluator、把 toy demo 当 Adapter 或通过无关历史强制合并 |
| `DQ-012` | `P0` | Developer Preview 的 DBA、DBOS、SAEE 公开表面采用什么许可证？ | `READY_FOR_REVIEW` | 当前无根 LICENSE、目标复用方式、专利与贡献边界；推荐 `Apache-2.0` | 外部复制、修改、分发与 GitHub Release 的法律边界 | Open Infrastructure 自动等于 Apache/MIT，或 public repo 自动授予复用权 |
| `DQ-013` | `P0` | 百度正式发布是否采用 `redcrag.cn/trusted-multi-agent-infrastructure/` 独立路径？ | `SUPERSEDED` | Human Owner 明确旧应用资产已过期并授权清理；见 `ADR-019` | 网站候选改用 `https://redcrag.cn/` 根入口；不授权 Developer Preview Release | 网站上线或健康检查自动等于正式发布 |
| `DQ-014` | `P0` | DBOS 何时从 private repository 转为 public repository？ | `READY_FOR_REVIEW` | clean clone、许可证、secret/private-material audit、外部试用方式与 rollback | 匿名开发者能否获取 SDK、Quick Start 和 Demo | authenticated clone 自动等于 public availability，或 trial collaborator access 自动等于公开发布 |

## 3. Closed Program Decision（已关闭项目群决策）

| decision_reference | 结果 | 来源 | 效力 |
|---|---|---|---|
| `ADR-016` | `ACCEPTED`：DBA 升级为 Program Governance + Architecture Specification cockpit | 2026-07-21 用户明确目标 | 允许更新 DBA 文档和治理入口；不授权修改 DBOS、SAEE、Pilot、Runtime 或外部状态 |
| `ADR-017` | `ACCEPTED`：进入 Trusted Multi-Agent Infrastructure Developer Preview v0.1 阶段 | 2026-07-21 用户明确目标 | 允许按 DBA / DBOS / Demo / SAEE 责任域推进受限实现；不授权发布、生产 Runtime、自动 Permission 或 Evidence 改写 |
| `ADR-018` | `ACCEPTED`：在发布前建立 3–5 人 External Developer Trial Gate | 2026-07-21 用户明确目标 | 允许建立试用计划、测量与 gate；不授权招募、外部联系、试用执行、客户验证或发布 |
| `ADR-019` | `ACCEPTED_AND_EXECUTED`：清理过期云端应用资产并在 `redcrag.cn` 根入口部署双语 TMAI 网站候选 | 2026-07-21 用户明确清理与网站要求 | 只授权公开网站候选及其 GitHub prerelease；不授权 Developer Preview Release、DBOS 公开、SAEE 边界变更或外部试用 |

## 4. Decision Closure Contract（决策关闭契约）

任何 `DECIDED` 项必须至少记录：

```text
decision_id=
decision_result=accepted|rejected|deferred|superseded
decided_by_ref=
decided_at=
accepted_scope=
rejected_scope=
affected_projects=
required_followups=
execution_authorized=true|false
release_authorized=true|false
```

如果 `decided_by_ref` 缺失，状态必须保持 `OPEN` 或 `BLOCKED_INPUT`。

```text
DECISION_QUEUE_ACTIVE=true
OPEN_DECISIONS=13
QUEUE_CREATES_AUTHORITY=false
QUEUE_CREATES_PERMISSION=false
QUEUE_EXECUTES_DECISIONS=false
```
