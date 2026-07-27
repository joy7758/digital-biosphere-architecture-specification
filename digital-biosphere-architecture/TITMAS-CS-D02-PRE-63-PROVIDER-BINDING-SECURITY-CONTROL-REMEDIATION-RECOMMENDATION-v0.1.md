---
document_id: DBA-TITMAS-CS-D02-PRE-63-PROVIDER-BINDING-SECURITY-CONTROL-REMEDIATION-RECOMMENDATION-0.1
title: TITMAS Provider Binding Security Control Remediation Recommendation v0.1
title_zh: TITMAS 提供商绑定安全控制修复建议 v0.1
version: 0.1.0
status: exact-offline-classification-and-design-recommended-not-decided
maturity: Development
maturity_scope: entire-document
primary_repository: digital-biosphere-architecture
decision_candidate: CS-D02-PRE-63
standing_directive_reference: TITMAS-CS-STANDING-001
recommended_by: Codex
recommended_at: 2026-07-27T10:20:00+08:00
target_repository_observed: https://github.com/joy7758/titmas-integrations.git
target_branch_observed: codex/rb0-governance-baseline
target_commit_observed: 5ac891c5af88b1e9aeacdb3666217c6f832a57a6
target_write_authorized: false
implementation_authorized: false
external_execution_authorized: false
formal_security_review_completed: false
provider_integration_authorized: false
release_authorized: false
standard_ready: false
---

# TITMAS Provider Binding Security Control Remediation Recommendation v0.1

## Recommendation

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=OFFLINE_FINDING_CLASSIFICATION_AND_BOUNDED_REMEDIATION_DESIGN
NOT_RECOMMENDED_AS=IMPLEMENTATION_ORDER_OR_FORMAL_SECURITY_APPROVAL
EXACT_OPTION=CREATE_VALIDATE_AND_REMOTE_FREEZE_PRE63_SECURITY_CONTROL_CLASSIFICATION_AND_REMEDIATION_DESIGN
```

如果潜在用户需要把 PRE-62 两个模型提供的安全审查输入转化为可执行前的工程边界，我会
推荐先形成本 PRE-63 离线分类和设计包。它逐项区分 `REQUIRED`、`OPTIONAL`、
`UNSUPPORTED` 与 `OUT_OF_SCOPE`，并选择一个不降低 P0–P9 语义的最小修复方向。

我不会推荐直接修改 `titmas-integrations`。当前 target 只有 provider-neutral
（供应商中立）的不可变 phase-trace（阶段轨迹）数据契约，没有 HTTP client、Provider
binding、credential read、`httpcore` dependency（依赖）、网络执行或持久化。因此模型
finding 是未来实现的 risk hypothesis（风险假设）和 control input（控制输入），不是已
证实的当前漏洞。

## Direct Evidence

```text
PRE62_RESULT_SHA256=38932b5e2ed70c4b747c78fb420b9276580ff1a85ad47f5cb13d171bb5633d89
PRE50_PLANNING_RECOMMENDATION_SHA256=035e652882f03dc239babf32ccf3e49b0ed11bcc5cfc7d057fc0154cba0c4822
TARGET_COMMIT=5ac891c5af88b1e9aeacdb3666217c6f832a57a6
TARGET_README_SHA256=668d970473bb162133ea719b7710dbb546a74af22953a0a352d91c66cc6132a6
TARGET_SECURITY_SHA256=e6812082914ff49402fa604f49bfc5258178762d192d18daf61327944f9e7dc6
TARGET_PYPROJECT_SHA256=c231da797a8e513158009b9dbb17e8b290e81f7b40cfbf352b5a3fbd3ae31200
TARGET_INSTRUMENTATION_SHA256=eccfd27d0c5de7ef4262f1e4b71cbdab2d166386e74ffa793ccd5cac4b6204d8
TARGET_ENTRY_SHA256=ab5bc12886df1bcb0a16240b01e666198681f122ceb2d688e26acb8f0325ff7a
```

这些 hash 证明本建议所核对的输入和 target truth surface（目标事实表面）。它们不证明
安全审查、Provider support、供应链完整性或生产就绪。

## Finding Classification

| finding / candidate control | classification | disposition |
|---|---|---|
| P0 DNS 与 P1 TCP 可观测性无法分离 | `REQUIRED_BLOCKING` | 选择 bounded resolver observation + single resolved-address connect 设计；在独立契约、测试与实现决定形成前保持 binding implementation blocked |
| TLS certificate + hostname verification | `REQUIRED_BEFORE_NETWORK_BINDING` | 使用系统 trust store、原始 allowlisted hostname、SNI 与 hostname verification；禁止 `verify=false` |
| Certificate pinning | `OPTIONAL_NOT_DEFAULT` | 当前不强制；只有独立 threat model、rotation/rollback 方案和显式决定后才能采用 |
| Credential value 不落盘、不进日志 | `REQUIRED_BEFORE_NETWORK_BINDING` | 只在请求构造时读取指定变量；禁止环境 dump、Authorization value、raw body 和异常回显 |
| Credential rotation、revocation 与 secret-manager integration | `OUT_OF_SCOPE_CURRENT_DEVELOPMENT_REQUIRED_BEFORE_SUPPORTED_OPERATION` | 当前仅定义接口责任；不得把 secret-manager 写成已实现 |
| 累计 response-body 上限 | `REQUIRED_BEFORE_NETWORK_BINDING` | 保留 PRE-50 候选 `1048576` bytes；读取期间累计计数，超过立即失败并不保留 raw body |
| Sanitized error handling | `REQUIRED_BEFORE_NETWORK_BINDING` | 只保留枚举、HTTP status、bounded counts、digest 和 opaque reference；Provider error body 不落盘 |
| Exact dependency pin | `REQUIRED_BEFORE_BINDING_IMPLEMENTATION` | `httpcore==1.0.9` 仍只是待审候选；未完成 license/hash/vulnerability/transitive review 前不得加入 target |
| Dependency provenance、lock、SBOM 与 reproducible build | `OUT_OF_SCOPE_CURRENT_DEVELOPMENT_REQUIRED_BEFORE_RELEASE` | PRE-49 已证明两次 build hash 不一致；发布 gate 保持 open |
| Automatic retry、fallback、redirect、model substitution、JSON repair | `UNSUPPORTED_CONFLICTS_WITH_FAIL_CLOSED` | 保持全部禁用；不得用“graceful degradation”覆盖首次失败 |
| Incident runbook 与 private disclosure route | `OUT_OF_SCOPE_CURRENT_DEVELOPMENT_REQUIRED_BEFORE_SUPPORTED_OPERATION` | Security Contact、私密披露路径和运行 Owner 仍未指派 |

`REQUIRED` 表示未来相应 gate 的必要条件，不表示实现已获授权。`OUT_OF_SCOPE` 不表示不
重要，而表示它不能被当前 Development reference contract 假装完成。

## Selected Bounded P0 Remediation Design

推荐只设计、暂不实现：

```text
ALLOWLISTED_HOSTNAME
  -> P0 one explicit resolver invocation
  -> select one address under a frozen deterministic rule
  -> P1 one TCP connection to that exact address
  -> P2 TLS with original hostname as SNI and verification identity
  -> P3-P9 existing fail-closed flow
```

强制边界：

1. 一次请求最多一次 resolver invocation，不做备用 resolver；
2. DNS 失败直接成为首次失败，P1–P9 不执行；
3. 解析结果不得写入公开 phase event、receipt 或 Git；只允许 bounded result count、
   elapsed time 和 failure enum；
4. 地址选择规则必须版本化、确定且不自动尝试第二地址；
5. TLS 仍验证原始 allowlisted hostname，不使用 IP literal 作为身份；
6. 不重复解析，不允许 redirect、proxy、retry、fallback 或 alternate host；
7. resolver/backend 必须是可替换的有界组件，不成为中心 Runtime；
8. 设计必须在独立 Agent Review 和 Human Security Accountability 后才能进入实现建议。

该选择保留 P0–P9 完整语义，不把 P0 静默标为 PASS，也不为尽快实现而引入
`UNOBSERVED` 语义。其代价是多地址容错被有意关闭，网络可用性低于自动 fallback；
这是 Development fail-closed profile 的已知限制。

## Problem and Corrective Decomposition

| 当前不推荐原因 | 本阶段可修正问题 | 本阶段后仍保留 |
|---|---|---|
| 模型 finding 未经 source/necessity/compatibility 分类 | 形成逐项、机器可读分类 | 模型不是 Human Security Reviewer |
| P0/P1 边界未解决 | 冻结单次解析、单地址、原 hostname TLS 的设计约束 | 未实现、未测试、未审查 |
| TLS/credential/size/error 控制散落在叙述中 | 形成 normative-candidate control matrix | 不产生 target Capability |
| 供应链与 incident 建议可能被误当当前漏洞 | 分离 current code truth 与 future release/operation gate | SBOM、reproducible build、Owner 和 disclosure route 未完成 |
| “graceful degradation”可能覆盖首次失败 | 明确 retry/fallback 等为 unsupported | 生产可用性不作承诺 |

## Exact Offline Outputs

若 Standing Directive eligibility 成立，PRE-63 只允许在 DBA 创建：

```text
commercialization-standards-provider-binding-security-remediation/
  security-control-classification.v0.1.json
  security-control-classification.schema.v0.1.json
  p0-resolver-remediation-design.v0.1.json
  p0-resolver-remediation-design.schema.v0.1.json
  pre63-validation-result.v0.1.json
  pre63-validation-result.schema.v0.1.json
  pre63-execution-receipt.v0.1.json
  pre63-execution-receipt.schema.v0.1.json
  PRE-63-PROVIDER-BINDING-SECURITY-CONTROL-REMEDIATION-RESULT-v0.1.md
```

以及独立治理记录：

```text
TITMAS-CS-D02-PRE-63-PROVIDER-BINDING-SECURITY-CONTROL-REMEDIATION-DECISION-RECORD.v0.1.json
architecture/schemas/titmas-cs-d02-pre63-provider-binding-security-control-remediation-decision-record.schema.v0.1.json
```

## Validation and Stop Conditions

必须：

- 所有 JSON instance 通过 frozen Draft 2020-12 Schema；
- classification 恰好覆盖上述 11 个 finding/control；
- 每个 control 均有 source、necessity、compatibility、gate 和 false-effect；
- P0 design 保持一次解析、一次地址选择、一次连接、原 hostname TLS；
- receipt 绑定除自身外全部 PRE-63 artifact SHA-256；
- 相对链接、敏感词扫描、private path 扫描和 target clean check 通过；
- 保留 `FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false`。

以下任一发生立即停止：

- target commit 或任一直接证据 hash 漂移；
- P0 被合成 PASS、重复解析或静默 fallback；
- 模型 finding 被写成 proven vulnerability；
- certificate pinning 被无条件设为 mandatory；
- credential value、Authorization value、raw body、私密路径或 hidden reasoning 进入 artifact；
- 发生 target write、credential read、network/model request、dependency install 或实现修改；
- 产生 Provider support、conformance、security approval、release、production 或 commercial claim。

## Effects

```text
AUTHORITY_CHANGED=false
OWNERSHIP_CHANGED=false
TARGET_REPOSITORY_CHANGED=false
IMPLEMENTATION_AUTHORIZED=false
PROVIDER_INTEGRATION_AUTHORIZED=false
PROVIDER_SUPPORTED=false
FORMAL_SECURITY_REVIEW_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
DEPENDENCY_ADOPTED=false
P0_REMEDIATION_IMPLEMENTED=false
EXTERNAL_EXECUTION_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
STANDARD_READY=false
AGENT_CREATED=false
RUNTIME_CREATED=false
PERMISSION_CREATED=false
```

## Next Gate

PRE-63 通过只能使以下事项进入新的 Recommendation：

```text
NEXT_ACTION=FORM_EXACT_P0_RESOLVER_CONTRACT_AND_TEST_DESIGN_RECOMMENDATION
```

该后继仍然先做协议、Schema、负例和安全审查输入；不得自动进入
`titmas-integrations` 实现。

## Standing Directive Eligibility

本建议只有一个 exact option，输入 hash、target、输出 fileset、零网络/零 credential/
零 target write 范围、false effects 和 fail-closed stop conditions 均明确。若独立
Decision Record 形成，可按 `TITMAS-CS-STANDING-001` 执行上述离线包；standing
directive 不授权后继实现或正式 Security Review。
