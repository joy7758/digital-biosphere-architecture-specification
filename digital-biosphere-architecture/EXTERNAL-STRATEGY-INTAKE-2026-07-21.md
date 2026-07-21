---
document_id: DBA-EXTERNAL-STRATEGY-INTAKE-2026-07-21
title: Agent Governance and Verifiable Execution External Strategy Intake
title_zh: 智能体治理与可验证执行外部战略情报采纳记录
status: verified-reference-only-intake
observed_at: 2026-07-21
freshness: point-in-time
primary_repository: DBA
classification: architecture-governance-and-strategy-intelligence
source_artifact: user-provided-ai-agent-governance-brief-2026-07-21
implementation_authorized: false
roadmap_effect: none
decision_effect: none
capability_effect: none
evidence_effect: none
permission_effect: none
release_effect: none
validation_status: pass-local-documentation-and-pinned-git-refs
local_links_checked: true
external_git_refs_checked: true
---

# Agent Governance and Verifiable Execution External Strategy Intake

中文：智能体治理与可验证执行外部战略情报采纳记录。

## 1. Intake Boundary（采纳边界）

本记录核验并分类 2026-07-21 收到的外部智能体治理简报。它是
reference-only strategy intake（仅引用的战略情报采纳），不是 Architecture
Decision（架构决定）、Implementation Mapping（实现映射）、Roadmap change（路线图变更）
或 Release Authorization（发布授权）。

```text
PRIMARY_REPOSITORY=DBA
INTAKE_STATUS=SOURCE_VERIFIED_REFERENCE_ONLY
CHILD_REPOSITORIES_MODIFIED=false
ARCHITECTURE_CONTRACT_CHANGED=false
ROADMAP_CHANGED=false
CAPABILITY_CREATED=false
EVIDENCE_OBJECT_CREATED=false
IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_ACTION_AUTHORIZED=false
```

外部项目的文档、release note（发布说明）、issue（议题）和论文只证明相应来源公开了
某项主张；本记录没有安装、运行、审计或独立复现相应实现。外部来源状态会变化，后续
提案必须重新核验。

### Status vocabulary（状态词汇）

| 状态 | 含义 |
|---|---|
| `VERIFIED` | 当前一手来源直接支持该事实 |
| `VERIFIED_WITH_BOUNDARY` | 核心事实成立，但必须同时保留成熟度、范围或非声明边界 |
| `CORRECTED` | 原简报存在版本、对象或结论漂移，本记录已按当前一手来源修正 |
| `PARTIAL` | 只有部分主张或作者声明可核验，不能外推完整结论 |
| `SECONDARY_ONLY` | 只有新闻、厂商观点或个人分析；不进入能力、采用或市场事实 |
| `DEFERRED` | 值得跟踪，但没有形成采纳、实现或路线图变化 |

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

问题：如果潜在用户需要把多来源智能体治理信号按职责、证据等级和采纳闸门同步进
Digital Biosphere，我是否会推荐当前项目？

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=PROGRAM_GOVERNANCE_AND_ARCHITECTURE_STRATEGY_INTAKE
NOT_RECOMMENDED_AS=RUNTIME_ADAPTER_OR_EVALUATION_IMPLEMENTATION
RECOMMENDATION_IS_IMPLEMENTATION_AUTHORIZATION=false
```

条件推荐理由：DBA 能保留来源、版本、项目边界、未知项和下游 gate，适合做外部信号的
非执行分类与检索入口。

原始不推荐原因及本次修正：

| 不推荐原因 | 分解问题 | 本次修正证据 | 剩余停止条件 |
|---|---|---|---|
| 缺少规范的 external strategy intake（外部战略情报采纳）入口 | 外部简报可能直接污染 Roadmap、Capability 或子项目事实 | 本文件增加逐项来源、状态和非效力字段 | 任何实现提案仍需 `G1` 至 `G5` 与独立人工决定 |
| 原简报混合 Dapr Runtime 与 Dapr Agents | Runtime 特性不能自动成为 framework capability（框架能力），反之亦然 | 第 3.1 节分别固定两个项目的 tag 和 commit | 未完成代码级实现审计前不得声称互相继承全部能力 |
| Microsoft 差异化结论已经漂移 | `#1249` 的特定回执提案与工具包后续发布能力不是同一事实 | 第 3.2 节同时记录 issue 与 `v3.6.0` / `v4.1.0` | 未审计实现和验证器前不得声称独立可验证性已完整满足 |
| 外部研究结果容易被升级为产品充分性 | 单篇论文、workshop 或小样本不能创建 SAEE 规则 | 第 3.4 节保留样本、复现和非归档边界 | 进入 SAEE 前需独立研究提案、数据审查和 Evaluation gate |

## 3. Source-verified Signal Register（来源核验信号登记）

### 3.1 Dapr Runtime 与 Dapr Agents 必须分开

| signal_id | 当前核验事实 | 状态 | 边界 |
|---|---|---|---|
| `EXT-DAPR-RUNTIME-001` | Dapr Runtime 当前稳定 release（发布）是 `v1.18.1`，tag commit 为 `4cef924a0b1360c69d810deec8cd59bf853f6721`；`v1.18.2-rc.4` / `f984249aa7630b2a13acff661171ba3322586264` 是 prerelease（预发布） | `CORRECTED` | “Dapr 1.18 已发布”成立，但最新稳定点版本不是笼统的 `1.18`，也不能把 RC 写成稳定版 |
| `EXT-DAPR-RUNTIME-002` | Dapr `v1.18` 引入 opt-in（选择启用）的 workflow history signing（工作流历史签名）、跨应用 attestation（证明）、history propagation（历史传播）、`WorkflowAccessPolicy` 和 `MCPServer` resource（资源） | `VERIFIED_WITH_BOUNDARY` | `WorkflowHistorySigning` 是 preview feature（预览功能）、依赖 mTLS 且默认关闭；无 policy 时 `WorkflowAccessPolicy` 保持开放；`MCPServer` 使用 `dapr.io/v1alpha1` 和 workflow `v1.0-beta1` 表面 |
| `EXT-DAPR-AGENTS-001` | Dapr Agents 当前稳定 release 是 `v1.0.5`，tag commit 为 `745bd41e09c1ec3e09d9f592d2385800e2f21864`；它是建立在 Dapr 之上的 agent framework（智能体框架） | `CORRECTED` | 顶部仓库链接不能替代对 Dapr Runtime 的独立核验；框架 README 的产品主张不是本项目的运行验证 |
| `EXT-DAPR-AGENTS-002` | `v1.0.4` release note 记录 MCPServer auto-discovery（自动发现）与 workflow orchestration（工作流编排）；`v1.0.5` 主要包含依赖自动升级、HITL 状态存储修复和 message-router filter（消息路由过滤） | `VERIFIED` | 这些是上游 release note 事实，不表示 DBOS、ARO、Agent Evidence 或 SAEE 已有适配 |

一手来源：

- [Dapr v1.18 release announcement](https://blog.dapr.io/posts/2026/06/10/dapr-v1.18-is-now-available/)
- [Dapr workflow history signing](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-history-signing/)
- [Dapr preview features](https://docs.dapr.io/operations/support/support-preview-features/)
- [Dapr MCPServer resource](https://docs.dapr.io/developing-ai/mcp/mcp-server-resource/)
- [Dapr Runtime releases](https://github.com/dapr/dapr/releases)
- [Dapr Agents repository](https://github.com/dapr/dapr-agents)
- [Dapr Agents releases](https://github.com/dapr/dapr-agents/releases)

对 Digital Biosphere 的允许解释：

```text
Dapr workflow history signature
  -> candidate Evidence Material or Evidence Reference
  -> not automatically a DBOS Canonical Evidence Object
  -> not automatically independently portable evidence
  -> not automatically SAEE evidence sufficiency
  -> not automatically readiness, authorization, or release
```

Dapr 的 SPIFFE identity（身份）标识签名 workload（工作负载），不自动等于 POP persona
（人格）、DBOS Digital Entity Identity（数字主体身份）、Agent Passport、Permission 或
Human Authority。`WorkflowAccessPolicy` 是上游运行时访问控制，不自动成为 DBOS
Permission record（权限记录）。

### 3.2 Microsoft Agent Governance Toolkit 结论需要收窄

| signal_id | 当前核验事实 | 状态 | 边界 |
|---|---|---|---|
| `EXT-MS-AGT-001` | GitHub issue `#1249` 于 2026-04-21 提议 pre/post bilateral signed receipts（执行前/后双向签名回执）和 signed `DENIED` receipt；issue 已关闭，页面仍显示没有关联 branch 或 PR | `VERIFIED_WITH_BOUNDARY` | 只证明特定提案未通过该 issue 形成可见实现链，不能证明整个工具包没有其他 tamper-evident evidence（防篡改证据）能力 |
| `EXT-MS-AGT-002` | `v3.6.0` / `492b72011cebfd5831397d5db833bd735f52003f` 的 Public Preview release note 已列出 `Audit and Compliance v1.0`，包括 Merkle-chained logs、retention 和 evidence export | `CORRECTED` | 这是上游 release claim（发布主张），本次没有审计其实现、离线验证器、信任根或完整覆盖范围 |
| `EXT-MS-AGT-003` | 当前 latest release 是 `v4.1.0` / `0de71ca6c95cf8b9b975ac96f48eaa7826bbe258`，发布于 2026-06-09 | `VERIFIED` | 最新版本存在不等于 GA、独立验证完整、客户采用或与本项目兼容 |

一手来源：

- [Issue #1249](https://github.com/microsoft/agent-governance-toolkit/issues/1249)
- [Agent Governance Toolkit releases](https://github.com/microsoft/agent-governance-toolkit/releases)

修正后的竞争判断：Microsoft 工具包已经公开声称具备链式审计与证据导出能力；尚未由
`#1249` 证明的是其特定的双阶段、双边签名回执格式。SAEE 与 Agent Evidence 的差异
不能建立在“微软没有防篡改日志”这一过时前提上，应建立在清晰的 object boundary
（对象边界）、portable verification contract（可移植验证契约）与 bounded evidence
sufficiency evaluation（有界证据充分性评价）上，并等待各自仓库的直接能力审计。

### 3.3 OpenTelemetry GenAI 仍不适合作为冻结合同

| signal_id | 当前核验事实 | 状态 | 边界 |
|---|---|---|---|
| `EXT-OTEL-001` | 独立 `open-telemetry/semantic-conventions-genai` 仓库当前 `main` 为 `150760c6252a4bb63c49c9915bad11997d316a15`；仓库页面仍显示 `Schema URL: TODO` 且没有 published release（已发布版本） | `VERIFIED` | core semantic conventions（核心语义约定）已有带 GenAI 变化的版本，不等于独立 GenAI 仓库已形成冻结发布 |
| `EXT-OTEL-002` | core conventions 已发生 `gen_ai.system` 到 `gen_ai.provider.name` 等演化，并继续增加 agent/tool/evaluation 字段 | `VERIFIED_WITH_BOUNDARY` | 不能把任一观察时点的 `gen_ai.*` 字段直接写成 SAEE 或 ARO 不可变合同 |

一手来源：

- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai)
- [OpenTelemetry Semantic Conventions releases](https://github.com/open-telemetry/semantic-conventions/releases)

允许的兼容路径保持为：

```text
version-pinned raw telemetry
  -> explicit OpenTelemetry mapping profile
  -> ARO or DBOS reference mapping
  -> Evidence profile
  -> SAEE evaluation input
```

每次 mapping（映射）必须记录上游 commit/version、字段重命名、unsupported fields（不支持
字段）、内容敏感性和失败行为。Mapping 不创建 Canonical Evidence Object，也不证明
Execution、Identity、Authorization 或 Truth。

### 3.4 KDD 与 arXiv 研究信号只进入研究候选

| signal_id | 当前核验事实 | 状态 | 边界 |
|---|---|---|---|
| `EXT-KDD-001` | KDD 2026 的 Evaluation and Trustworthiness of Agentic AI workshop（智能体 AI 评价与可信性研讨会）定于 2026-08-09 下午举行；官方页面说明接收论文不进入 KDD proceedings（正式论文集） | `VERIFIED` | 截至核验时官方 Accepted Papers 页面仍为 `TBD`，不能由 workshop 页面确认具体两篇论文的接收状态 |
| `EXT-KDD-002` | arXiv `2607.07405v1` 报告：四个 deterministic gates（确定性闸门）使完整 50 任务结果提升 `+12.4pp`；在 26 个触发任务上提升 `+19.2pp`，并在另一组 15 seeds 上复现总体提升 | `VERIFIED_WITH_BOUNDARY` | frontier model（前沿模型）部分仅 `n=5` 且未复现；论文是作者 arXiv preprint，并自述为 non-archival workshop（非归档研讨会）接收 |
| `EXT-KDD-003` | arXiv `2607.12338v1` 的严格条件结果为 AppWorld `15%`、tau-bench `25%`、SWE-bench Verified `90%` 首次满足其全部目标 | `VERIFIED_WITH_BOUNDARY` | 这些比例依赖论文的选择、覆盖与决策规则，不是跨 benchmark 或 SAEE 的通用充分性阈值 |
| `EXT-RESEARCH-001` | arXiv `2606.30970v1` 描述 AgentBound 的授权、行为宪法、site action contract（站点动作契约）与可重放治理回执 | `PARTIAL` | 论文/框架描述不是跨框架采用、独立第三方验证、商业可用性或本地实现证据 |

一手来源：

- [KDD 2026 workshops](https://kdd2026.kdd.org/workshops/)
- [KDD Evaluation and Trustworthiness workshop](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/)
- [arXiv:2607.07405](https://arxiv.org/abs/2607.07405)
- [arXiv:2607.12338](https://arxiv.org/abs/2607.12338)
- [arXiv:2606.30970](https://arxiv.org/abs/2606.30970)

这些研究可进入 literature comparison（文献对照）和 proposal question（提案问题），
不能直接修改 SAEE score（评分）、coverage threshold（覆盖阈值）、Recommendation、
Capability inventory 或当前 Phase。

### 3.5 NIST 与 ITU 是治理方向信号，不是合规或标准完成证明

| signal_id | 当前核验事实 | 状态 | 边界 |
|---|---|---|---|
| `EXT-NIST-001` | NIST AI `800-5` 于 2026-05-18 发布 RFI response summary（征求意见回复摘要），记录了新型 agent security（智能体安全）威胁、传统网络安全需适配、实施指南、信息共享和标准推动需求 | `VERIFIED_WITH_BOUNDARY` | 这是意见汇总，不是具体 SAEE/DBOS 实现指南、认证或合规认可 |
| `EXT-ITU-001` | ITU 于 2026-07-09 宣布 FG-TIDA，关注人类与 agentic AI 的 identity、trust、lifecycle assurance、interoperability、continuous assessment 和 human control；向感兴趣专家开放 | `VERIFIED_WITH_BOUNDARY` | Focus Group（焦点组）不是已发布 ITU 标准；首次会议计划在 2026-11 举行且页面仍标为待确认 |

一手来源：

- [NIST AI 800-5](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai)
- [ITU FG-TIDA announcement](https://www.itu.int/en/mediacentre/Pages/PR-2026-07-09-focus-group-agentic-AI.aspx)
- [ITU FG-TIDA workspace](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/default.aspx)

允许的处理只有 standards watch（标准跟踪）和未来 contribution preparation（贡献准备）。
不得声称 NIST 或 ITU 已采用、认可、认证或验证 Digital Biosphere、DBOS、Agent Evidence
或 SAEE。

### 3.6 企业市场报道保持 `SECONDARY_ONLY`

附件中的 TechRadar、Economic Times 和企业高管观点可以说明行业讨论正在转向运行级
身份、权限、撤销、编排和治理，但它们不是市场规模、采购、采用、客户需求或产品差异的
直接证据。

```text
ENTERPRISE_MARKET_SIGNAL_STATUS=SECONDARY_ONLY
CUSTOMER_DEMAND_VALIDATED=false
MARKET_SIZE_VALIDATED=false
CUSTOMER_ADOPTION_VALIDATED=false
COMMERCIAL_OFFERING_CREATED=false
```

## 4. Architecture Impact Matrix（架构影响矩阵）

| 外部信号 | DBA 允许记录的关系 | DBOS / POP / ARO / Agent Evidence 边界 | SAEE 边界 | 当前处理 |
|---|---|---|---|---|
| Dapr history signing | 外部 runtime evidence source candidate（运行时证据来源候选） | SPIFFE workload identity、history signature 和 attestation 只能先作为有版本材料或引用；不自动成为 Entity Identity、Canonical Evidence 或独立真相 | 可评价材料完整性与适用性，但不能重签、补造或把签名升级为充分性 | `REFERENCE_AND_MAPPING_QUESTION_ONLY` |
| Dapr MCP / access policy | 外部执行与访问控制候选 | 不复制其 agent framework、workflow runtime 或 RBAC；未来只定义最小交接契约 | 不获得 tool authorization 或 runtime write authority | `NO_ADAPTER_AUTHORIZED` |
| Microsoft AGT | 竞争与互操作对照 | 先审计 receipt、Merkle chain、export、offline verifier 和 trust-root 边界 | 不以过时的“无防篡改能力”建立差异化 | `COMPARISON_REQUIRED` |
| OpenTelemetry GenAI | versioned telemetry normalization candidate（版本化遥测归一化候选） | 字段映射必须保留来源版本、内容敏感性和未知 | 仅消费有界 profile，不冻结上游 development 字段 | `VERSION_PIN_REQUIRED` |
| KDD / AgentBound | research input（研究输入） | 不创建 runtime gate、receipt schema 或 authorization service | 可形成充分性研究问题，不形成当前算法、阈值或结果 | `RESEARCH_PROPOSAL_ONLY` |
| NIST / ITU | standards watch（标准跟踪） | 可用于未来术语、身份、授权、审计与非否认对照 | 可用于评价与持续监测问题对照 | `NO_COMPLIANCE_CLAIM` |

## 5. Accepted Interpretation and Deferred Work（允许解释与延期工作）

### Compatible interpretation now（当前兼容解释）

本期外部信号强化但不修改现有架构边界：

```text
history exists
  != history is tamper-evident
  != evidence is portable and independently verifiable
  != evidence is sufficient for a scoped claim
  != action is authorized
  != agent is ready
  != release is authorized
```

这与 [`architecture/evidence-schema-mapping.md`](architecture/evidence-schema-mapping.md)、
[`architecture/saee-dbos-contract.md`](architecture/saee-dbos-contract.md) 和
[`INTEGRATION-GATES.md`](INTEGRATION-GATES.md) 已有不变量一致，不构成新规范版本。

### Deferred mapping questions（延期映射问题）

以下问题可以进入后续独立提案，但本次不进入 Roadmap 或实施：

1. 哪些 Dapr history / attestation 字段只能作为 Evidence Material，哪些可以形成
   Evidence Reference，谁负责解析和版本固定？
2. Agent Evidence 当前是否有执行前、执行后、拒绝三种 receipt semantics（回执语义），
   以及 offline verification（离线验证）、key rotation（密钥轮换）和 revocation（撤销）
   边界？
3. ARO 是否只做 audit projection（审计投影），还是拥有独立验证结果；它与 DBOS
   Verification 和 SAEE Evaluation 如何保持三分？
4. SAEE 在什么 task selection、risk coverage、negative case 和 uncertainty 条件下才有资格
   输出某类 Recommendation；证据不足时如何稳定输出 `HOLD` / `REVIEW_REQUIRED`？

这些问题涉及相邻候选项目，仍受 `DQ-006`、`R-007`、`G0` 至 `G5` 和各子项目 canonical
source 约束。

### Local capability reconciliation（本地能力对账）

2026-07-21 的只读本地核对进一步修正了“外部信号等于本地新缺口”的误读：

- SAEE 的 `capability-package/manifest.json#canonical_inventory` 已把
  `saee.evaluate_evidence` 登记为 implemented local bounded evaluation（已实现本地有界
  评价）；不能再次立项一个平行 Evidence Adequacy evaluator；
- 同一 inventory 已把 `saee.otel_style_candidate_mapping` 登记为 experimental synthetic
  mapping（实验性合成映射）；真正缺失的是 `saee.otel_sdk_or_otlp_ingestion`、
  `saee.trusted_trace_to_evidence_conversion`、`saee.external_identity_binding` 和
  `saee.delegation_binding`；
- Agent Evidence 已提供可移植 export、offline bundle、verification receipt 与本地验证
  表面，但其仓库同时明确否认 production、external validation、完整身份／证明与法律不可
  否认性；
- ARO 已提供 tamper-evident journal、receipt、exportable evidence 和 bounded verifier
  （防篡改日志、回执、可导出证据与有界验证器）参考，不能再新增平行 hash/Merkle stack；
  其通用 stale receipt / replay freshness policy（过期回执／重放新鲜度策略）仍为 partial；
- DBOS 当前本地 verifier 不满足 independent verification（独立验证），因此不能把结构
  validation、测试 PASS 或 clean worktree 写成 E4/V4 或外部验证。

对应的责任链、来源候选与停止规则已记录在
[`PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET.md`](PROGRAM-SOURCE-AND-RESPONSIBILITY-DECISION-PACKET.md)
和
[`architecture/program-source-and-responsibility-registry.json`](architecture/program-source-and-responsibility-registry.json)。
该对账没有修改任何子项目实现或 canonical inventory。

```text
LOCAL_CAPABILITY_RECONCILIATION_RECORDED=true
EXISTING_EVALUATOR_REUSED=true
EXISTING_SYNTHETIC_OTEL_MAPPING_RECOGNIZED=true
DUPLICATE_RECEIPT_OR_HASH_STACK_AUTHORIZED=false
CHILD_PROJECT_CAPABILITY_FACT_CHANGED=false
```

### Explicitly not adopted（明确未采纳）

- 不新增 Dapr adapter、OpenTelemetry adapter 或 Microsoft receipt format；
- 不修改 DBOS Identity、Evidence、Verification、Permission 或 Runtime；
- 不修改 SAEE algorithm、threshold、Capability inventory 或 Phase；
- 不把附件中的“唯一主线 PR”“今日行动排名”写入 DBA `MASTER-ROADMAP.md`；
- 不创建论文项目、workshop 投稿、ITU/NIST 对外贡献或作者联系；
- 不把外部 release、issue、论文或报道写成 Digital Biosphere 已集成、已验证、已采用、
  已商用或已获标准认可。

## 6. Commercial Language Boundary（商业语言边界）

| 层次 | 可以说什么 | 当前不能说什么 |
|---|---|---|
| Runtime verifiability（运行时可验证性） | 某上游 runtime 可以对特定历史做签名、链路或策略检查 | 来源真实、授权有效、全链路完整、业务结论成立 |
| Evidence portability（证据可移植性） | 某证据包在明确 trust root、schema 和 verifier 下可脱离生产系统验证 | 内容为真、覆盖完整、适用于任何环境 |
| Evidence sufficiency（证据充分性） | 在声明 scope、claim、coverage 和 uncertainty 下评价材料是否足以支持建议 | 全局安全、合规认证、生产就绪或发布授权 |

当前最保守且可防守的表述是：

> Digital Biosphere separates runtime records, evidence references, verification,
> evaluation, human decision, execution, and release. External runtime signatures can
> become bounded inputs; they do not collapse those stages.

中文：Digital Biosphere 分离运行记录、证据引用、验证、评价、人工决定、执行与发布。
外部运行时签名可以成为有界输入，但不能抹平这些阶段。

## 7. Final Intake State（最终采纳状态）

```text
EXTERNAL_SIGNALS_REVIEWED=true
PRIMARY_SOURCES_CHECKED=true
SOURCE_DRIFT_CORRECTED=true
REFERENCE_ONLY_INTERPRETATION_RECORDED=true
NEW_CAPABILITY_GAP_DECLARED=false
NEW_ARCHITECTURE_PROPOSAL_CREATED=false
NEW_DECISION_CREATED=false
ROADMAP_PRIORITY_CHANGED=false
IMPLEMENTATION_TASK_CREATED=false
RESEARCH_TASK_CREATED=false
EXTERNAL_CONTRIBUTION_AUTHORIZED=false
VALIDATION=PASS_LOCAL_DOCUMENTATION_AND_PINNED_GIT_REFS
```

本记录完成“同步最新信息”的治理层工作。未来若要实现任何 Dapr、OpenTelemetry、receipt
或 SAEE 充分性功能，必须创建独立提案，重新核验上游版本，指定一个 primary repository，
完成 duplicate construction review（重复建设审查），并通过相应 Integration Gate。
