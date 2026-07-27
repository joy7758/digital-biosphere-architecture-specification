---
document_id: DBA-TITMAS-PUBLIC-ENTRY-AND-AGENT-AUTOMATION-RECOMMENDATION-0.1
title: TITMAS Public Entry and Agent Automation Recommendation v0.1
title_zh: TITMAS 公开入口与智能体自动化强化建议 v0.1
version: 0.1.0
status: recommended-exact-bounded-development-contract
maturity: Development
maturity_scope: entire-document
owner_ref: zhangbin
decision_reference: TITMAS-CS-STANDING-001
supersedes: NONE
superseded_by: NONE
compatibility_statement: "Recommendation for one additive Development machine contract; no Runtime, API, product, SLA, certification, commercial offering, or production compatibility claim."
implementation_feedback_refs: []
conformance_refs: []
known_limitations: [SEE_DOCUMENT_BODY]
document_type: bounded-commercialization-standard-recommendation
architecture_domain: TITMAS
primary_repository: digital-biosphere-architecture
observed_at: 2026-07-27
authority_effect: none
---

# TITMAS Public Entry and Agent Automation Recommendation v0.1

## 1. Recommendation（建议）

推荐采用一个精确、有界动作：

```text
ADOPT_AGENT_EVALUATION_ENTRY_CONTRACT_V0_1_AS_DEVELOPMENT_MACHINE_CONTRACT
```

目标是在不扩大 TITMAS 产品范围的情况下，让第一次接触项目的 AI Agent 能够按同一契约：

```text
Discover
  -> Fetch
  -> Verify Artifact
  -> Install
  -> Validate
  -> Classify Failure
  -> Make a Bounded Recommendation
```

这个契约只连接已经存在的 Commercial Evaluation Pack v0.2、公开 wheel、合成 fixture
和只读 validator。它不创建新的 Runtime、API、Agent、Permission、Certification、
SLA 或 Commercial Offering（商业产品）。

## 2. Why This Is the Next Smallest Complete Step（为何这是下一最小完整步骤）

CE-G1 已证明：

- 4/4 智能体评审会话建议把 TITMAS 用于离线评估；
- 4/4 不建议用于生产；
- 2 个 Provider 能在边界不抬升的情况下理解评估包；
- 首次运行最终可复现；
- 公开入口曾出现 3 次瞬时传输失败。

因此当前缺口不是更多功能，而是把分散在人类文档中的入口事实收敛成一个机器对象：

- exact wheel filename、URL、SHA-256 和 Python 版本；
- 必须安装声明依赖，禁止把 `--no-deps` 作为合规路径；
- exact fixture、命令、预期退出码和 PASS 的有界含义；
- 可重试与不可重试失败的分类；
- availability observation（可用性观察）与 SLA 的分离；
- “可评估推荐”与“生产推荐”的分离。

## 3. Agent Advisory Input（智能体咨询输入）

本建议参考了 2026-07-27 的两个外部模型咨询。模型输出只作为 advisory input（建议输入），
不是事实、决策、符合性证据或 Authority。

| Provider / model | Bounded useful finding | Rejected error |
|---|---|---|
| Alibaba Cloud Model Studio / `qwen3.7-plus` | 建议提供单一版本化 discovery/install/failure machine contract | 错误声称现有 wheel 文件名不符合 PEP 427；该文件名和安装路径已通过公开首跑 |
| Baidu Qianfan / `deepseek-v4-flash` | 建议明确 evaluation-only、依赖和失败码 | 生成了不存在的 `dbos.inc` URL；不得进入任何规范或公开入口 |

另一个已纠正的测试事实：

> 使用 `pip --no-deps` 后缺少 `jsonschema` 是测试 harness（测试工具链）错误，不是当前公开
> 安装指南或 wheel 的已证产品缺陷。正式契约明确禁止把 `--no-deps` 视为合规安装路径。

## 4. Exact Scope（精确范围）

允许：

- 创建 `TITMAS Agent Evaluation Entry Contract v0.1` Development 规范；
- 创建对应 JSON Schema 和一个机器实例；
- 绑定既有公开 artifact、fixture、validator 与 Commercial Evaluation Pack v0.2；
- 定义 fail-closed failure codes（失败关闭错误码）；
- 定义推荐前置条件与永久非抬升规则；
- 准备网站静态源文件和 Agent Index 引用；
- 本地运行 Schema、负例、站点和边界验证；
- path-scoped commit and push。

不允许：

- 修改 DBOS 或 SAEE；
- 创建 Runtime、API、Agent、Entity、Permission 或 Capability；
- 运行真实 Agent 任务；
- 创建产品、价格、合同、SLA、认证或证书；
- 声称客户采用、生产就绪或公共可用性保证；
- 部署网站或发布新的 Release；
- 把模型回答升级为 Architecture Decision。

## 5. Preconditions（前置条件）

```text
COMMERCIAL_EVALUATION_PACK_V0_2_DEFINED=true
EXTERNAL_AGENT_FIRST_RUN_VALIDATION_PASS=true
PUBLIC_WHEEL_EXACT_HASH_AVAILABLE=true
SYNTHETIC_FIXTURE_AVAILABLE=true
OFFLINE_VALIDATOR_AVAILABLE=true
AVAILABLE_COMMERCIAL_OFFERING=false
PRODUCTION_READY=false
```

## 6. Stop Rules（停止规则）

发生任一情况立即停止并保持失败记录：

- exact artifact URL、filename、version 或 SHA-256 无法绑定；
- Schema 允许 `evaluation_only=false`；
- Schema 允许 `no_deps_allowed=true`；
- 推荐策略允许 production use；
- 任何 effect 创建 Authority、Permission、Runtime、Agent、Entity、Certification 或
  Commercial Offering；
- 站点 source 与 canonical contract 不一致；
- 需要修改 DBOS/SAEE 才能让契约成立。

## 7. Recommendation Result（建议结果）

```text
RECOMMENDATION=ADOPT_AGENT_EVALUATION_ENTRY_CONTRACT_V0_1_AS_DEVELOPMENT_MACHINE_CONTRACT
STANDING_DIRECTIVE_APPLICABLE=true
EXACT_DECISION_RECORD_REQUIRED=true

IMPLEMENTATION_AUTHORIZED=false
EXTERNAL_OUTREACH_AUTHORIZED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
PUBLIC_RELEASE_OR_DEPLOYMENT_AUTHORIZED=false
```
