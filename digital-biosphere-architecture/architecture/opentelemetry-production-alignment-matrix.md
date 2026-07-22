---
spec_id: TMAI-OTEL-PRODUCTION-ALIGNMENT-MATRIX-0.1
title: TMAI OpenTelemetry Production Alignment Matrix v0.1
title_zh: TMAI OpenTelemetry 生产对齐矩阵 v0.1
status: proposed-control-crosswalk-no-implementation-authority
architecture_owner: digital-biosphere-architecture
external_baseline_observed_at: 2026-07-22
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# TMAI OpenTelemetry Production Alignment Matrix v0.1

中文：TMAI OpenTelemetry 生产对齐矩阵 v0.1。

## 1. Purpose（目的）

本矩阵把 OpenTelemetry（开放遥测）的官方 protocol、Collector deployment、resiliency、scaling、internal telemetry 和 security guidance，映射到 TMAI 的合同、闸门、测试与证据。它回答“为什么需要这条控制”和“什么直接证据才能关闭它”，但不把 OpenTelemetry 建议升级为 DBOS Authority（DBOS 权力）、合规认证或生产通过。

```text
OpenTelemetry requirement
  -> TMAI architecture control
  -> exact gate
  -> direct evidence
  -> scoped Human Decision

OpenTelemetry documentation != TMAI conformance evidence
TMAI control mapping != implementation
Manifest shape validation != gate PASS
```

## 2. External Baseline Snapshot（外部基线快照）

| surface | observed baseline | TMAI treatment |
|---|---|---|
| OpenTelemetry Specification | candidate release `v1.59.0@a824fb4eba795c5c65dd397b3d22e7c28e934de3`; observed HEAD `2b04e8b...` is separate and not adopted | 记录实际使用版本；不跟随 `latest`，不把 moving HEAD 写成 release |
| OTLP | candidate `v1.11.0@790608c...` | `DQ-022` 待决；Trace/Metric/Log Stable；Profiles Development 并在 v0.1 production profile 拒绝 |
| Semantic Conventions | core candidate `v1.43.0@89aae438...`; GenAI pinned Development candidate `2e994c6d...` | `DQ-023` 待决；core 与 GenAI/MCP 属性分开锁定；实验属性不能成为 canonical DBOS 字段 |
| Telemetry Schema / Resource / Entity | Schema and Resource SDK stable subset at exact OTel `v1.59.0`; Resource Data Model and Entity/Propagation Development; core schema artifact `1.43.0` candidate | `DQ-024` 待决；exact source/digest、runtime-fetch-off、transform lineage、Resource provenance、Development Entity quarantine 与 data-governance binding；45 cases 全部未执行 |
| Collector distribution | `NOT_SELECTED` | 必须锁定 distribution、version、image digest、component inventory、SBOM 和签名／来源 |
| Collector configuration | `NOT_CREATED` | 必须保存无秘密 reviewed source、normalized digest、Owner、rollback 和 running-state attestation |

该快照是 2026-07-22 的 architecture input（架构输入），不是对未来上游状态的永久声明。official `v1.10.0@ca839c...` → `v1.11.0@790608c...` delta、compatibility 和两路 Agent Review 已记录，但 `DQ-022` 未决定，因此 `1.11.0` 仍是 candidate reference。以后任何已冻结版本变化必须走 Version Governance（版本治理），不能由文档抓取或依赖更新自动完成。

`Collector distribution=NOT_SELECTED` 和 `configuration=NOT_CREATED` 是刻意的 fail-closed state（失败关闭状态）：S0 Architecture Contract Freeze（架构合同冻结）只冻结选择标准、证据合同和 `DQ-020` 闸门，不能越过 `DQ-018/019` 提前创建或选择运行制品。只有 `DQ-020` 输入齐备并经 Human Decision 后，才能在 S3 形成独立 Deployment Profile Freeze（部署配置冻结）并选定 exact distribution/config；在此之前 `PR-G3` 必须保持未通过。两种 freeze 不得互相替代。

## 3. Normative Alignment Matrix（规范对齐矩阵）

| control | official behavior / guidance | TMAI control | gate | minimum direct evidence |
|---|---|---|---|---|
| `OTEL-C001` | OTLP 只定义 client/server hop，end-to-end delivery 在范围外 | `OTLP_ACK_NE_END_TO_END_DELIVERY`；逐 hop accounting 与 DBOS admission reconciliation 分离 | `PR-G3A-F` | sender/receiver/exporter/admission counts、unknown inventory、loss upper bound |
| `OTEL-C002` | partial success 必须带 rejected counts；client 不应重试该请求 | 保存 accepted/rejected/error limitation；禁止 whole-request retry | `PR-G3A/G3D` | Trace/Metric/Log partial fixtures、no-retry observation、recorded rejected counts |
| `OTEL-C003` | retryable 与 non-retryable error 不同；HTTP 仅 429/502/503/504 属指定 retryable set | exact gRPC/HTTP outcome matrix、bounded backoff、permanent drop counter | `PR-G3A/G3D` | protocol fixtures、retry schedule、drop/retry counters、timeout outcome |
| `OTEL-C004` | 断连或未收到 acknowledgement 时重发可能产生 duplicate | `UNKNOWN_DELIVERY`、duplicate assessment、DBOS idempotency；不声称 global exactly-once | `PR-G2A/G3` | disconnect-before/after-commit fault、duplicate confirmed/suspected inventory |
| `OTEL-C005` | Trace/Metric/Log 为 Stable，Profiles 为 Development | v0.1 production profile 拒绝 Profiles；未知 signal fail closed | `PR-G3A` | signal allowlist、Profiles rejection fixture、version record |
| `OTEL-C006` | OTLP 将来的版本需互操作并退化到共同能力 | 明示 producer/receiver capability、unknown field preservation/rejection policy、cross-version fixture | `PR-G3A/G3B` | old/new fixture matrix、capability negotiation record、limitation |
| `OTEL-C007` | Agent-to-Gateway 是官方部署模式；gateway 可独立扩展 | 首选有界 Agent-to-Gateway candidate；AI Agent 与 Collector Agent 严格分离 | `DQ-020/PR-G3` | topology digest、network policy、replica inventory、failure-domain map |
| `OTEL-C008` | tail sampling、cumulative-to-delta 等 stateful processing 需要 data-aware routing | trace-ID/stream-aware affinity 或经证明等价机制；routing 不是 DBOS Authority | `PR-G3E` | routing config digest、reshard/mixed-version tests、trace/series completeness query |
| `OTEL-C009` | metric gateway horizontal scaling 必须保持 single-writer principle | 每个 metric stream 的唯一 writer/aggregation owner | `PR-G3E` | stream-to-writer mapping、duplicate series negative test、failover evidence |
| `OTEL-C010` | remote exporter 应使用 sending queue 并监控 queue size/capacity | `Q0/Q1/Q2` durability class、容量和 overflow/drop 告警 | `PR-G3B-F` | queue config/digest、load/overflow/recovery tests、queue telemetry |
| `OTEL-C011` | file-storage WAL 可跨 Collector restart 恢复，但 disk failure/full 和 retry expiry 仍会丢失 | 每 replica 独占 WAL；WAL 不是 consensus，也不继承 DBOS RPO | `PR-G3E/PR-G5` | crash/restart/PVC-loss/disk-full tests、replay duplicates、loss limitation |
| `OTEL-C012` | critical cross-network paths 可使用 message queue，代价是额外运维复杂度 | 只有 `Q2_MESSAGE_QUEUE` 可候选跨 zone transport durability；需独立 Owner/HA/security | `DQ-020/PR-G3F` | broker topology/version、producer buffering、broker failure/restore、cost/ops review |
| `OTEL-C013` | Collector internal telemetry 应支持 queue、failure、CPU、memory 和 throughput 诊断 | Collector plane 自身 SLI，不自动证明 system trust 或 Evidence completeness | `PR-G3F/PR-G5` | dashboards/alerts、alert-fire test、queue/export/refusal/drop/resource time series |
| `OTEL-C014` | Collector config 可能含 token/private key，应使用安全存储和受控注入 | secret-free reviewed config、managed secret injection、logs/attributes/manifest secret canary | `PR-G3D/PR-G5` | config scan、secret canary、access audit、rotation/revocation test |
| `OTEL-C015` | Collector 运行应 least privilege，server-like component 访问受控 | minimal distribution、non-root/least privilege、最小 listener/network/filesystem 权限 | `PR-G3D/PR-G5` | component inventory、RBAC/UID/network policy、unauthenticated/forbidden access tests |
| `OTEL-C016` | OTLP `v1.11.0` candidate 要求 receiver/client 在 request/response 的压缩前与解压后执行限制；recommended request `64 MiB`、response `4 MiB`，并定义 `413` / `RESOURCE_EXHAUSTED` / non-retryable / acceptance unknown | deployment profile 必须显式冻结 inbound/outbound、compressed/decompressed request/response limits；超限保留 discard/unknown record，禁止重试风暴 | `DQ-022/PR-G3A-F/PR-G5` | gRPC+HTTP 八类 size boundary、decompression bomb、diagnostic truncation、unknown acceptance、invalid/HTTP-date `Retry-After`、high-cardinality、concurrency、5x burst tests |
| `OTEL-C017` | 配置与处理必须防止敏感数据泄露 | default content capture off、allowlist、redaction lineage、retention/residency/access gate | `PR-G3/PR-G2C/PR-G5` | sensitive fixtures、sample inspection、policy/version/ref、deletion/retention evidence |
| `OTEL-C018` | Collector scaling/configuration会产生 topology 与 runtime drift | desired/running distribution、components、config digest reconciliation；drift fail closed | `PR-G3F` | periodic attestation、mixed-version/drift alert、rollback exercise |
| `OTEL-C019` | Resource 和 Instrumentation Scope 描述被观察资源与插桩来源 | 两者分开保存；Resource attribute 不创建 DBOS Identity、Entity、Permission 或 Evidence | `PR-G2I/PR-G3` | forged `entity_id`/`service.name` negative tests、canonical identity continuity query |
| `OTEL-C020` | Collector pipeline 是传输/处理基础设施，不是治理权威 | Telemetry Admission 与 Evidence Admission 独立；Collector status/attributes 不产生 Verification/Truth | `PR-G2A/G2C/G3` | OTLP success→no Evidence test、`verified=true` rejection、independent Verification record |
| `OTEL-C021` | Semantic Convention 稳定性按领域和字段独立，不由仓库版本统一决定 | exact OTel Spec/core SemConv/GenAI source registry；47/47 字段逐项 stability inventory；drift fail closed | `DQ-023/PR-G2/PR-G3` | exact source/tag/commit/digest、field inventory、old/new delta、validator result |
| `OTEL-C022` | `service.instance.id` 是 service instance；`gen_ai.agent.id` 是 hosted-agent resource hint | 二者都只能进入 non-authoritative hint；DBOS binding 必须来自独立 `DBOS_CONTEXT` + record digest | `DQ-023/PR-G2I/PR-G3` | forged ID negatives、DBOS binding source/digest、identity continuity query |
| `OTEL-C023` | `invoke_agent`、`execute_tool`、tool name/type/call ID 是 observed operation metadata | 不创建 Agent/Entity、Capability、Permission、Authorization 或完整 Execution | `DQ-023/PR-G2A/PR-G3` | operation/tool injection negatives、zero canonical effects、independent execution lookup |
| `OTEL-C024` | `gen_ai.evaluation.*` 是 upstream evaluator material | 不创建 SAEE Fitness/Risk/Evolution Recommendation 或 Governance Decision | `DQ-023/PR-G3/PR-G4` | evaluation-elevation negatives、evaluator/version binding、SAEE read-only/no-writeback proof |
| `OTEL-C025` | GenAI input/output/instruction/tool/retrieval/evaluation content 可能包含敏感数据 | 默认 disabled；opt-in 需要 Decision、policy digest、allowlist、retention/residency/access/redaction binding | `DQ-023/PR-G2C/PR-G3/PR-G5` | disabled-content negatives、authorized redacted fixture、retention/deletion/access evidence |
| `OTEL-C026` | Baggage 可跨进程传播且不适合凭据或权力状态 | strict envelope 不提供 Baggage；authority namespace/field injection reject-or-strip-with-auditable-limitation | `DQ-023/PR-G2/PR-G3/PR-G5` | baggage/`dbos.*`/`tmai.*`/permission injection negatives、limitation record |
| `OTEL-C027` | 高基数属性会放大 Metric 成本与资源风险 | instance/trace/span/agent/conversation/tool-call IDs 禁止作 Metric label；低基数字段需 per-tenant/service/window budget；overflow 不静默 | `DQ-023/DQ-020/PR-G3/PR-G5` | label-rejection tests、budget/config digest、overflow aggregate/drop limitation、5x burst |
| `OTEL-C028` | GenAI conventions 为 Development，旧 core GenAI 字段已 Deprecated | exact commit isolation、deprecated reject+diagnostic、tag/Schema URL 变化也走完整 Human Version Decision | `DQ-023/PR-G3` | deprecated fixtures、missing/schema drift tests、mapping replay、human decision reference |
| `OTEL-C029` | Telemetry Schema URL 可通过 HTTP(S) 获取并可能 redirect；已发布 schema 声称 immutable/cachable | Runtime fetch 默认关闭；build/release acquisition 逐 hop/final host/DNS/private-range 检查并绑定 exact URL/version/digest/format | `DQ-024/DQ-020/PR-G3/PR-G5` | source resolution trace、SSRF/DNS rebinding/redirect loop/size/MIME/parser negatives、artifact digest |
| `OTEL-C030` | Resource* 与 contained InstrumentationLibrary*/Scope 两级 non-empty `schema_url` 时 contained value 对其 signal data 取 precedence | 保留两个原始 URL/domain；precedence 只决定 contained signal effective schema，不是 trust authority 或覆盖 | `DQ-022/DQ-024/PR-G2/PR-G3` | five precedence fixtures、effective-reason lineage、cross-family rejection |
| `OTEL-C031` | Schema conversion 由版本化 schema transformations 描述，breaking/impossible conversion 可能存在 | 只执行 pinned transform；原始 projection immutable；transformer/source/target/input/output/environment 全 digest；unknown/lossy fail closed | `DQ-023/DQ-024/DQ-018/PR-G2/PR-G3` | six transform cases、transformer artifact/config digest、original-vs-output replay、authority-field canary |
| `OTEL-C032` | Resource SDK merge 对 empty/same/different non-empty Schema URL 有明确规则；conflicting non-empty result undefined/implementation-specific | 精确复现可定义规则；冲突输出拒绝；每个 detector/value/order/config/source 保留 provenance；merge precedence != trust | `DQ-024/DQ-018/PR-G2/PR-G3` | seven Resource cases、merge matrix、detector drift/duplicate/order evidence、canonical identity non-creation |
| `OTEL-C033` | `OTEL_RESOURCE_ATTRIBUTES` 是 environment input，parse error 应整项丢弃；user Resource precedence 更高 | environment origin 明示且 untrusted；malformed input 整项拒绝；user precedence 不产生 identity/permission | `DQ-024/DQ-018/PR-G2/PR-G5` | malformed/percent-decode fixtures、whole-variable rejection、conflict provenance、zero authority effects |
| `OTEL-C034` | OTel Entity Data Model 与 Entity Propagation 在 exact `v1.59.0` 为 Development | TMAI `quarantine_record_schema_version=0.1` 精确绑定 source/digest；OTel Entity != Digital Entity；无 direct promotion | `DQ-024/DQ-018/PR-G2/PR-G5` | eight Entity cases、malformed/duplicate/partial/schema-conflict fixtures、DBOS admission/registration lookup |
| `OTEL-C035` | Telemetry Resource/Entity/environment/diagnostic 可能携带个人、凭据、token 或租户数据 | classification/minimization/redaction、tenant/purpose/retention/access/encryption policy、opaque reference/low-entropy protection、auditable disposition | `DQ-024/PR-G2/PR-G3/PR-G5/PR-G6` | seven data-governance cases、policy refs、cross-tenant non-disclosure、redaction/retention/disposition evidence |
| `OTEL-C036` | Schema/Resource/Entity conformance result 本身不是 OpenTelemetry 或 TMAI governance authority | strict result set 要求 45/45、6/6 source、exact digests、Decision、validator、independent review、data governance；effects 恒 false | `DQ-024/PR-G2/PR-G3/PR-G5/PR-G6` | frozen result、catalog/result reconciliation、37 negative controls、Human gate decision separate |
| `OTEL-C037` | Collector release tag 是观察标签；官方 releases 仓库说明 tags 可能因发布修复而变化 | source identity 绑定 exact releases/core/contrib commits 与 exact manifest/component byte digests；tag drift 进入新版本决策 | `DQ-025/DQ-020/PR-G3/PR-G5` | source resolution、tag-to-commit drift negative、11-source byte reconciliation |
| `OTEL-C038` | 官方发行版组件集合不同；组件稳定性按 signal/component 独立，不能由 Collector 整体版本推断 | v0.1 只提议 custom-minimal 8 components + env/file providers；Profiles、remote providers 和所有未登记 component 均排除；Alpha/Beta 边界明示 | `DQ-025/PR-G3/PR-G5` | compiled component graph、allowlist/denylist negatives、stability inventory、Profiles absence proof |
| `OTEL-C039` | Collector binary/image 来源与依赖图是独立 supply-chain（供应链）事实，预构建 manifest 或 signed tag 不能证明自定义 binary | exact OCB/module lock；binary/image/SBOM/license/provenance/signature/vulnerability/reproducibility/component inventory 全 digest 并互相 reconciliation | `DQ-025/DQ-020/PR-G3/PR-G5` | build manifest、module graph、SBOM、signature policy、vulnerability SLA、independent reproducible build |
| `OTEL-C040` | Collector configuration providers 和 enabled components 扩大配置与网络攻击面 | 仅 env/file providers；禁止 runtime HTTP(S)/YAML source fetch；normalized redacted config、feature gates、component graph、secrets、TLS/network/limits/tenant policies exact digest | `DQ-025/DQ-020/PR-G3/PR-G5` | provider/component scan、remote-provider negative、secret canary、desired/running config reconciliation |
| `OTEL-C041` | Processor 顺序和 OTTL 变换会改变内存保护、identity、cardinality、privacy 与错误传播；Transform 官方警告 unsound/identity/orphan 风险 | `memory_limiter → transform → batch` 固定；`error_mode=propagate` 明示但不作为充分证明；配置错误、永久数据错误与瞬时 downstream 错误分离，poison retry 有界 | `DQ-023/DQ-024/DQ-025/DQ-020/PR-G3/PR-G5` | pipeline-order diff、OTTL config/runtime matrix、authority canary、retry/terminal timeline、transform lineage |
| `OTEL-C042` | sending queue、retry 与 file storage 提升局部韧性但仍可满、超时、损坏或丢失，并可能重复交付 | 每 destination 独立 queue/WAL；每 replica 单 writer；disk/corruption/restart/retry-exhaustion/unknown-ack 形成显式 loss/duplicate accounting；不声明 exactly-once 或 canonical durability | `DQ-020/PR-G3/PR-G5/PR-G6` | queue/WAL topology、crash/replay、disk-full/corruption、retry exhaustion、delivery reconciliation |
| `OTEL-C043` | Collector internal telemetry 与 health endpoint 只描述 Collector 的局部观察状态；health check extension 仍为 Alpha | failure path 使用独立低基数自观测；health restricted 且只能作 bounded signal；不得单独驱动 readiness、TMAI trust、Evidence 或 gate | `DQ-025/DQ-020/PR-G3/PR-G5` | independent self-telemetry、health/exporter/queue divergence、endpoint exposure negative、alert-fire test |
| `OTEL-C044` | Collector distribution conformance result 是可审查材料，不是 distribution adoption、build/deployment authorization、Evidence Truth 或 gate authority | strict result set 要求 48/48、8/8 groups、exact inventory/catalog/build/config/runtime/validator、independent technical+security review；effects 恒 false | `DQ-025/DQ-020/PR-G3/PR-G5/PR-G6` | frozen result、catalog/result reconciliation、PASS shape + fail-closed negatives、separate Human gate decision |
| `OTEL-C045` | Deployment pattern/profile 只描述候选形状，不是 Collector config 或运行状态 | machine deployment profile 的 effects 永久为 false；真实 build/config/runtime/result 使用独立工件与 digest | `DQ-020/PR-G3/PR-G7` | profile Schema、zero-effect negatives、separate deployment repository/config/result bindings |
| `OTEL-C046` | Agent-to-gateway 增加运维复杂度；无 stateful processing 时 gateway 可普通扩展，stateful use 需要 data-aware affinity | edge tier optional/not selected；gateway 只在 `G3E` 进入且 candidate replicas >=2；首个 baseline 无 cross-request stateful processor，只有 per-exporter queue/per-replica WAL 本地例外 | `DQ-020/PR-G3E/PR-G5` | topology/failure-domain/LB digest、stateful-component absence、replica/WAL ownership/failover tests |
| `OTEL-C047` | Collector receiver 会接收调用方送入的数据；官方部署模式本身不提供 TMAI staging-data authority | `G3D/G3E` 只允许 approved synthetic fixture + immutable digest/source/purpose/retention；未批准、未标记或 real-data canary fail closed | `DQ-020/PR-G3/PR-G5` | source/network allowlist、fixture manifest、unapproved/real-data negative、bounded diagnostic scan |
| `OTEL-C048` | OpAMP/remote configuration 是可选管理能力，不是 Collector 生产必需条件 | v0.1 明确不编译、不允许 remote config/OpAMP；唯一更新路径是 immutable versioned config + gates + canary + rolling restart + exact rollback | `DQ-025/DQ-020/PR-G3/PR-G5` | provider/component absence、versioned rollout record、drift/rollback/restart tests、new-control-plane decision negative |
| `OTEL-C049` | Collector receiver 可使用 TLS/authentication；authentication extension 需要进入 distribution 并在 service/config 启用 | 首阶段只候选 native TLS/mTLS + external network/source policy；OIDC/bearer 等 extension 缺失时不得隐式配置，必须回到 `DQ-025` inventory | `DQ-025/DQ-020/PR-G3D/PR-G5` | cert rotation/revocation/wrong-source negatives、component/service graph、tenant identity binding、zero fallback |
| `OTEL-C050` | 默认 health/internal telemetry 只能暴露局部状态，且 internal telemetry 配置 schema/internal traces 有稳定性限制 | external composite readiness 至少绑定 process/config/listener/queue/WAL/exporter/self-telemetry/drift；threshold 未选时 fail closed；internal traces baseline 禁用 | `DQ-020/PR-G3E-F/PR-G5` | readiness truth table、health divergence、stale self-telemetry、queue/WAL/exporter fault、schema-version binding |
| `OTEL-C051` | Collector internal telemetry 的 declarative configuration schema 仍在发展，internal traces 仍为 experimental | v0.1 只要求受限、独立失败路径的 internal metrics/logs；禁用 internal traces；exact config 与 endpoint 未绑定时不得开始测量 | `DQ-020/PR-G3/PR-G5` | exact internal telemetry config/digest、restricted endpoint/destination、trace-absence check、45/45 profile negatives |
| `OTEL-C052` | OTLP 与 Prometheus 暴露的 metric 名称会受 `_total`、unit suffix、dots/underscores、views 和 verbosity 影响，instrument stability 也逐项不同 | 规范语义使用 OTLP instrument name；记录 projection、view、verbosity、Collector version 和 per-instrument stability；third-party `http.*`/`rpc.*` 不继承 Collector stability | `DQ-020/PR-G3/PR-G5` | exact metric inventory/version/digest、OTLP↔Prometheus mapping、query replay、renamed/missing metric negative |
| `OTEL-C053` | Internal metric、log、health、runtime、storage、destination receipt 各只观察局部事实 | 12 类 observation 强制分离 Collector、Runtime controller、storage monitor、blackbox、reconciler、destination 与 DBOS admission 来源；任何单源不能替代另一源 | `DQ-020/PR-G3/PR-G5` | source/destination/failure-path digests、cross-source reconciliation、single-source-loss fault matrix |
| `OTEL-C054` | Counter 可能随 restart/reset，metric 可能缺失、改名或 stale；internal log 格式无稳定保证 | reset 按 instance lifecycle 分窗；missing/stale/renamed=`UNKNOWN`；mixed version 不聚合；关键 log 与独立 lifecycle 记录对账，禁止 zero-fill | `DQ-020/PR-G3/PR-G5` | reset/stale/no-data/mixed-version fixtures、lifecycle correlation、zero-fill rejection、unknown inventory |
| `OTEL-C055` | queue/refusal/send-failure/process metrics 是诊断输入，不是完整端到端健康证明 | 12 类 observation 和 6 类 derived SLI 同时覆盖 process、receiver、processor、enqueue、send、queue、WAL、listener、drift、freshness、lifecycle 与 delivery closure | `DQ-020/PR-G3E-F/PR-G5` | exact query/formula bundle、dimension/cardinality audit、per-hop and end-to-end reconciliation result |
| `OTEL-C056` | Collector scaling guidance要求同时观察 queue、refusal、send failure；增加 Collector 可能放大 downstream bottleneck | readiness 要求八个谓词全部 true/fresh；任一 unknown/critical=`NOT_READY`；health、dashboard 和人工 override 均不能覆盖 | `DQ-020/PR-G3E-F/PR-G5` | predicate truth table、backend saturation/scale divergence、no-data and health-green fault results |
| `OTEL-C057` | WAL/queue 提升局部韧性，但磁盘满、损坏、retry expiry 与 crash 仍可丢失或重复 | WAL readiness 必须使用外部磁盘/写入探针、queue event 和 delivery reconciliation；internal metric 或 replay success 不能证明 canonical durability/RPO0 | `DQ-020/PR-G3/PR-G5/PR-G6` | disk-free/write probe、crash/corruption/replay、duplicate/loss bound、DBOS persistence separation |
| `OTEL-C058` | 自观测与安全建议要求资源耗尽、失败和受限接口可被及时发现，但文档本身不提供 TMAI alert authority | warning/critical 分离、SLO multi-window burn rate、no-data alert、clock-skew bound、alert delivery test 和每个 critical alert 的 runbook 都须 exact digest | `DQ-020/PR-G3/PR-G5` | rule/route/runbook digests、alert-fire/no-data/delivery drills、review/ack timeline、non-authority remediation test |
| `OTEL-C059` | Exporter `sent`/destination receipt 只证明局部 hop；OTLP 不定义端到端交付 | emitted 必须对账为 terminal/buffered/retrying/unknown/duplicate-suspected，并与 DBOS admission 分离；不能用 hop counter 推断 Evidence | `DQ-020/PR-G3F/PR-G5/PR-G6` | emitter→Collector→destination→admission accounting、unknown/duplicate/loss inventory、window/clock binding |
| `OTEL-C060` | Collector telemetry、health、dashboard 和 alert 是观察材料，不是治理或执行权威 | self-report、dashboard、health、zero-fill 均不能关闭 gate；Telemetry != DBOS Evidence != Truth；告警自动修复不得扩大 Authority | `DQ-020/PR-G3/PR-G5/PR-G7` | strict profile/schema、45/45 negative controls、independent review、separate Human Decision and Evidence admission |

## 4. Exact Conformance Case Binding（精确符合性用例绑定）

[`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json) 是 control → case 的机器事实源；[`schemas/otlp-conformance-case-catalog.schema.v0.1.json`](schemas/otlp-conformance-case-catalog.schema.v0.1.json) 只验证形状。分组绑定如下：

| case group | primary controls | gate boundary | current truth |
|---|---|---|---|
| `OTLP-CG-SIGNAL_SCHEMA` | `OTEL-C005/C006/C001` | `DQ-018/PR-G2` | 9 cases，`NOT_EXECUTED` |
| `OTLP-CG-GRPC_SIZE` | `OTEL-C016/C001/C003` | `DQ-020/PR-G3A/PR-G5` | 9 cases，`NOT_EXECUTED` |
| `OTLP-CG-HTTP_SIZE` | `OTEL-C016/C001/C003` | `DQ-020/PR-G3A/PR-G5` | 9 cases，`NOT_EXECUTED` |
| `OTLP-CG-RETRY_PARTIAL` | `OTEL-C001/C002/C003/C016` | `DQ-020/PR-G3A/G3D/PR-G5` | 16 cases，`NOT_EXECUTED` |
| `OTLP-CG-DELIVERY_RECONCILIATION` | `OTEL-C001/C002/C010/C011/C013` | `PR-G3/PR-G5/PR-G6` | 5 cases，`NOT_EXECUTED` |
| `OTLP-CG-AUTHORITY_BOUNDARY` | `OTEL-C019/C020` | `DQ-018/PR-G2/PR-G3` | 3 cases，`NOT_EXECUTED` |
| `OTLP-CG-DEPLOYMENT_SECURITY_CAPACITY` | `OTEL-C013/C014/C015/C016/C017` | `DQ-020/PR-G3/PR-G5` | 5 cases，`NOT_EXECUTED` |

`DQ-018` 不得执行 deployment groups，`DQ-020` 不得跳过 reference/authority results；`PR-G3` 要求 56/56 required cases 有直接结果，但其中 `UNKNOWN` acceptance 可以是符合预期的保守结果。case result 不能自动改变 Version Decision、Evidence Truth、Permission 或 Production Authorization。

`OTEL-C021`–`OTEL-C028` 现已绑定 [47-field semantic mapping](opentelemetry-semantic-mapping.v0.1.json)、
[46-case semantic conformance catalog](opentelemetry-semantic-conformance-cases.v0.1.json)
及其 [strict result-set schema](schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json)。
8 个语义分组和 gate 关系如下；所有用例仍是 `NOT_EXECUTED`：

| semantic case group | primary controls | gate boundary | current truth |
|---|---|---|---|
| `SEM-CG-VERSION_SOURCE` | `OTEL-C021/C028` | `DQ-023/DQ-018/PR-G2` | 5 cases，`NOT_EXECUTED` |
| `SEM-CG-CORE_STABLE` | `OTEL-C019/C021/C022` | `DQ-018/PR-G2` | 5 cases，`NOT_EXECUTED` |
| `SEM-CG-GENAI_METADATA` | `OTEL-C021/C022/C023/C024/C028` | `DQ-023/DQ-018/PR-G2` | 6 cases，`NOT_EXECUTED` |
| `SEM-CG-SENSITIVE_CONTENT` | `OTEL-C017/C025` | `DQ-018/PR-G5` | 10 cases，`NOT_EXECUTED` |
| `SEM-CG-DEPRECATED_DRIFT` | `OTEL-C021/C028` | `DQ-023/DQ-018/PR-G2` | 5 cases，`NOT_EXECUTED` |
| `SEM-CG-AUTHORITY_BOUNDARY` | `OTEL-C019/C020/C022/C023/C024/C026` | `DQ-018/PR-G2/PR-G5` | 7 cases，`NOT_EXECUTED` |
| `SEM-CG-CARDINALITY` | `OTEL-C027` | `DQ-020/PR-G3/PR-G5` | 4 cases，`NOT_EXECUTED` |
| `SEM-CG-RESULT_BOUNDARY` | `OTEL-C020/C021` | `PR-G2/PR-G3/PR-G6` | 4 cases，`NOT_EXECUTED` |

目录与 synthetic `NOT_ASSESSED` 结果示例已通过 shape validation；12/12 目录负例和
23/23 结果负例被拒绝，47/47 mapping coverage、case/group closure 与零权力效果通过
architecture-only semantic check。它们仍不是 DBOS implementation evidence：独立 validator、
真实 fixture、artifact/environment digest、46/46 结果和人工 Decision 均不存在。先前
20/20 mapping/observation Schema rehearsal 与本次 46-case conformance execution 必须分开记录。

`OTEL-C029`–`OTEL-C036` 绑定 [Schema/Resource/Entity provenance profile](opentelemetry-schema-resource-entity-provenance-profile.md)、
[45-case catalog](opentelemetry-schema-resource-conformance-cases.v0.1.json) 与
[strict result-set schema](schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json)。
7 个分组和 gate 关系如下；全部仍是 `NOT_EXECUTED`：

| provenance case group | primary controls | gate boundary | current truth |
|---|---|---|---|
| `OSR-CG-SCHEMA_SOURCE` | `OTEL-C029/C031/C035` | `DQ-024/DQ-020/PR-G2/PR-G3/PR-G5` | 8 cases，`NOT_EXECUTED` |
| `OSR-CG-SCHEMA_PRECEDENCE` | `OTEL-C030` | `DQ-022/DQ-024/DQ-018/PR-G2` | 5 cases，`NOT_EXECUTED` |
| `OSR-CG-TRANSFORMATION` | `OTEL-C031/C036` | `DQ-023/DQ-024/DQ-018/PR-G2/PR-G3` | 6 cases，`NOT_EXECUTED` |
| `OSR-CG-RESOURCE_PROVENANCE` | `OTEL-C032/C033` | `DQ-024/DQ-018/PR-G2/PR-G3/PR-G5` | 7 cases，`NOT_EXECUTED` |
| `OSR-CG-ENTITY_QUARANTINE` | `OTEL-C034/C035` | `DQ-024/DQ-018/PR-G2/PR-G5` | 8 cases，`NOT_EXECUTED` |
| `OSR-CG-DATA_GOVERNANCE` | `OTEL-C035/C036` | `DQ-024/DQ-018/PR-G2/PR-G3/PR-G5/PR-G6` | 7 cases，`NOT_EXECUTED` |
| `OSR-CG-RESULT_AUTHORITY` | `OTEL-C036` | `DQ-024/PR-G2/PR-G3/PR-G5/PR-G6` | 4 cases，`NOT_EXECUTED` |

两种 JSON Schema 与 synthetic `NOT_ASSESSED` example 已通过 architecture-only validation；
14/14 catalog negatives 和 37/37 result negatives 被拒绝。模型审查推荐 bounded design
reference 和 human review，同时拒绝当前 runtime recommendation。以上均不是 45-case runtime
execution、privacy compliance、interoperability 或 production evidence。

`OTEL-C037`–`OTEL-C060` 绑定 [Collector distribution profile](opentelemetry-collector-distribution-profile.md)、
[8-component inventory](opentelemetry-collector-component-inventory.v0.1.json)、
[48-case catalog](opentelemetry-collector-distribution-conformance-cases.v0.1.json) 与
[strict result-set schema](schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json)，
并由 [machine deployment profile](opentelemetry-collector-deployment-profile.v0.1.json) 与
[deployment readiness matrix](opentelemetry-collector-deployment-readiness-matrix.md) 绑定具体候选空位。
8 个分组和 gate 关系如下；全部仍是 `NOT_EXECUTED`：

| distribution case group | primary controls | gate boundary | current truth |
|---|---|---|---|
| `ODC-CG-SOURCE` | `OTEL-C037/C039/C044` | `DQ-025/DQ-020/PR-G3/PR-G5` | 7 cases，`NOT_EXECUTED` |
| `ODC-CG-ALLOWLIST` | `OTEL-C038/C039` | `DQ-025/DQ-020/PR-G3` | 7 cases，`NOT_EXECUTED` |
| `ODC-CG-CONFIG` | `OTEL-C040/C041/C045/C048` | `DQ-020/PR-G3/PR-G5` | 8 cases，`NOT_EXECUTED` |
| `ODC-CG-SECURITY` | `OTEL-C040/C041/C043/C047/C049/C050` | `DQ-020/PR-G3/PR-G5` | 7 cases，`NOT_EXECUTED` |
| `ODC-CG-DURABILITY` | `OTEL-C042/C046` | `DQ-020/PR-G3/PR-G5/PR-G6` | 6 cases，`NOT_EXECUTED` |
| `ODC-CG-OPERABILITY` | `OTEL-C040/C043/C045/C048/C050` | `DQ-020/PR-G3/PR-G5` | 5 cases，`NOT_EXECUTED` |
| `ODC-CG-CAPACITY_HA` | `OTEL-C038/C042/C043/C046/C050` | `DQ-020/PR-G3/PR-G5` | 4 cases，`NOT_EXECUTED` |
| `ODC-CG-AUTHORITY` | `OTEL-C044/C045/C047/C049` | `DQ-025/DQ-020/PR-G3/PR-G6` | 4 cases，`NOT_EXECUTED` |

三种 Schema 与 synthetic `NOT_ASSESSED` example 已通过 architecture-only validation；完整
`PASS` shape control、115/115 result Schema negatives 与 4/4 required future-validator semantic
negatives 被拒绝。两路模型复评后 required
document corrections 为 0，均只推荐 bounded design reference 和 Human Review，同时保持当前
runtime recommendation=`DO_NOT_RECOMMEND`。这些结果不构成 binary、image、config、48-case
runtime execution、security approval、interoperability 或 production evidence。

`OTEL-C051`–`OTEL-C060` 进一步绑定
[Collector operational evidence contract](opentelemetry-collector-operational-evidence-contract.md)、
[machine profile](opentelemetry-collector-operational-evidence-profile.v0.1.json) 与
[strict Schema](schemas/opentelemetry-collector-operational-evidence-profile.schema.v0.1.json)。它们不创建
第五套 conformance catalog，而是复用 `ODC-CG-OPERABILITY`、`ODC-CG-CAPACITY_HA`、
`ODC-CG-DURABILITY`、OTLP delivery reconciliation 与既有 authority cases。机器画像 canonical
validation 和 45/45 fail-closed negatives 已通过；两路模型最终均推荐 limited architecture review，
同时保持 runtime/deployment=false、production=false。12 类 observation、6 类 SLI、所有 threshold、
query、alert、route、runbook 和真实结果当前均未配置／未执行，因此这些控制仍未实施。

## 5. Evidence Binding Rules（证据绑定规则）

每个 control 的 `PASS` 必须同时通过：

- [`production-gate-evidence-manifest-specification.md`](production-gate-evidence-manifest-specification.md)；
- [`schemas/production-gate-evidence-manifest.schema.v0.1.json`](schemas/production-gate-evidence-manifest.schema.v0.1.json)；
- [`production-gate-evidence-profiles.v0.1.json`](production-gate-evidence-profiles.v0.1.json) 的 exact version/profile。

绑定内容至少包括：

1. immutable DBA commit/tree 和 normative file digests；
2. exact implementation source commit、artifact/image/config/SBOM digest；
3. exact environment、topology、failure domain、workload、seed 和 observation window；
4. positive、negative、fault、security、recovery、rollback、capacity 与 data-governance coverage；
5. failed、unknown、partial、dropped、duplicate 和 revoked evidence；
6. scoped Owner、Reviewer、Human Decision 和 expiration/revalidation boundary。

Schema validation 只证明字段形状。只有 schema、gate profile、artifact existence、digest verification、required test coverage、review separation 和 Human Decision 全部通过，才可形成 exact scoped gate result。

## 6. Upstream Drift Rule（上游漂移规则）

发现新的 OTel、OTLP、Semantic Convention、Collector 或 component 版本时：

```text
OBSERVED
  -> DELTA_INVENTORIED
  -> WIRE_SCHEMA_BEHAVIOR_REVIEWED
  -> SECURITY_AND_STABILITY_REVIEWED
  -> FIXTURES_UPDATED
  -> COMPATIBILITY_TESTED
  -> HUMAN_VERSION_DECISION
  -> PROFILE_UPDATED
```

在 `HUMAN_VERSION_DECISION` 前，旧冻结 profile 继续有效，新版本状态为 `OBSERVED_NOT_ADOPTED`。不得用“官方 latest”“SemVer compatible”“Collector can start”或“test suite still green”代替 delta review。

## 7. Current State（当前状态）

```text
OTEL_PRODUCTION_ALIGNMENT_MATRIX_DEFINED=true
OTEL_PRODUCTION_ALIGNMENT_CONTROL_COUNT=60
OTEL_SPEC_REFERENCE_CANDIDATE=1.59.0@a824fb4eba795c5c65dd397b3d22e7c28e934de3
OTLP_REFERENCE_CANDIDATE=1.11.0@790608c4d51e6ffc12210b541e8514cbed9e91a4
OTLP_REFERENCE_ADOPTED=true
OTLP_VERSION_DECISION=DQ-022-READY_FOR_REVIEW
OTLP_CONFORMANCE_PROFILE_DEFINED=true
OTLP_CONFORMANCE_CASE_COUNT=56
OTLP_CONFORMANCE_CASE_GROUP_COUNT=7
OTLP_CONFORMANCE_TESTS_EXECUTED=0
SEMANTIC_CONVENTIONS_REFERENCE=1.43.0
SEMANTIC_MAPPING_DECISION=DQ-023-READY_FOR_REVIEW
SEMANTIC_MAPPING_COUNT=47
SEMANTIC_MAPPING_SOURCE_REGISTRY_COUNT=9
SEMANTIC_MAPPING_RECOMMENDED_BY_TWO_AGENTS=true
SEMANTIC_MAPPING_ADOPTED=true
SEMANTIC_CONFORMANCE_PROFILE_DEFINED=true
SEMANTIC_CONFORMANCE_CASE_COUNT=46
SEMANTIC_CONFORMANCE_CASE_GROUP_COUNT=8
SEMANTIC_CONFORMANCE_MAPPING_COVERAGE=47/47
SEMANTIC_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
SEMANTIC_CONFORMANCE_AGENT_REVIEW_COMPLETE=true
SEMANTIC_CONFORMANCE_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
SEMANTIC_CONFORMANCE_VALIDATOR_IMPLEMENTED=false
SEMANTIC_CONFORMANCE_TESTS_EXECUTED=0
SCHEMA_RESOURCE_ENTITY_DECISION=DQ-024-READY_FOR_REVIEW
SCHEMA_RESOURCE_ENTITY_CASE_COUNT=45
SCHEMA_RESOURCE_ENTITY_CASE_GROUP_COUNT=7
SCHEMA_RESOURCE_ENTITY_SOURCE_COUNT=6
SCHEMA_RESOURCE_ENTITY_AGENT_REVIEW_COMPLETE=true
SCHEMA_RESOURCE_ENTITY_REFERENCE_ADOPTED=true
SCHEMA_RESOURCE_ENTITY_VALIDATOR_IMPLEMENTED=false
SCHEMA_RESOURCE_ENTITY_TESTS_EXECUTED=0
COLLECTOR_DISTRIBUTION_DECISION=DQ-025-READY_FOR_REVIEW
COLLECTOR_DISTRIBUTION_CANDIDATE=custom-minimal-v0.156.0@aa158b23c8f89d795b21a05a49b3978565dfebd4
COLLECTOR_DISTRIBUTION_COMPONENT_COUNT=8
COLLECTOR_DISTRIBUTION_CONFIG_PROVIDER_COUNT=2
COLLECTOR_DISTRIBUTION_CASE_COUNT=48
COLLECTOR_DISTRIBUTION_CASE_GROUP_COUNT=8
COLLECTOR_DISTRIBUTION_AGENT_REVIEW_COMPLETE=true
COLLECTOR_DISTRIBUTION_SELECTED=false
COLLECTOR_DISTRIBUTION_VALIDATOR_IMPLEMENTED=false
COLLECTOR_DISTRIBUTION_TESTS_EXECUTED=0
COLLECTOR_CONFIGURATION_CREATED=false
COLLECTOR_DEPLOYMENT_PROFILE_DEFINED=true
COLLECTOR_DEPLOYMENT_PROFILE_STATUS=PROPOSED_DQ_020_INPUT_NOT_AUTHORIZED_NOT_CONFIGURED_NOT_DEPLOYED
COLLECTOR_OPERATIONAL_EVIDENCE_PROFILE_DEFINED=true
COLLECTOR_OPERATIONAL_EVIDENCE_NEGATIVE_CONTROLS=45/45
COLLECTOR_OPERATIONAL_EVIDENCE_AGENT_REVIEW_COMPLETE=true
COLLECTOR_OPERATIONAL_MEASUREMENT_STARTED=false
OTEL_CONTROLS_IMPLEMENTED=false
OTEL_GATE_EVIDENCE_COLLECTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
