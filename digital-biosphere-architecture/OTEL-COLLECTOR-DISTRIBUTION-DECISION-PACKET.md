---
document_id: TMAI-OTEL-COLLECTOR-DISTRIBUTION-DECISION-PACKET-20260722-001
title: OpenTelemetry Collector Minimal Distribution Adoption Decision Packet
title_zh: OpenTelemetry Collector 最小发行版采纳决策包
status: ready-for-human-review-not-decided
decision_id: DQ-025
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# OpenTelemetry Collector Minimal Distribution Adoption Decision Packet

中文：OpenTelemetry Collector 最小发行版采纳决策包。

## Decision Question（决策问题）

是否把 OpenTelemetry Collector Releases `v0.156.0` 的 exact source commits 和 8-component
custom minimal inventory（定制最小组件清单）采纳为 TMAI 首个 Collector distribution
architecture reference（采集器发行版架构参考）？

本决定只固定未来 build/config/staging 必须遵循的 source/component boundary。它不：

- 创建 OCB manifest、binary、image、SBOM、signature 或 configuration；
- 授权修改 DBOS/SAEE；
- 打开 OTLP listener；
- 部署 Collector 或收集 Telemetry；
- 创建 Evidence、Permission、Runtime 或 production claim；
- 替代 `DQ-020` 的独立 build/config/staging/deployment authorization。

## Source Facts（来源事实）

- 2026-07-22，官方 Collector Releases 页面把 `v0.156.0` 标为 latest；release commit 为
  `aa158b23c8f89d795b21a05a49b3978565dfebd4`；
- exact core commit 为 `0a6056f97e2e5fe8f3a52a45bc26d3fb64b731d4`；
- exact contrib commit 为 `41e24cd516dd69a5b4277465cdb2ff4ef0676f49`；
- 官方 releases README 明确警告 tags 可能变化，不能只依赖 tag；
- `otelcol-otlp` exact manifest 只有 5 个 component/provider units，缺生产候选所需
  memory limiter、batch、health 和 file storage；
- `otelcol` exact manifest 有 32 units，仍缺 file storage，且有多余 receiver/exporter/
  diagnostic/remote-provider surface；
- `otelcol-k8s` exact manifest 有 74 units，具备所需原语但攻击面显著过大；
- proposed custom inventory 只包含 8 components + 2 local providers；
- 8 components 中 health check 为 Alpha，file storage、memory limiter、batch、transform
  为 Beta；因此 “minimal” 不等于 “stable” 或 “production-proven”。

## Recommended Option（推荐选项）

`OPTION_A_CUSTOM_MINIMAL_PINNED_UPSTREAM_COMPONENTS`

推荐理由：

1. 精确保留 OTel OTLP interoperability（互操作）而不引入大而全发行版攻击面；
2. 包含 memory protection、bounded batching、redaction/allowlist、health 和 per-replica WAL
   所需最小原语；
3. component inventory、stability、warning、source commit 和 digest 可被机器验证；
4. 不引入自定义 Collector component，避免复制 DBOS admission/Evidence authority；
5. 未来每个新组件必须增量决策，而不是整包切换 distribution。

代价：TMAI 对 OCB build、dependency update、SBOM、signature/provenance、vulnerability response、
component regression 和 release cadence 承担明确维护责任。

## Options（选项）

| option | result | trade-off |
|---|---|---|
| `OPTION_A_CUSTOM_MINIMAL_PINNED_UPSTREAM_COMPONENTS` | 采纳 8+2 exact inventory 为架构参考 | 最小攻击面；需要自建、签名、SBOM、升级与完整符合性 |
| `OPTION_B_OTELCOL_OTLP_PREBUILT` | 使用最小官方 OTLP 发行版 | 供应链简单，但缺生产韧性／运维原语，不满足当前 profile |
| `OPTION_C_OTELCOL_K8S_PREBUILT` | 使用官方 Kubernetes 发行版 | 功能齐全，但 74 units 显著扩大攻击面和审查范围 |
| `OPTION_D_RETURN_FOR_REVISION` | 暂不采纳 | 必须指出 source、component、stability、security、resilience 或 authority 缺口 |

## Exact Human Decision Tokens（精确人工决定令牌）

```text
DQ-025=ADOPT_OTEL_COLLECTOR_V0_156_CUSTOM_MINIMAL_INVENTORY
decided_by_ref=<human-reference>
```

```text
DQ-025=ADOPT_OTEL_COLLECTOR_V0_156_PREBUILT_ALTERNATIVE
decided_by_ref=<human-reference>
selected_distribution=<otelcol-otlp|otelcol-k8s>
exception_reason=<required>
```

```text
DQ-025=RETURN_OTEL_COLLECTOR_DISTRIBUTION_FOR_REVISION
decided_by_ref=<human-reference>
revision_reason=<required>
```

## Accepted Scope If Option A Is Chosen（选择 A 时的接受范围）

- exact release/core/contrib commits and byte digests；
- 8 compiled component IDs and 2 local config providers；
- Trace/Metric/Log only；Profiles excluded；
- remote config、debug/file exporters、pprof/zPages/OpAMP、discovery receivers、connectors、
  tail sampling 和其他 unlisted components excluded；
- `memory_limiter -> transform(error_mode=propagate) -> batch -> per-destination exporter queue/WAL`；
- 48-case / 8-group pre-registered conformance contract；
- build、config、runtime、review 和 gate effects 恒 false，除非后续独立授权与直接证据存在。

## Required Follow-ups After Adoption（采纳后的必要后续）

1. 冻结 immutable DBA commit/tree 和 exact inventory/catalog/schema digests；
2. `DQ-022/023/024` 独立决定，不被 `DQ-025` 代替；
3. `DQ-018` 只可授权 offline DBOS adapter/validator，仍不可构建或部署 Collector；
4. 建立 deployment-specific repository、Owner、build pipeline、secret policy 和 environment；
5. 只有新的 `DQ-020` 人工决定可授权 exact build/config/staging；
6. 产生 binary/image/SBOM/license/provenance/signature/vulnerability/reproducibility evidence；
7. 执行 48/48 direct case-level tests，并与 56 OTLP、46 Semantic、45 Schema/Resource cases
   分开保存结果；
8. independent technical + security reviewers 审查，Human Gate 决定仍在结果之外。

其中 vulnerability process 必须覆盖 builder/toolchain/base image/direct+transitive dependencies，
exception 带 Owner/Reviewer/expiry/Human Decision；cross-tenant batching 必须用两个隔离测试租户
验证 queue/WAL/error/self-telemetry；Alpha health 只能作为输入信号，不能单独驱动 readiness 或 gate。

这些项目是 `OPTION_A` 被采纳后的 future PASS prerequisites，不是 Human Review 前置完成项。
`READY_FOR_REVIEW` 允许人类现在审查清晰的架构候选；不允许把尚未完成的 Decision、build、validator
或 48-case runtime execution 写成已完成。`115/115` result Schema negatives 与 `4/4`
future-validator semantic negatives 只是内存中的合同设计演练，不构成 validator implementation。

## Current Truth（当前事实）

```text
DQ_025_DECISION_RECORDED=false
AGENT_REVIEW_COMPLETE=true
POST_HARDENING_DELTA_REVIEW_COMPLETE=true
HUMAN_REVIEW_RECOMMENDED_BY_TWO_MODELS=true
BOUNDED_DESIGN_REFERENCE_RECOMMENDED_BY_TWO_MODELS=true
CURRENT_RUNTIME_RECOMMENDATION=DO_NOT_RECOMMEND
REQUIRED_DOCUMENT_CORRECTIONS_OPEN=0
POST_HARDENING_FACTUAL_OR_AUTHORITY_ERRORS=0
INVENTORY_NEGATIVE_CONTROLS_REJECTED=18/18
CATALOG_SCHEMA_NEGATIVE_CONTROLS_REJECTED=16/16
CATALOG_SEMANTIC_NEGATIVE_CONTROLS_REJECTED=6/6
RESULT_SCHEMA_NEGATIVE_CONTROLS_REJECTED=115/115
FUTURE_VALIDATOR_SEMANTIC_NEGATIVE_REHEARSAL=4/4
COLLECTOR_REFERENCE_CANDIDATE=v0.156.0
CUSTOM_MINIMAL_COMPONENTS_PROPOSED=8
CONFIG_PROVIDERS_PROPOSED=2
CONFORMANCE_CASE_GROUPS=8
CONFORMANCE_CASES=48
CONFORMANCE_TESTS_EXECUTED=0
CUSTOM_DISTRIBUTION_ADOPTED=false
BUILD_MANIFEST_CREATED=false
BINARY_BUILT=false
IMAGE_BUILT=false
CONFIGURATION_CREATED=false
LISTENER_OPENED=false
COLLECTOR_DEPLOYED=false
VALIDATOR_IMPLEMENTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```

审查记录：[`OTEL-COLLECTOR-DISTRIBUTION-AGENT-RECOMMENDATION.md`](OTEL-COLLECTOR-DISTRIBUTION-AGENT-RECOMMENDATION.md)。
