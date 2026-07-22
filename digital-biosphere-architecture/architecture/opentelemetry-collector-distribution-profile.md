---
document_id: TMAI-OTEL-COLLECTOR-DISTRIBUTION-PROFILE-0.1
title: TMAI OpenTelemetry Collector Minimal Distribution Profile v0.1
title_zh: TMAI OpenTelemetry Collector 最小发行版画像 v0.1
status: proposed-ready-for-human-review-not-adopted-not-built-not-deployed
decision_reference: DQ-025
primary_repository: digital-biosphere-architecture
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# TMAI OpenTelemetry Collector Minimal Distribution Profile v0.1

中文：TMAI OpenTelemetry Collector 最小发行版画像 v0.1。

## 1. Purpose（目的）

本画像把 [`otlp-collector-production-profile.md`](otlp-collector-production-profile.md)
中的抽象 Collector（采集器）要求收窄为一个 exact-source、minimal、replaceable 和
agent-readable（精确来源、最小化、可替换、智能体可读）的发行版候选。

它解决 [`R-027`](../RISK-AND-BLOCKER-REGISTER.md)、`R-028` 与 `B-016` 中的三个缺口：

1. 没有 exact Collector release/component source（精确发行版／组件来源）；
2. 直接使用大而全 distribution（发行版）会扩大 receiver/exporter/extension 攻击面；
3. 直接使用过小 distribution 又缺少 memory limiting、health 与 persistent queue 基础。

本画像不创建 OCB manifest、binary、image、SBOM、signature、Collector config、listener、
Runtime、Telemetry、Evidence、Identity、Permission 或生产部署。

```text
Distribution selection != Build authorization
Build artifact != Approved configuration
Approved configuration != Deployment authorization
Collector health != Delivery or Trust
Collector output != Evidence
```

## 2. Exact Upstream Observation（精确上游观察）

2026-07-22 只读核验结果：

| source | exact binding | observed fact |
|---|---|---|
| Collector Releases | `v0.156.0` release commit `aa158b23c8f89d795b21a05a49b3978565dfebd4` | GitHub release 页面标为 latest；tag 已签名；只作候选 |
| Collector Core | `v0.156.0@0a6056f97e2e5fe8f3a52a45bc26d3fb64b731d4` | OTLP receiver/exporters Stable；memory limiter/batch Beta |
| Collector Contrib | `v0.156.0@41e24cd516dd69a5b4277465cdb2ff4ef0676f49` | transform Beta；file storage Beta；health check Alpha |
| Config providers | `envprovider/fileprovider v1.62.0` | exact official manifests 中的版本；禁止 HTTP(S) remote provider |

重要上游警告：`opentelemetry-collector-releases` 官方 README 明确说明 release tag
可能为修复发布问题而变化，不应作为唯一固定来源。因此 TMAI 必须同时固定：

- observed tag；
- exact repository commit；
- manifest/component metadata byte digest；
- 最终构建 dependency lock、SBOM、binary/image digest 和 signature/provenance；
- 后续发现 tag 或 source drift 时重新进入 Human Version Decision（人工版本决定）。

官方来源：

- [Collector v0.156.0 release](https://github.com/open-telemetry/opentelemetry-collector-releases/releases/tag/v0.156.0)；
- [official distributions](https://opentelemetry.io/docs/collector/distributions/)；
- [Collector hosting security](https://opentelemetry.io/docs/security/hosting-best-practices/)；
- [Collector configuration security](https://opentelemetry.io/docs/security/config-best-practices/)；
- [Collector resiliency](https://opentelemetry.io/docs/collector/resiliency/)；
- [Collector internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)；
- [Collector source/image signature verification](https://github.com/open-telemetry/opentelemetry-collector#verifying-the-images-signatures)。

引用不表示 OpenTelemetry 项目认证或支持 TMAI；OpenTelemetry 当前不认证第三方 distribution。

## 3. Prebuilt Distribution Assessment（预构建发行版评估）

机器事实源：[`opentelemetry-collector-component-inventory.v0.1.json`](opentelemetry-collector-component-inventory.v0.1.json)。

| candidate | exact manifest units | result | reason |
|---|---:|---|---|
| `otelcol-otlp` | 5 | `NOT_SELECTED` | 只有 1 receiver、2 exporters、2 providers；缺 memory limiter、batch、health、file storage |
| `otelcol` | 32 | `NOT_SELECTED` | 包含多个未需要 receiver/exporter/debug surface 与 remote providers；仍缺 file storage |
| `otelcol-k8s` | 74 | `NOT_SELECTED` | 含所需原语，但 Kubernetes discovery、9 connectors、15 receivers 等显著扩大第一画像攻击面 |
| `CUSTOM_MINIMAL_FROM_PINNED_UPSTREAM_COMPONENTS` | 8 components + 2 providers | `RECOMMENDED_FOR_HUMAN_REVIEW` | 只编译已列入 allowlist 的 upstream modules；仍需承担自建、升级和供应链责任 |

`custom minimal` 不是自行 fork OpenTelemetry，也不允许 TMAI 私自改变组件语义。它使用
OpenTelemetry Collector Builder（OCB）组合 exact upstream modules；任何自定义组件必须另立
ADR、Owner、威胁模型、API/ABI/version policy 和独立 conformance contract，v0.1 默认禁止。

## 4. Proposed Compiled Allowlist（拟议编译白名单）

| component | source/stability | bounded role | mandatory boundary |
|---|---|---|---|
| `receiver/otlp` | core `v0.156.0`; Trace/Metric/Log Stable | OTLP gRPC/HTTP intake | Profiles Alpha 不编译到 allowed signal；ack 只为 hop result |
| `processor/memory_limiter` | core；Beta | 资源保护和显式 refusal | 必须是每条 pipeline 的第一个 processor；refusal/drop 可见 |
| `processor/transform` | contrib；Beta | exact allowlist、content removal、redaction、非权威 normalization | upstream 明示 unsound transformation、identity conflict、orphan risk；固定 OTTL + `error_mode=propagate`，禁止改 ID/authority |
| `processor/batch` | core；Beta | 有界批处理 | 在 transform 后、export queue 前；不能跨 tenant 混批或丢 attribution |
| `exporter/otlp` | core；Trace/Metric/Log Stable | mTLS OTLP/gRPC destination | 每目标独立 queue/retry；不宣称 exactly-once |
| `exporter/otlphttp` | core；Trace/Metric/Log Stable | 有界 OTLP/HTTP interoperability | 未被 exact destination profile 选择时不启用 |
| `extension/file_storage` | contrib；Beta | per-replica sending queue WAL | 非 DBOS canonical store、非共识、非 `RPO=0` |
| `extension/health_check` | contrib；Alpha | 受限 liveness/readiness endpoint | 不公开；不证明 exporter、delivery、security 或 Evidence |

配置 provider 只允许：

- `fileprovider v1.62.0`：读取单一、已审查、本地文件；
- `envprovider v1.62.0`：只注入 secret reference 与有界环境标量。

HTTP、HTTPS、YAML-inline remote/dynamic providers 不进入候选 build。provider 存在也不表示
任意环境变量可以改变 component set、listener、processor order、network destination 或 policy。

## 5. Required Pipeline Order（强制管道顺序）

```text
OTLP receiver: explicit interface + TLS/mTLS + auth + byte/item/rate/concurrency limits
  -> memory_limiter
  -> transform: exact frozen program, error_mode=propagate
  -> batch: tenant-safe bounded batching
  -> destination-specific exporter queue/retry + file_storage
```

规则：

1. `memory_limiter` 必须是第一个 processor；
2. `transform` 默认 feature gate 可能把 error mode 变为 `ignore`，候选配置必须显式写
   `error_mode: propagate`，并通过 malformed/unsupported statement 负例证明不会静默继续；
3. OTTL 不得修改 trace/span parent IDs、metric identity、Resource DBOS-like identity、
   `tmai.*`、`dbos.*`、`saee.*`、Evidence、Verification、Permission、Authorization 或 Decision；
4. body/content 默认清空或不采集；保留字段必须来自 frozen allowlist + policy digest；
5. batch 不得跨 tenant/purpose/security domain；若组件无法证明该隔离，按 tenant 建独立 pipeline；
6. 每个 exporter 使用独立 queue、WAL namespace、retry budget 和 counters；
7. configuration 未列入 pipeline 的 compiled component 保持 inactive；编译存在不等于运行启用。

`error_mode: propagate` 只是禁止静默吞掉 transform error，不自动证明 failure classification
（失败分类）正确。确定性数据错误若被 receiver/exporter 当作 retryable，可能形成 poison retry
（毒消息重试）或整批阻塞。staging 必须证明：

- 配置／OTTL parse error 在启动前失败；
- runtime deterministic transform error 不形成无限重试或隐藏丢失；
- permanent bad material 与 transient downstream failure 分开记账；
- 若 exact upstream component 不能提供有界、可复验的行为，该 transform 不得用于 untrusted
  ingress，相关 normalization 必须退回 offline DBOS admission adapter，`PR-G3` 保持关闭。

## 6. Excluded Surface（排除表面）

v0.1 build 不包含：

- Profiles signal；
- `debug` / `file` exporter；
- Jaeger、Zipkin、Prometheus、Kafka、hostmetrics、Kubernetes discovery receiver/exporter；
- pprof、zPages、OpAMP；
- HTTP(S) remote config provider；
- tail sampling、routing/failover connectors、dynamic component loading；
- 所有未列入 8-component allowlist 的组件。

排除不是永远禁止。未来确需 stateful routing、message queue 或 Kubernetes discovery 时，必须
以独立 workload、failure domain、stability、component/source digest 和 Human Decision 增量采用，
不得把 `otelcol-k8s` 整包切换当作快捷升级。

## 7. Build and Supply-chain Gate（构建与供应链闸门）

只有 `DQ-025` 采纳 candidate inventory 且另有实现授权后，build job 才能产生：

```text
exact OCB version and digest
exact source commits and module checksums
normalized OCB manifest + sha256
dependency graph / go.sum lock
binary per-platform digest
container image digest, never floating tag
SPDX or CycloneDX SBOM digest
license inventory
SLSA-compatible provenance or equivalent signed build statement
signature identity / issuer / verification record
vulnerability scan database/version/time + exceptions
reproducible-build comparison or explicit non-reproducibility limitation
component inventory extracted from the built binary
```

官方 prebuilt image 的 cosign verification 示例不能自动证明 TMAI custom image；TMAI 必须为
自己的 build pipeline、builder identity、source digest 和 output 签名负责。

Release page signed tag 也不是 binary/image content proof。tag、commit、asset checksum、SBOM、
provenance 与 signature 是不同证明，必须分别记录。

### 7.1 Minimum build evidence（最小构建证据）

以下项目缺一项即 `BLOCKED`，不得由 aggregate `build_pass=true` 代替：

1. exact OCB/module/source commit 与 byte digest；
2. normalized manifest、dependency graph 和 checksum lock；
3. binary/image/platform digest 与 extracted component inventory；
4. SPDX/CycloneDX SBOM 和 license inventory；
5. builder identity、issuer、source/material subjects 和 signed provenance；
6. signature verification policy/result；
7. vulnerability scanner、database digest/version、scan time 和 scope；
8. reproducible-build comparison；若不能 bit-for-bit reproducible，必须记录原因、可比字段、
   independent rebuild 和 residual risk，不能写成 `PASS`；
9. independent technical/security review references。

### 7.2 Vulnerability and stability response（漏洞与稳定性响应）

- source、builder、Go toolchain、OS/base image、direct/transitive module 和 runtime image 均进入扫描；
- policy-blocking vulnerability、known exploited issue、invalid signature 或 component stability/
  warning/feature-gate drift 立即阻止新 promotion，并可触发已批准 artifact `REVOKED`；
- exception 必须包含 vulnerability、affected digest/environment、exploitability、compensating control、
  Owner、Reviewer、expiry 和 Human Decision；build job 不能自批 exception；
- 修复必须生成新 artifact digest、SBOM、provenance、scan 和 conformance result，不能覆盖旧记录；
- scanner 无结果、数据库过期或 source unavailable 是 `UNKNOWN/BLOCKED`，不是“无漏洞”。

## 8. Configuration Gate（配置闸门）

Proposed deployment-level defaults（拟议部署级默认值）和未决空位登记在
[`opentelemetry-collector-deployment-profile.v0.1.json`](opentelemetry-collector-deployment-profile.v0.1.json)，
覆盖关系见 [`opentelemetry-collector-deployment-readiness-matrix.md`](opentelemetry-collector-deployment-readiness-matrix.md)。
该对象保持 `configuration_created=false`，不能作为真实 Collector 配置输入。

配置必须独立于 build inventory，并满足：

- exact build/image/component inventory digest；
- normalized, secret-redacted config digest；
- TLS/mTLS endpoint、CA/cert/key secret references 与 rotation/revocation policy；
- listener/exporter network allowlist；
- receiver size/rate/concurrency/decompression limits；
- memory soft/hard limit、batch、queue、retry、WAL/disk/retention budget；
- fixed OTTL source + artifact digest + semantic delta report；
- self-telemetry endpoint/path 与 independent failure path；
- per-tenant pipeline or proven tenant isolation；
- graceful drain、rollback、config drift 和 emergency change policy；
- unused compiled component rejection and unknown component/config field failure。

生成或验证配置不打开 listener；configuration `PASS` 不等于 deployment authorization。

v0.1 明确拒绝 remote config 与 OpAMP。更新机制仅允许 immutable versioned config 经
static/security/synthetic gates、canary、滚动重启和 exact digest rollback。若未来确需动态控制面，
必须先扩展 component/provider inventory 并完成独立 Human Decision，不能把管理便利性当作安全要求。

Cross-tenant batching validation（跨租户批处理验证）必须同时使用两个真实隔离测试租户：交换
tenant reference、相同 payload digest、枚举 queue key、错误响应、restart replay 和 destination
failure，证明 batch/queue/WAL/error/self-telemetry 均不泄露另一租户的存在、内容或计数。任何
组件不能提供该证明时，必须使用 tenant-separated pipeline/process/storage；不得靠命名约定通过。

## 9. Runtime, Security and Resilience Obligations（运行、安全与韧性义务）

生产候选必须直接证明：

- non-root、read-only root filesystem、dropped capabilities、seccomp/AppArmor 或等价；
- file storage 独立 writable mount、单 replica writer、quota、full/corrupt/PVC-loss handling；
- unauthenticated、expired/revoked/wrong-tenant certificate 全部拒绝；
- secret canary 不出现在 config dump、logs、metrics、errors、diagnostics 或 output；
- 1x steady、2x sustained、5x bounded burst 的首个 refusal/drop point；
- restart replay、duplicate、unknown delivery、retry exhaustion、多目标隔离；
- readiness 在 queue saturation/exporter failure 时 fail closed，而 liveness 不制造重启风暴；
- self-telemetry independent path 可在主 exporter 失败时报告 queue/drop/failure；
- mixed version、config drift、rolling rollback、component CVE revocation；
- `OTLP success -> Evidence absent`、`health OK -> production gate absent` 等权力负例。

`health_check` 为 Alpha，只能作为一个 bounded signal（有界信号）。生产 readiness 必须由部署层
把 process health、receiver acceptance、queue saturation、WAL health、exporter reachability 和
config drift 组合后决定；Alpha extension 单独 `200 OK` 不得进入 load balancer readiness、SLO
pass 或 production gate。若无法独立验证该组合，移除 health extension 或保持 `PR-G3=FAIL`，
不得自行创建 TMAI health authority。

## 10. Version and Revocation Rule（版本与撤销规则）

```text
NEW_RELEASE_OR_TAG_DRIFT_OBSERVED
  -> exact commit/manifest/module/metadata delta
  -> component stability + feature-gate + warning delta
  -> security/CVE + config/schema behavior review
  -> inventory and conformance fixtures updated
  -> agent recommendation
  -> Human Version Decision
  -> build authorization remains separate
  -> deployment authorization remains separate
```

紧急 CVE 可以撤销 candidate/build/deployment approval，但不能静默改 tag、image 或 component。
撤销后保留历史 digest、受影响环境、停止时间、处置和重验证引用。

## 11. Human Review Readiness vs Future PASS（人工审查就绪与未来通过分离）

`READY_FOR_REVIEW` 只要求候选 scope、exact source、component/stability inventory、风险、选项、
non-claims 和采纳后义务足够清晰，可由 Human Architecture Authority 作出 `DQ-025` 决定。
它不要求先批准这个决定，也不要求先构建或执行；否则会形成“决定前必须已有决定／实现”的循环。

以下是 adoption 后、未来某一具体 build/config/runtime result 申请 `PASS` 时的 prerequisites，
不是提交本架构候选给 Human Review 前的文档修正：

- 六个适用 Decision 的有效 reference、decider 和 timestamp；
- binary/image/SBOM/license/provenance/signature/vulnerability/reproducibility direct evidence；
- exact configuration/runtime/environment binding；
- 48/48 direct case result；
- independent technical/security review records；
- implemented validator 的 cross-document、artifact existence、review separation 和 time-order reconciliation。

当前记录的 `115/115` Schema negatives 与 `4/4` future-validator semantic negatives 是 ephemeral
in-memory contract rehearsal（临时内存契约演练）。后者只检验拟议 validator predicate 能拒绝
duplicate/unknown case set、same reviewer 和 reversed window；没有 validator artifact、version、digest、
report 或运行事实，因此 `VALIDATOR_IMPLEMENTED=false` 与 `RUNTIME_CASES_EXECUTED=0` 保持不变。

## 12. Decision and Gate Binding（决策与闸门绑定）

- `DQ-025`：只决定是否采纳 exact `v0.156.0` minimal component inventory；
- `DQ-022`：OTLP wire reference，独立决定；
- `DQ-023`：Semantic Convention mapping，独立决定；
- `DQ-024`：Schema/Resource/Entity provenance，独立决定；
- `DQ-018`：offline DBOS adapter/validator implementation，不能构建或运行 Collector；
- `DQ-020`：只有 prerequisites 和 evidence 满足后，才可能授权具体 build/config/staging；
- `PR-G3`：要求 exact distribution/config/runtime result，不因 `DQ-025` 自动通过。

## 13. Current Truth（当前事实）

```text
COLLECTOR_REFERENCE_CANDIDATE=v0.156.0
COLLECTOR_REFERENCE_COMMIT=aa158b23c8f89d795b21a05a49b3978565dfebd4
CUSTOM_MINIMAL_COMPONENTS_PROPOSED=8
CONFIG_PROVIDERS_PROPOSED=2
EXACT_SOURCE_BYTES_VERIFIED=11/11
INVENTORY_NEGATIVE_CONTROLS_REJECTED=18/18
CATALOG_SCHEMA_NEGATIVE_CONTROLS_REJECTED=16/16
CATALOG_SEMANTIC_NEGATIVE_CONTROLS_REJECTED=6/6
RESULT_SCHEMA_NEGATIVE_CONTROLS_REJECTED=115/115
FUTURE_VALIDATOR_SEMANTIC_NEGATIVE_REHEARSAL=4/4
POST_HARDENING_TWO_MODEL_REVIEW_COMPLETE=true
PREBUILT_DISTRIBUTION_SELECTED=false
CUSTOM_DISTRIBUTION_ADOPTED=true
BUILD_MANIFEST_CREATED=false
BINARY_BUILT=false
IMAGE_BUILT=false
SBOM_CREATED=false
SIGNATURE_VERIFIED=false
CONFIGURATION_CREATED=false
VALIDATOR_IMPLEMENTED=false
RUNTIME_CASES_EXECUTED=0
LISTENER_OPENED=false
COLLECTOR_DEPLOYED=false
TELEMETRY_COLLECTED=false
DQ_025_STATUS=DECIDED_REFERENCE_ADOPTED
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
