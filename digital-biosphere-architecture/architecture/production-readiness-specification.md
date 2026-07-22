---
spec_id: TMAI-PRODUCTION-READINESS-0.1
title: TMAI Production Readiness Specification v0.1
title_zh: TMAI 生产就绪规范 v0.1
status: accepted-non-executable-production-readiness-baseline
decision_reference: ADR-023-trusted-multi-agent-protocol-and-production-observability.md
decided_by_ref: zhangbin
primary_repository: digital-biosphere-architecture
production_ready: false
implementation_authorized: false
deployment_authorized: false
runtime_created: false
---

# TMAI Production Readiness Specification v0.1

## 1. Readiness Claim Boundary（就绪声明边界）

Production Ready（生产就绪）是针对 exact version、deployment profile、environment 和 declared workload（声明负载）的证据结论，不是对 Digital Biosphere 整个项目群的永久标签。

```text
Developer Preview != Production Ready
Release != Deployment
Deployment != Adoption
Telemetry != Evidence != Truth
Specification != Implementation
```

## 2. First Production Profile（首个生产配置）

v0.1 推荐但尚未实现的首个目标是：

```text
profile_id=TMAI-SELF-HOSTED-SINGLE-TENANT-1
hosting=self-hosted
tenancy=single-tenant
governance=human-governed
evidence_policy=provenance-preserving-fail-closed
dbos_role=existence-and-record-authority
saee_role=read-only-evaluation-and-recommendation
automatic_permission_escalation=false
automatic_evolution_execution=false
```

多租户 SaaS、跨区域联邦、金融或医疗高影响动作不属于首个 Production Profile。

## 3. Production Readiness Lifecycle（生产就绪生命周期）

```text
ARCHITECTURE_BASELINE
  → IMPLEMENTATION_AUTHORIZED
  → IMPLEMENTED
  → CONFORMANCE_PASS
  → SECURITY_AND_RECOVERY_PASS
  → BOUNDED_PILOT_PASS
  → PRODUCTION_AUTHORIZED
  → PRODUCTION_DEPLOYED
  → CONTINUOUSLY_OBSERVED

Side states:
REJECTED | REVOKED | ROLLED_BACK | DEGRADED | UNKNOWN
```

任何后续状态不能仅由测试数量、文档、模型推荐、Release 或单次 Demo 推导。

## 4. Required Production Domains（生产必需领域）

| 领域 | 必须证明 | 最小证据 |
|---|---|---|
| Architecture | 部署画像、Owner、对象、边界、失败和版本明确 | 本规范、TMAP、OTel Profile、ADR、兼容声明 |
| DBOS Durability | Identity、Lifecycle、Execution、Evidence、Verification 记录可持久化、幂等、迁移和恢复 | [`production-persistence-adapter-specification.md`](production-persistence-adapter-specification.md)、schema/migration tests、HA/PITR、replay protection、backup/restore drill |
| Authorization | Capability、Authorization、Permission、Execution 严格分离 | 正负权限测试、revocation、expiry、least privilege |
| Observability | Trace/Metric/Log、Context、Collector 和数据缺口可见；自观测、blackbox、storage、drift 和 delivery source 独立 | [`opentelemetry-production-alignment-matrix.md`](opentelemetry-production-alignment-matrix.md)、[`otlp-collector-production-profile.md`](otlp-collector-production-profile.md)、[`opentelemetry-collector-operational-evidence-contract.md`](opentelemetry-collector-operational-evidence-contract.md)、OTel conformance、HA/failover、drop/partial/retry/no-data evidence、alert/runbook drills |
| Evidence Integrity | Telemetry admission 与 Evidence admission 分离，来源、重复、顺序、采样、身份和 Verification 边界明确 | [`telemetry-to-evidence-admission-contract.md`](telemetry-to-evidence-admission-contract.md)、intake/admission records、provenance/attestation、integrity checks、failure retention |
| SAEE Isolation | 只读消费、版本契约、失败隔离和 advisory-only 输出 | contract tests、timeout/fallback、zero writeback checks |
| Reliability | SLO、容量、过载、故障、恢复和回滚经验证 | load/soak/fault tests、RTO/RPO drill、runbooks |
| Security | 威胁模型、身份、秘密、供应链、Collector 和数据隐私经审查 | threat model、SBOM、signed artifact、scan、independent review |
| Operations | 明确 Owner、on-call、告警、事故响应和变更管理 | [`production-gate-evidence-manifest-specification.md`](production-gate-evidence-manifest-specification.md)、runbooks、alerts、incident and rollback exercises |
| Adoption | 有界真实工作流达到预冻结指标 | pilot record、limitations、human production decision |

## 5. Responsibility Routing（责任路由）

| 工作 | Primary repository | DBA gate |
|---|---|---|
| Production profile、协议、SLO 和 release claim | DBA | Architecture/Production Decision |
| DBOS 持久化、身份、执行记录、Evidence、Verification、OTel intake | DBOS | Implementation Mapping + Conformance |
| SAEE 生产 Adapter、Evaluation SLO 与 writeback prohibition | SAEE | Read-only Contract Conformance |
| Collector/Backend deployment manifests | deployment-specific infrastructure repository | Security/Operations Review |
| Digital Entity task instrumentation | Digital Entity/Application repository | Entity-specific Admission and Capability Review |

DBA 不实现 Collector、DBOS 或 SAEE；跨项目推进必须按 primary repository 分开实施和验证。

## 6. Production Gates（生产闸门）

### PR-G0 Architecture Baseline

TMAP、OTel Profile、Production Profile、SLO、threat boundaries 和 ADR 完整；`DQ-022`
OTLP、`DQ-023` semantic mapping、`DQ-024` Schema/Resource/Entity provenance 与 `DQ-025`
Collector distribution 分别有 exact
source、conformance contract 和 Human Decision。智能体推荐只允许进入人工审查。

### PR-G1 Implementation Mapping

每个规范字段映射到现有或候选实现；缺失、重复权威和 unsupported fields 明确。未通过不得开始生产集成声明。

### PR-G2 DBOS Core Conformance

持久化、幂等、状态转换、授权、失败保留、Evidence/Verification、semantic trusted binding、
Schema/Resource provenance、Development Entity quarantine、data governance 和版本迁移正负例通过。

### PR-G3 OTel Observability Conformance

OTLP、Resource、Context、Trace/Metric/Log、Collector exact source/build/config/runtime/failure、Schema source/cache/transform、
Resource detector/merge、OTel Entity quarantine、敏感数据、重复、丢弃和 sampling 边界通过；
56/56 OTLP、46/46 semantic、45/45 provenance 与 48/48 Collector distribution results 独立绑定。`DQ-020` 另以
[`opentelemetry-collector-deployment-profile.v0.1.json`](opentelemetry-collector-deployment-profile.v0.1.json)
和 [`opentelemetry-collector-deployment-readiness-matrix.md`](opentelemetry-collector-deployment-readiness-matrix.md)
绑定 exact deployment profile（精确部署剖面）、synthetic-only input gate（仅合成输入闸门）、immutable rollout（不可变发布）与 composite readiness（复合就绪性）；它复用四套结果，不构成第五套符合性目录。
[`opentelemetry-collector-operational-evidence-profile.v0.1.json`](opentelemetry-collector-operational-evidence-profile.v0.1.json)
另行约束 internal metric/log、instrument naming/stability、12 类 observation、6 类 derived SLI、
counter reset/no-data/mixed-version、独立 self-observation、blackbox/storage/drift、alert/route/runbook 和
端到端 delivery reconciliation。其 exact 值当前故意为 `null` 并失败关闭，不能阻断规范审查，但必须
阻断实现、测量、部署和本 gate 关闭。

### PR-G4 SAEE Isolation Conformance

只读数据交换、timeout、unsupported version、conflicting assessment 和 zero direct writeback 通过。

### PR-G5 Security and Recovery

威胁模型、供应链、秘密、访问控制、备份恢复、灾难恢复、回滚与故障注入通过；Collector no-data、
alert delivery、route 和 critical runbook drill 直接通过；Critical/High 未处置风险为零。

### PR-G6 Bounded Production Pilot

在已批准的低风险 workload 上完成连续观察期，达到 [`production-slo-and-evidence-gates.md`](production-slo-and-evidence-gates.md) 的指标，并保留所有失败和人工干预。

### PR-G7 Production Authorization

Human Production Authority 复核 exact artifact、environment、SLO、风险、pilot、runbooks 和 rollback，形成 deployment-specific Decision。Decision 仍不等于 Deployment。

## 7. Agent Recommendation Gate（智能体推荐闸门）

2026-07-22，Ark `deepseek-v4-flash-260425` 与 Qianfan `ernie-4.5-turbo-128k` 对同一生产观测方案均返回 `CONDITIONALLY_RECOMMENDED`。

共同认可：

- OTel 协议、Resource、Context、Signals 和 Collector 解耦适合 TMAI；
- `Telemetry ≠ Evidence ≠ Truth` 与 Collector 非权威边界正确；
- DBA/DBOS/SAEE 分离适合长期治理。

共同阻塞：

- GenAI Semantic Conventions 仍需版本钉住和迁移路径；
- Telemetry→Evidence 接纳、差异处理和完整性必须正式定义；
- DBOS 故障恢复、SLO 和容量行为未验证；
- 身份、能力和证据边界需要安全审计与真实运行证据。

本规范已把这些问题映射到 `PR-G1` 至 `PR-G6`。推荐结论不授权实现、部署或生产声明。完整记录见 [`../PRODUCTION-READINESS-AGENT-RECOMMENDATION.md`](../PRODUCTION-READINESS-AGENT-RECOMMENDATION.md)。

## 8. Stop and Rollback Rules（停止与回滚规则）

出现以下任一情况必须停止进入下一 gate：

- 身份、Permission 或授权链缺失；
- acknowledged canonical record（已确认规范记录）无法恢复；
- telemetry drop/partial/sampling 被隐藏；
- 敏感内容默认进入 telemetry；
- SAEE 直接写回或 Recommendation 被当作 Command；
- Collector/Backend 被当作 Evidence Truth 或 Verification Authority；
- Collector tag/source/component/build/config/runtime drift 未被识别，或 health/startup 被当作 gate pass；
- Collector metric 缺失／改名／stale 被 zero-fill，counter reset 或 mixed version 被静默聚合；
- self-telemetry 与主 exporter 共享不可观察失败路径，或 alert no-data/route/runbook 未经直接演练；
- GenAI 语义版本漂移未被识别；
- Critical/High 风险未修复或没有显式、限时风险接受；
- rollback 或 restore drill 失败；
- 真实 pilot 未达到预冻结 SLO。

## 9. Current State（当前状态）

```text
PRODUCTION_READINESS_SPECIFICATION_DEFINED=true
FIRST_PRODUCTION_PROFILE_DEFINED=true
PRODUCTION_IMPLEMENTATION_MAPPING_COMPLETE=true
PR_G1_READ_ONLY_MAPPING_PASS=true
PRODUCTION_IMPLEMENTATION_SEQUENCE_DEFINED=true
PRODUCTION_PATH_AGENT_REVIEW_COMPLETE=true
PRODUCTION_IMPLEMENTATION_SEQUENCE_RECOMMENDED_BY_TWO_AGENTS=true
DQ_024_STATUS=DECIDED_REFERENCE_ADOPTED
OTEL_SCHEMA_RESOURCE_ENTITY_REFERENCE_ADOPTED=true
OTEL_SCHEMA_RESOURCE_ENTITY_CONFORMANCE_TESTS_EXECUTED=0
DQ_025_STATUS=DECIDED_REFERENCE_ADOPTED
OTEL_COLLECTOR_DISTRIBUTION_ADOPTED=false
OTEL_COLLECTOR_DISTRIBUTION_BUILT=false
OTEL_COLLECTOR_DISTRIBUTION_CONFORMANCE_TESTS_EXECUTED=0
OTEL_COLLECTOR_OPERATIONAL_EVIDENCE_PROFILE_DEFINED=true
OTEL_COLLECTOR_OPERATIONAL_EVIDENCE_AGENT_REVIEW_COMPLETE=true
OTEL_COLLECTOR_OPERATIONAL_MEASUREMENT_STARTED=false
OTEL_COLLECTOR_OPERATIONAL_EVIDENCE_CREATED=false
PRODUCTION_PERSISTENCE_BACKEND_SELECTED=false
OTLP_COLLECTOR_DEPLOYMENT_AUTHORIZED=false
EVIDENCE_ADMISSION_AUTHORIZED=false
DBOS_PRODUCTION_CONFORMANCE_PASS=false
OTEL_PRODUCTION_CONFORMANCE_PASS=false
SAEE_PRODUCTION_CONFORMANCE_PASS=false
SECURITY_AND_RECOVERY_PASS=false
BOUNDED_PRODUCTION_PILOT_PASS=false
PRODUCTION_AUTHORIZED=false
PRODUCTION_DEPLOYED=false
PRODUCTION_READY=false
```
