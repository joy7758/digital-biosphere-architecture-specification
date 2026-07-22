---
spec_id: TMAI-OTEL-SEMANTIC-CONFORMANCE-PROFILE-0.1
title: TMAI OpenTelemetry Semantic Conformance Profile v0.1
title_zh: TMAI OpenTelemetry 语义符合性配置 v0.1
status: proposed-not-adopted-not-executed
observed_at: 2026-07-22
decision_reference: DQ-023
primary_repository: digital-biosphere-architecture
case_count: 46
case_group_count: 8
tests_executed: false
validator_implemented: false
implementation_authorized: false
production_ready: false
---

# TMAI OpenTelemetry Semantic Conformance Profile v0.1

中文：TMAI OpenTelemetry 语义符合性配置 v0.1。

## 1. Purpose（目的）

本配置把 [`opentelemetry-semantic-conventions-profile.md`](opentelemetry-semantic-conventions-profile.md)
和 47 项 [semantic mapping catalog](opentelemetry-semantic-mapping.v0.1.json)
转化为可预注册、可逐项执行、可失败关闭并可绑定生产闸门的 conformance
contract（符合性合同）。

它回答“未来实现需要怎样证明字段解释正确且没有越权”，但不采纳 `DQ-023`，
不实现 validator（验证器），不运行测试，不修改 DBOS/SAEE，也不产生 Telemetry、
Identity、Execution、Evidence、Verification、Permission 或 SAEE Evaluation。

```text
Exact upstream source
  -> exact mapping rule
  -> deterministic fixture
  -> observed mapping or rejection
  -> authority and data-governance assertions
  -> immutable result binding
  -> independent review

Case catalog defined != Test executed
Schema valid != Semantic conformance
Telemetry mapped != DBOS fact created
Result set PASS != Gate closed
```

## 2. Machine Contracts（机器合同）

- [`opentelemetry-semantic-conformance-cases.v0.1.json`](opentelemetry-semantic-conformance-cases.v0.1.json)：46 项预注册用例；
- [`schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-case-catalog.schema.v0.1.json)：目录形状和无权力效果约束；
- [`schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json`](schemas/opentelemetry-semantic-conformance-result-set.schema.v0.1.json)：逐用例结果、实现／环境／验证器绑定；
- [`examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json`](examples/opentelemetry-semantic-conformance-result-set.not-assessed.example.json)：synthetic `NOT_ASSESSED` 示例。

## 3. Exact Contract Binding（精确合同绑定）

每次执行必须冻结：

| surface | required binding | 当前状态 |
|---|---|---|
| OTel Specification | `v1.59.0@a824fb4eba795c5c65dd397b3d22e7c28e934de3` | candidate |
| core Semantic Conventions | `v1.43.0@89aae438b3b3b0a8dd33003c9d70592baf7dbd0d` | `DQ-023` 未决定 |
| GenAI Semantic Conventions | `2e994c6d59a93bb4fc1752c5378eedb9b8e14d6b` | pinned Development candidate |
| OTLP | `v1.11.0@790608c4d51e6ffc12210b541e8514cbed9e91a4` | `DQ-022` 未决定 |
| mapping catalog | path + SHA-256 + catalog ID | digest 尚未冻结 |
| conformance catalog | path + SHA-256 + catalog ID | digest 尚未冻结 |
| implementation | repository + source commit + artifact digest | 不存在 |
| environment | environment ID + runtime/config digest | 不存在 |
| validator | ID + version + artifact digest | 未实现 |

任一 source、mapping、catalog、implementation、configuration、runtime environment
或 validator digest 改变，旧结果不得自动继承。

## 4. Eight Required Case Groups（八个必需用例组）

| group | purpose | minimum gate |
|---|---|---|
| `SEM-CG-VERSION_SOURCE` | exact tag/commit/schema URL/source binding 与 drift | `DQ-023` review；执行需 `DQ-018` |
| `SEM-CG-CORE_STABLE` | Resource、SDK、Scope、Trace、Span、Error Stable metadata | `DQ-018/PR-G2` |
| `SEM-CG-GENAI_METADATA` | Agent、workflow、model、usage、tool、evaluation Development fields | `DQ-018/PR-G2` |
| `SEM-CG-SENSITIVE_CONTENT` | 8 类默认禁用内容与完整 Data Governance opt-in | `DQ-018/PR-G5` |
| `SEM-CG-DEPRECATED_DRIFT` | deprecated、unknown、mapping/upstream drift | `DQ-018/PR-G2` |
| `SEM-CG-AUTHORITY_BOUNDARY` | Identity、Execution、Capability、Permission、Evidence、SAEE 权力注入 | `DQ-018/PR-G2` |
| `SEM-CG-CARDINALITY` | Metric label 禁止项、预算、overflow、no-silent-drop | `DQ-020/PR-G3` |
| `SEM-CG-RESULT_BOUNDARY` | 结果集 fail closed、digest、review 与 gate 非自授权 | `PR-G2/PR-G3` |

46 项用例覆盖全部 47 个 mapping ID；部分跨字段用例会重复覆盖高风险字段。
每个 mapping 至少必须被一个 case 覆盖，但“被列出”不表示测试已经执行。

## 5. Fixture Rules（夹具规则）

所有用例必须使用 deterministic fixture（确定性夹具），并记录：

- fixture ID、media type、size 和 SHA-256；
- signal surface、Instrumentation Scope 和 source version；
- 原始属性顺序不作为语义；重复键、类型错误、超长值和未知字段单独测试；
- 预期 mapping IDs、expected outcome、limitations 和 forbidden effects；
- content fixture 只能是 synthetic canary（合成金丝雀），不得包含真实 prompt、凭证、个人、医疗、金融或客户数据；
- rejected raw material 进入隔离测试输出，不进入 canonical DBOS object。

## 6. Execution Layers（执行层）

### 6.1 Offline semantic adapter layer（离线语义适配层）

对应未来 `DQ-018/S1`：只允许纯函数／离线 adapter、合成夹具、无 listener、
无 Collector、无外部网络、无 DBOS canonical write。验证字段选择、类型、稳定性、
unknown/deprecated 处理和所有 authority boundary。

### 6.2 Authenticated telemetry path（认证遥测路径）

对应未来 `DQ-020/S3`：只有 deployment Owner、认证、TLS、Collector distribution、
component/image/config digest、安全、容量和 rollback 齐备后，才允许验证 Collector
transformation 后的字段来源、redaction、cardinality 和 drift。Collector transformation
必须单独记录，不能伪装成原始 SDK 输出。

### 6.3 Trusted DBOS binding layer（可信 DBOS 绑定层）

只有独立 `DBOS_CONTEXT`、exact reference 与 binding record digest 可以把 observation
关联到 `entity_reference`、`execution_reference` 或 `capability_reference`。即使绑定
成功，也只是关联，不自动产生 Evidence、Verification、Permission 或执行成功。

## 7. Required Semantic Validation（必需语义验证）

JSON Schema 不能证明跨文件语义。未来 validator 还必须检查：

1. 46 个 case ID 唯一，8 个 group 精确覆盖全部 case；
2. 47 个 mapping ID 全部至少被一个 case 覆盖，case 不得引用未知 mapping；
3. mapping catalog、profile、case catalog 的 exact IDs 和 digests 匹配；
4. Stable / Development / Deprecated 与 exact source registry 一致；
5. `GENAI_DEVELOPMENT_PINNED` 不得被结果升级为 Stable；
6. 8 类 sensitive content 在默认禁用时全部拒绝；
7. opt-in 缺任一 decision/policy/allowlist/retention/residency/access/redaction binding 时拒绝；
8. `tmai.*`、`dbos.*`、`saee.*` 和裸 authority-like fields 被拒绝；
9. Metric labels 不含 instance/trace/span/agent/conversation/tool-call IDs；
10. mapping、case、result 和 validator effects 全部为 false；
11. PASS 时 required case set 与 case result set 一致，summary 可重算；
12. `UNKNOWN`、`REJECTED`、`PARTIAL`、failure 和 limitation 被保留；
13. synthetic result 永远不能 PASS；
14. result set 不能关闭 gate，独立 reviewer 和 Human Decision 仍为必要条件。

## 8. Result Evidence Contract（结果证据合同）

每个已执行 case 至少记录：

```text
case_id
fixture_id_and_digest
mapping_catalog_digest
conformance_catalog_digest
implementation_commit_and_artifact_digest
environment_and_configuration_digest
validator_id_version_and_digest
input_signal_and_attribute_inventory
matched_mapping_ids
output_projection_digest
rejection_or_limitation_codes
authority_assertions
data_governance_assertions
started_at_and_ended_at
result=PASS|FAIL|BLOCKED|NOT_ASSESSED
raw_observation_refs
```

`PASS` 表示该 case 的预期映射／拒绝行为被直接观察，不表示字段是真实的、Agent
可信、执行完整、Evidence 有效或部署生产就绪。结果集必须由独立 validator 验证
catalog/digest/case-set/summary，并由独立 reviewer 审查。

## 9. Gate Binding（闸门绑定）

- `DQ-023`：只决定是否采纳语义参考与 mapping contract；
- `DQ-018`：只可能授权离线 Telemetry Admission Foundation；
- `DQ-020`：只可能授权认证 transport/Collector staging；
- `PR-G2`：要求离线语义 mapping、authority 和 failure retention 直接证据；
- `PR-G3`：要求真实 hop 的 transformation/cardinality/data-governance 证据；
- `PR-G5`：要求敏感数据、安全、恢复和 incident controls；
- `PR-G6/PR-G7`：仍需 bounded pilot 和 Human Production Decision。

任何 conformance result 都不能自行关闭上述 gate。

## 10. Agent Recommendation Question（智能体推荐问题）

> 如果潜在 Agent developer 需要供应商中立、版本钉住、失败关闭且不把 telemetry
> 提升为身份／权限／证据事实的语义符合性合同，是否会推荐本配置作为未来实现和
> 互操作测试的架构输入？

回答必须同时区分：contract recommendation、implementation authorization、
conformance evidence 和 production customer recommendation。

[`OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md`](../OTEL-SEMANTIC-CONFORMANCE-AGENT-RECOMMENDATION.md)
记录两路独立 provider 的初审和证据复核。两路最终都推荐本合同作为 bounded
architecture/governance reference（有界架构／治理参考）进入 Human Review；审查前
必改项为 0。该结果不采纳 `DQ-023`，不表示 validator、interoperability 或 production
customer recommendation 已成立。

## 11. Current State（当前状态）

```text
SEMANTIC_CONFORMANCE_PROFILE_DEFINED=true
SEMANTIC_CONFORMANCE_CASE_CATALOG_DEFINED=true
SEMANTIC_CONFORMANCE_CASE_COUNT=46
SEMANTIC_CONFORMANCE_CASE_GROUP_COUNT=8
SEMANTIC_MAPPING_COVERAGE=47/47
SEMANTIC_CONFORMANCE_RESULT_SET_SCHEMA_DEFINED=true
SEMANTIC_CONFORMANCE_CATALOG_NEGATIVES_REJECTED=12/12
SEMANTIC_CONFORMANCE_RESULT_NEGATIVES_REJECTED=23/23
SEMANTIC_CONFORMANCE_AGENT_REVIEW_COMPLETE=true
SEMANTIC_CONFORMANCE_FREEZE_RECOMMENDED_BY_TWO_AGENTS=true
DQ_023_REFERENCE_ADOPTED=true
SEMANTIC_VALIDATOR_IMPLEMENTED=false
SEMANTIC_CONFORMANCE_TESTS_EXECUTED=0
SEMANTIC_CONFORMANCE_EVIDENCE_COLLECTED=false
IMPLEMENTATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
PRODUCTION_READY=false
```
