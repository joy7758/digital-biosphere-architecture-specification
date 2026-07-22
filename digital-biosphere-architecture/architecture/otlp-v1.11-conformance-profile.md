---
spec_id: TMAI-OTLP-1.11-CONFORMANCE-PROFILE-0.1
title: TMAI OTLP v1.11 Conformance Profile v0.1
title_zh: TMAI OTLP v1.11 符合性配置 v0.1
status: proposed-not-adopted-not-executed
decision_reference: DQ-022
reference_version_adopted: false
tests_executed: false
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# TMAI OTLP v1.11 Conformance Profile v0.1

中文：TMAI OTLP v1.11 符合性配置 v0.1。

## 1. Purpose（目的）

本配置把 official `open-telemetry/opentelemetry-proto` candidate `v1.11.0@790608c4d51e6ffc12210b541e8514cbed9e91a4` 的 selected stable Trace/Metric/Log scope（选定稳定追踪／指标／日志范围）、size limits（大小限制）、partial success（部分成功）、retry（重试）与 `Retry-After` 语义，转化为可预注册、可逐项执行和可绑定生产闸门的 conformance contract（符合性合同）。

它不采纳该版本，不实现测试框架，不运行测试，不选择 SDK/Collector，不创建 listener、Telemetry、Evidence 或 Permission，也不证明生产符合性。

```text
Upstream requirement
  -> exact TMAI case
  -> exact implementation/environment binding
  -> direct test observation
  -> scoped gate review

Case catalog defined != Test executed
Protocol conformance != Deployment security
OTLP hop success != End-to-end delivery
Telemetry != Evidence
```

机器契约：

- [`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json)；
- [`schemas/otlp-conformance-case-catalog.schema.v0.1.json`](schemas/otlp-conformance-case-catalog.schema.v0.1.json)；
- [`schemas/otlp-conformance-result-set.schema.v0.1.json`](schemas/otlp-conformance-result-set.schema.v0.1.json)；
- [`examples/otlp-conformance-result-set.not-assessed.example.json`](examples/otlp-conformance-result-set.not-assessed.example.json)。

## 2. Reference Boundary（参考边界）

| field | value | current truth |
|---|---|---|
| repository | `open-telemetry/opentelemetry-proto` | official upstream |
| prior comparison point | `v1.10.0@ca839c51f706f5d53bfb46f06c3e90c3af3a52c6` | observed |
| adopted reference | `v1.11.0@790608c4d51e6ffc12210b541e8514cbed9e91a4` | `ADOPTED_REFERENCE_NOT_RUNTIME_PROOF` |
| selected signals | Trace、Metric、Log | Stable upstream scope selected for TMAI v0.1 |
| excluded | Profiles、Process Context | Profiles/Process Context are Development；Process Context is not OTLP transport |
| version authority | `DQ-022` | Human Decision pending |

Normative sources（规范来源）：

- [release](https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.11.0)；
- [v1.10.0...v1.11.0 comparison](https://github.com/open-telemetry/opentelemetry-proto/compare/v1.10.0...v1.11.0)；
- [changelog](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/CHANGELOG.md)；
- [OTLP specification at v1.11.0](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/docs/specification.md)；
- [maturity table](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.11.0/README.md#maturity-level)。

## 3. Four Conformance Layers（四层符合性）

### 3.1 Reference Decoder（参考解码器）

对应 `DQ-018/S1`。只允许 offline（离线）、no-listener（无监听器）、synthetic fixture（合成测试夹具）的 decoder/schema behavior（解码器／结构行为）验证：

- Trace/Metric/Log allowlist；
- Profiles 和 Process Context exclusion；
- malformed、empty、unknown-field 和 cross-version fixture；
- 不接收网络流量，不部署 Collector，不生成 Evidence。

### 3.2 Deployment Transport（部署传输）

对应 `DQ-020/S3`。只有 Human Decision、Owner、distribution/image/config digest、TLS/authn、network、capacity 和 rollback 输入齐备后，才允许验证真实 client/server/Collector hop：

- gRPC/HTTP request/response size limits；
- compression/decompression budget；
- partial、retryable、permanent、disconnect、queue/WAL outcomes；
- `Retry-After`；
- load、resource exhaustion、security 和 drift。

### 3.3 End-to-end Reconciliation（端到端核对）

对应 `PR-G3`，逐 hop 记录 emitted、received、accepted、rejected、partial、dropped、retried、duplicate 和 unknown。它允许不等式与 `UNKNOWN`，不允许用 Collector ack 推断 DBOS admission 或 Evidence completeness。

### 3.4 Authority Boundary（权力边界）

任何层都必须证明：

- Resource/Scope/attribute 不能创建 DBOS Identity；
- `verified=true`、OTLP success 或 Collector status 不能创建 Verification/Evidence/Truth；
- Capability/Permission/Decision 不能从 Telemetry 推导；
- SAEE Evaluation 不在本合同内执行；
- failure、partial、drop 和 unknown 不可静默删除。

## 4. Size-limit Profile（大小限制配置）

`v1.11.0` upstream recommended reference（上游建议参考）为：

| direction | measurement point | reference maximum | oversize outcome |
|---|---|---:|---|
| client request outbound | pre-compression | `64 MiB` / `67108864` bytes | do not send；local discard/failure record |
| server request inbound | post-decompression | `64 MiB` | gRPC `RESOURCE_EXHAUSTED` or HTTP `413`；non-retryable |
| server response outbound | pre-compression | `4 MiB` / `4194304` bytes | trim optional diagnostics；otherwise gRPC `RESOURCE_EXHAUSTED` or HTTP `500`；acceptance may be `UNKNOWN` |
| client response inbound | post-decompression | `4 MiB` | non-retryable local failure；request acceptance may be `UNKNOWN` |

这些值是 reference maximum（参考最大值），不是已部署配置。未来 deployment profile 必须冻结 exact lower/equal values；任何偏离都需要 capacity/security rationale 和重新生成 boundary fixtures。压缩前与解压后都必须计量，避免 compression/decompression bomb（压缩／解压炸弹）。

### 4.1 Wire Compatibility vs Mapped Shape（线协议兼容与映射形状）

TMAI 对 unknown field（未知字段）采用两层规则，不能混写：

1. OTLP protobuf wire layer（线协议层）：old/new selected-stable messages 的 additive unknown protobuf field 不得单独导致请求或响应被拒绝；receiver 处理已知字段，并记录 runtime 对 unknown-field preservation/ignore 的实际行为；
2. TMAI mapped envelope（映射信封）：进入 Telemetry Admission 的对象只允许 frozen schema allowlist；未知应用字段必须被明确省略或拒绝，不能动态产生 Identity、Evidence、Capability、Permission 或其他语义。

因此 `OTLP-CF-SIG-006/SIG-009` 的 wire compatibility 与 `TA-C005` 的 mapped-shape fail-closed 同时成立，不是互相矛盾。

## 5. Retry and Acceptance Profile（重试与接收状态）

| outcome | retry behavior | retained truth |
|---|---|---|
| full success | no retry | accepted at that hop only |
| populated partial success | no whole-request retry | accepted/rejected counts + bounded diagnostic |
| HTTP `400` or permanent bad data | no retry | rejected permanent |
| HTTP `429/502/503/504` or declared retryable gRPC status | bounded exponential backoff + jitter | retry attempts + terminal outcome |
| request oversize | no retry | not sent or rejected before processing |
| response oversize / disconnect after possible processing | no blind retry | `UNKNOWN` acceptance + reconciliation requirement |
| disconnect before acknowledgement | bounded retry may occur | duplicate possible + `UNKNOWN_DELIVERY` |

`Retry-After` 必须支持 delay-seconds 和 HTTP-date。invalid/past value 不能造成负等待或无限重试；future value 不能被提前绕过。若 server delay 超过本地总 retry budget，客户端终止并保留 `RETRY_BUDGET_EXHAUSTED`，不能在更早时间违反 server 指示再次发送。

## 6. Required Case Groups（必需用例组）

| group | purpose | earliest execution gate |
|---|---|---|
| `OTLP-CG-SIGNAL_SCHEMA` | Stable allowlist、Development exclusion、malformed/empty/cross-version | `DQ-018` after authorization |
| `OTLP-CG-GRPC_SIZE` | gRPC request/response and decompression boundaries | `DQ-020` after authorization |
| `OTLP-CG-HTTP_SIZE` | HTTP request/response and decompression boundaries | `DQ-020` after authorization |
| `OTLP-CG-RETRY_PARTIAL` | partial、retry matrix、`Retry-After`、disconnect | `DQ-020` after authorization |
| `OTLP-CG-DELIVERY_RECONCILIATION` | drop、sampling、duplicate、queue、unknown | `PR-G3` |
| `OTLP-CG-AUTHORITY_BOUNDARY` | identity/evidence/permission non-elevation | `DQ-018` after authorization |
| `OTLP-CG-DEPLOYMENT_SECURITY_CAPACITY` | auth/TLS、sensitive data、cardinality and burst boundary | `DQ-020` after authorization |

`required_case_ids` 的 machine source of truth（机器事实源）是 JSON catalog。当前共 56 cases；若 profile、catalog、schema 或 adopted reference 改变，旧测试结果不能自动继承。

## 7. Execution Evidence Contract（执行证据合同）

Case-level output（逐用例输出）必须符合 `otlp-conformance-result-set.schema.v0.1.json`。该结果集同时绑定 catalog digest、Decision、gate/step、implementation artifact、environment/topology、required cases、逐 case observation/evidence/limitation 和独立 review。Production Gate Evidence Manifest 的 `case_results_ref` 只能指向该结构或经 Version Governance 明确取代的后续版本。

Result Set 还必须绑定独立 `validation_binding`：validator ID/version/artifact digest、schema/semantic/case-set/summary checks、catalog/Decision/implementation/environment digest verification 和 validation report digest。当前 validator 未实现，因此合成示例全部为 `NOT_ASSESSED/false/null`；不能构造合法的 `PASS`。Schema 要求 `PASS` 时这些验证全部成功，但 Schema 本身不能验签或读取外部制品，最终 gate evaluator 仍必须重新验证引用。

每个 executed case（已执行用例）未来至少绑定：

```text
case_id
catalog_digest
adopted_reference_tag_and_commit
decision_refs
implementation_source_commit
artifact_image_component_config_digests
environment_topology_digest
transport_and_signal
fixture_digest_and_size
compression_mode
command_or_runner_ref
started_at_and_ended_at
protocol_status
retry_attempts_and_schedule
accepted_rejected_partial_drop_duplicate_unknown_counts
raw_evidence_refs
limitations
result=PASS|FAIL|BLOCKED|NOT_ASSESSED
```

对于 `PR-G3`：

- 所有 required case 必须有结果；
- required case pass rate 必须为 `1.0`；
- failed 或 `NOT_ASSESSED` required cases 数量必须为 `0`；
- `UNKNOWN` acceptance 可以是正确预期，但必须进入核对记录，不能被伪写为成功；
- 任一 artifact/config/reference digest 变化都需要新 run。

JSON Schema 不能验证计数相加、required IDs 与 result IDs 一致或 Decision scope 对齐；未来 validator 必须额外检查：

```text
summary.required == len(required_case_ids)
summary.executed == passed + failed
summary.required == passed + failed + blocked + not_assessed
case_result_ids are unique and subset of required_case_ids
PASS requires one result per required case
PR-G2 required set == SIGNAL_SCHEMA + AUTHORITY_BOUNDARY
PR-G3 required set == all 56 catalog cases
```

`UNKNOWN` acceptance case 可以在 expected behavior 被正确保留时得到 case `PASS`；这表示“未知被正确记录”，不是交付成功。

`effects.*=false` 是刻意的不变量：Result Set 只报告观察，永远不执行 state transition（状态转换）。是否关闭 gate 由独立 gate evaluator + Reviewer + Human Decision 决定；把 `production_ready=true` 写入结果文件会形成自我授权，因此被 schema 拒绝。

同一边界通过 `authority_boundary` 直接编码：Result Set 不是 Gate Decision 或 Human Authorization，不能改变 Runtime；独立 gate evaluator、独立 Reviewer 和 Human Decision 均为 gate closure 前置。该常量即使在 case `PASS` 时也不能改变。

## 8. Semantic Validation Rules（语义验证规则）

JSON Schema 只验证 shape（形状）。未来 validator 还必须检查：

1. case ID 唯一；
2. group 引用的 case 全部存在，且每个 case 至少属于一个 group；
3. `REFERENCE_DECODER` case 不得要求真实 listener/Collector/network；
4. `DEPLOYMENT_TRANSPORT` case 必须包含 `DQ-020`，并要求 auth/TLS/config/environment evidence；
5. `END_TO_END_RECONCILIATION` case 必须包含 `PR-G3` 和 delivery accounting；
6. `PROFILES`/`PROCESS_CONTEXT` 只能作为 rejection/exclusion case；
7. 每个 case 必须列出 forbidden inference；
8. 所有 effects 必须为 `false`；
9. `DQ-022` 未决定时，不得把 `adoption_status` 改成 adopted；
10. case result 不得自动修改 Decision、Permission、Evidence Truth 或 production status。

## 9. Gate Binding（闸门绑定）

- `DQ-022`：只决定是否采纳 exact external reference；
- `DQ-018`：只可能授权 Reference Decoder / Telemetry Admission Foundation 实施；
- `DQ-020`：只可能授权 authenticated transport/Collector staging；
- `PR-G3`：要求所有 required cases、逐 hop accounting、安全、恢复、容量与配置漂移直接证据；
- `PR-G6/PR-G7`：仍需要 bounded production pilot 和 Human Production Authorization，不能由符合性目录替代。

## 10. Current State（当前状态）

```text
OTLP_1_11_CONFORMANCE_PROFILE_DEFINED=true
OTLP_1_11_CONFORMANCE_CATALOG_DEFINED=true
OTLP_1_11_REFERENCE_ADOPTED=true
CONFORMANCE_VALIDATOR_IMPLEMENTED=false
CONFORMANCE_TESTS_EXECUTED=false
CONFORMANCE_EVIDENCE_COLLECTED=false
DQ_018_IMPLEMENTATION_AUTHORIZED=false
DQ_020_DEPLOYMENT_AUTHORIZED=false
PR_G3_PASS=false
PRODUCTION_READY=false
```
