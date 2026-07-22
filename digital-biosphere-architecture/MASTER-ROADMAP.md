---
document_id: DBA-MASTER-ROADMAP-0.1
title: Digital Biosphere Master Roadmap v0.1
title_zh: 数字生物圈总路线图 v0.1
status: production-architecture-sequencing-baseline
current_milestone: PR-0
roadmap_is_authorization: false
roadmap_is_implementation: false
last_reviewed: 2026-07-22
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

### 2.1 Strategic Priority Envelope（战略优先级包络）

以下顺序固定“做什么”的长期优先级；production gates 固定“什么证据允许继续”。两者不得互相替代。

| priority | 战略目标 | 当前事实 | 下一 truth-preserving step（保真下一步） |
|---|---|---|---|
| `SP-1` | 完成 Developer Preview 发布 | `GATE_PASSED` | 保留 release history 和已披露限制；不写成 production release |
| `SP-2` | 形成公开 Protocol 和 SDK | TMAP protocol 已定义；exact public-safe DBOS wheel 已发布；稳定 SDK adoption 未证明 | 优先 schema/SDK contract/conformance，不扩建封闭平台 |
| `SP-3` | 吸引外部 Agent developer / machine customer | agent-native validation 12/12 rerun pass；open-web discovery 仍 partial | 改善 agent-readable discovery、复用和第三方 adapter entry；不写成 customer adoption |
| `SP-4` | 建立 Adapter ecosystem | DBOS→SAEE read-only preview adapter 存在；production adapter isolation 未验证 | 先定义版本、失败关闭、zero-writeback 和 conformance profile |
| `SP-5` | 积累真实多智能体长期运行数据 | 未授权、未执行 | 必须先通过 DBOS production core、安全/恢复和 bounded pilot authorization |
| `SP-6` | 推动 SAEE 长期评价能力 | public preview evaluation 为 advisory-only；长期生产评价未验证 | 只读、版本钉住、evidence-bound、no-execution 的长期评价 gate |

```text
STRATEGIC_DIRECTION=TRUSTED_MULTI_AGENT_INFRASTRUCTURE
PROGRAM_MODEL=ONE_PROGRAM_MULTIPLE_RESPONSIBILITY_DOMAINS
PROTOCOLIZATION_BEFORE_PLATFORM_EXPANSION=true
DBOS_NE_AGENT_FRAMEWORK=true
SAEE_NE_CONTROLLER=true
```

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

Developer Preview 发布历史保持不变。当前新增的 Production Readiness（生产就绪）路线只定义从已发布预览版走向有界生产部署的进入条件，不把规范、计划或 OpenTelemetry（开放遥测）映射写成实现事实。

| production milestone | 目标 | primary repository | 当前状态 | 完成证据 | 下一步 |
|---|---|---|---|---|---|
| `PR-0` | 冻结 Trusted Multi-Agent Protocol（可信多智能体协议）与生产可观测性架构基线 | DBA | `GATE_PASSED_REMOTE_BASELINE_VERIFIED` | content commit `264f317...` / tree `b83f25d...`、OpenTelemetry profiles、56/46/45/48-case contracts、`ADR-023`–`ADR-028`、六项 exact decision 与远端 freeze receipt | 保持基线；不授权 Collector build/config/deploy 或 production claim |
| `PR-1` | 建立 DBOS/SAEE production implementation mapping（生产实现映射） | 子项目提供事实；DBA 审查边界 | `GATE_PASSED_READ_ONLY_MAPPING` | `PRODUCTION-IMPLEMENTATION-MAPPING-REPORT.md`：remote commits、334 tests、34 validators、8 adapter tests、OTel capability inventory、缺口与重复权威审查 | `DQ-018` decision packet 和两路 next-step recommendation 已就绪，等待人类决策 |
| `PR-2` | 建立最小 DBOS production core（生产核心） | DBOS | `PR_G2A_LINUX_ARM64_SUPPLEMENT_READY_G2B_G2T_G2I_G2C_BLOCKED` | DQ-018 exact source `57c7b9e…`、receipt `1c8f3d9…`、533/533 tests、199/199 telemetry tests、30 validators PASS + 5 external-source fail closed、OTel authorized 68/68、TA-P001—P005 PASS、Linux arm64 remote receipt | 审查 PR-G2A；未批准前不进入 DQ-019/PR-G2B；完整 PR-G2=false |
| `PR-3` | 建立 OpenTelemetry conformance and operations（符合性与运维） | DBOS + deployment infrastructure | `NOT_STARTED` | 版本锁定、exact custom-minimal Collector build/config/runtime/topology 绑定、deployment + operational-evidence profiles 的 synthetic-input/immutable-rollout/metric-stability/self-observation/no-data-alert/composite-readiness/delivery-reconciliation obligations、56/56 OTLP、46/46 semantic、45/45 Schema/Resource/Entity provenance 与 48/48 Collector distribution cases 的四个独立结果绑定 | 不得创建第五套重复目录；不得把 Telemetry 自动升级为 Evidence/Truth，也不得把 profile/schema/health/dashboard/binary startup 当实现、测量或生产证据 |
| `PR-4` | 验证 SAEE production adapter isolation（生产适配隔离） | SAEE | `NOT_STARTED` | 只读消费、版本兼容、失败关闭、无 DBOS 写回、无 Decision/Permission | 不调用未获准算法或生成 Authority |
| `PR-5` | 通过 Security / Recovery / Capacity gates（安全、恢复与容量闸门） | DBOS + DBA review | `NOT_STARTED` | threat model、secret handling、data minimization、backup/restore、灾难恢复、容量与队列压力证据 | 所有 critical gap 关闭后才可进入 Pilot |
| `PR-6` | 执行 bounded production pilot（有界生产试点） | 明确授权的部署责任方 | `NOT_STARTED` | 7 天 staging、30 天有界观察、真实但受控工作负载、SLO、failure drill、rollback、Human Review | 需要独立 Pilot Authorization；不得由路线图自动启动 |
| `PR-R` | Production Readiness Decision（生产就绪决策） | Human Production Authority | `NOT_STARTED` | `PR-G0` 至 `PR-G7` 全部 scoped pass、残余风险接受、部署版本与责任人明确 | 显式 ADR/Decision 后才可称 deployment-specific production ready |

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

Production continuation:
PR-0 Protocol and Observability Baseline
  → PR-1 DBOS Implementation Mapping
  → PR-2 DBOS Production Core
  → PR-3 OpenTelemetry Conformance and Operations
  → PR-4 SAEE Adapter Isolation
  → PR-5 Security / Recovery / Capacity
  → PR-6 Bounded Production Pilot
  → PR-R Human Production Readiness Decision

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
CURRENT_FOCUS=PRODUCTION_ARCHITECTURE_HUMAN_DECISION_CONVERGENCE
NEXT_BLOCKER=HUMAN_DECISIONS_AND_IMMUTABLE_DBA_BASELINE_NOT_RECORDED
NEXT_DECISION=DQ_022_TO_DQ_025_REFERENCE_DECISIONS_AND_DQ_018_EXACT_IMPLEMENTATION_SLICE
NEXT_ARCHITECTURE_VERSION_DECISIONS=DQ_022_OTLP_1_11_REFERENCE_ADOPTION,DQ_023_OTEL_SEMANTIC_MAPPING_ADOPTION,DQ_024_OTEL_SCHEMA_RESOURCE_ENTITY_PROVENANCE_ADOPTION,DQ_025_OTEL_COLLECTOR_DISTRIBUTION_ADOPTION
NEXT_DELIVERY=DQ_018_HUMAN_DECISION_OR_NO_IMPLEMENTATION
NEXT_INTEGRATION=NONE_AUTHORIZED_UNTIL_DQ_018
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
TRUSTED_MULTI_AGENT_PROTOCOL_BASELINE_DEFINED=true
OPENTELEMETRY_OBSERVABILITY_PROFILE_DEFINED=true
DQ_018_DECISION_PACKET_READY=true
DQ_018_AGENT_RECOMMENDATION_COMPLETE=true
DQ_018_NEXT_SLICE_RECOMMENDED_BY_TWO_AGENTS=true
DQ_018_HUMAN_DECISION_RECORDED=true
DQ_018_IMPLEMENTATION_AUTHORIZED=true
DQ_018_IMPLEMENTATION_MAY_START=false
DQ_018_IMPLEMENTATION_MAY_START_REASON=ALREADY_COMPLETED_EXACT_SLICE_NO_NEW_SCOPE_AUTHORIZED
DQ_018_IMPLEMENTATION_COMPLETE=true
DQ_018_SOURCE_COMMIT=57c7b9e55dfcab84e81e7c5f61e9d8ea61045dbe
DQ_018_RECEIPT_COMMIT=1c8f3d949f7b9686567b43bc8ebc316597ce9cfc
DQ_018_IMPLEMENTATION_MANIFEST=sha256:d0951d6c6252109261f7d2806082b850741df3d1decc4ff5c6418602dff69710
DQ_018_STREAMING_INTEGRITY_HARDENED=true
DQ_018_TA_P001_TO_TA_P005_PASS=true
DQ_018_LINUX_ARM64_REFERENCE_VALIDATED=true
DQ_018_LINUX_ARM64_REMOTE_RECEIPT_VERIFIED=true
PR_G2A_READY_FOR_HUMAN_REVIEW=true
PR_G2A_HUMAN_REVIEW_APPROVED=false
FULL_PR_G2_READY=false
PRODUCTION_IMPLEMENTATION_SEQUENCE_DEFINED=true
PRODUCTION_PATH_AGENT_REVIEW_COMPLETE=true
PRODUCTION_IMPLEMENTATION_SEQUENCE_RECOMMENDED_BY_TWO_AGENTS=true
ADR_024_STATUS=ACCEPTED
DQ_019_STATUS=BLOCKED_INPUT
DQ_020_STATUS=BLOCKED_INPUT
DQ_020_MACHINE_DEPLOYMENT_PROFILE_DEFINED=true
DQ_020_MACHINE_DEPLOYMENT_PROFILE_AUTHORIZES_NOTHING=true
DQ_021_STATUS=BLOCKED_INPUT
DQ_022_STATUS=DECIDED_REFERENCE_ADOPTED
DQ_022_HUMAN_DECISION_RECORDED=true
DQ_023_STATUS=DECIDED_REFERENCE_ADOPTED
DQ_023_HUMAN_DECISION_RECORDED=true
DQ_024_STATUS=DECIDED_REFERENCE_ADOPTED
DQ_024_HUMAN_DECISION_RECORDED=true
DQ_025_STATUS=DECIDED_REFERENCE_ADOPTED
DQ_025_HUMAN_DECISION_RECORDED=true
PRODUCTION_HUMAN_DECISION_READINESS_REGISTRY_DEFINED=true
PRODUCTION_HUMAN_DECISION_READINESS_REGISTRY_SCHEMA_VALID=true
PRODUCTION_DECISION_AGENT_PRIORITY_CONSENSUS=false
NEW_PRODUCTION_TECHNICAL_SPECIFICATION_ALLOWED=false
PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
BOUNDED_DQ_018_IMPLEMENTATION_AUTHORIZED=true
IMMUTABLE_DBA_BASELINE_CREATED=true
PRODUCTION_PILOT_AUTHORIZED=false
PRODUCTION_READY=false
```

当前不应继续增加新的技术规范、Entity、生产 Runtime 或无验证接口承诺。优先任务是审查
`PR-G2A` exact offline slice，并在明确批准后收敛 `DQ-019` 的真实候选输入。

Developer Preview 已发布，`PR-G1` 已完成，DQ-022–025 与 ADR-024 已采纳，DQ-018
离线实现切片也已在固定 Linux arm64 参考环境完成远端绑定验证。当前 gate 是
`PR-G2A Human Review`。后继 production
persistence、OTLP/Collector staging、Identity/Evidence integration 和 SAEE/Pilot 仍按
[`architecture/production-implementation-sequence.md`](architecture/production-implementation-sequence.md)
分阶段独立决定；任何 build、configuration、deployment、真实 Pilot 或生产声明都不能由
Agent recommendation 或单个切片 PASS 自动授权。

## 5. Roadmap Non-claims（路线图非声明）

```text
ROADMAP_DEFINED=true
ROADMAP_APPROVES_IMPLEMENTATION=false
ROADMAP_APPROVES_EXECUTION=false
ROADMAP_APPROVES_EXPERIMENT=false
ROADMAP_PROVES_INTEGRATION=false
ROADMAP_PROVES_ADOPTION=false
ROADMAP_PROVES_PRODUCTION_READINESS=false
PRODUCTION_READY=false
```
