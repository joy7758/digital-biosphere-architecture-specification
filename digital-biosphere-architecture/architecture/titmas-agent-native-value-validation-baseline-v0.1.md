---
document_id: DBA-TITMAS-AGENT-NATIVE-VALUE-VALIDATION-BASELINE-0.1
title: TITMAS Agent-Native Value Validation Baseline v0.1
title_zh: TITMAS 智能体原生价值验证基线 v0.1
version: 0.1.0
status: verified-design-baseline
maturity: Development
owner_ref: zhangbin
decision_reference: USER_GOAL_2026-07-29
implementation_effect: none
experiment_effect: none
authority_effect: none
---

# TITMAS Agent-Native Value Validation Baseline v0.1

## 1. Scope and source

本基线只核验
`joy7758/digital-biosphere-architecture-specification` 的远端连续基线
`codex/titmas-xiarizhihai-brand-identity-v1@69df945c7b2663a87b15b275fa78b065fb23f70a`。
它不导入本地主工作区的未跟踪材料，也不把 DBOS、SAEE 或 Agent Evidence 的目标描述
升级为当前实现事实。

允许的事实分类：

- `IMPLEMENTED`：本仓库存在可执行、可复验的实现表面；
- `DOCUMENTED`：有文档或契约，但不能据此推导实现；
- `PILOT_TESTED`：在已声明限制的受控 Pilot 中执行过；
- `DESIGN_ONLY`：仅为设计、候选 Profile 或解释层；
- `UNKNOWN`：当前远端基线没有足够证据；
- `CONFLICT`：多个来源对同一事实给出不兼容结论。

## 2. Verified capability matrix

| surface | classification | verified fact | limitation |
|---|---|---|---|
| TITMAS v1.1 machine discovery, registries, CLI and conformance | `IMPLEMENTED` | `agent-index.json`、12 项任务、Schemas、CLI、Harness 和本地测试存在 | Development candidate，不是公开社区或 Stable 标准 |
| TITMAS v1.1 controlled agent-native pilot | `PILOT_TESTED` | 7 个隔离 session、1 条独立模型 lineage，Pilot 状态 `PASS` | 合成、本地、单 lineage；不是采用或价值证明 |
| Agent-native operational value | `DOCUMENTED` | 已显式记录 `TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false` | 未证明 |
| Agent-native self-maintenance | `DOCUMENTED` | 已显式记录 `TITMAS_AGENT_COMMUNITY_SELF_MAINTENANCE_DEMONSTRATED=false` | 未证明 |
| Agent Evidence | `DOCUMENTED` | 作为既有 Evidence 输入／映射边界被引用 | 本仓库未核验其当前实现与远端版本 |
| VEAP | `DESIGN_ONLY` | 存在 Development 阶段 envelope、crosswalk、问题验证与审查材料 | 不是发布标准、运行实现或商业采用 |
| VEC | `DESIGN_ONLY` | 仅作为 execution-proof candidate 名称出现 | 没有证书 Authority、Stable Schema 或实现事实 |
| DBOS boundary | `DOCUMENTED` | DBOS governs existence，并拥有 canonical Evidence／Verification 边界 | 本任务未改动或重新验证 DBOS 代码 |
| SAEE boundary | `DOCUMENTED` | SAEE 提供只读 Evaluation、Risk 和 Recommendation | Evaluation 不等于 Authority；本任务未改动 SAEE |
| Digital Survival Dynamics | `UNKNOWN` | 选定远端基线没有找到可作为 current truth 的规范文件 | 不从本地未跟踪候选回填 |
| TITMAS Agent-Native Community v1.1 | `IMPLEMENTED` | 内部机器基础设施候选和受控 Pilot 证据存在 | `PUBLIC_AGENT_COMMUNITY_AUTHORIZED=false`、`COMMUNITY_ESTABLISHED=false` |

没有发现同一 canonical fact 的直接 `CONFLICT`；发现的是成熟度和声明范围不同，已在表中分开。

## 3. Frozen negative evidence

以下来自 v1.1 的 `Agent Immune` 五任务 value-gate fixture，必须原样保留：

```text
TOTAL_AGENT_OUTPUTS=25
UNIQUE_FACTUALLY_VALID_FINDINGS=3
DUPLICATE_FINDINGS=5
FALSE_OR_NOT_APPLICABLE_FINDINGS=17
FINAL_OUTCOME_IMPROVEMENTS=0
HARMFUL_MODIFICATIONS=0
AGENT_NOISE_RATE=0.88
FINAL_OUTCOME_IMPROVEMENT_RATE=0.0
OUTPUT_VOLUME_NE_VALUE=true
```

受控 Pilot 还记录：

```text
SESSION_COUNT=7
MODEL_COUNT=1
INDEPENDENT_LINEAGE_COUNT=1
CURRENT_HUMAN_INTERVENTION_RATE=0.0833
LONG_TERM_HUMAN_INTERVENTION_TARGET_MAX=0.01
```

`Pilot Pass` 只说明已定义的基础设施阈值通过。它不证明操作价值、外部采用、模型独立性、
自维护、生产就绪或商业价值。

## 4. Baseline result

```text
TITMAS_AGENT_NATIVE_BASELINE_VERIFIED=true
TITMAS_AGENT_NATIVE_PILOT_TESTED=true
TITMAS_AGENT_NATIVE_PILOT_PASSED=true
TITMAS_AGENT_NATIVE_VALUE_VALIDATION_EXECUTED=false
TITMAS_AGENT_OPERATIONAL_VALUE_DEMONSTRATED=false
TITMAS_AGENT_COMMUNITY_SELF_MAINTENANCE_DEMONSTRATED=false
OUTPUT_VOLUME_NE_VALUE=true
BASELINE_CONFLICT=false
```

