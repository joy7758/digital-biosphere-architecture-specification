---
document_id: DBA-RISK-BLOCKER-REGISTER-0.1
title: Digital Biosphere Program Risk and Blocker Register v0.1
title_zh: 数字生物圈项目群风险与阻塞台账 v0.1
status: active-risk-register
as_of_date: 2026-07-21
risk_acceptance_authority_assigned: false
---

# Digital Biosphere Program Risk and Blocker Register v0.1（数字生物圈项目群风险与阻塞台账 v0.1）

## 1. Risk Scale（风险等级）

- `CRITICAL`：可能导致越权、历史破坏、错误发布或不可恢复状态；
- `HIGH`：阻塞核心项目群推进或使驾驶舱失真；
- `MEDIUM`：增加重复建设、漂移或维护成本；
- `LOW`：局部可恢复问题。

风险等级不自动产生停止、授权或风险接受决定。

## 2. Active Risks（当前风险）

| risk_id | level | 风险 | 当前证据 | 缓解措施 | Owner 状态 |
|---|---|---|---|---|---|
| `R-002` | `HIGH` | DBA 本地 Git root 是 `/Users/zhangbin/Documents/New project`，不是 DBA 目录；远端树保留额外目录层 | 2026-07-21 `git rev-parse --show-toplevel` 与已发布远端结构 | 处理 `DQ-002`；在决定前禁止历史重写、删除或 force push | `DECISION_REQUIRED` |
| `R-003` | `HIGH` | 核心项目没有经 DBA 确认的统一 canonical status source | DBOS、SAEE 有多个 README、status、manifest 和证据表面；Pilot 有独立 readiness 状态 | 处理 `DQ-003`，为每项目记录一个规范入口及冲突规则 | `DOMAIN_CONFIRMATION_REQUIRED` |
| `R-004` | `MEDIUM` | 核心项目工作树存在大量当前变化，静态快照容易过期或误读 | 2026-07-21 只读 Git observation | 驾驶舱只记录 commit、branch、时间和状态来源；dirty count 不作为成熟度 | `MITIGATED_BY_POLICY` |
| `R-005` | `HIGH` | DBOS ↔ SAEE 接口曾只有 Specification，容易被误写成已集成 | 2026-07-21 已完成同一 synthetic envelope 的 scoped local conformance；没有生产 Runtime、写回或真实 Evidence | 保留 `SCOPED_LOCAL` 限定；clean clone 与 source release 后再评审更高状态 | `LOCAL_MITIGATION_VALIDATED_NOT_RELEASED` |
| `R-006` | `MEDIUM` | Research Agent Pilot 没有发现 `origin`，且当前 `NOT_READY` | Pilot README、Git observation | 先完成 Human Review 和 source approval；远端决策独立处理 | `PILOT_OWNER_INPUT_REQUIRED` |
| `R-007` | `MEDIUM` | POP、ARO、Agent Evidence、Token Governor 与 DBOS/SAEE 存在潜在重复责任 | DBA project mapping 与本地候选发现 | 逐项目执行 Portfolio Admission 和 duplicate capability review | `REVIEW_REQUIRED` |
| `R-008` | `MEDIUM` | 静态驾驶舱可能把旧观察继续展示为当前事实 | 当前没有 refresh cadence 或只读 adapter | 每个快照必须带 `observed_at`；过期标记 `STALE`；处理 `DQ-007` | `POLICY_DEFINED_IMPLEMENTATION_PENDING` |
| `R-009` | `HIGH` | Program Governance 被误读为 DBOS/SAEE 执行或代码控制权 | 用户原始管理意图与现有 authority model 的语义张力 | 在 Charter、Program Governance Spec 和 AGENTS 中固定权力分离 | `MITIGATED_BY_SPECIFICATION` |
| `R-010` | `HIGH` | 当前 Program Governance Cockpit 与既有 DBA public meaning layer 可能形成双重 DBA 入口和规范漂移 | README canonicality、project mapping 与既有独立公开仓库 | 处理 `DQ-008`；决定单一前门、交叉引用、迁移或长期分工，决定前不得声称已完成 canonical reconciliation | `DECISION_REQUIRED` |
| `R-011` | `HIGH` | DBOS 当前文档演化与 `DBOS-EXP-0001` 冻结 identity evidence 的校验语义冲突 | Version-aware historical binding 已实现；旧 digest 未改写；34/34 validators 通过并对当前漂移发 warning | source 隔离与 clean-clone 回归后再决定是否正式关闭 | `LOCAL_MITIGATION_VALIDATED_NOT_RELEASED` |
| `R-012` | `MEDIUM` | DBOS 默认顶层测试曾发现 0 tests，开发者可能误读结果 | `tools/run_tests.py` 现在逐目录运行且零测试失败；331/331 tests | 发布时只推荐单一 runner，并保留其自测 | `LOCAL_MITIGATION_VALIDATED_NOT_RELEASED` |
| `R-013` | `HIGH` | Developer Preview 尚未形成三个包含当前 Owner 决定、许可证和公共 Adapter 的最终远端 source commits | DBA/DBOS 已有前一远端基线；SAEE 精确提取已授权但未实现；原 SAEE 内部工作树仍高度脏且不可作为发布源 | 各仓库使用隔离分支；SAEE 从 public `origin/main` 提取精确 blob；合并后从最终远端复验 | `BLOCKING_RELEASE` |
| `R-014` | `HIGH` | 3–5 人小样本、个别正面反馈或试用 PASS 可能被过度解释为客户验证、市场采用或发布授权 | External Developer Trial Plan 明确样本仅验证 onboarding、理解、使用和问题相关性信号 | 预冻结成功阈值；保留失败；Trial Result、Customer Validation、Release、Adoption 分开；发布仍需 `DQ-009` | `MITIGATED_BY_PLAN_NOT_YET_TESTED` |

## 3. Active Blockers（当前阻塞）

| blocker_id | 阻塞事项 | 阻塞范围 | 解除条件 | 不阻塞 |
|---|---|---|---|---|
| `B-002` | DBA Git topology（Git 拓扑）未决定 | 独立仓库根、干净发布结构和后续自动化 | `DQ-002` 选择并执行单独授权的迁移方案 | 当前工作树内的非破坏性文档更新 |
| `B-003` | canonical status source 未确认 | 自动或周期性可信状态汇总 | DBOS、SAEE、Pilot 各自提供 source + freshness + conflict policy | 当前时间点只读 snapshot |
| `B-004` | Research Agent Human Review 与 approved source 不完整 | Prototype Authorization Review 和实验 | Pilot 自己的 readiness gate 达到可审查状态并获得人工决定 | Pilot 规范改进和 DBA 项目群规划 |
| `B-005` | 两个 DBA 语义表面未完成 canonical reconciliation | 对外唯一入口、规范优先级和自动检索路由 | `DQ-008` 形成决定并完成引用/迁移验证 | 当前仓库作为 Program Governance Cockpit 的工作树基线 |
| `B-007` | 三仓库本阶段变化尚未形成隔离、可引用的 source commits，且未做 clean-clone 复验 | Developer Preview release、真实外部开发者试用和 `DQ-009` | 精确变更隔离、审查、commit 与 clean-clone validation | 当前本地候选演示、测试和文档审查 |

## 4. Resolved Risk and Cleared Blockers（已解决风险与已解除阻塞）

| item_id | 原问题 | 解除证据 | 保留边界 |
|---|---|---|---|
| `R-001` | Program Authority 未指派 | `ADR-020` 指派 `zhangbin` 并记录复核、替代和权力边界 | 不产生运行、演化、账号或发布权；重大 release 时复核 |
| `B-001` | 没有已记录的 Program Owner / decision source | `DQ-001` / `ADR-020`，`decided_by_ref=zhangbin` | 每个执行、外部联系和发布动作仍遵循各自 gate |

| blocker_id | 原阻塞 | 解除证据 | 保留边界 |
|---|---|---|---|
| `B-006` | 冻结 `README.md` digest 与当前文档漂移导致 validator 失败 | Version-aware historical binding；34/34 validators `PASS`；旧 digest 未改写 | 仅当前本地工作树解除；未发布、未做 clean clone |

## 5. Risk Handling Rules（风险处理规则）

1. 风险只能由显式人工决定接受、缓解、转移或关闭；
2. `MITIGATED_BY_SPECIFICATION` 不表示运行风险已消失；
3. 失败、冲突和未知必须保留历史；
4. 子项目风险事实由子项目维护，DBA 只引用与项目群相关的摘要；
5. `CRITICAL` 或 `HIGH` 风险涉及 destructive action（破坏性操作）、权限、发布或外部影响时必须停止并请求新授权；
6. blocker 解除必须引用直接证据，不能只因计划存在而关闭。

```text
TRACKED_RISKS=14
ACTIVE_RISKS=13
RESOLVED_RISKS=1
ACTIVE_BLOCKERS=5
BLOCKERS_CLEARED=2
LOCAL_BLOCKERS_CLEARED_NOT_RELEASED=1
RISKS_ACCEPTED=0
RISK_REGISTER_GRANTS_AUTHORITY=false
```
