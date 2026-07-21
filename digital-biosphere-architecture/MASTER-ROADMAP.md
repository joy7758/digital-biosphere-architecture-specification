---
document_id: DBA-MASTER-ROADMAP-0.1
title: Digital Biosphere Master Roadmap v0.1
title_zh: 数字生物圈总路线图 v0.1
status: program-sequencing-baseline
current_milestone: DP-R
roadmap_is_authorization: false
roadmap_is_implementation: false
last_reviewed: 2026-07-21
---

# Digital Biosphere Master Roadmap v0.1（数字生物圈总路线图 v0.1）

## 1. Roadmap Rule（路线图规则）

本路线图定义跨项目推进顺序和进入条件，不授权代码修改、Runtime、Agent、实验、部署、发布或外部采用。里程碑只有在对应 gate evidence（闸门证据）存在时才能升级状态。

合法状态：

```text
NOT_STARTED
PLANNED
IN_PROGRESS
BASELINE_DEFINED
GATE_PASSED
BLOCKED
DEFERRED
SUPERSEDED
```

## 2. Program Milestones（项目群里程碑）

Developer Preview 是当前执行主线；原 `M0` 至 `M8` 继续保留为长期项目群路线，不因阶段切换被删除。

| preview milestone | 目标 | primary repository | 当前状态 | 完成证据 | 下一步 |
|---|---|---|---|---|---|
| `DP-1` | 建立 Digital Biosphere 统一公开入口 | DBA | `GATE_PASSED` | Public Overview、Developer Preview Plan、Release Plan、ADR-017、链接与边界验证 | 保持未发布边界 |
| `DP-2` | 建立可复制、可回归测试的 DBOS Developer Preview | DBOS | `GATE_PASSED` | `main@cd3f867`、local editable install、334/334 tests、34/34 validators、public-safe wheel clean install；历史 Evidence 未改写 | 由 `DQ-016` 决定是否公开 exact wheel |
| `DP-3` | 建立三角色 Multi-Agent Trust Demo 和跨项目 fixture | Demo + DBOS | `GATE_PASSED` | Research/Analysis/Review 角色链、3/3 records、11/11 tests、确定性重放、同一 SAEE envelope | 保持 synthetic/non-Agent 边界 |
| `DP-4` | 建立并测试 SAEE Evaluation Layer v0.1 | SAEE | `GATE_PASSED` | public `main@2173c25` 精确 19/19 blobs、8/8 tests、公共 smoke、跨项目 Clean Clone、无写回 | 保持只读和 advisory-only 边界 |
| `DP-5A` | 冻结 Agent Customer Validation Protocol | DBA | `GATE_PASSED` | `AGENT-CUSTOMER-VALIDATION-PROTOCOL.md`、6 个画像、12 个会话、预冻结阈值与 ADR-021 | 执行受控跨模型基线 |
| `DP-5B` | 执行 Agent Customer Validation baseline | DBA + Human Program Owner | `GATE_PASSED_CONDITIONAL` | 千帆／方舟 12/12 完成；公开识别 6/6；权限安全错误 0；总体 `CONDITIONAL` | 修复 4 个失败阈值，不扩展 DBOS 功能 |
| `DP-5C` | Agent-readable remediation and rerun（智能体可读修复与复测） | DBA | `GATE_PASSED` | `TMAI-ACV-20260722-002`：12/12 sessions、全部阈值、权限安全和负控通过；overall verdict 12/12 `CONDITIONAL` | 保留 API 会话的 `OPEN_WEB_DISCOVERY=NOT_ASSESSED`，由 DP-5D 单独观察自然发现 |
| `DP-5D` | Open-web discovery observation（开放网络发现观察） | DBA | `GATE_PASSED_WITH_ACCEPTED_LIMITATION` | `TMAI-OWD-20260722-001=PARTIAL_METADATA_ONLY`；`ADR-022` 为 v0.1 接受并要求继续披露 | 索引刷新后继续复查，不升级当前发现事实 |
| `DP-R` | Developer Preview Release Decision | DBA + Human Release Authority | `GATE_PASSED` | `ADR-022`、`released_by_ref=zhangbin`、exact wheel、GitHub Release、百度云 formal deployment 与公开复验 | 进入发布后观察；不自动启动新功能或长期 `M2` |

| milestone | 目标 | primary repository | 当前状态 | 完成证据 | 下一步 |
|---|---|---|---|---|---|
| `M0` | 建立 DBA、DBOS、SAEE、Digital Entity 和 Governance Decision 的基本边界 | DBA | `GATE_PASSED` | 当前架构规范、接口契约、ADR-001 至 ADR-015 | 保持一致性，不再重复定义 |
| `M1` | 将 DBA 建成项目群治理与架构总驾驶舱 | DBA | `BASELINE_DEFINED` | 本路线图、Portfolio、Status、Decision、Gate、Risk、Program Governance Spec 和 ADR-016 | 完成验证并决定版本发布 |
| `M2` | 为核心项目确认 canonical status source 与刷新规则 | DBA 协调；各项目提供来源 | `PLANNED` | DBOS、SAEE、Research Agent Pilot 的明确状态入口、Owner、freshness 和冲突处理记录 | 处理 `DQ-003` |
| `M3` | 建立 DBOS ↔ SAEE contract conformance baseline（契约符合性基线） | DBA 协调；DBOS/SAEE 分别实施 | `PLANNED` | 字段映射、版本、正负用例、验证结果；不要求真实 Runtime 调用 | 处理 `DQ-004` |
| `M4` | 建立 Digital Entity admission and registration conformance（准入与登记符合性） | DBOS；DBA gate | `NOT_STARTED` | Candidate、Decision、Authorization、Registration 的连续引用和负例证据 | M2、M3 先通过 |
| `M5` | 决定 Research Agent Prototype（科研智能体原型）是否获准创建 | Research Agent Pilot；DBA 协调 | `NOT_STARTED` | Human Review、approved sources、protocol freeze、prototype authorization | 当前保持 `NOT_READY` |
| `M6` | 执行第一个受控 Digital Entity research loop（数字主体研究闭环） | Research Agent Pilot + DBOS + SAEE | `NOT_STARTED` | 显式实验授权、执行记录、Evidence、Verification、Evaluation、Human Decision | 不得由路线图自动启动 |
| `M7` | 建立可重复的多主体接入和联邦符合性 | DBOS + future Digital Entities | `NOT_STARTED` | 至少一个已验证 Pilot 后的通用接入契约和负例 | 不能从单一 Pilot 直接外推 |
| `M8` | 推进开发者生态、认证与商业服务 | 各相应项目 | `DEFERRED` | 实现、采用和商业状态分别有独立证据 | 不得用战略文档声称已提供 |

## 3. Critical Path（关键路径）

```text
DP-1 Public Entry
  → DP-2 DBOS Developer Preview
  → DP-3 Multi-Agent Trust Demo
  → DP-4 SAEE Evaluation Layer
  → DP-5A Agent Customer Protocol
  → DP-5B Agent Customer Baseline
  → DP-5C Agent-readable Remediation and Rerun
  → DP-5D Open-Web Discovery Observation
  → DP-R Human Release Decision

Long-term continuation:
M2 Canonical Status Sources
  → M3 DBOS / SAEE Conformance
  → M4 Entity Admission Conformance
  → M5 Human Prototype Decision
  → M6 Controlled Research Loop
  → M7 Repeatable Multi-entity Onboarding
```

`M8` 不是 `M6` 或 `M7` 的自动结果。Commercial Offering（商业服务）、Certification（认证）和 Marketplace（市场）需要独立决策与证据。

## 4. Current Program Focus（当前项目群焦点）

```text
CURRENT_FOCUS=DEVELOPER_PREVIEW_V0_1_POST_RELEASE_OBSERVATION
NEXT_BLOCKER=NONE_FOR_RELEASE_V0_1_OPEN_WEB_LIMIT_REMAINS_DISCLOSED
NEXT_DECISION=SEPARATE_DECISION_REQUIRED_FOR_ANY_NEW_IMPLEMENTATION_OR_PRODUCTION_CLAIM
NEXT_DELIVERY=ANONYMOUS_INSTALL_AND_AGENT_REUSE_OBSERVATION
NEXT_INTEGRATION=NONE_AUTOMATICALLY_AUTHORIZED_BY_RELEASE
DQ_015_AGENT_NATIVE_VALIDATION_ACCEPTED=true
BASELINE_VALIDATION_ID=TMAI-ACV-20260721-001
BASELINE_RESULT=CONDITIONAL
RERUN_VALIDATION_ID=TMAI-ACV-20260722-002
RERUN_RESULT=PASS
OPEN_WEB_DISCOVERY_OBSERVATION_ID=TMAI-OWD-20260722-001
OPEN_WEB_DISCOVERY_RESULT=PARTIAL_METADATA_ONLY
GITHUB_DISCOVERY_METADATA_REMEDIATED=true
GITHUB_METADATA_DESCRIPTION_MATCH=true
OPEN_WEB_CANONICAL_NAME_MATCH=false
CROSS_PROJECT_CLEAN_CLONE_PASS=true
HUMAN_PARTICIPANT_SOURCE_REQUIRED=false
RESEARCH_AGENT_PROTOTYPE_AUTHORIZED=false
```

当前不应继续增加新的 Entity、生产 Runtime 或无验证接口承诺。优先任务是形成公开开发者可运行、可展示、可验证的最小链路，同时让驾驶舱持续回答：现在在哪里、谁负责、缺什么证据、哪个决定阻塞下一步。

## 5. Roadmap Non-claims（路线图非声明）

```text
ROADMAP_DEFINED=true
ROADMAP_APPROVES_IMPLEMENTATION=false
ROADMAP_APPROVES_EXECUTION=false
ROADMAP_APPROVES_EXPERIMENT=false
ROADMAP_PROVES_INTEGRATION=false
ROADMAP_PROVES_ADOPTION=false
```
