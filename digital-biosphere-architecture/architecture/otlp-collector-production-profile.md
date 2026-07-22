---
spec_id: TMAI-OTLP-COLLECTOR-PRODUCTION-PROFILE-0.1
title: TMAI OTLP and Collector Production Profile v0.1
title_zh: TMAI OTLP 与 Collector 生产配置 v0.1
status: proposed-pending-dq-020-not-deployed
primary_repository: deployment-specific-infrastructure-repository
architecture_owner: digital-biosphere-architecture
collector_distribution_selected: false
listener_authorized: false
collector_deployed: false
telemetry_collected: false
production_ready: false
---

# TMAI OTLP and Collector Production Profile v0.1

中文：TMAI OTLP 与 Collector 生产配置 v0.1。

## 1. Purpose（目的）

本配置定义 `TMAI-SELF-HOSTED-SINGLE-TENANT-1` 在 `DQ-018` Telemetry Admission Foundation 之后，如何建立可维护、可审计、可观测、有界丢失的 OTLP/Collector transport plane（传输平面）。

本文件重度参考 OpenTelemetry 官方：

- [OTLP Specification](https://opentelemetry.io/docs/specs/otlp/)；
- [Collector deployment patterns](https://opentelemetry.io/docs/collector/deploy/)；
- [Agent-to-gateway pattern](https://opentelemetry.io/docs/collector/deploy/other/agent-to-gateway/)；
- [Gateway pattern](https://opentelemetry.io/docs/collector/deploy/gateway/)；
- [Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/)；
- [Collector internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)；
- [Collector scaling](https://opentelemetry.io/docs/collector/scaling/)；
- [Collector hosting security](https://opentelemetry.io/docs/security/hosting-best-practices/) 和 [configuration security](https://opentelemetry.io/docs/security/config-best-practices/)。

引用官方指导不表示已部署、已符合或获得 OpenTelemetry 认证。

Exact test contract（精确测试合同）由 [`otlp-v1.11-conformance-profile.md`](otlp-v1.11-conformance-profile.md) 与 [`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json) 预注册。该目录中 `DEPLOYMENT_TRANSPORT`、`END_TO_END_RECONCILIATION` 和 deployment security/capacity cases 必须在 `DQ-020` 授权后执行；目录存在不表示 Collector 已选择、已部署或已符合。

具体 staging candidate（试运行候选）的 topology/config/security/capacity 空位和 fail-closed defaults
由 [`opentelemetry-collector-deployment-profile.v0.1.json`](opentelemetry-collector-deployment-profile.v0.1.json)
与 [`opentelemetry-collector-deployment-readiness-matrix.md`](opentelemetry-collector-deployment-readiness-matrix.md)
定义。机器画像不是 Collector YAML、deployment manifest（部署清单）或 `DQ-020` Authorization。

## 2. Hard Boundaries（硬边界）

```text
Collector Agent != AI Agent
OTLP Acknowledgement != End-to-end Delivery
Collector Queue != DBOS Canonical Store
Collector Processing != Evidence Admission
Sampling != Complete Execution History
Trace Context != Identity or Authorization
Collector Health != System Trust
```

Collector 是 observation transport/processing component（观测传输/处理组件），不得创建 Identity、Permission、Evidence、Verification、Fitness、Decision 或 Agent。

## 3. Standards and Artifact Pinning（标准与制品锁定）

| surface | architecture baseline | deployment requirement |
|---|---|---|
| OTel Specification | `1.59.0` | 记录实际对齐版本和 stability |
| OTLP | candidate `v1.11.0@790608c...` | `DQ-022` 待决；Trace/Metric/Log Stable；Profiles rejected in v0.1；reference adoption 不等于 Collector/SDK selection |
| Semantic Conventions | `1.43.0` | 每个 Resource/Scope 保留 exact schema URL |
| Collector distribution | `DQ-025` candidate only: custom-minimal `v0.156.0@aa158b23...` | [exact inventory](opentelemetry-collector-component-inventory.v0.1.json) 与 [distribution profile](opentelemetry-collector-distribution-profile.md)；尚未采纳、构建或选择 image |
| Collector configuration | not created | normalized configuration digest + secret-free reviewed source |

`latest`、floating tag 或只有 image name 不能进入 staging/production gate。Collector 组件的 stability 必须逐个登记，不能因 core Collector 可用而推断 receiver/processor/exporter/extension 均稳定。

`DQ-025` 只决定是否采纳 architecture component inventory。即使采纳，也必须由独立的
`DQ-020` implementation/deployment authorization 绑定 build repository、Owner、OCB/module lock、
binary/image/SBOM/license/provenance/signature/vulnerability/config/runtime digests，并用
[48-case distribution catalog](opentelemetry-collector-distribution-conformance-cases.v0.1.json)
形成 48/48 的 case-level result。官方 release tag、prebuilt distribution、health endpoint 或
Collector 启动成功均不能替代这条证据链。

## 4. Target Topology（目标拓扑）

```text
Instrumented Digital Entity / Service
  ├─ evidence-critical direct DBOS record path (not sampled)
  └─ OTLP over authenticated TLS
       ↓
Local Collector Agent / Sidecar tier
  ↓ OTLP over authenticated internal TLS + bounded queue/WAL
Gateway Collector tier (>=2 candidate replicas)
  ├─ Observability backend branch
  └─ DBOS Telemetry Transport Adapter branch
       ↓
Telemetry Observation Envelope
       ↓
Telemetry Admission Record
       ↓ separate Evidence Admission Contract
Canonical Evidence Object + independent Verification Object
       ↓ read-only
SAEE Evaluation / Recommendation
```

Agent-to-gateway 模式是首个生产候选，但小规模 deployment 可经人工决策采用 gateway-only。拓扑变化必须重跑 load、failure、security 和 delivery accounting tests。

机器画像把 edge Collector tier 保持为 `OPTIONAL_NOT_SELECTED`。`G3D` 只允许显式 loopback 的
synthetic transport；`G3E` 才允许在 prior gates 通过后冻结 gateway replicas/failure domains/LB。
这里的 Collector Agent 只是 OpenTelemetry 的本地 Collector 模式，不是 Digital Entity 或 AI Agent。

## 5. Pipeline Classes（管道类别）

| pipeline | purpose | sampling | persistence | authority |
|---|---|---|---|---|
| `diagnostic_traces` | latency/error/correlation | head/tail sampling allowed with explicit policy | Collector queue/WAL + backend | observation only |
| `operational_metrics` | SLI/capacity/health | aggregation allowed；single-writer required | queue/WAL + metrics backend | observation only |
| `operational_logs` | bounded diagnostics | filtering/redaction required | queue/WAL + log backend | observation only |
| `dbos_admission_material` | selected metadata-only provenance material | no hidden probabilistic sampling | queue/WAL then Telemetry Admission | material only; not Evidence |
| `evidence_critical_records` | governed lifecycle/execution/evidence-critical facts | OTel pipeline prohibited as sole path | direct DBOS canonical persistence | DBOS contract only |

不得把 `dbos_admission_material` 和 `evidence_critical_records` 合并成同一采样管道。

## 6. Receiver Boundary（接收器边界）

生产候选必须：

- 显式启用 OTLP/gRPC 和/或 OTLP/HTTP，未启用的 protocol 不监听；
- default bind 收紧到 required interface，不以 `0.0.0.0` 作为无审查默认；
- mTLS 或等价 workload identity + receiver authentication；
- connection、request bytes、decompressed bytes、items、depth、concurrency、rate 和 timeout 有硬上限；
- gzip/no-compression 按 OTLP 要求支持，解压前后都有 budget；
- 若 `DQ-022` 采纳 `v1.11.0` reference，deployment profile 必须分别声明 gRPC/HTTP 的 request/response、inbound/outbound、pre-compression/post-decompression limit；recommended baseline 为 request `64 MiB`、response `4 MiB`，任何偏离必须有 capacity/security rationale；
- gRPC request 超限使用 non-retryable `RESOURCE_EXHAUSTED`，HTTP request 超限使用 `413`；response 超限、diagnostic truncation 和 acceptance unknown 必须进入 retained failure/limitation record，不能静默重试；
- `Retry-After` parser 必须支持 HTTP-date 与 delay-seconds，并对 clock skew、invalid、expired 和 excessive delay fail closed；
- permanent bad data 返回 non-retryable outcome，不得用 5xx 诱导重试；
- partial success 的 rejected item count 和 bounded diagnostic 完整记录；
- receiver acknowledgement 只表示当前 client/server hop 的 outcome。

上述每一项必须通过 machine catalog 中的 `OTLP-CG-GRPC_SIZE`、`OTLP-CG-HTTP_SIZE`、`OTLP-CG-RETRY_PARTIAL` 和 `OTLP-CG-DEPLOYMENT_SECURITY_CAPACITY` exact cases；只运行 Collector 自带 smoke test 不满足 `PR-G3`。

## 7. Processor Order and Policy（处理器顺序与策略）

候选逻辑顺序：

```text
receiver authentication / transport limits
  → memory/resource limiter
  → schema and signal allowlist
  → sensitive attribute deny/allowlist + redaction
  → resource/scope normalization without identity promotion
  → routing and optional diagnostic sampling
  → bounded batching
  → per-destination queue/retry/export
```

每个 processor 必须记录 component version、configuration digest、drop/error counters 和 known semantic changes。Transform 不得伪造 provenance，redaction 不得将“已删除”改写成“从未存在”。

## 8. Delivery, Retry and Duplicate Matrix（交付、重试与重复矩阵）

| condition | sender action | DBOS limitation |
|---|---|---|
| full OTLP success | dequeue for that destination | hop accepted only |
| populated partial success | do not retry rejected subset automatically | accepted/rejected counts + diagnostic |
| HTTP 400 permanent bad data / equivalent | no retry | `REJECTED_PERMANENT` |
| 429/502/503/504 or retryable gRPC | exponential backoff + jitter + bounded elapsed time | `RETRYING` then terminal outcome |
| disconnect/no acknowledgement | retry allowed; duplicate possible | `UNKNOWN_DELIVERY` + duplicate assessment |
| queue full | explicit drop/reject according to signal policy | `DROPPED_QUEUE_FULL` |
| retry elapsed | terminal drop | `DROPPED_RETRY_EXHAUSTED` |
| Collector crash with memory queue | in-memory items may be lost | loss limitation mandatory |
| Collector crash with WAL | replay after restart; duplicate possible | WAL recovery + duplicate limitation |
| multi-destination | independent queue/ack/retry per destination | one backend success cannot imply other success |

## 9. Queue and Durability Classes（队列与耐久等级）

| class | use | required proof |
|---|---|---|
| `Q0_MEMORY` | low-value diagnostics only | queue overflow/drop visible; restart loss accepted |
| `Q1_FILE_WAL` | gateway/agent selected material | disk budget、permissions、restart replay、corruption/full disk、retention |
| `Q2_MESSAGE_QUEUE` | critical cross-zone/network decoupling candidate | broker HA、retention、producer ack、consumer offset、poison message、cost/operations |

OpenTelemetry 官方指出 sending queue 和 retry 仍可在 queue full、retry timeout、disk failure 时丢数据；message queue 提高耐久性但增加运维复杂度。因此 queue class 必须由 workload criticality 和 measured outage budget 选择，不得一律称为 reliable delivery。

## 10. Scaling and Single-writer（扩展与单写者）

- gateway 横向扩展前必须知道哪些 processor 是 stateful；
- tail sampling 或 trace-level state 要求 trace-aware routing，否则不得声称完整追踪；
- metric stream 必须遵守 single-writer principle（单写者原则），Resource/stream identity 必须全局唯一；
- HPA 或自动扩展指标不只看 CPU，至少包含 queue utilization、refused/dropped items、export latency、memory 和 backend saturation；
- scale-in 必须 drain queue、限时等待 acknowledgement，并记录未交付数量；
- 负载均衡、DNS 更新、gateway restart 和版本混跑必须直接测试。

### 10.1 Gateway HA and Failover（Gateway 高可用与故障切换）

`P2` 生产候选至少必须定义：

- 每个声明 failure domain 至少 2 个 gateway replicas，并使用 anti-affinity/topology spread 或等价隔离；
- load balancer 只向 readiness pass 的 replica 发送新请求，readiness 必须考虑 queue saturation 和 exporter health；
- scale-in/upgrade 先摘流、再 drain，限时后明示记录 undelivered items；
- 每个 replica 使用自己的 WAL，禁止多个 Collector 并发写同一 file-storage directory；
- tail sampling 等 stateful processor 使用 OTel load-balancing exporter 按 trace ID 路由或经证明等价机制；这是 OTel 官方 gateway 模式支持的 affinity，不把 Collector 误写成 DBOS state authority；
- metric streams 的 single-writer identity 在 replica 重启、failover、DNS 变更和混版期不得重复；
- 至少演练 replica crash、node/zone loss、load balancer failure、DNS stale、WAL loss、backend outage 和 rolling upgrade；
- 为 Collector plane 单独记录 availability SLI、accepted/refused/dropped items、failover time 和丢失上界，不继承 DBOS RPO/RTO。

Per-replica Collector WAL 不是 consensus log（共识日志），本配置不要求多 replica 同步 WAL。一个 replica/PVC 丢失时，其未交付队列可能丢失；必须用 receiver/exporter/queue counters 和 emitted-to-admitted reconciliation 估算上界并记录 limitation。需要跨 replica/zone 持久的 transport 必须另选 `Q2_MESSAGE_QUEUE`。DBOS canonical `RPO=0` 不能由 Collector WAL 提供或继承。

### 10.2 Capacity Envelope（容量包络）

部署前必须冻结：expected/peak items and bytes per second、batch sizes、concurrent requests、queue/WAL capacity、maximum downstream outage、retention、CPU/memory/disk/network budgets 和 high-cardinality budgets。压测必须至少覆盖 1x steady、2x sustained 和 5x bounded burst，并记录首个 drop/refusal point；这是候选表征，不能预先声称容量达标。

## 11. Security Profile（安全配置）

1. 使用最小 Collector distribution，只包含已审查组件；
2. non-root、read-only root filesystem、drop capabilities、seccomp/AppArmor 或等价控制；
3. receiver/exporter/server-like extensions 的网络入口只允许明确 source/destination；
4. TLS certificate、token 和 backend credentials 通过 secret manager 注入，不出现在配置 source、telemetry 或 error output；
5. file storage/WAL 使用独立持久目录、最小权限、容量限制和生命周期策略；
6. prompt、response、tool args/results、Baggage、credential、PII/PHI/financial data 默认不采集；
7. config 在部署前做 schema validation、component allowlist、secret scan、network surface diff 和 policy tests；
8. resource exhaustion、malformed protobuf、decompression bomb、high cardinality 和 log injection 纳入负例。

## 12. Collector Internal Telemetry（Collector 内部遥测）

必须建立独立 self-observation path，避免主管道失败时同时丢失故障证据。精确来源、命名、稳定性、
query、readiness、alert 和 evidence binding 由
[`opentelemetry-collector-operational-evidence-contract.md`](opentelemetry-collector-operational-evidence-contract.md)
与 [machine profile](opentelemetry-collector-operational-evidence-profile.v0.1.json) 约束。至少覆盖：

- receiver accepted/refused items and bytes；
- processor dropped/filtered/transformed counts；
- exporter sent/failed items；
- queue size/capacity/utilization；
- retry count/elapsed/exhaustion；
- WAL bytes、replay、corruption、disk free；
- CPU、memory、GC、goroutines/threads、uptime；
- config reload/version/digest；
- TLS/auth failures；
- gateway backend count/latency and routing errors。

Collector internal telemetry 不得使用 trace ID、entity ID、user ID、prompt 或任意高基数值作为 metric labels。
以上是 observation requirements（观察要求），不是对 OpenTelemetry first-party instrument availability
（一方测量工具可用性）的声明。WAL/disk、listener、config drift、lifecycle 和端到端交付必须结合外部
storage monitor、blackbox、Runtime controller、immutable reconciler 与 destination/DBOS records；缺失时
标记 `UNKNOWN`，不得创建同名假指标或用 health/dashboard 补齐。

## 13. Configuration Lifecycle（配置生命周期）

```text
PROPOSED
  → STATIC_VALIDATED
  → SECURITY_REVIEWED
  → SYNTHETIC_REPLAY_PASS
  → STAGING_CANARY
  → STAGING_SOAK_PASS
  → HUMAN_APPROVED
  → PRODUCTION_CANARY
  → CURRENT

Side: REJECTED | ROLLED_BACK | REVOKED | DEGRADED
```

配置修改必须带 exact diff、component version/digest、容量影响、敏感数据影响、rollback 和 owner。不允许直接编辑生产配置或用 hot reload 绕过 review。

v0.1 不引入 remote config 或 OpAMP control plane。配置更新只允许 immutable versioned config
（不可变版本化配置）经过 static/security/synthetic review、canary、滚动重启和 exact prior digest
rollback；未来动态管理需要独立 inventory、威胁模型和 Human Decision。

Continuous drift control（持续漂移控制）：

- 运行中 Collector 定期上报 distribution digest、component inventory 和 normalized config digest；
- 与 approved desired state 不一致时告警并进入 `DEGRADED`，不自动将未审查配置认为 current；
- emergency change 也必须有 incident reference、time-bounded approval、post-review 和 rollback；
- drift detector 的失效不得被记为“无漂移”。

## 14. Transport-to-Admission Integration Gate（传输到准入集成闸门）

打开真实 listener 前必须依次通过：

```text
G3A_OFFLINE_OTLP_DECODER
  → G3B_DECODER_TO_REFERENCE_ADMISSION
  → G3C_DECODER_TO_PRODUCTION_PERSISTENCE_STAGING
  → G3D_AUTHENTICATED_LOOPBACK_LISTENER
  → G3E_AGENT_GATEWAY_STAGING
  → G3F_FAILURE_DELIVERY_ACCOUNTING
```

| sub-gate | required evidence |
|---|---|
| `G3A` | pinned protobuf/OTLP fixtures、malformed/oversize/permanent/retryable outcomes、no network |
| `G3B` | exact Envelope mapping、partial/drop/duplicate limitations、no Evidence creation |
| `G3C` | Collector storage 与 DBOS canonical store 隔离，commit/unknown/retry 端到端故障 |
| `G3D` | localhost-only authenticated listener、TLS/auth/rate/decompression negative tests |
| `G3E` | >=2 gateway replicas、routing/single-writer、queue/WAL、config drift、scale/failover |
| `G3F` | emitted/received/accepted/rejected/partial/retried/dropped/unknown/duplicate reconciliation |

任一 sub-gate 失败不得绕过到下一步。

## 15. Required Test Matrix（必需测试矩阵）

| group | minimum cases |
|---|---|
| protocol | gRPC/HTTP、gzip/none、Trace/Metric/Log、empty/malformed/oversize、version drift |
| outcomes | full success、partial success、400、429、502/503/504、disconnect、timeout |
| queues | memory full、WAL restart、WAL corrupt、disk full、retry exhausted、multi-destination isolation |
| WAL ownership | per-replica exclusive writer、PVC reattach/replay、replica/PVC permanent loss accounting、shared-WAL rejection |
| topology | agent unavailable、gateway unavailable、backend unavailable、load balancer/DNS change、scale in/out |
| stateful routing | tail-sampling trace affinity、metric single-writer、out-of-order/duplicate streams |
| security | unauthenticated/expired cert、forbidden network、secret canary、payload bomb、high cardinality |
| authority | Resource 不变 Identity；OTLP success 不变 Evidence；Collector 不生成 Permission/Fitness |
| operations | config rollback、Collector upgrade/mixed version、alert fire、runbook execution |

## 16. Exit Gate（退出闸门）

```text
OTLP_COLLECTOR_PRODUCTION_PROFILE_DEFINED=true
COLLECTOR_DISTRIBUTION_DECISION=DQ-025-READY_FOR_REVIEW
COLLECTOR_DISTRIBUTION_CANDIDATE=custom-minimal-v0.156.0@aa158b23c8f89d795b21a05a49b3978565dfebd4
COLLECTOR_DISTRIBUTION_ADOPTED=false
COLLECTOR_DISTRIBUTION_BUILT=false
COLLECTOR_DISTRIBUTION_CONFORMANCE_CASES_EXECUTED=0
COLLECTOR_DISTRIBUTION_SELECTED=false
COLLECTOR_CONFIGURATION_CREATED=false
OTLP_LISTENER_AUTHORIZED=false
COLLECTOR_DEPLOYED=false
OTLP_DELIVERY_CONFORMANCE_PASS=false
COLLECTOR_SECURITY_REVIEW_PASS=false
PR_G3_PASS=false
PRODUCTION_READY=false
```
