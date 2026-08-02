---
document_id: TITMAS-AGENT-SAFETY-SIGNAL-RELAY-DECISION-REPORT-0.1-AMENDMENTS
title: TITMAS Agent Safety Signal Relay Decision Report v0.1 Amendment Notes
title_zh: TITMAS 智能体安全信号中继决策报告 v0.1 修订说明
status: ACCEPTED_P0_P3_AMENDMENT_RECORD
subsequent_decision_ref: ADR-041
source_report_sha256: 61837df3dc9d687f5b2b71e9dc1735af84556b6ad95a83bd4a8d409d6941842b
decision_ref: ADR-040
implementation_status: NOT_IMPLEMENTED
---

# TITMAS 智能体安全信号中继决策报告 v0.1 修订说明

## 1. Source preservation（原始报告保留）

审查输入：
[`titmas-agent-safety-signal-relay-decision-report-v0.1.md`](titmas-agent-safety-signal-relay-decision-report-v0.1.md)

```text
SOURCE_REPORT_SHA256=61837df3dc9d687f5b2b71e9dc1735af84556b6ad95a83bd4a8d409d6941842b
SOURCE_REPORT_MODIFIED=false
SOURCE_REPORT_STATUS_REINTERPRETED_AS_IMPLEMENTED=false
```

原始报告继续是 `PROPOSED_REVIEW_REQUIRED` 的架构审查输入。本修订说明和 ADR-040 记录后续
Human Decision，不回写或删除原报告的当时事实。

## 2. Human amendments（人工修订）

| v0.1 area | Amendment | Normative destination |
|---|---|---|
| 授权范围 | 只批准 P0–P3；P4–P10、实现、建仓、公共信号仍未授权 | ADR-040 |
| Owner | DBA 为架构事实源；未来候选仓库未生效 | ADR-040 |
| Publisher trust | `publisher_assurance` 与 `recipient_local_trust_decision` 分离；无全局分数 | P2/P3 |
| Applicability | 只保留三值；本地测试使用独立四值结果 | P2 |
| beneficial capability | 限于检测、恢复、防御、隔离、安全候选发现 | P2 |
| Disclosure | 加入四级字段级 disclosure ceiling | P2/P3 |
| Cause | 加入五类 cause status；异常不自动证明攻击 | P2 |
| Standard reuse | 增加 OpenID SSF、SCITT，并细化 STIX/TAXII/AOP/DBOS/Agent Evidence/ARO | P1 |
| Publication/privacy/revocation | 冻结提交、复现、高影响发布、隐私、保留、撤回和攻击处置规则 | P3 |
| DQ-006/R-007 | 形成 Relay-scope exact disposition；不冒充全局 Portfolio closure | ADR-040、驾驶舱台账 |

## 3. Unchanged conclusions（保持不变）

- 候选未来主仓名仍为 `titmas-agent-safety-signal-relay`，但未创建、未激活；
- Signal lifecycle 不等于 Agent Identity/Execution/Evidence lifecycle；
- `tiamas-scout` 只能是未来可选只读候选生产者；
- `redcrag.cn` 只能派生展示，不是事实源；
- 收到信号、适用性匹配、证据引用和发布者保证都不产生行动授权或 Truth；
- 当前服务推荐仍是 `NO_GO`，条件认可只指未来离线试点评审门，不是生产推荐。

## 4. Decision effect（决定效力）

```text
P0_P3_ARCHITECTURE_WORK_AUTHORIZED=true
P4_P10_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
NEW_REPOSITORY_AUTHORIZED=false
PUBLIC_SIGNAL_AUTHORIZED=false
PUBLIC_PRODUCTION_RECOMMENDED=false
```
