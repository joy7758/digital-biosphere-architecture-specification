---
document_id: DBA-EAGIR-20260723-001
title: External Agent Governance Intelligence Review
title_zh: 外部智能体治理情报纠偏审查
status: reference-only-corrected-mainline-drift-detected
observed_at: 2026-07-23T11:26:18+08:00
implementation_effect: none
external_effect: none
---

# External Agent Governance Intelligence Review（外部智能体治理情报纠偏审查）

## 1. Outcome（结果）

```text
REVIEW_ID=DBA-EAGIR-20260723-001
REVIEW_STATUS=REFERENCE_ONLY_CORRECTED_MAINLINE_DRIFT_DETECTED
SOURCE_COUNT=13
CORRECTION_COUNT=10
MAINLINE_DRIFT_DETECTED=true
POTENTIAL_CUSTOMER_RECOMMENDATION=COMPOSE_WITH_SAEE
DEVELOPMENT_RECOMMENDATION=DO_NOT_IMPLEMENT_FROM_BRIEF
CAPABILITY_ADOPTED=false
PRODUCT_CREATED=false
PHASE1_AUTHORIZED=false
PULL_REQUEST_CREATED=false
EXTERNAL_SUBMISSION_SENT=false
PRODUCTION_READY=false
```

用户提供的《AI Agent Governance Intelligence Brief（2026-07-23）》包含真实且重要的行业信号，但不能作为 SAEE capability（能力）、产品、成熟度或开发授权来源。审查确认：

1. Agent security（智能体安全）、identity（身份）、runtime control（运行时控制）、observability（可观测性）和 review-gate governance（审查闸门治理）正在加速；
2. OpenTelemetry 是重要 observation substrate（观察底座），但 telemetry（遥测）不自动成为 Evidence、Truth、Authority 或 compliance proof（合规证明）；
3. 简报对 ACS、OpenTelemetry GenAI、Traccia、SAEE 的成熟度与产品状态存在提升式表述；
4. 简报把 Evidence Governance 提升为 SAEE 主线并提出 `SAEE Agent Compliance Engine`，触发 `MAINLINE_DRIFT_DETECTED`；
5. 当前只允许 reference-only（仅参考）同步与纠偏，不允许据此创建 Runtime、产品或三个建议 PR。

机器可读投影见
[`architecture/external-agent-governance-intelligence-review.2026-07-23.v0.1.json`](architecture/external-agent-governance-intelligence-review.2026-07-23.v0.1.json)，约束见
[`architecture/schemas/external-agent-governance-intelligence-review.schema.v0.1.json`](architecture/schemas/external-agent-governance-intelligence-review.schema.v0.1.json)。

## 2. Pre-development Agent Recommendation Gate（开发前智能体推荐闸门）

如果潜在客户询问“现在是否推荐 SAEE”，智能体的可支持回答是：

```text
recommendation=COMPOSE_WITH_SAEE
```

推荐 SAEE 用于：

- 对 closed evidence package（封闭证据包）做有界、离线、确定性的 evidence-adequacy evaluation（证据充分性评价）；
- 在上线前识别可靠性、证据缺口和边界风险，并保留明确的非授权语义。

不推荐 SAEE 用于：

- production runtime control（生产运行时控制）或 inline authorization（内联授权）；
- 法律／监管 compliance certification（合规认证）；
- real OTLP ingestion（真实 OTLP 准入）或任意 OpenTelemetry 归一化；
- externally authenticated identity（外部认证身份）或 delegation（委托）验证；
- non-repudiation（不可抵赖）或证明真实世界事件一定发生。

因此，本简报的开发建议是：

```text
DEVELOPMENT_RECOMMENDATION=DO_NOT_IMPLEMENT_FROM_BRIEF
```

阻塞原因是：Phase 1 未授权、公共投影与治理历史分叉、建议部分重复现有能力、真实 OTLP／可信转换／身份／委托仍缺失，以及主线发生 audit-first（审计优先）漂移。

## 3. Primary-source Verification（一手来源核验）

| signal | 核验结果 | 允许解释 |
|---|---|---|
| Reuters autonomous-agent incident | 报道真实，重点是 containment、sandbox、guardrail 与 cyber-defense 限制 | 安全与边界紧迫性；不能直接验证 SAEE 架构 |
| NIST AI 800-5 | 2026-05-18 发布的 RFI response summary（意见征询回应摘要） | 证明风险、实践、评估和标准讨论加速；不是绑定标准 |
| NIST AI Agent Standards Initiative | 已启动，聚焦行业标准、开放协议、安全、认证与身份研究 | 适合作为版本化战略参考 |
| OWASP Agentic AI Security and Governance 2.01 | 2026-06-01 发布的实践指南 | 支持治理需求；不证明 Evidence Layer 为空 |
| OpenSearch Agent Traces | OpenSearch 3.6 已提供 Agent trace 工作流，使用 OTLP 与 GenAI semantic conventions | 证明可观测产品化；不证明 trace 真实性或治理结论 |
| OpenTelemetry core / GenAI | core Semantic Conventions 为 `1.43.0`；GenAI 已迁移到独立活跃仓库，观察时没有发布版 | OTel 是强观察底座；GenAI 字段仍需 exact pin 与 stability 隔离 |
| Traccia | `arXiv:2607.14309v1`，作者预印本 | 研究参考；不能提升为独立合规、法律证明或市场采用 |
| ACS | 官网称 specification actively evolving；仓库 `version.txt=0.1.0`、无 tag／Release、由 OWASP AOS fork，官网 Apache-2.0 与仓库 MIT 元数据不一致 | emerging proposal（新兴提案），不是当前成熟标准 |
| Agent security survey | `arXiv:2603.11088v1`，页面声明 accepted to USENIX Security 2026 | 支持安全研究重要性；不定义 Evidence Object 标准 |
| Governance Manifest | `arXiv:2607.15769v1`，preprint under journal review | 支持项目侧 governability 研究；不是已采纳标准 |
| GitHub Agent Control Plane | Enterprise AI Controls 已 GA；MCP allowlists 仍为 public preview | 证明企业需求；属于 vendor product，不是通用标准 |

固定来源、URL、版本／commit 与观察状态记录在机器文件的 `sources`。

## 4. Required Corrections（必须修正）

### 4.1 Industry corrections（行业修正）

| 简报表述 | 修正 |
|---|---|
| “Evidence Layer 仍空缺” | 该领域不是空白，而是碎片化：receipt、attestation、audit、telemetry、governance 与 evidence semantics 并存，机会在互操作与边界，不在宣称独占空层 |
| “OpenTelemetry 是 Agent 世界的 TCP/IP” | 这是战略比喻，不是已证明事实；OTel 可统一 observation，但不自动证明 identity、authority、completeness 或 truth |
| “Traccia = hash ledger + compliance evidence” | 这是预印本中的系统主张；hash 可支持覆盖字段的完整性检查，不自动建立不可抵赖、可信来源、法律事实或监管符合性 |
| “ACS 标准已经形成” | 更准确状态是 actively evolving open proposal；当前仓库版本、Release、fork 与 license 表面仍有成熟度问题 |
| “GitHub Agent Control 代表通用治理成熟” | 它证明企业产品需求，不能外推为 vendor-neutral standard；MCP allowlist 仍在 preview |
| “论文热点 = SAEE 标准／商业窗口已验证” | 论文证明研究相关性，不证明 SAEE 独特性、客户需求、采用或付费意愿 |

### 4.2 SAEE truth corrections（SAEE 真值修正）

治理来源固定为 `697ae2080f11b7905b20c39079914eb98169783b`，公共投影固定为 `2173c258f91aed03fc02c0097d4250a87be703aa`。

| 简报表述 | 当前规范事实 |
|---|---|
| Evidence Object 对应“不可抵赖执行证明” | SAEE 有本地有界 evidence／receipt／digest 原语；不能证明真实事件、外部身份、完整 chain of custody 或不可抵赖 |
| OpenTelemetry Bridge 是全新空白 | synthetic OTel-style candidate mapping 已 `implemented/experimental`；general trace normalization 为 `partial`；重复 mapper 已被防重复建设规则禁止 |
| “任何 Agent Trace → SAEE Evidence → Verify” | real OTLP ingestion、trusted trace-to-evidence conversion、external identity binding 与 delegation binding 均为 `missing` |
| MCP／云市场商品／demo 是商业入口 | local MCP 存在；public MCP endpoint、marketplace listing、customer validation 与 production readiness 均为 `false` |
| Persona Object 应由 SAEE 建立身份标准 | POP 是 external reference；SAEE 的 external identity binding 仍缺失，不能成为并行 identity provider |
| SAEE Governance 已可包装 | `SAEE Governance=target_not_implemented`；三个客户版本是目标，不是当前全部实现 |
| 应新增 `SAEE Agent Compliance Engine` | 固定目标只有 `SAEE Evidence / SAEE Evaluation / SAEE Governance`；第四产品和 audit-first 重构均不允许 |

## 5. Mainline Drift Decision（主线漂移决定）

```text
MAINLINE_DRIFT_DETECTED
```

触发原因：

1. 把 Evidence Governance 提升到受控 `SAEE + Agent Evidence` 合并主线之上；
2. 把 SAEE 从 `EVOLUTION_INTELLIGENCE_LAYER` 重构为 audit/compliance engine；
3. 创建固定三客户版本之外的第四产品；
4. 把 POP reference 提升为 SAEE identity ownership；
5. 把 local digest、demo、MCP contract 与 marketplace review 提升为 proof、service 或 commercial validation；
6. 推荐 workshop 路线，而 SAEE 宪法只允许经核验的零强制作者费用同行评审期刊路线。

该信号停止 feature implementation（功能实现），但不阻止本次 reference-only 情报纠偏。

## 6. Corrected Action Order（纠正后的行动顺序）

1. **保留外部情报为 source-pinned reference-only input。** 不改变 capability、DQ、Runtime、产品或发布状态。
2. **先协调 SAEE 历史。** 公共 `origin/main@2173c258f...` 已合并 DBOS preview projection；规范治理／能力分支 `697ae2080...` 与其分叉。新增能力前先形成独立历史协调与人工授权。
3. **Evidence Object 不新建平行标准。** 通过现有 SAEE／Agent Evidence provenance、license、schema-crosswalk、reuse 和 migration gate 进入。
4. **OTLP 只保留 conditional proposal。** 第一候选范围只能是 bounded offline sanitized OTLP JSON；无 listener、无自动 Evidence 提升、无 conformance claim，并固定 SemConv 版本。
5. **Identity／Persona 只做 crosswalk 与 threat model。** POP 保持外部 reference；未来 binding 必须依赖独立认证 identity、delegation trust policy、expiry／revocation 与 fail-closed 结果。
6. **Compliance 改为 evidence-to-control crosswalk。** 只说明“哪些材料可支持哪条 control review”，不输出法律合规、认证或不可抵赖结论。
7. **不创建 `SAEE Agent Compliance Engine`。** 保持三个目标客户版本。
8. **不按本简报投稿 workshop。** 学术路线仍走真实、零强制作者费用的同行评审期刊 gate。
9. **外部回复保持人工 gate。** ACS、FDO、conference、journal、客户和 marketplace 的发言／提交均未授权、未发送。

## 7. Validation（验证）

本记录完成后必须满足：

```text
JSON_SCHEMA_VALIDATION=PASS
SOURCE_IDS_UNIQUE=true
CORRECTION_SOURCE_CLOSURE=true
SAEE_GOVERNANCE_SNAPSHOT_VALIDATED=true
SAEE_PUBLIC_PROJECTION_VALIDATED=true
SAEE_MAINLINE_GUARD=PASS
RUNTIME_EFFECT=false
EXTERNAL_EFFECT=false
```

这些 PASS 只证明文档、机器投影和现有规范真值在声明范围内一致；不证明外部标准已采纳、SAEE 已实现新能力、PR 已创建、外部讨论已发送或生产就绪。

## 8. Primary Sources（主要来源）

- [Reuters: Chinese AI's role in stopping rogue OpenAI agent shows cost of US guardrails](https://www.reuters.com/legal/litigation/chinese-ais-role-stopping-rogue-openai-agent-shows-cost-us-guardrails-2026-07-22/)
- [NIST AI 800-5](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai)
- [NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative)
- [OWASP State of Agentic AI Security and Governance 2.01](https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/)
- [OpenSearch 3.6 Agent traces](https://docs.opensearch.org/3.6/observing-your-data/agent-traces/index/)
- [OpenTelemetry Semantic Conventions 1.43.0](https://opentelemetry.io/docs/specs/semconv/)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai)
- [Traccia](https://arxiv.org/abs/2607.14309)
- [Agent Control Standard](https://agentcontrolstandard.org/)
- [ACS repository](https://github.com/Agent-Control-Standard/ACS)
- [The Attack and Defense Landscape of Agentic AI](https://arxiv.org/abs/2603.11088)
- [Making Agent-Mediated Contributions Governable](https://arxiv.org/abs/2607.15769)
- [GitHub Enterprise AI Controls and agent control plane](https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/)
