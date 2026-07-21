---
document_id: DBA-DECISION-QUEUE-0.1
title: Digital Biosphere Program Decision Queue v0.1
title_zh: 数字生物圈项目群决策队列 v0.1
status: active-decision-register-owner-decisions-recorded
decision_records_created: true
authority_assignments_created: true
last_reviewed: 2026-07-21
---

# Digital Biosphere Program Decision Queue v0.1（数字生物圈项目群决策队列 v0.1）

## 1. Queue Rule（队列规则）

本队列暴露需要人工决定的项目群事项。进入队列不等于批准；Priority（优先级）不等于 Authorization（授权）；关闭事项必须保留结果、理由、范围和 `decided_by_ref`。

合法状态：`OPEN`、`READY_FOR_REVIEW`、`BLOCKED_INPUT`、`DECIDED`、`DEFERRED`、`REJECTED`、`SUPERSEDED`。

## 2. Open Decisions（开放决策）

| decision_id | Priority | 决策问题 | 当前状态 | 所需输入 | 决策影响 | 禁止自动推断 |
|---|---|---|---|---|---|---|
| `DQ-002` | `P0` | DBA 是否应成为独立 Git root（Git 根目录），而不是父目录仓库中的子目录？ | `READY_FOR_REVIEW` | 当前本地/远端拓扑、历史保留方案、迁移风险 | 仓库边界、GitHub 根展示、后续自动化和发布 | 允许重写历史、删除父仓库或强制推送 |
| `DQ-003` | `P0` | DBOS、SAEE、Research Agent Pilot 各自哪个文件/manifest 是 canonical status source？ | `READY_FOR_REVIEW` | [`PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET.md`](PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET.md) 与机器可读 registry 已给出候选；仍需各 Domain Owner 确认、刷新频率和冲突规则 | 驾驶舱状态可信度和后续只读同步 | 候选来源自动成为 canonical；README、测试数量或 Git dirty 自动等于项目状态 |
| `DQ-004` | `P1` | 第一个跨项目里程碑是否选择 DBOS ↔ SAEE data contract conformance？ | `OPEN` | 字段映射、版本、现有实现审计、正负用例范围 | `M3` 的正式启动与 Owner 分派 | 已存在接口实现或允许直接调用 SAEE |
| `DQ-005` | `P1` | Research Agent Pilot 何时可以进入 Prototype Authorization Review（原型授权审查）？ | `BLOCKED_INPUT` | Human Review、approved sources、independent reviewer decision、protocol freeze | `M5` 是否进入人工授权 | `NOT_READY` 自动升级，或由 DBA 创建 Agent/Runtime |
| `DQ-006` | `P2` | POP、ARO、Agent Evidence、Token Governor、ACP 哪些进入正式 Portfolio？ | `OPEN` | [`architecture/responsibility-matrix.md`](architecture/responsibility-matrix.md) 已澄清 ARO / Agent Evidence 责任链；仍需逐项目 purpose、Owner、canonical source、license 和准入审查 | 项目组合与依赖范围 | 责任澄清、本地发现、历史关联或相邻角色等于正式准入 |
| `DQ-007` | `P2` | 驾驶舱状态采用人工周期刷新，还是未来建立只读 adapter（适配器）？ | `OPEN` | source contracts、安全边界、维护成本、staleness 需求 | 状态同步机制 | 允许 DBA 写入子仓库或自动改变项目状态 |
| `DQ-008` | `P0` | 当前 Program Governance Cockpit 与既有 Digital Biosphere public meaning layer 的 canonical relationship（规范关系）是什么？ | `READY_FOR_REVIEW` | 两个仓库的使命、受众、当前 URL、历史、重叠文件和迁移/引用方案 | 单一前门、规范优先级和避免双重 DBA 权威 | 当前驾驶舱自动覆盖、删除或合并既有 public meaning layer |
| `DQ-009` | `P0` | `Trusted Multi-Agent Infrastructure Developer Preview v0.1` 何时允许发布？ | `BLOCKED_INPUT` | 冻结 source commits、Clean Clone、Trial Plan、Guide 与已知限制已齐；仍缺真实 `participant_source`、3–5 人 Trial Result、试用后 DBOS 分发决定和 `released_by_ref` | `DP-R` 是否进入 `RELEASED` | ADR-017、测试通过、本地 Demo、Clean Clone 或 Trial PASS 自动等于发布授权 |

## 3. Closed Program Decision（已关闭项目群决策）

| decision_reference | 结果 | 来源 | 效力 |
|---|---|---|---|
| `ADR-016` | `ACCEPTED`：DBA 升级为 Program Governance + Architecture Specification cockpit | 2026-07-21 用户明确目标 | 允许更新 DBA 文档和治理入口；不授权修改 DBOS、SAEE、Pilot、Runtime 或外部状态 |
| `ADR-017` | `ACCEPTED`：进入 Trusted Multi-Agent Infrastructure Developer Preview v0.1 阶段 | 2026-07-21 用户明确目标 | 允许按 DBA / DBOS / Demo / SAEE 责任域推进受限实现；不授权发布、生产 Runtime、自动 Permission 或 Evidence 改写 |
| `ADR-018` | `ACCEPTED`：在发布前建立 3–5 人 External Developer Trial Gate | 2026-07-21 用户明确目标 | 允许建立试用计划、测量与 gate；不授权招募、外部联系、试用执行、客户验证或发布 |
| `ADR-019` | `ACCEPTED_AND_EXECUTED`：清理过期云端应用资产并在 `redcrag.cn` 根入口部署双语 TMAI 网站候选 | 2026-07-21 用户明确清理与网站要求 | 只授权公开网站候选及其 GitHub prerelease；不授权 Developer Preview Release、DBOS 公开、SAEE 边界变更或外部试用 |
| `ADR-020 / DQ-001` | `ACCEPTED`：指派 `zhangbin` 为 Human Program Owner | `decided_by_ref=zhangbin`，2026-07-21T22:48:39+08:00 | 项目群决定来源生效，重大 release 时复核；不产生 DBOS 运行权、SAEE 演化权或自动发布权 |
| `ADR-020 / DQ-010` | `DECIDED_CONDITIONAL`：`AUTHORIZE_AFTER_CLEAN_CLONE_PASS`，协调者 `zhangbin` | Clean Clone 与 `TMAI-DP-v0.1-TRIAL-20260721-001` 已冻结 | 真实 `participant_source` 仍缺失，因此外部联系、协作者添加与试用执行仍为 `false` |
| `ADR-020 / DQ-011` | `ACCEPTED`：`A_PUBLIC_SAFE_EXTRACTION_EXACT_19_FILES` | `decided_by_ref=zhangbin`、`saee_domain_owner_ref=zhangbin` | 只允许冻结 19 文件及精确 blob；不允许 private core、第二套 evaluator 或正式发布 |
| `ADR-020 / DQ-012` | `ACCEPTED`：DBA、DBOS、SAEE Owner-created public surfaces 采用 `Apache-2.0` | `decided_by_ref=zhangbin` | 允许发布根 `LICENSE`；不重许可第三方材料、数据或依赖 |
| `ADR-019 / DQ-013` | `SUPERSEDED`：不再采用独立子路径问题 | 2026-07-21 Human Owner 清理和网站决定 | `redcrag.cn` 根入口网站候选已执行；不等于 Developer Preview Release |
| `ADR-020 / DQ-014` | `ACCEPTED`：`PRIVATE_COLLABORATOR_TRIAL` | `decided_by_ref=zhangbin` | DBOS 保持 private；不授权 public visibility、具体协作者、Permission 或发布 |

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
OPEN_DECISIONS=8
CONDITIONALLY_DECIDED_NOT_EFFECTIVE=1
QUEUE_CREATES_AUTHORITY=false
QUEUE_CREATES_PERMISSION=false
QUEUE_EXECUTES_DECISIONS=false
```
