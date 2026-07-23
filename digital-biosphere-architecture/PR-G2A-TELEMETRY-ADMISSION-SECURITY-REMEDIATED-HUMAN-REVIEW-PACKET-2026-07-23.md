---
document_id: TMAI-PR-G2A-TELEMETRY-ADMISSION-SECURITY-REMEDIATED-HUMAN-REVIEW-PACKET-20260723-017
title: DBOS PR-G2A Telemetry Admission Security-Remediated Human Review Packet
title_zh: DBOS PR-G2A 遥测准入安全修复版人工审查决策包
status: ready-for-human-security-review-not-approved
decision_reference: PR-G2A
implementation_decision_reference: DQ-018
supersedes_packet: TMAI-PR-G2A-TELEMETRY-ADMISSION-HARDENED-HUMAN-REVIEW-PACKET-20260722
decided_by_ref: null
production_ready: false
---

# DBOS PR-G2A Telemetry Admission Security-Remediated Human Review Packet

中文：DBOS PR-G2A 遥测准入安全修复版人工审查决策包。

## 1. Decision Question（决策问题）

是否批准 DBOS `DQ-018` 的 exact security-remediated offline Telemetry Admission reference slice
（精确安全修复版离线遥测准入参考切片）通过 `PR-G2A`？

批准只表示该离线 SQLite reference slice 满足本阶段有界架构、完整性、恢复、供应链、安全停止条件
和可复现性要求，并允许 `DQ-019` 的候选输入审查开始。批准不等于完整 `PR-G2`、production
persistence 选型或实施授权，也不授权 PR、merge、main、release、deployment、listener、
Collector、production database、Evidence、Permission、Agent、Runtime、Entity 或 SAEE output。

## 2. Exact Review Subject（精确审查对象）

```text
DBA_BRANCH=codex/production-observability-baseline
DBA_REVIEW_PACKET_COMMIT=PENDING_THIS_PACKET_COMMIT
DBOS_REPOSITORY=joy7758/digital-biosphere-os
DBOS_BRANCH=codex/telemetry-admission-foundation
DBOS_EXACT_SECURITY_REMEDIATED_SOURCE_COMMIT=ee90c0c84964f1f3e4dbeb8dffaf888f9822b6a5
DBOS_EXACT_SECURITY_REMEDIATED_SOURCE_TREE=a8f2768b707c467607d4939d3e797327af4e9d31
DBOS_SECURITY_REMEDIATION_RECEIPT_COMMIT=901bf0dda66e46f8b1c0b5873f5c5f20e9d03920
DBOS_SECURITY_REMEDIATION_RECEIPT_TREE=aa5d909e3f39d84cc0f787472845eb904c1d9fcd
IMPLEMENTATION_MANIFEST=sha256:306435cd3c5fc65e46995f0e2a57b1322f950889af350f1b0bcbd13c35644fd9
IMPLEMENTATION_FILES=58
IMPLEMENTATION_BYTES=730759
SECURITY_REMEDIATION_ATTESTATION=TMAI-PR-G2A-SECURITY-REMEDIATION-ATTESTATION-20260723-016
```

DBOS canonical review receipt：

`reports/telemetry-admission-foundation/DBOS-PR-2A-SECURITY-REMEDIATION-NATIVE-REVALIDATION-2026-07-23.json`

DBA independent attestation：

[`PR-G2A-SECURITY-REMEDIATION-ATTESTATION-2026-07-23.md`](PR-G2A-SECURITY-REMEDIATION-ATTESTATION-2026-07-23.md)
/ [JSON](PR-G2A-SECURITY-REMEDIATION-ATTESTATION-2026-07-23.json)

## 3. Successor Reason（后继原因）

2026-07-23 security precheck 在 source `23c8f08…` 发现两个 High finding：

- `HSR-PRE-001`：explicit store/backup direct parent 未强制 caller ownership 和非 group/world writable；
- `HSR-PRE-002`：`id_factory` / `clock` callback 输出可绕过 persistence boundary validation。

当前 source `ee90c0c…` 在 DQ-018 授权范围内关闭这两个 finding，增加 4 个对应负例，并完成全仓、
原生 Linux x86_64、供应链、负载、恢复和远端 clean-clone 重验证。旧 preparation、旧 source 和旧
receipt 保留为历史，不被覆盖或改写。

## 4. Review Evidence（审查证据）

| evidence | observed result | boundary |
|---|---|---|
| remote receipt | `901bf0d…` fresh clone，exact source parent `ee90c0c…` | remote branch exact binding |
| source manifest | 58/58 files，730,759 bytes，`sha256:306435cd…44fd9` | reports excluded from source manifest |
| full tests | `538/538 PASS` | 16 test directories |
| focused telemetry tests | `204/204 PASS` | synthetic metadata-only |
| validators | 30 PASS + 5 expected external-source fail-closed + 0 unexpected | telemetry validator `25/25` |
| OTel authorized cases | Semantic `32/32` + Schema/Resource `36/36` | 23 DQ-020 deployment cases blocked |
| HSR-PRE-001 negatives | world-writable direct parent rejected | does not prove multi-tenant isolation |
| HSR-PRE-002 negatives | invalid/sensitive/exception callbacks rejected without reflection or persistence | DBOS-local callback boundary only |
| static quality/security | Ruff 0; Bandit 5,422 LOC / 0 findings / 0 `nosec` | automated result, not Human Security Review |
| locked dependencies | 7 runtime packages / 0 known vulnerabilities | `pip-audit 2.10.1`; point-in-time lock |
| reproducible wheel | two builds identical, `sha256:18679ffc…928d` | not published or released |
| native load/recovery | `TA-P001`—`TA-P005` and rollback all `PASS` | characterization, not SLO |
| authority | all receipt effect fields `false` | no gate or governed-state change |

## 5. Finding Disposition and Open Risks（发现处置与开放风险）

| finding | status | decision boundary |
|---|---|---|
| `HSR-PRE-001` High | `CLOSED_BY_REMEDIATION_AND_INDEPENDENT_REMOTE_ATTESTATION` | current exact source only |
| `HSR-PRE-002` High | `CLOSED_BY_REMEDIATION_AND_INDEPENDENT_REMOTE_ATTESTATION` | current exact source only |
| `HSR-PRE-003` Medium | `OPEN_SCOPED_RESIDUAL` | digest is not signature; DQ-019/PR-G2B authenticity input |
| `HSR-PRE-004` Medium | `OPEN_SCOPED_RESIDUAL` | no listener/decoder; DQ-020 must prove pre/post-decode budgets |

Additional non-claims：

- independent Human Security Review 尚未执行或记录；
- SQLite reference 不证明 HA、PITR、production RPO/RTO、容量或 SLO；
- production persistence backend、Owner、topology、cost/security 和 direct drills 尚未决定；
- `PR-G2T`、`PR-G2I`、`PR-G2C` 与 DQ-020 的 deployment cases 未完成；
- Telemetry 不自动成为 Evidence、Verification、Truth、Permission 或 SAEE authority。

## 6. Agent Recommendation（智能体建议）

```text
recommendation=ENTER_PR_G2A_HUMAN_SECURITY_REVIEW
confidence=HIGH_WITH_EXPLICIT_SCOPE_LIMITS
recommended_as=EXACT_SECURITY_REMEDIATED_OFFLINE_SQLITE_TELEMETRY_ADMISSION_REFERENCE_SLICE
not_recommended_as=HUMAN_SECURITY_APPROVED_PRODUCTION_PERSISTENCE_OR_TELEMETRY_SERVICE
production_customer_recommendable_now=false
full_pr_g2_ready=false
```

潜在客户若询问 production-approved trusted persistence layer、Collector/OTLP service 或 production
SLO，不推荐当前切片；若其需要一个可审查、失败关闭、无 listener 的 offline reference slice，
推荐把当前 exact source 提交给 Human Security Review。

## 7. Human Review Checklist（人工审查清单）

人工审查者必须逐项记录：

1. exact source / tree / receipt / manifest 是否与本包完全一致；
2. `HSR-PRE-001/002` 的修复是否充分且不存在新的 Critical/High finding；
3. `HSR-PRE-003/004` 是否继续保持 scoped Medium residual，不被误写为已关闭；
4. no listener、no Collector、no production persistence、no Evidence、no Permission 和 no SAEE 是否保持；
5. native load、automated scans 和 remote attestation 是否没有被升级成生产 SLO 或安全批准；
6. approval 是否只允许 `DQ-019` candidate input review，而不授权 implementation；
7. 如需批准、退回或拒绝，必须使用下方精确 token 和人类 `decided_by_ref`。

## 8. Human Decision Tokens（人工决策 Token）

只接受以下一个精确 token：

```text
PR-G2A=APPROVE_DQ_018_SECURITY_REMEDIATED_OFFLINE_TELEMETRY_ADMISSION_REFERENCE_SLICE
```

或：

```text
PR-G2A=RETURN_DQ_018_SECURITY_REMEDIATED_OFFLINE_TELEMETRY_ADMISSION_FOR_REVISION
```

或：

```text
PR-G2A=REJECT_DQ_018_SECURITY_REMEDIATED_OFFLINE_TELEMETRY_ADMISSION_REFERENCE_SLICE
```

同时必须提供：

```text
decided_by_ref=<human-review-authority>
```

当前没有收到上述 token；因此：

```text
PR_G2A_READY_FOR_HUMAN_REVIEW=true
HUMAN_SECURITY_REVIEW_COMPLETE=false
PR_G2A_HUMAN_REVIEW_APPROVED=false
```

## 9. Effect of Future Approval（未来批准的效力）

```text
PR_G2A=PASS
DQ_019_CANDIDATE_INPUT_REVIEW_MAY_PROCEED=true
DQ_019_IMPLEMENTATION_AUTHORIZED=false
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

批准只允许进入下一项独立 decision-input convergence（决策输入收敛），不允许创建或部署
production resource。
