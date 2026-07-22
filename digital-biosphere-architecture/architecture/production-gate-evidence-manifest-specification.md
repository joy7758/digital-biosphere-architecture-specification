---
spec_id: TMAI-PRODUCTION-GATE-EVIDENCE-MANIFEST-0.1
title: TMAI Production Gate Evidence Manifest Specification v0.1
title_zh: TMAI 生产闸门证据清单规范 v0.1
status: proposed-contract-no-validator-or-runtime
architecture_owner: digital-biosphere-architecture
implementation_authorized: false
deployment_authorized: false
production_ready: false
---

# TMAI Production Gate Evidence Manifest Specification v0.1

中文：TMAI 生产闸门证据清单规范 v0.1。

## 1. Purpose（目的）

本规范定义每个 `PR-G0`–`PR-G7` gate（闸门）如何提交 machine-auditable evidence manifest（机器可审计证据清单）。它把测试、制品、配置、SLO、OpenTelemetry delivery accounting（交付核对）、安全发现、恢复演练、Owner、Review 和 Human Decision 绑定到一个 exact claim scope（精确声明范围）。

它不实现 validator，不运行测试，不生成 Evidence Object，不授权 implementation/deployment，也不允许一个 JSON 文件自己把 gate 改成 `PASS`。

```text
Evidence Manifest = indexed claims + immutable references + limitations
Evidence Manifest != Evidence Truth
Schema Valid != Gate Pass
Gate Pass != Production Authorization
Production Decision != Deployment
```

## 2. Contract Artifacts（契约工件）

| artifact | role | current effect |
|---|---|---|
| [`schemas/production-gate-evidence-manifest.schema.v0.1.json`](schemas/production-gate-evidence-manifest.schema.v0.1.json) | JSON Schema 2020-12 shape contract（形状契约） | 只验证结构和少量跨字段不变量 |
| [`production-gate-evidence-profiles.v0.1.json`](production-gate-evidence-profiles.v0.1.json) | 每个 gate 的 required coverage、SLO、Owner、drill 和 observation profile | `PROPOSED_NOT_ADOPTED`；不能独立关闭 gate |
| [`examples/production-gate-evidence-manifest.not-assessed.example.json`](examples/production-gate-evidence-manifest.not-assessed.example.json) | synthetic `NOT_ASSESSED` 示例 | 不是运行结果或证据 |
| [`opentelemetry-production-alignment-matrix.md`](opentelemetry-production-alignment-matrix.md) | OTel 官方要求到 TMAI control/gate/evidence 的 crosswalk（交叉映射） | 不证明 OTel conformance |
| [`otlp-v1.11-conformance-profile.md`](otlp-v1.11-conformance-profile.md) | OTLP selected scope、四层符合性、size/retry/acceptance 和 gate binding | `REFERENCE_ADOPTED_NOT_EXECUTED` |
| [`otlp-v1.11-conformance-cases.v0.1.json`](otlp-v1.11-conformance-cases.v0.1.json) | 56 个 exact preregistered cases（精确预注册用例） | `NOT_EXECUTED`；不采纳 reference |
| [`schemas/otlp-conformance-result-set.schema.v0.1.json`](schemas/otlp-conformance-result-set.schema.v0.1.json) | case-level result、catalog/decision/implementation/environment binding、summary 和 fail-closed PASS shape | 只定义结果结构；不运行 validator |
| [`examples/otlp-conformance-result-set.not-assessed.example.json`](examples/otlp-conformance-result-set.not-assessed.example.json) | 12 个 `PR-G2/S1` required cases 的 synthetic `NOT_ASSESSED` 示例 | `executed=0`；不是证据 |
| [`opentelemetry-semantic-conformance-cases.v0.1.json`](opentelemetry-semantic-conformance-cases.v0.1.json) | 8 组、46 个 semantic mapping/authority/privacy/cardinality/result cases | `NOT_EXECUTED`；47/47 mapping coverage 不表示实现 |
| [`schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json) | semantic case-level result、47/47 coverage、digest、Decision 与 independent review 绑定 | 只定义结果结构；不关闭 gate |
| [`examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json) | 46 个 required semantic cases 的 synthetic `NOT_ASSESSED` 示例 | `executed=0`；不是证据 |
| [`opentelemetry-schema-resource-conformance-cases.v0.1.json`](opentelemetry-schema-resource-conformance-cases.v0.1.json) | 7 组、45 个 Schema source/cache/transform、Resource provenance、Entity quarantine、data-governance/result cases | `NOT_EXECUTED`；不采纳 `DQ-024` |
| [`schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-schema-resource-conformance-result-set.schema.v0.1.json) | 45-case result、6-source、Decision、implementation/environment/policy、independent review 与零权力效果绑定 | 只定义结果结构；不关闭 gate |
| [`examples/opentelemetry-schema-resource-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-schema-resource-conformance-result-set.not-assessed.example.json) | 45 个 required provenance cases 的 synthetic `NOT_ASSESSED` 示例 | `executed=0`；不是证据 |
| [`opentelemetry-collector-distribution-conformance-cases.v0.1.json`](opentelemetry-collector-distribution-conformance-cases.v0.1.json) | 8 组、48 个 exact source/build/allowlist/config/security/durability/operability/capacity/authority cases | `NOT_EXECUTED`；不采纳 `DQ-025`、不构建或部署 Collector |
| [`schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-collector-distribution-conformance-result-set.schema.v0.1.json) | 48-case result、inventory/catalog/Decision/build/config/runtime/validator/双重独立审查与零权力效果绑定 | 只定义结果结构；不关闭 gate |
| [`examples/opentelemetry-collector-distribution-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-collector-distribution-conformance-result-set.not-assessed.example.json) | 48 个 required distribution cases 的 synthetic `NOT_ASSESSED` 示例 | `executed=0`；不是 build、runtime 或符合性证据 |

任何实现必须同时应用 schema、exact gate profile、digest/artifact verifier 和本规范的语义规则。只应用其中一部分必须返回 `NOT_ASSESSED` 或 `BLOCKED`。

## 3. Manifest Lifecycle（清单生命周期）

```text
DRAFT
  -> artifacts and results collected
  -> digest and scope reconciliation
  -> reviewer separation check
  -> FROZEN
  -> gate review
  -> PASS | FAIL | BLOCKED | NOT_ASSESSED
  -> REVOKED | ARCHIVED
```

- `DRAFT` 可重复生成，但不能用于 gate pass；
- `FROZEN` 必须有 `frozen_at` 和对 canonical serialization（规范序列化）的 `manifest_digest`；
- `REVOKED` 不删除原清单，必须记录 revocation reason/reference/time；
- `ARCHIVED` 只表示历史保留，不恢复效力；
- 任何 source、artifact、config、environment、workload、decision 或 profile 变化都必须产生新 manifest ID，不覆盖旧记录。

## 4. Claim Scope（声明范围）

Manifest 必须锁定：

- `gate_id` 和 `step_id`；
- production profile ID；
- environment ID/class 和 topology digest；
- workload scope、time window 和 observation duration；
- DBA architecture commit/tree、decision packet 和 normative file digests；
- implementation repo/source commit、artifact/config/SBOM/dependency digests；
- exact Owner、Reviewer、Human Decision 和 expiration/revalidation boundary。

一个 manifest 的 `PASS` 不能外推到另一个 environment、region、tenant model、workload、version、component set、config 或更长 retention/failure domain。

Architecture binding 对应 S0 Architecture Contract Freeze；implementation binding 对应后续 Deployment Profile Freeze。S0 manifest 允许 implementation binding 明示为 `null/NOT_ASSESSED`，但这使它只能评价架构 gate；`PR-G2`–`PR-G7` 的 exact profile 若缺 implementation binding 必须失败关闭。

## 5. Required Evidence Domains（必需证据域）

| domain | required meaning | forbidden shortcut |
|---|---|---|
| positive | 预注册正常路径结果 | “程序可启动”替代对象/状态/交付验证 |
| negative | 错误输入与越权请求 fail closed | 只测 happy path |
| fault | crash、network、disk、dependency、unknown commit、duplicate/partial/drop | mock exception 被写成真实 failure-domain evidence |
| security | authn/authz、secret、supply chain、payload/resource abuse、data access | scanner green 自动等于安全通过 |
| recovery | backup/PITR/restore/fencing/reconciliation | backup created 自动等于可恢复 |
| rollback | exact artifact/config/schema rollback 和 re-entry | 删除失败记录或重新部署同版本 |
| migration | forward/backward compatibility、mixed version、interruption | schema parses 自动等于兼容 |
| capacity | steady、2x sustained、5x bounded burst、queue/disk/memory limits | 单次 benchmark 自动等于 SLO |
| data governance | purpose、classification、residency、retention、access、incident | technical integrity 自动等于 legal/compliance approval |
| authority separation | Telemetry/Evidence/Verification/Evaluation/Decision/Execution 不越权 | `verified=true`、OTLP 200 或模型建议自动升级 |

`NOT_APPLICABLE_WITH_APPROVAL` 只能在 gate profile 允许、Human Decision 明示、理由和替代控制可追溯时使用；普通 `N/A` 不是合法状态。

## 6. Fail-closed Evaluation（失败关闭评价）

Gate evaluator（闸门评价器）的语义顺序必须是：

```text
1. schema validation
2. gate profile exact-version resolution
3. immutable architecture/decision binding verification
4. implementation artifact existence and digest verification
5. environment/topology/workload/time-window reconciliation
6. required coverage and SLO completeness
7. OTel emitted/received/accepted/rejected/partial/dropped/duplicate/unknown reconciliation
8. security/recovery/rollback/open-unknown review
9. Owner/Reviewer/Human Decision separation
10. scoped result computation
```

任一步 `FAIL`、无法访问、digest mismatch、superseded/revoked decision、missing required evidence 或 unresolved blocking unknown，最终只能是 `FAIL`、`BLOCKED` 或 `NOT_ASSESSED`。

涉及 `PR-G2` OTLP reference-decoder/semantic-adapter/provenance subset、`PR-G3`、`PR-G5` 或
`PR-G6` 的相关 `test_runs` 必须分别绑定 exact OTLP、semantic、Schema/Resource/Entity 或 Collector distribution
`conformance_catalog_ref`/digest、全部 executed `conformance_case_ids` 和独立
`case_results_ref`。一个 test run 只能绑定一个 catalog；同一 gate 同时要求多个 catalog
时必须形成可分别验证的 run/result binding，不能把 56 个 OTLP、46 个 semantic、45 个
Schema/Resource/Entity 和 48 个 Collector distribution case 混成一个自报汇总。profile 要求的 case group 必须 100% 覆盖；
任何 required case 为 `FAIL`、`BLOCKED` 或 `NOT_ASSESSED` 都不能形成 gate `PASS`。
不属于这四类 catalog 的
test run 使用 `null` 和空 case list，不得伪造关联。

`PR-G3`/`PR-G5` 还必须绑定
[`opentelemetry-collector-operational-evidence-profile.v0.1.json`](opentelemetry-collector-operational-evidence-profile.v0.1.json)
的 exact profile/schema digest、metric stability/naming/Resource/query bundle、独立 self-observation/
blackbox/storage/drift 结果、counter-reset/no-data/mixed-version 负例、alert delivery/route/runbook drill 和
end-to-end reconciliation。该 profile 复用上述 Collector/OTLP cases，不创建或伪造第五个 catalog。

## 7. PASS Invariants（通过不变量）

`result=PASS` 必须同时满足：

1. `manifest_status=FROZEN` 且 `synthetic_example=false`；
2. schema 和 exact gate profile 均通过；
3. DBA baseline 已 commit/push，所有 normative refs 与 decision packet digest 匹配；
4. implementation artifact、config、SBOM、dependency lock 和 environment topology 可读取且 digest 匹配；
5. gate profile 要求的 coverage 全为 `PASS` 或有明确允许的 approved alternative；
6. required SLO 全有预冻结 threshold、query、window、raw evidence 和 limitation；
7. 没有 unresolved blocking unknown；
8. 没有 unresolved exploitable Critical/High finding；risk acceptance 必须是独立 Human Decision 且不违反 zero-tolerance boundary；
9. Reviewer 不得只依赖 artifact producer 的自我声明；
10. decision 状态为 exact-scope `AUTHORIZED` 或 profile 明确允许 `NOT_REQUIRED`；
11. manifest 自身 `effects.*` 全为 `false`；它不能创建 Agent、Runtime、Permission、Evidence Truth 或生产授权。

测试数量、覆盖率、elapsed time 或 “all green” 不能替代这些条件。

## 8. OpenTelemetry Delivery Accounting（OpenTelemetry 交付核对）

涉及 `PR-G3`/`S3` 的 manifest 必须记录每 signal、hop 和 window 的：

```text
emitted
received
accepted
rejected
partial
dropped
retried
duplicate_confirmed
duplicate_suspected
unknown_delivery
queue_start
queue_end
```

Accounting 必须允许不等式和 unknown，不强迫“数字相等”。reconciliation result 只能是 `PASS_WITHIN_DECLARED_BOUND`、`FAIL`、`BLOCKED` 或 `NOT_ASSESSED`，并说明 sampling、filtering、redaction、batching、temporality、fan-out 和 retry 的影响。

OTLP response、Collector queue 或 backend ingest 只证明对应 hop；不能填充 DBOS canonical acceptance、Evidence Admission、Verification 或 Truth。

## 9. Human Decision Binding（人工决策绑定）

Manifest 引用 Decision，但不创建 Decision。Decision binding 至少包含：

- exact decision ID/reference/status；
- `decided_by_ref`、`decided_at`、scope digest；
- expiration/revalidation condition；
- accepted risks/conditions；
- revocation/supersession state。

Decision scope 与 manifest scope 不一致时必须 `BLOCKED`。Agent recommendation、Reviewer approval、CI status、GitHub merge 或 manifest `PASS` 都不能填充 `decided_by_ref`。

## 10. Revocation and Revalidation（撤销与复验）

以下任一变化使旧 manifest 不再支持新声明：

- architecture/decision/profile version 改变；
- source/artifact/image/component/config/SBOM/dependency digest 改变；
- topology、failure domain、network/identity/secret boundary 改变；
- workload、tenant、region、residency、retention 或 SLO 改变；
- Critical/High vulnerability、incident、restore failure 或 evidence tamper；
- Owner、runbook、on-call、Decision 撤销或过期。

旧记录继续 append-only 保留，状态改为 `REVOKED` 或 `ARCHIVED`；不得覆盖成“从未通过”。

## 11. Agent Recommendation Gate（智能体推荐闸门）

本合同是 [`production-implementation-sequence.md`](production-implementation-sequence.md) 已经两路 Agent 推荐的 Evidence Package Per Step（逐步证据包）的结构化投影，不扩大已评审的实施范围。两路评审均要求 immutable baseline、Owner/runbook、direct recovery/security evidence 和逐阶段 gate；本 Schema 回应这些要求，但 Agent recommendation 仍不是 Architecture Decision 或 Implementation Authorization。

## 12. Current State（当前状态）

```text
PRODUCTION_GATE_EVIDENCE_MANIFEST_SPEC_DEFINED=true
PRODUCTION_GATE_EVIDENCE_SCHEMA_DEFINED=true
PRODUCTION_GATE_PROFILE_REGISTRY_DEFINED=true
OTLP_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
OTLP_CONFORMANCE_RESULT_SET_VALIDATOR_IMPLEMENTED=false
SEMANTIC_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
SEMANTIC_CONFORMANCE_RESULT_SET_VALIDATOR_IMPLEMENTED=false
COLLECTOR_DISTRIBUTION_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
COLLECTOR_DISTRIBUTION_CONFORMANCE_RESULT_SET_VALIDATOR_IMPLEMENTED=false
PRODUCTION_GATE_EVIDENCE_VALIDATOR_IMPLEMENTED=false
PRODUCTION_GATE_EVIDENCE_COLLECTED=false
ANY_PRODUCTION_GATE_PASS_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
