---
document_id: DBA-DECISION-QUEUE-0.1
title: Digital Biosphere Program Decision Queue v0.1
title_zh: 数字生物圈项目群决策队列 v0.1
status: active-decision-register-owner-decisions-recorded
decision_records_created: true
authority_assignments_created: true
last_reviewed: 2026-07-23
---

# Digital Biosphere Program Decision Queue v0.1（数字生物圈项目群决策队列 v0.1）

## 1. Queue Rule（队列规则）

本队列暴露需要人工决定的项目群事项。进入队列不等于批准；Priority（优先级）不等于 Authorization（授权）；关闭事项必须保留结果、理由、范围和 `decided_by_ref`。

Production-path（生产路径）的集中人工审查入口是
[`PRODUCTION-ARCHITECTURE-HUMAN-DECISION-READINESS-REGISTRY.md`](PRODUCTION-ARCHITECTURE-HUMAN-DECISION-READINESS-REGISTRY.md)
及其 [machine registry](PRODUCTION-ARCHITECTURE-HUMAN-DECISION-READINESS-REGISTRY.v0.1.json)。该注册表只聚合本队列状态、
现有 `ADR-024`、packet readiness（决策包就绪度）、精确 token 和依赖，不创建新 Decision，也不能自动修改本队列或 ADR。

合法状态：`OPEN`、`READY_FOR_REVIEW`、`BLOCKED_INPUT`、`DECIDED`、`DEFERRED`、`REJECTED`、`SUPERSEDED`。

## 2. Active and Recently Decided Items（活动与近期已决定事项）

| decision_id | Priority | 决策问题 | 当前状态 | 所需输入 | 决策影响 | 禁止自动推断 |
|---|---|---|---|---|---|---|
| `DQ-002` | `P0` | DBA 是否应成为独立 Git root（Git 根目录），而不是父目录仓库中的子目录？ | `READY_FOR_REVIEW` | 当前本地/远端拓扑、历史保留方案、迁移风险 | 仓库边界、GitHub 根展示、后续自动化和发布 | 允许重写历史、删除父仓库或强制推送 |
| `DQ-003` | `P0` | DBOS、SAEE、Research Agent Pilot 各自哪个文件/manifest 是 canonical status source？ | `OPEN` | 各 Domain Owner 的来源确认、刷新频率、冲突规则 | 驾驶舱状态可信度和后续只读同步 | README、测试数量或 Git dirty 自动等于项目状态 |
| `DQ-004` | `P1` | 第一个跨项目里程碑是否选择 DBOS ↔ SAEE data contract conformance？ | `OPEN` | 字段映射、版本、现有实现审计、正负用例范围 | `M3` 的正式启动与 Owner 分派 | 已存在接口实现或允许直接调用 SAEE |
| `DQ-005` | `P1` | Research Agent Pilot 何时可以进入 Prototype Authorization Review（原型授权审查）？ | `BLOCKED_INPUT` | Human Review、approved sources、independent reviewer decision、protocol freeze | `M5` 是否进入人工授权 | `NOT_READY` 自动升级，或由 DBA 创建 Agent/Runtime |
| `DQ-006` | `P2` | POP、ARO、Agent Evidence、Token Governor、ACP 哪些进入正式 Portfolio？ | `OPEN` | 每个项目的目的、Owner、canonical source、重复能力和接口边界 | 项目组合与依赖范围 | 本地发现、历史关联或相邻角色等于正式准入 |
| `DQ-007` | `P2` | 驾驶舱状态采用人工周期刷新，还是未来建立只读 adapter（适配器）？ | `OPEN` | source contracts、安全边界、维护成本、staleness 需求 | 状态同步机制 | 允许 DBA 写入子仓库或自动改变项目状态 |
| `DQ-008` | `P0` | 当前 Program Governance Cockpit 与既有 Digital Biosphere public meaning layer 的 canonical relationship（规范关系）是什么？ | `READY_FOR_REVIEW` | 两个仓库的使命、受众、当前 URL、历史、重叠文件和迁移/引用方案 | 单一前门、规范优先级和避免双重 DBA 权威 | 当前驾驶舱自动覆盖、删除或合并既有 public meaning layer |
| `DQ-018` | `P0` | 是否批准 `DBOS-PR-2A-TELEMETRY-ADMISSION-FOUNDATION` 作为第一个 production-path reference-conformance slice（生产路径参考符合性切片），由 DBOS Domain Owner 实施？ | `AUTHORIZED_IMPLEMENTED_SECURITY_REMEDIATED_NATIVE_REMOTE_ATTESTED_PR_G2A_HUMAN_REVIEW_READY_NOT_APPROVED` | exact source `ee90c0c…` / receipt `901bf0d…` / manifest `306435cd…` 已远端证明；[security remediation attestation](PR-G2A-SECURITY-REMEDIATION-ATTESTATION-2026-07-23.md) / [JSON](PR-G2A-SECURITY-REMEDIATION-ATTESTATION-2026-07-23.json) 关闭 2 High 并保留 2 scoped Medium residuals | 执行 Human Security Review；在精确 `PR-G2A` token 之前不得进入 DQ-019 implementation | native load PASS、0 automated findings、DBOS/DBA attestation、finding closure 或 Agent recommendation 自动等于 Human Security Review complete、PR-G2A approval、完整 PR-G2 或 production readiness |
| `PR-G2A` | `P0` | 是否批准 DQ-018 exact security-remediated offline Telemetry Admission reference slice 通过阶段闸门？ | `READY_FOR_HUMAN_SECURITY_REVIEW_NOT_APPROVED` | [current human review packet](PR-G2A-TELEMETRY-ADMISSION-SECURITY-REMEDIATED-HUMAN-REVIEW-PACKET-2026-07-23.md) / [JSON](PR-G2A-TELEMETRY-ADMISSION-SECURITY-REMEDIATED-HUMAN-REVIEW-PACKET-2026-07-23.json)；DBOS source `ee90c0c…` / receipt `901bf0d…`；2 High closed + 2 scoped Medium residuals | Human reviewer 使用精确 token 批准、退回或拒绝；当前没有 Human Decision | review-ready、automated scan、test count、native load、remote attestation 或 risk closure 自动等于 Human Review complete、security approval 或 production readiness |
| `DQ-019` | `P0` | 选择哪个 production persistence backend/profile，并是否授权 DBOS production persistence adapter 实施？ | `BLOCKED_INPUT` | [`architecture/production-persistence-adapter-specification.md`](architecture/production-persistence-adapter-specification.md)、[due-diligence contract](architecture/production-persistence-candidate-due-diligence-contract.md)、[machine profiles](architecture/production-persistence-candidate-profiles.v0.1.json) / [Schema](architecture/schemas/production-persistence-candidate-profiles.schema.v0.1.json)、[candidate assessment](DQ-019-PRODUCTION-PERSISTENCE-CANDIDATE-ASSESSMENT.md) / [JSON](DQ-019-PRODUCTION-PERSISTENCE-CANDIDATE-ASSESSMENT.json)、[two-provider recommendation](DQ-019-PRODUCTION-PERSISTENCE-AGENT-RECOMMENDATION.md)、[blocked decision packet](DQ-019-PRODUCTION-PERSISTENCE-DECISION-PACKET.md) / [JSON](DQ-019-PRODUCTION-PERSISTENCE-DECISION-PACKET.json)、PR-G2A approval、exact candidate profile、Owner/topology/cost/security/RPO/RTO/direct drills | production canonical store 的选型和实施范围；不授权数据迁移、外部云资源或生产部署 | Schema valid、candidate shortlist、Agent recommendation、SQLite pass、供应商 SLA/HA 名称或路线图自动等于 backend selection、production durability、measured SLO 或实施授权 |
| `DQ-020` | `P0` | 是否允许 pinned offline OTLP decoder 逐步进入 authenticated listener 和 Collector-edge-to-gateway staging？ | `BLOCKED_INPUT` | [`architecture/otlp-collector-production-profile.md`](architecture/otlp-collector-production-profile.md)、[machine deployment profile](architecture/opentelemetry-collector-deployment-profile.v0.1.json) / [Schema](architecture/schemas/opentelemetry-collector-deployment-profile.schema.v0.1.json)、[operational evidence profile](architecture/opentelemetry-collector-operational-evidence-profile.v0.1.json) / [Schema](architecture/schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json) / [contract](architecture/opentelemetry-collector-operational-evidence-contract.md) / [two-provider review](OTEL-COLLECTOR-OPERATIONAL-EVIDENCE-AGENT-RECOMMENDATION.md)、[readiness matrix](architecture/opentelemetry-collector-deployment-readiness-matrix.md) / [deployment review](OTEL-COLLECTOR-DEPLOYMENT-PROFILE-AGENT-RECOMMENDATION.md)、[OTLP conformance profile](architecture/otlp-v1.11-conformance-profile.md) / [56-case catalog](architecture/otlp-v1.11-conformance-cases.v0.1.json)、DQ-018/DQ-019 和 DQ-022–025 decisions/direct evidence、deployment Owner/repository、exact build/image/config/runtime/topology/security/capacity/readiness/metric/query/alert/route/runbook/rollback bindings | 只允许按 `G3A`–`G3F` 逐闸门实施和 synthetic staging；不授权公网 endpoint、production traffic、real customer data 或 Evidence creation | proposed profile、模型 human-review recommendation、OpenTelemetry 官方模式、catalog defined、health/dashboard OK 或 config Schema valid 自动等于 tests executed、measurement、deployment authorization、end-to-end delivery 或 production readiness |
| `DQ-021` | `P0` | 是否实施独立 Telemetry-to-Evidence Admission，创建 EvidenceAdmissionRequest/Record 并连接 canonical Evidence/Verification？ | `BLOCKED_INPUT` | [`architecture/telemetry-to-evidence-admission-contract.md`](architecture/telemetry-to-evidence-admission-contract.md)、PR-G2I Identity Continuity、Data Governance Gate、P0–P3 provenance、Evidence policy/schema/security/retention 和 DQ-018/020 直接证据 | DBOS Evidence admission 实施范围；不授权 Truth、Permission、SAEE writeback、high-impact use 或数据收集扩张 | Telemetry/Collector/signature/Verification/Human Review 自动等于 Truth 或可执行授权 |
| `DQ-022` | `P0` | 是否采纳 official `opentelemetry-proto v1.11.0` / `790608c...` 为 TMAI v0.1 production-path 的 OTLP reference baseline，并冻结 size-limit / `Retry-After` delta？ | `READY_FOR_REVIEW` | [`OTLP-1.11-VERSION-DELTA-ASSESSMENT.md`](OTLP-1.11-VERSION-DELTA-ASSESSMENT.md)、[decision packet](OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.md) / [JSON](OTLP-1.11-VERSION-ADOPTION-DECISION-PACKET.json)、[conformance profile](architecture/otlp-v1.11-conformance-profile.md) / [56-case catalog](architecture/otlp-v1.11-conformance-cases.v0.1.json) / [catalog schema](architecture/schemas/otlp-conformance-case-catalog.schema.v0.1.json) / [result schema](architecture/schemas/otlp-conformance-result-set.schema.v0.1.json) / [two-provider conformance review](OTLP-1.11-CONFORMANCE-PROFILE-AGENT-RECOMMENDATION.md)、[`ADR-025`](architecture/ADR-025-adopt-otlp-1.11-reference-baseline.md)、[two-provider version review](OTLP-1.11-VERSION-ADOPTION-AGENT-RECOMMENDATION.md) | 只决定 external architecture reference 与后续 conformance controls；不选择或升级 SDK/Collector/Runtime；不把 56 个 `NOT_EXECUTED` case 改成已执行 | Agent recommendation、official stable label、schema valid 或目录定义自动等于 Version Adoption、Implementation、test execution 或 interoperability proof |
| `DQ-023` | `P0` | 是否采纳 core Semantic Conventions `v1.43.0@89aae438...` selected stable mapping 与 GenAI `2e994c6d...` pinned Development mapping 为 TMAI v0.1 semantic reference，并冻结对应 46-case conformance/result contract？ | `READY_FOR_REVIEW` | [semantic profile](architecture/opentelemetry-semantic-conventions-profile.md)、[47-field mapping](architecture/opentelemetry-semantic-mapping.v0.1.json)、[46-case/8-group conformance catalog](architecture/opentelemetry-semantic-conformance-cases.v0.1.json)、[conformance profile](architecture/opentelemetry-semantic-conformance-profile.md)、[catalog schema](architecture/schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json)、[result schema](architecture/schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json)、[decision packet](OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.md) / [JSON](OTEL-SEMANTIC-CONVENTIONS-ADOPTION-DECISION-PACKET.json)、[`ADR-026`](architecture/ADR-026-opentelemetry-semantic-conventions-boundary.md)、[mapping review](OTEL-SEMANTIC-CONVENTIONS-AGENT-RECOMMENDATION.md) 和 [conformance review](OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md)；47/47 mapping coverage、12/12 + 23/23 schema negatives，两路最终推荐 bounded human review；0 cases executed，production=false | 只决定 architecture mapping/conformance reference、稳定性通道和 non-authority boundary；不创建 custom namespace、SDK/Collector、Identity、Execution、Evidence、Evaluation、Permission 或实现授权 | Agent recommendation、47/47 coverage、schema rehearsal、Stable/Development 标签或 synthetic example 自动等于 adoption、implementation、executed conformance、interoperability 或 production proof |
| `DQ-024` | `P0` | 是否采纳 OpenTelemetry Specification `v1.59.0` Stable Telemetry Schema / Resource SDK 子集、core schema `1.43.0` exact artifact binding，以及 Development Entity quarantine 为 TMAI v0.1 Schema/Resource/Entity provenance boundary？ | `READY_FOR_REVIEW` | [provenance profile](architecture/opentelemetry-schema-resource-entity-provenance-profile.md)、[45-case/7-group catalog](architecture/opentelemetry-schema-resource-conformance-cases.v0.1.json)、[catalog schema](architecture/schemas/opentelemetry-schema-resource-conformance-case-catalog.schema.v0.1.json)、[result schema](architecture/schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json)、[decision packet](OTEL-SCHEMA-RESOURCE-ADOPTION-DECISION-PACKET.md) / [JSON](OTEL-SCHEMA-RESOURCE-ADOPTION-DECISION-PACKET.json)、[`ADR-027`](architecture/ADR-027-opentelemetry-schema-resource-entity-boundary.md) 与 [three-pass two-provider review](OTEL-SCHEMA-RESOURCE-AGENT-RECOMMENDATION.md)；2/2 Schema、3/3 positive fixtures、14/14 + 37/37 negatives，required document corrections 0；45 cases executed=0 | 只决定 exact Schema/Resource reference、transform/detector provenance、data-governance binding 和 OTel Entity quarantine；不采纳 Development Entity 为 DBOS identity，不授权实现、网络 fetch、Collector、Registration、Evidence 或部署 | 两路 bounded design recommendation、Schema valid、45-case catalog、observed digest 或 official Stable 标签自动等于 adoption、runtime conformance、customer runtime proof 或 production readiness |
| `DQ-025` | `P0` | 是否采纳 OpenTelemetry Collector `v0.156.0@aa158b23...` 的 exact custom-minimal component inventory 作为 TMAI v0.1 Collector distribution architecture reference？ | `DECIDED` | [distribution profile](architecture/opentelemetry-collector-distribution-profile.md)、[8-component/2-provider inventory](architecture/opentelemetry-collector-component-inventory.v0.1.json)、[48-case/8-group catalog](architecture/opentelemetry-collector-distribution-conformance-cases.v0.1.json)、对应 [catalog schema](architecture/schemas/opentelemetry-collector-distribution-conformance-case-catalog.schema.v0.1.json) / [result schema](architecture/schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json)、[decision packet](OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET.md) / [JSON](OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET.json)、[`ADR-028`](architecture/ADR-028-opentelemetry-collector-minimal-distribution.md) 与 [two-provider review](OTEL-COLLECTOR-DISTRIBUTION-AGENT-RECOMMENDATION.md)；exact upstream commits/bytes、component stability、supply-chain/config/runtime/authority controls 已登记；48 cases executed=0 | 只决定 architecture inventory reference；不构建 binary/image，不生成 config，不选择 deployment repo/Owner，不开放 listener，不授权 `DQ-020` 或生产部署 | official latest、signed tag、prebuilt manifest、agent recommendation、Schema valid、health OK 或 48-case catalog 自动等于 source immutability、build provenance、runtime conformance、Evidence、gate pass 或 production readiness |

截至 `2026-07-22T12:05:04+08:00`，上表中的 `DQ-018`、`DQ-022`、`DQ-023`、`DQ-024`
也已由 `decided_by_ref=zhangbin` 关闭为 `DECIDED`。精确 token、effect 和前置条件以
[machine registry](PRODUCTION-ARCHITECTURE-HUMAN-DECISION-READINESS-REGISTRY.v0.1.json) 及下方 closed record 为准；
表内较早 packet readiness 文本只保留审查输入的历史状态，不构成当前状态。

## 3. Closed Program Decision（已关闭项目群决策）

| decision_reference | 结果 | 来源 | 效力 |
|---|---|---|---|
| `ADR-016` | `ACCEPTED`：DBA 升级为 Program Governance + Architecture Specification cockpit | 2026-07-21 用户明确目标 | 允许更新 DBA 文档和治理入口；不授权修改 DBOS、SAEE、Pilot、Runtime 或外部状态 |
| `ADR-017` | `ACCEPTED`：进入 Trusted Multi-Agent Infrastructure Developer Preview v0.1 阶段 | 2026-07-21 用户明确目标 | 允许按 DBA / DBOS / Demo / SAEE 责任域推进受限实现；不授权发布、生产 Runtime、自动 Permission 或 Evidence 改写 |
| `ADR-018` | `SUPERSEDED_AS_PRIMARY_BY_ADR-021`：3–5 人 External Developer Trial 保留为可选次级研究 | 2026-07-21 原目标与后继客户模型决定 | 不授权招募、外部联系、试用执行、客户验证或发布 |
| `ADR-019` | `ACCEPTED_AND_EXECUTED`：清理过期云端应用资产并在 `redcrag.cn` 根入口部署双语 TMAI 网站候选 | 2026-07-21 用户明确清理与网站要求 | 只授权公开网站候选及其 GitHub prerelease；不授权 Developer Preview Release、DBOS 公开、SAEE 边界变更或外部试用 |
| `ADR-020 / DQ-001` | `ACCEPTED`：指派 `zhangbin` 为 Human Program Owner | `decided_by_ref=zhangbin`，2026-07-21T22:48:39+08:00 | 项目群决定来源生效，重大 release 时复核；不产生 DBOS 运行权、SAEE 演化权或自动发布权 |
| `ADR-020 / DQ-010` | `SUPERSEDED_FOR_PRIMARY_ROUTE`：原决定为 `AUTHORIZE_AFTER_CLEAN_CLONE_PASS` | Clean Clone 与原技术包仍保留 | 人类试用未执行；不再作为首要发布 gate，也不产生外部联系或协作者权限 |
| `ADR-020 / DQ-011` | `ACCEPTED`：`A_PUBLIC_SAFE_EXTRACTION_EXACT_19_FILES` | `decided_by_ref=zhangbin`、`saee_domain_owner_ref=zhangbin` | 只允许冻结 19 文件及精确 blob；不允许 private core、第二套 evaluator 或正式发布 |
| `ADR-020 / DQ-012` | `ACCEPTED`：DBA、DBOS、SAEE Owner-created public surfaces 采用 `Apache-2.0` | `decided_by_ref=zhangbin` | 允许发布根 `LICENSE`；不重许可第三方材料、数据或依赖 |
| `ADR-019 / DQ-013` | `SUPERSEDED`：不再采用独立子路径问题 | 2026-07-21 Human Owner 清理和网站决定 | `redcrag.cn` 根入口网站候选已执行；不等于 Developer Preview Release |
| `ADR-020 / DQ-014` | `ACCEPTED`：`PRIVATE_COLLABORATOR_TRIAL` | `decided_by_ref=zhangbin` | DBOS 保持 private；不授权 public visibility、具体协作者、Permission 或发布 |
| `ADR-021 / DQ-010` | `SUPERSEDED_FOR_PRIMARY_ROUTE`：人类参与者招募不再是首要客户验证路径 | 2026-07-21 Human Owner 明确核心客户是 AI agent | 不把未执行的人类试用改写成通过；可作为未来次级可用性研究保留 |
| `ADR-021 / DQ-015` | `ACCEPTED_AND_EXECUTED_PASS`：`ADOPT_AGENT_NATIVE_CUSTOMER_VALIDATION` | `decided_by_ref=zhangbin`；`001=CONDITIONAL`、`002=PASS` | 两轮各 12 次会话全部保留；不创建 Agent／Runtime，不授权发布、DBOS 公开或客户采用 |
| `ADR-022 / DQ-016` | `ACCEPTED_EXECUTION_AUTHORIZED`：只公开 exact public-safe wheel，DBOS 整仓保持 private | `decided_by_ref=zhangbin`；`DQ-016=PUBLISH_PUBLIC_SAFE_DBOS_WHEEL`；`WHOLE_DBOS_REPOSITORY_VISIBILITY=KEEP_PRIVATE` | 只授权精确 hash/bytes/source 的 GitHub Release asset；不授权整仓公开、PyPI、Runtime、Permission 或扩大 package 内容 |
| `ADR-022 / B-011` | `ACCEPTED_LIMITATION_FOR_V0_1`：接受 `PARTIAL_METADATA_ONLY` 作为 Developer Preview v0.1 的已披露发现限制 | `OPEN_WEB_LIMITATION=ACCEPT_PARTIAL_METADATA_ONLY_FOR_V0_1`；`decided_by_ref=zhangbin` | 不再阻塞 v0.1；不得写成规范名称或公开网络自然发现已经通过，后续仍可复查 |
| `ADR-022 / DQ-009` | `ACCEPTED_EXECUTION_AUTHORIZED`：批准 `Trusted Multi-Agent Infrastructure Developer Preview v0.1` 正式发布 | `released_by_ref=zhangbin`；2026-07-22T02:59:31+08:00 | 授权 GitHub Release、exact wheel 和百度云 formal deployment；只有执行和外部复验全部通过后才可记录为 `RELEASED` |
| `ADR-023 / DQ-017` | `ACCEPTED_ARCHITECTURE_BASELINE`：采纳 TMAP 协议化方向、OpenTelemetry 对齐的观察平面和有界生产就绪路线 | 2026-07-22 用户明确战略更新与“向生产级推进、重度参考 OpenTelemetry”；`decided_by_ref=zhangbin` | 允许在 DBA 定义协议、生产画像、SLO 和 gate；不授权 DBOS/SAEE 实施、Collector 部署、Production Runtime 或生产声明 |
| `ADR-024` | `ACCEPTED`：采纳 staged Telemetry production path | `ADR-024=ACCEPT_STAGED_TELEMETRY_PRODUCTION_PATH`；`decided_by_ref=zhangbin`；2026-07-22T12:05:04+08:00 | 只采纳 S0–S9 架构顺序；每阶段仍需独立证据和决定，不授权部署或生产流量 |
| `ADR-025 / DQ-022` | `ACCEPTED_REFERENCE_ADOPTION`：OTLP `v1.11.0` exact reference | `DQ-022=ADOPT_OTLP_1_11_0_REFERENCE_BASELINE`；`decided_by_ref=zhangbin`；2026-07-22T12:05:04+08:00 | 只采纳 external reference；不选择 SDK/Collector/Runtime，不把 conformance cases 写成已执行 |
| `ADR-026 / DQ-023` | `ACCEPTED_REFERENCE_ADOPTION`：core SemConv `v1.43.0` + pinned GenAI Development mapping | `DQ-023=ADOPT_OTEL_SEMCONV_1_43_CORE_AND_PINNED_GENAI_MAPPING`；`decided_by_ref=zhangbin`；2026-07-22T12:05:04+08:00 | 不创建 custom namespace，不把 telemetry mapping 写成 DBOS/SAEE canonical authority |
| `ADR-027 / DQ-024` | `ACCEPTED_REFERENCE_ADOPTION`：OTel Schema/Resource `v1.59` + Development Entity quarantine | `DQ-024=ADOPT_OTEL_SCHEMA_RESOURCE_1_59_AND_QUARANTINE_DEVELOPMENT_ENTITY`；`decided_by_ref=zhangbin`；2026-07-22T12:05:04+08:00 | OTel Entity 不成为 DBOS Digital Entity；不授权 runtime fetch、Registration、Evidence 或部署 |
| `ADR-028 / DQ-025` | `ACCEPTED_REFERENCE_ADOPTION`：Collector `v0.156.0` custom-minimal inventory | `DQ-025=ADOPT_OTEL_COLLECTOR_V0_156_CUSTOM_MINIMAL_INVENTORY`；`decided_by_ref=zhangbin`；2026-07-22T12:05:04+08:00 | 只采纳 8+2 architecture inventory；不构建 binary/image/config/listener，不授权 `DQ-020` |
| `DQ-018` | `ACCEPTED_IMPLEMENTED_SECURITY_REMEDIATED_NATIVE_REMOTE_ATTESTED_PR_G2A_HUMAN_REVIEW_READY_NOT_APPROVED`：DBOS PR-2A Telemetry Admission Foundation | `DQ-018=AUTHORIZE_DBOS_PR_2A_TELEMETRY_ADMISSION_FOUNDATION`；`dbos_domain_owner_ref=zhangbin`；source `ee90c0c…`；receipt `901bf0d…` | native Linux x86_64、DBOS remote receipt 与 DBA independent attestation 已通过；`HSR-PRE-001/002` closed；Human Security Review、Collector、listener、Evidence、Runtime、Permission 和生产声明仍未完成或未获授权 |
| `DQ-018 DBOS PR-2A Git action` | `AUTHORIZED_AND_EXECUTED`：security remediation source 与 native revalidation public-safe receipt commits 已非强制推送并远端 clean-clone 复验；`PR-G2A` 已 review-ready 但未批准 | predecessor Git authorization record；current source `ee90c0c84964f1f3e4dbeb8dffaf888f9822b6a5`；receipt `901bf0dda66e46f8b1c0b5873f5c5f20e9d03920`；manifest `306435cd…44fd9` | 不授权 PR、merge、main、release、deployment、Collector、DBOS Evidence 或 production claim；完整 PR-G2 仍为 false |
| `DBA production baseline Git action` | `AUTHORIZED`：允许当前 DBA 生产观测性基线 commit/push | `AUTHORIZE_DBA_PRODUCTION_BASELINE_COMMIT_AND_PUSH=true`；`target_branch=codex/production-observability-baseline`；`decided_by_ref=zhangbin` | 只允许当前 DBA scope；不自动授权 DBOS commit/push、PR、merge、deployment 或 release |

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
OPEN_DECISIONS=10
CONDITIONALLY_DECIDED_NOT_EFFECTIVE=0
QUEUE_CREATES_AUTHORITY=false
QUEUE_CREATES_PERMISSION=false
QUEUE_EXECUTES_DECISIONS=false
HUMAN_DECISION_READINESS_REGISTRY_DEFINED=true
HUMAN_DECISION_READINESS_REGISTRY_RECORDS_SUPPLIED_DECISIONS=true
HUMAN_DECISION_READINESS_REGISTRY_CREATES_DECISIONS=false
```
