---
document_id: TMAI-OTEL-COLLECTOR-DEPLOYMENT-READINESS-MATRIX-0.1
title: TMAI OpenTelemetry Collector Deployment Readiness Matrix v0.1
title_zh: TMAI OpenTelemetry Collector 部署就绪矩阵 v0.1
status: proposed-dq-020-input-no-runtime-effect
primary_repository: digital-biosphere-architecture
decision_reference: DQ-020
new_conformance_catalog_created: false
configuration_created: false
deployment_authorized: false
production_ready: false
---

# TMAI OpenTelemetry Collector Deployment Readiness Matrix v0.1

中文：TMAI OpenTelemetry Collector（开放遥测采集器）部署就绪矩阵 v0.1。

## 1. Purpose（目的）

本矩阵把机器可读的
[`opentelemetry-collector-deployment-profile.v0.1.json`](opentelemetry-collector-deployment-profile.v0.1.json)
映射到已经预注册的 conformance cases（符合性用例）、SLO（服务等级目标）和 production gates
（生产闸门）。它回答“未来具体部署必须证明什么”，不回答“当前是否已经部署”。

部署形状以外的运行证据语义由
[`opentelemetry-collector-operational-evidence-profile.v0.1.json`](opentelemetry-collector-operational-evidence-profile.v0.1.json)、
[strict Schema](schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json) 和
[operational evidence contract](opentelemetry-collector-operational-evidence-contract.md) 定义。两个画像都只
提供未来实现的失败关闭输入，不是 config、query、alert、runbook、measurement 或 Runtime。

本轮不新建第五套 Collector conformance catalog。部署画像复用四个彼此独立的现有目录：

| catalog | scope | required cases | executed now |
|---|---|---:|---:|
| `otlp-v1.11-conformance-cases.v0.1.json` | OTLP wire（线路）与 delivery（交付）语义 | 56 | 0 |
| `opentelemetry-semantic-conformance-cases.v0.1.json` | semantic mapping（语义映射） | 46 | 0 |
| `opentelemetry-schema-resource-conformance-cases.v0.1.json` | Schema / Resource / Entity provenance（来源） | 45 | 0 |
| `opentelemetry-collector-distribution-conformance-cases.v0.1.json` | build/config/runtime/security/durability/operations | 48 | 0 |

```text
Deployment profile != Collector configuration
Profile schema valid != Runtime conformance
Catalog reuse != Tests executed
Health OK != Readiness
WAL replay != End-to-end delivery
```

## 2. Official OpenTelemetry Constraints（OpenTelemetry 官方约束）

| official area | retained constraint | TMAI profile consequence |
|---|---|---|
| [Collector configuration](https://opentelemetry.io/docs/collector/configuration/) | 定义组件不等于在 `service.pipelines` 启用；processor 顺序具有语义 | compiled component 与 active component 分开；固定 `memory_limiter → transform → batch`，运行图必须与 approved graph 对账 |
| [Agent-to-gateway](https://opentelemetry.io/docs/collector/deploy/other/agent-to-gateway/) | 模式增加运维复杂度；无 stateful processing 时 gateway 可普通负载均衡；metric 仍须 single writer | edge tier 保留 optional；gateway 只在 `G3E` 进入，至少两个候选 replica；首个基线禁用 stateful processor |
| [Gateway pattern](https://opentelemetry.io/docs/collector/deploy/gateway/) | 多 Collector 可水平扩展，但 state-aware processing 要 affinity；metric stream 保持 single writer | baseline 不引入 tail sampling/load-balancing exporter；若未来增加，必须新决定和新用例 |
| [Resiliency](https://opentelemetry.io/docs/collector/resiliency/) | sending queue、WAL 和 message queue 均有不同失效与丢失条件 | 默认只提出 `Q1_FILE_WAL`；每 destination 独立 queue、每 replica 独占 WAL；明确禁止 exactly-once 与 `RPO=0` 声明 |
| [Internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/) | 内部 metrics/logs 可用于监控；internal trace 与声明式配置 schema 有稳定性限制 | internal metrics/logs 必须有独立失败路径；internal traces 从首个基线排除；内部 schema 版本必须绑定 |
| [Configuration security](https://opentelemetry.io/docs/security/config-best-practices/) | secret 应安全存储；通信应加密认证；减少组件；绑定受限接口；资源限制需显式设计 | 仅 `file/env` providers；无 remote config/OpAMP；`0.0.0.0` 禁止作为默认；non-root、最小组件、secret references、DoS 负例为必需 |
| [Hosting security](https://opentelemetry.io/docs/security/hosting-best-practices/) | 最小权限、目录保护、受限 server-like components 和资源自观测 | 仅 WAL 路径可写、无 privileged host access、listener/network policy 明确、容量和资源耗尽必须直接验证 |

这些引用是 design input（设计输入），不是 OpenTelemetry 对 TMAI 的认证，也不证明具体部署安全。

## 3. Profile-to-case Reuse Matrix（画像到现有用例复用矩阵）

| profile domain | exact profile rule | existing required cases / groups | gate binding | current result |
|---|---|---|---|---|
| Decision and version binding | `DQ-018/019/022/023/024/025` 均独立；`DQ-020` 仍 `BLOCKED_INPUT` | `ODC-CG-AUTHORITY`、`ODC-CF-AUT-002`–`004` | `PR-G0`, `PR-G3`, `PR-G7` | `NOT_ASSESSED` |
| Distribution source/build | exact `v0.156.0@aa158b23...`，无 binary/image/SBOM | `ODC-CG-SOURCE` 7 cases | `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Component activation | 8 compiled candidates；未进入 pipeline 即 inactive | `ODC-CG-ALLOWLIST` 7 cases | `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Config source and providers | 单一本地 reviewed root；仅 `file/env`；remote/OpAMP=false | `ODC-CF-ALL-006`, `ODC-CF-CFG-001`, `002`, `008` | `G3A`–`G3F`, `PR-G3` | `NOT_EXECUTED` |
| Processor order | `memory_limiter → transform → batch` | `ODC-CF-CFG-003` | `G3B`–`G3F`, `PR-G3` | `NOT_EXECUTED` |
| Transform activation | `G3D` synthetic transport 前禁用；`G3E` 前须通过 CFG 004/005/006 | `ODC-CF-CFG-004`–`006`; semantic sensitive/authority groups; OSR transform group | `G3D`, `G3E`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Listener scope | `G3D` exact loopback；公网和 unspecified address 均禁止 | `ODC-CF-SEC-002`, `005`, `007`; OTLP deployment security/capacity group | `G3D`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Authentication and identity | TLS + mTLS/equivalent workload identity；不将 cert/Resource 变成 DBOS Identity | `ODC-CF-SEC-002`, `003`; `ODC-CG-AUTHORITY`; OTLP/semantic/OSR authority groups | `G3D`–`G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Receiver limits | bytes、decompressed bytes、items、rate、connection、concurrency、timeout 均须 exact | `ODC-CF-CFG-006`, `ODC-CF-SEC-005`; OTLP gRPC/HTTP size groups | `G3D`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Tenant isolation | baseline single tenant；cross-tenant batch/queue/WAL 禁止 | `ODC-CF-CFG-007`, `ODC-CF-SEC-002`, `004`, `006`; OSR data-governance group | `G3E`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Queue and WAL | per destination queue/retry；per replica exclusive WAL；无 shared writer | `ODC-CG-DURABILITY` 6 cases | `G3C`, `G3E`, `G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Delivery accounting | success/partial/retry/drop/unknown/duplicate 全部保留 | OTLP retry/partial and delivery reconciliation groups；`ODC-CF-DUR-005`, `006` | `G3F`, `PR-G3` | `NOT_EXECUTED` |
| HA topology | gateway >=2 only at `G3E`；failure domain/LB 尚未选定；stateful processor=false | `ODC-CF-CAP-002`, `003`; `ODC-CF-DUR-004`; OTLP deployment group | `G3E`, `G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Metric single writer | scale/failover/mixed-version 时仍须唯一 writer identity | OTLP deployment group；`ODC-CF-CAP-002`, `003` | `G3E`, `PR-G3` | `NOT_EXECUTED` |
| Self-observation | 独立 metrics/logs；internal traces disabled；health 仅 Alpha liveness signal；12 类 observation 与 6 类 SLI 均须 exact binding | `ODC-CG-OPERABILITY` 5 cases；`ODC-CF-SEC-007`；operational evidence profile | `G3E`, `G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Metric naming/stability | OTLP canonical names 与 Prometheus projection、views、verbosity、per-instrument stability、Collector version 分开绑定 | `ODC-CF-OPS-001`, `003`, `005`; `ODC-CF-CAP-001` | `G3E`, `G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Alert/runbook delivery | warning/critical、multi-window、no-data、route、delivery test、clock 和 critical runbook 全部有 exact digest | `ODC-CF-OPS-003`–`005`; `ODC-CF-CAP-004` | `G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Runtime confinement | non-root、read-only root、drop capabilities、仅 WAL writable | `ODC-CF-SEC-001`, `004`; `ODC-CF-DUR-003`, `004` | `G3D`–`G3F`, `PR-G5` | `NOT_EXECUTED` |
| Capacity | exact workload 未选；必须 1x/2x/5x 并测首个 refusal/drop | `ODC-CG-CAPACITY_HA` 4 cases | `G3E`, `G3F`, `PR-G3`, `PR-G5` | `NOT_EXECUTED` |
| Change/rollback | desired/running digest 对账；canary、drain、exact prior rollback；失败历史保留 | `ODC-CF-CFG-008`, `ODC-CF-OPS-004`, `005` | `G3E`, `G3F`, `PR-G5` | `NOT_EXECUTED` |
| Authority separation | Collector/OTLP 不创建 Identity/Evidence/Permission，不关闭 gate | `ODC-CG-AUTHORITY`; OTLP/semantic/OSR authority/result groups | all gates | `NOT_EXECUTED` |

三个容易被误读的边界补充如下：

1. `stateful_processors_allowed=false` 指跨 request（请求）的 tail sampling、aggregation 或
   data-aware routing state；per-exporter queue 和 per-replica WAL 是唯一允许的本地 transport state，
   仍不共享、不形成共识，也不成为 DBOS canonical state；
2. 首个基线不编译 authentication extension（认证扩展）。`G3D` 只允许 Collector receiver 原生
   TLS/mTLS 与外部 network/source policy 的候选组合；如果 exact tenant identity 需要 OIDC、bearer
   或其他 extension，必须先修改 `DQ-025` inventory，不能从本文档隐式获得；
3. 禁止 remote config/OpAMP 不是缺失一个隐藏控制面。v0.1 的唯一更新机制是 immutable,
   versioned configuration（不可变、版本化配置）经 static/security/synthetic gates、canary、滚动重启和
   exact digest rollback；任何未来动态控制面须独立决定。

### Composite readiness floor（组合就绪下限）

外部 deployment controller（部署控制器）的 readiness 最少同时要求：process running、approved
config digest match、认证 listener 在批准范围内接受、queue utilization 低于 critical threshold、WAL
可写且未超 quota、必要 exporter 在 outage budget 内可达、self-telemetry fresh、无 blocking config/
security drift。Alpha `health_check` 只能贡献 liveness signal，不能替代上述谓词。

exact threshold、window、query 和 failure action 仍是 `DQ-020` 输入；它们为空时 readiness 必须 fail closed，
不得用默认值或 `200 OK` 补齐。

### Staging input gate（试运行输入闸门）

`G3D/G3E` 在 production traffic 获得独立授权前只接收有 immutable fixture reference、fixture digest、
source identity、purpose=`CONFORMANCE` 和 retention policy 的批准 synthetic fixture（合成样本）。
缺标签、来源不在 allowlist、purpose 不符或 real-customer-data canary 命中时，listener 必须拒绝并只
保留 bounded non-secret diagnostic（有界非秘密诊断）。该要求是未来 runtime test obligation，本文档
没有创建 enforcement implementation（执行实现）。

## 4. Stage Freeze Contract（阶段冻结契约）

| stage | may freeze | must remain absent | exit evidence |
|---|---|---|---|
| Architecture review | profile/schema/matrix | config、listener、image、runtime、data | JSON Schema + consistency + human review input |
| `G3A`–`G3C` | offline decoder/admission/persistence bindings | network listener、Collector traffic | DQ-018/019 scoped evidence；OTLP offline cases |
| `G3D` | exact loopback listener/config/build/runtime for synthetic traffic | gateway/public ingress/real customer data/Evidence creation | auth/limit/secret/size/rollback negative cases |
| `G3E` | exact gateway replicas/failure domains/LB/queue/WAL/capacity | public ingress/production traffic | 48/48 distribution + required OTLP/semantic/OSR cases and independent review |
| `G3F` | delivery accounting and failure reconciliation | exactly-once/RPO0/Truth claims | emitted-to-terminal accounting + retained unknown/duplicate/loss |
| `PR-G7` | deployment-specific Human Decision | global or platform-independent production claim | all scoped gates + residual risk acceptance |

后续真实 configuration（配置）必须存在于明确的 deployment repository（部署仓库），而不是 DBA。
DBA 只维护 normative profile（规范画像）和 evidence contract（证据合同）。

机器画像中的 `effects.*` 永远保持 `false`；未来 build/config/deployment result 是独立工件，不通过把
本架构画像中的 effects 改成 `true` 来表示推进。

## 5. DQ-020 Readiness Gaps（DQ-020 就绪缺口）

两个机器画像把抽象缺口转为 18 个可审查输入，但当前仍全部未关闭：

1. `DQ-018` Human Decision 和实施证据；
2. `DQ-019` persistence decision（持久化决定）及直接证据；
3. `DQ-022`–`DQ-025` 四个独立架构决定；
4. Collector Platform Owner（采集器平台负责人）；
5. deployment repository；
6. exact build/image/SBOM/provenance/signature/vulnerability digests；
7. exact configuration/runtime/environment digests；
8. exact failure domains、load balancer 和 network policy；
9. exact identity/certificate/secret references；
10. exact receiver、memory、batch、queue、WAL、outage、retention 和 capacity budgets；
11. self-telemetry destination、alert thresholds 和 runbooks；
12. rollback artifacts；
13. 56/56 OTLP direct results；
14. 46/46 semantic direct results；
15. 45/45 Schema/Resource/Entity direct results；
16. 48/48 Collector distribution direct results和独立 technical/security review；
17. exact metric stability/naming/Resource/query/threshold/alert/route/runbook bundle digests；
18. independent self-telemetry/blackbox/storage/drift、no-data/alert-delivery 和端到端对账直接结果。

因此本轮只把 `B-016` 从“没有部署契约”收敛为“契约已定义，具体责任人、制品、配置、运行和证据仍缺失”；不得把 `DQ-020` 升级为 `READY_FOR_REVIEW`。

## 6. Current Truth（当前事实）

```text
COLLECTOR_DEPLOYMENT_PROFILE_DEFINED=true
COLLECTOR_DEPLOYMENT_PROFILE_SCHEMA_VALIDATION_REQUIRED=true
COLLECTOR_OPERATIONAL_EVIDENCE_PROFILE_DEFINED=true
COLLECTOR_OPERATIONAL_EVIDENCE_PROFILE_SCHEMA_VALIDATION_REQUIRED=true
COLLECTOR_OPERATIONAL_EVIDENCE_PROFILE_NEGATIVE_CONTROLS=45/45
NEW_COLLECTOR_CONFORMANCE_CATALOG_CREATED=false
DQ_020_STATUS=BLOCKED_INPUT
COLLECTOR_PLATFORM_OWNER_ASSIGNED=false
DEPLOYMENT_REPOSITORY_SELECTED=false
CONFIGURATION_CREATED=false
LISTENER_OPENED=false
COLLECTOR_DEPLOYED=false
REAL_TRAFFIC_ALLOWED=false
RUNTIME_CASES_EXECUTED=0
OPERATIONAL_MEASUREMENT_STARTED=false
OPERATIONAL_EVIDENCE_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
