---
profile_id: DBA-CAPABILITY-PROVENANCE-REASSESSMENT-0.1
title: Capability Provenance Reassessment Profile v0.1
title_zh: 能力来源重新评估剖面 v0.1
status: proposed-reference-only-research-profile
primary_repository: DBA
intelligence_source: ../DBA-INTELLIGENCE-BRIEF-2026-07-24.md
observed_at: 2026-07-24
verified_at: 2026-07-25
implementation_authorized: false
dbos_change_authorized: false
saee_change_authorized: false
external_action_authorized: false
---

# Capability Provenance Reassessment Profile v0.1

## 1. Purpose（目的）

本剖面定义：当模型、数据集、Skill、工具、依赖、凭据、评测隔离或运行环境发生重大变化时，既有 Agent readiness（就绪性）、reliability（可靠性）或 trust（信任）结论何时必须失效、暂停或重新评估。

它是 DBA 的只读 Strategy / Research contract（战略／研究契约），不是供应链扫描器、Runtime、SAEE 新能力、DBOS admission 实现、合规证明或自动授权机制。

```text
PROFILE_STATUS=PROPOSED_REFERENCE_ONLY_RESEARCH_PROFILE
PRIMARY_REPOSITORY=DBA
TRIGGER_CAN_INVALIDATE_PRIOR_CONCLUSION=true
TRIGGER_CAN_REVOKE_PERMISSION=false
TRIGGER_CAN_CHANGE_RUNTIME_STATE=false
OUTPUT_IS_RECOMMENDATION_ONLY=true
IMPLEMENTATION_AUTHORIZED=false
DBOS_CHANGE_AUTHORIZED=false
SAEE_CHANGE_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
```

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

问题：如果潜在用户需要判断“上游模型、数据或依赖变化后，原来通过的 Agent 是否仍可使用”，智能体是否会推荐当前方案？

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=BOUNDED_REASSESSMENT_CONTRACT_AND_RESEARCH_PROFILE
NOT_RECOMMENDED_AS=SUPPLY_CHAIN_SCANNER_OR_COMPLIANCE_ENGINE
```

条件性推荐原因：

- 已把“观察到变化”“证据充分”“评价结论”“权限变化”和“执行动作”分开；
- 默认 fail closed（失败关闭）：证据缺失时进入 `HOLD_MISSING_EVIDENCE`，不继承旧结论；
- 不复制 Microsoft、OpenTelemetry、SCITT、SPIFFE、MCP Registry 或既有供应链安全工具；
- 允许不同平台提供输入，但不把平台日志、签名或收据自动升级为 Truth（真值）。

不推荐原因与修正：

| 不推荐原因 | 当前修正 | 剩余缺口／停止条件 |
|---|---|---|
| 只有概念，没有可判定触发条件 | 定义 T1–T5 触发类型和最小输入 | 未形成子项目 canonical mapping 前不实施 |
| 可能把重评估建议变成自动停机或撤权 | 固定 Recommendation ≠ Decision ≠ Execution | 任何状态写入仍需独立 Human Decision 和子项目授权 |
| 可能重复供应链扫描器 | 只消费外部发现与版本证据，不扫描或修复资产 | Scanner、SBOM、Registry 或 Credential work 不进入本剖面 |
| 可能把 SAEE 推成 compliance engine | SAEE 只在未来独立授权后评估证据充分性 | 无 SAEE 变更授权时停止在 DBA research 层 |

## 3. Trigger Taxonomy（触发分类）

| trigger | 含义 | 示例 | 默认动作 |
|---|---|---|---|
| `T1_IDENTITY` | 主体、工作负载身份或委托链变化 | issuer、workload identity、delegation scope 变化 | `REVIEW_REQUIRED` |
| `T2_CAPABILITY_PROVENANCE` | 模型、数据、Skill、工具或依赖来源变化 | digest、版本、registry、签发者、开放权重／重新打包或依赖图变化 | `REASSESSMENT_REQUIRED` |
| `T3_EXECUTION` | 执行或隔离前提变化 | sandbox escape、credential exposure、tool boundary drift | `REASSESSMENT_REQUIRED` |
| `T4_EVIDENCE` | 证据来源、完整性或可重放性变化 | receipt、signature、lineage、retention、monitor／verifier version 或 coverage 变化 | `HOLD_MISSING_EVIDENCE` |
| `T5_GOVERNANCE` | 法律、政策、人工接管或披露要求变化 | 适用规则、risk class、human review gate 变化 | `REVIEW_REQUIRED` |

同一事件可以触发多个类型。类型只用于路由，不证明风险、影响或责任归属。

## 4. Minimum Input Contract（最小输入契约）

每次重新评估至少需要：

```text
event_ref
observed_at
source_refs[]
affected_asset_refs[]
previous_conclusion_ref
previous_conclusion_scope
previous_evidence_refs[]
evidence_producer_refs[]
trigger_types[]
known_changes[]
unknowns[]
conflicts[]
human_owner_ref
```

每个 asset reference（资产引用）应在可得时包含：

- 稳定标识符、版本与 digest；
- registry／repository／issuer 来源；
- 依赖或工具边界；
- 评测环境与授权范围；
- 凭据或秘密是否可能受影响的布尔状态，不记录秘密值；
- 证据采集时间、保留和验证器版本。

每个 monitor／verifier evidence producer（监控器／验证器证据生产者）还应记录：

- exact model、prompt／policy 与 threshold version；
- in-scope、not-routed 与 unknown action types；
- routing rules、known bypass classes 与 red-team evidence；
- false-positive／false-negative assessment；
- independent verification reference。

详细字段见
[`Monitor Evidence Profile and Gap Matrix v0.1`](monitor-evidence-profile-and-gap-matrix-v0.1.md)。

缺少必需字段时不得用默认值补成“安全”或“未变化”。

## 5. Reassessment State Model（重新评估状态模型）

```text
NOT_TRIGGERED
  -> REASSESSMENT_REQUIRED
     -> HOLD_MISSING_EVIDENCE
     -> REVIEW_REQUIRED
     -> REVALIDATED_BOUNDED
     -> INVALIDATED
```

状态含义：

- `NOT_TRIGGERED`：没有发现适用变化；不证明资产安全；
- `REASSESSMENT_REQUIRED`：旧结论不能自动继承；
- `HOLD_MISSING_EVIDENCE`：材料不足或冲突，保持失败关闭；
- `REVIEW_REQUIRED`：材料存在但需要指定人类责任方判断；
- `REVALIDATED_BOUNDED`：只在精确资产、版本、环境、时间和用途范围内重新成立；
- `INVALIDATED`：原结论在声明范围内不再成立。

任何状态都不直接创建、撤销或修改 Capability、Permission、Authority、Entity、Execution 或 Release。

## 6. Decision Logic（判定逻辑）

```text
IF confirmed_material_change_affects(previous_conclusion_scope)
  THEN state = REASSESSMENT_REQUIRED

IF required_evidence_is_missing OR official_sources_conflict
  THEN state = HOLD_MISSING_EVIDENCE

IF reassessment_material_is_complete AND human_decision_is_required
  THEN state = REVIEW_REQUIRED

IF bounded_revalidation_passes AND exact_scope_is_recorded
  THEN state = REVALIDATED_BOUNDED

IF direct_evidence_refutes(previous_conclusion)
  THEN state = INVALIDATED
```

禁止：

- 将 telemetry presence（遥测存在）写成 execution correctness（执行正确）；
- 将 SCITT receipt（透明服务收据）写成 statement truth（声明真实）；
- 将 signature（签名）写成 authorization validity（授权有效）；
- 将 Microsoft、OpenTelemetry、MCP、SPIFFE 或 Registry 状态写成 DBA／DBOS／SAEE 采纳；
- 将 `REVALIDATED_BOUNDED` 跨版本、跨环境、跨租户或跨用途继承；
- 将单一 monitor 的 `no alert` 或低 suspicion score 写成安全、授权或证据充分；
- 将 MCP Trace Context、session／handle、tool metadata 或 OAuth result 写成 Identity、Capability、Permission、完整 Evidence 或 Truth；
- 将输出直接转成 DBOS 写操作或 SAEE 自动控制。

## 7. Repository and Authority Routing（仓库与权力路由）

| 事项 | primary repository | 本剖面允许 | 仍需独立授权 |
|---|---|---|---|
| 触发分类、状态语义、跨项目边界 | DBA | 定义与维护本契约 | Architecture Decision |
| Identity、Execution、Evidence、Verification 事实 | DBOS | 只引用 canonical source | schema／implementation／runtime |
| Reliability、Risk、Stability、Evolution Recommendation | SAEE | 定义未来只读输入边界 | SAEE implementation／evaluation execution |
| 供应链发现、SBOM、Registry、凭据轮换 | 对应安全或平台组件 | 作为外部输入引用 | 扫描、修复、账号与生产动作 |
| 高影响接受、撤权、停机或发布 | Human Decision Authority | 接收 Recommendation | 显式 Decision 和执行授权 |

## 8. Source Reconciliation Example（来源对账示例）

2026-07 Hugging Face／OpenAI 事件采用：

```text
TRIGGERS=T2_CAPABILITY_PROVENANCE,T3_EXECUTION,T4_EVIDENCE
INCIDENT_ORIGIN=OPENAI_INTERNAL_CYBER_CAPABILITY_EVALUATION
EXTERNAL_MALICIOUS_ACTOR_CONFIRMED=false
OFFICIAL_SOURCE_COUNT=2
INCIDENT_SEQUENCE=CONFLICTED_PARTIAL_OFFICIAL_ACCOUNTS
DEFAULT_STATE=REASSESSMENT_REQUIRED
MISSING_OR_CONFLICTED_SEQUENCE_EFFECT=HOLD_MISSING_EVIDENCE
```

该示例只说明状态路由，不认定完整攻击链、责任、产品缺陷范围、客户影响或任何 Digital Biosphere 资产已经受影响。

## 9. Exit and Stop Conditions（出口与停止条件）

只有同时满足以下条件，才可提议进入子项目设计：

1. DBA Architecture Decision 明确采纳精确 profile version；
2. DBOS／SAEE canonical source、Owner 和输入输出边界已确认；
3. 不重复现有 scanner、Registry、Evidence 或 evaluator；
4. 有直接测试与 fail-closed negative cases（失败关闭负例）计划；
5. Human Decision、rollback、data governance 和 security gate 已定义；
6. 分别获得 implementation 与 execution 授权。

当前状态：

```text
PROFILE_DEFINED=true
PROFILE_ADOPTED=false
CHILD_REPOSITORY_MAPPING_COMPLETE=false
IMPLEMENTATION_PROPOSED=false
IMPLEMENTATION_AUTHORIZED=false
TESTS_DEFINED=false
TESTS_EXECUTED=0
RUNTIME_CREATED=false
EXTERNAL_SUBMISSION_SENT=false
```
