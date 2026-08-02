---
document_id: TITMAS-AGENT-SAFETY-SIGNAL-RELAY-OPEN-ISSUES-0.1
title: TITMAS Agent Safety Signal Relay Unresolved Issues v0.1
title_zh: TITMAS 智能体安全信号中继尚未解决问题清单 v0.1
status: ACTIVE_OPEN_ISSUES_AFTER_P0_P3
decision_ref: ADR-040
implementation_authorized: false
---

# TITMAS 智能体安全信号中继尚未解决问题清单 v0.1

P0–P3 完成不消除以下问题。它们不得被隐式默认、LLM 补齐或路线图语言改写为已解决。

| issue_id | Open question | Required owner/decision | Blocks |
|---|---|---|---|
| `ASSR-OI-001` | 是否创建 `titmas-agent-safety-signal-relay`，canonical remote/branch/license/status source 是什么 | Human Program Owner + G0/G1 | 建仓、全部实现 |
| `ASSR-OI-002` | CSAF compatibility 是 profile、extension 还是双格式映射；namespace/registration 如何确定 | DBA architecture + standards review | P4 schema freeze |
| `ASSR-OI-003` | DSSE/in-toto 与 SCITT COSE statement 是否并存、转换或择一；签名 bytes scope 如何固定 | Security architecture decision | P5 envelope work |
| `ASSR-OI-004` | TUF root/targets/snapshot/timestamp roles、threshold、rotation、recovery owner 如何分离 | Human security/key governance | P5 update/revocation work |
| `ASSR-OI-005` | OpenID SSF Agent Safety Signal event type、subject identifier 和 full-object retrieval profile 如何注册/命名 | Interoperability review | future delivery profile |
| `ASSR-OI-006` | STIX/TAXII adapter 的实际客户/生态需求是否足以支持采用 | Agent customer validation | adapter work；不阻塞 core spec |
| `ASSR-OI-007` | SCITT Transparency Service 是否必要，还是多镜像 + TUF 已足够 | Threat/cost review | public anti-equivocation design |
| `ASSR-OI-008` | DBOS stable identity、execution context、Evidence Admission 的 exact schema/version/ref mapping | DBOS Owner + independent G3 | P4/P5 integration mapping |
| `ASSR-OI-009` | `agent-evidence` receipt/bundle 的 exact canonical API/schema 选择及版本承诺 | Agent Evidence Owner + G3 | evidence adapter |
| `ASSR-OI-010` | ARO README 与 `docs/boundaries.md` 对 audit control plane 的表述冲突如何解决 | ARO Owner | ARO dependency；不阻塞 core spec |
| `ASSR-OI-011` | applicability predicate language、unknown/conflict precedence 和 cross-language determinism | DBA + future implementation review | P4 |
| `ASSR-OI-012` | high-impact taxonomy、minimum independent roles 和 evidence assurance threshold 的具体 profile | Human risk decision | public publication profile |
| `ASSR-OI-013` | P3 retention 数值仅为 `ARCHITECTURE_DEFAULT_PENDING_LEGAL_PRIVACY_REVIEW`；在不同司法/合同环境是否适用、legal hold/erasure 冲突如何处理 | Privacy/legal Owner | 任何真实数据保留、restricted/public service |
| `ASSR-OI-014` | `tiamas-scout` 无 canonical origin、现有普通 opportunity discovery 与 safety profile 如何物理隔离 | Scout Owner + G1/G2 | Scout 上游接入 |
| `ASSR-OI-015` | `redcrag.cn` source → build → release pointer → live parity 如何恢复并持续证明 | Site Owner | public derived entry |
| `ASSR-OI-016` | 谁可以担任 Publisher、Independent Reproducer、High-impact Reviewer、Emergency Revoker，如何证明独立 | Human governance decision | publication authorization |
| `ASSR-OI-017` | recipient proof-backed vs self-attested profile 的 assurance vocabulary 如何与 DBOS 对齐 | DBOS/DBA mapping decision | P4/P6 |
| `ASSR-OI-018` | public-safe exploit abstraction 到何种粒度既可检测又不增加攻击可用性 | Security/disclosure review | public signal content |
| `ASSR-OI-019` | P4–P6 是否授权，以及精确文件/仓库/测试/外部写入边界 | Human Program Owner | next stage |

## DQ-006 and R-007 status（DQ-006 与 R-007 状态）

这两项在 Relay scope 内不是未决：ADR-040 已做 exact disposition。仍未决的是 DQ-006 对
其它项目的全局 Portfolio Admission，以及 R-007 在非 Relay 场景的全局重复建设风险。

```text
DQ_006_RELAY_SCOPE_UNRESOLVED=false
R_007_RELAY_SCOPE_UNRESOLVED=false
DQ_006_GLOBAL_PORTFOLIO_QUESTION_OPEN=true
R_007_GLOBAL_DUPLICATION_RISK_OPEN=true
```

## Stop state（停止状态）

```text
P4_P10_AUTHORIZED=false
IMPLEMENTATION_AUTHORIZED=false
NEW_REPOSITORY_AUTHORIZED=false
PUBLIC_SIGNAL_AUTHORIZED=false
WORK_MUST_STOP_AFTER_P0_P3=true
```
