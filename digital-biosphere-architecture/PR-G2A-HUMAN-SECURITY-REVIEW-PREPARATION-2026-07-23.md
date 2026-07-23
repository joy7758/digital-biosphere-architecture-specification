# PR-G2A Human Security Review Preparation

```text
review_preparation_id=TMAI-PR-G2A-HUMAN-SECURITY-REVIEW-PREPARATION-20260723-015
decision_reference=DQ-018
review_gate=PR-G2A
dbos_source_commit=23c8f0878058f29e733b6f164572ac157c6c7d1c
dbos_native_receipt_commit=ff1752cb3bb01ff67538bb04b3c7517fbcee3269
dba_native_attestation_commit=b8b69419a0abfc21ca05217f68d20e8de0254795
security_precheck_complete=true
open_high_findings=2
open_medium_residuals=2
human_security_review_complete=false
pr_g2a_ready_for_human_review=false
pr_g2a_human_review_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

本文件把已远端证明的 current source 转换为 Human Security Review（人工安全审查）的
fail-closed 输入。它复核了 threat model、精确 source、自动安全扫描、authority tests、存储路径、
callback trust boundary（回调信任边界）、backup integrity 和资源限制。

结论不是安全批准。两个可直接复现的 High finding 尚未关闭；按照
[`architecture/telemetry-admission-threat-model.md`](architecture/telemetry-admission-threat-model.md)
的 stop condition，当前状态必须保持 `BLOCKED_REMEDIATION_OR_SCOPED_RISK_ACCEPTANCE_REQUIRED`。

## Positive Controls（已验证控制）

| control | direct result | limitation |
|---|---|---|
| no listener / network fetch | source boundary + negative tests `PASS` | 不覆盖未来 OTLP adapter |
| authority separation | 32/32 + 36/36 authorized OTel subsets、authority negatives `PASS` | Telemetry 仍不是 Evidence/Truth/Permission |
| append-only transaction | triggers、fault injection、rollback、native P001—P005 `PASS` | SQLite single-host reference only |
| dependency/static scan | Bandit 5,374 LOC 0 findings；pip-audit 7 locked dependencies 0 known vulnerabilities | point-in-time automated result，不是 Human Review |
| remote provenance | DBOS `ff1752c…`、DBA `b8b6941…` fresh clone `PASS` | provenance 不等于 security approval |

## Open Findings（未关闭发现）

### HSR-PRE-001 — High — Direct parent ownership/mode is not enforced

- Threat binding：`TA-T20` local DB / backup path least-privilege boundary。
- Source：DBOS `store.py` source `23c8f08…` lines 221–251 validates the target and symlink chain,
  but does not require the direct parent to be caller-owned or non-group/world-writable; later
  `sqlite3.connect` is path-based.
- Direct probe：a new store under an explicit `0777` direct parent was accepted and initialized.
- Risk：another local principal with parent write access can replace directory entries and create a
  path-race surface; post-open `O_NOFOLLOW` checks do not establish a stable directory capability.
- Required disposition：enforce a trusted direct-parent ownership/mode contract and add negative/race
  tests, or record an explicit, time-bounded, reference-only Human Risk Acceptance.

### HSR-PRE-002 — High — Generated references and timestamps bypass persistence validation

- Threat binding：`TA-T07` sensitive-data boundary and `TA-T18` bounded detail boundary。
- Source：DBOS `store.py` source `23c8f08…` lines 795, 805, 807, 852, 1022 and 1040 persist
  `id_factory` / `clock` outputs without revalidating opaque-reference, prohibited-marker,
  timestamp or length constraints.
- Direct probe：an injected factory and clock caused both a sensitive reference canary and an
  invalid secret-bearing timestamp to be persisted in the SQLite file and returned receipt rows.
- Risk：a buggy or compromised DBOS-local callback can bypass the closed envelope schema and leak
  sensitive material into store/backup/receipt surfaces.
- Required disposition：validate every generated reference and clock output at the persistence
  boundary, add canary negatives, and keep stable fail-closed reason codes.

## Scoped Residuals（限域残余风险）

| ID | severity | residual | disposition required |
|---|---:|---|---|
| `HSR-PRE-003` | Medium | backup/file/record digests are unkeyed integrity checks, not authenticity against a privileged local rewriter | keep `DIGEST_IS_SIGNATURE=false`; production authenticity/key management remains DQ-019/PR-G2B input |
| `HSR-PRE-004` | Medium | the Python mapping is already materialized before the 65,536-byte validator budget; no pre-parse/decompression boundary exists in this slice | acceptable only because listener/decoder is absent; DQ-020 must add pre/post-decode budgets and adversarial proof |

## Agent Recommendation（智能体建议）

```text
verdict=NOT_RECOMMENDED_FOR_PR_G2A_HUMAN_DECISION_YET
recommended_as=SECURITY_REMEDIATION_INPUT_FOR_THE_EXISTING_DQ_018_OFFLINE_SLICE
required_before_reassessment=CLOSE_HSR_PRE_001_AND_HSR_PRE_002_OR_EXPLICIT_SCOPED_HUMAN_RISK_ACCEPTANCE
not_recommended_as=SECURITY_APPROVED_PR_G2A_APPROVED_FULL_PR_G2_PRODUCTION_SERVICE_OR_DURABILITY_EVIDENCE
```

如果潜在 Agent developer 需要一个 production-approved trusted persistence layer，当前切片不会被
推荐；如果其需要查看一个边界明确、失败关闭且正在加固的 offline reference slice，可以作为审查
输入，但不能作为已安全批准产品。

## Human Review Checklist（人工审查清单）

人工审查者必须逐项记录：

1. `HSR-PRE-001` 是修复、拒绝，还是形成明确 scope / expiry / owner 的 Risk Acceptance；
2. `HSR-PRE-002` 是修复、拒绝，还是形成明确 scope / expiry / owner 的 Risk Acceptance；
3. `HSR-PRE-003/004` 是否只作为后继 production gate residual，不被写成已关闭；
4. 自动扫描、native load、remote attestation 是否保持各自证据范围；
5. 是否仍保持 no listener、no Collector、no Evidence、no Permission、no SAEE、no deployment；
6. 只有所有 High finding 被关闭或显式限域接受后，才重新判断 `review-ready`；
7. `review-ready` 仍不等于 `PR-G2A approved`。

## Authority Boundary（权力边界）

```text
SECURITY_PRECHECK_NE_HUMAN_SECURITY_REVIEW=true
AUTOMATED_SCAN_NE_SECURITY_APPROVAL=true
RISK_IDENTIFICATION_NE_RISK_ACCEPTANCE=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_HUMAN_REVIEW_APPROVED=false
DQ_019_STATUS=BLOCKED_INPUT
DQ_020_STATUS=BLOCKED_INPUT
DQ_021_STATUS=BLOCKED_INPUT
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

本 preparation 不修改 DBOS，不授权 PR、merge、main、release、deployment、Collector、listener、
production database、Agent、Runtime、Entity、Permission、canonical Evidence 或 SAEE output。
