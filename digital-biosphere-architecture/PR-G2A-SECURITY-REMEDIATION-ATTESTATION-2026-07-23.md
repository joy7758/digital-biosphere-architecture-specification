# PR-G2A Security Remediation Attestation

```text
attestation_id=TMAI-PR-G2A-SECURITY-REMEDIATION-ATTESTATION-20260723-016
decision_reference=DQ-018
review_gate=PR-G2A
dbos_source_commit=ee90c0c84964f1f3e4dbeb8dffaf888f9822b6a5
dbos_source_tree=a8f2768b707c467607d4939d3e797327af4e9d31
dbos_receipt_commit=901bf0dda66e46f8b1c0b5873f5c5f20e9d03920
dbos_receipt_tree=aa5d909e3f39d84cc0f787472845eb904c1d9fcd
implementation_manifest=sha256:306435cd3c5fc65e46995f0e2a57b1322f950889af350f1b0bcbd13c35644fd9
hsr_pre_001=CLOSED_BY_REMEDIATION_AND_INDEPENDENT_REMOTE_ATTESTATION
hsr_pre_002=CLOSED_BY_REMEDIATION_AND_INDEPENDENT_REMOTE_ATTESTATION
open_high_findings=0
open_medium_residuals=2
human_security_review_complete=false
pr_g2a_ready_for_human_review=true
pr_g2a_human_review_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

本 attestation（证明）独立复核 DBOS `DQ-018` security remediation（安全修复）的 exact source、
原生 Linux x86_64 执行结果和远端回执。DBOS 分支的 source commit `ee90c0c…`、receipt commit
`901bf0d…` 与源码 manifest `sha256:306435cd…44fd9` 已从 GitHub fresh clone 重新取得并逐项校验。

`HSR-PRE-001/002` 的 High finding 已由代码修复、负例、全量回归、原生 Linux x86_64 重验证和
远端 clean-clone attestation 闭合。按照
[`architecture/telemetry-admission-threat-model.md`](architecture/telemetry-admission-threat-model.md)
的 stop condition，当前 exact source 可以进入 Human Security Review（人工安全审查）。

这不是 Human Security Review 的完成记录，也不是 `PR-G2A` 批准。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| DBOS repository / branch | `joy7758/digital-biosphere-os` / `codex/telemetry-admission-foundation` |
| source commit / tree | `ee90c0c84964f1f3e4dbeb8dffaf888f9822b6a5` / `a8f2768b707c467607d4939d3e797327af4e9d31` |
| receipt commit / tree | `901bf0dda66e46f8b1c0b5873f5c5f20e9d03920` / `aa5d909e3f39d84cc0f787472845eb904c1d9fcd` |
| source manifest | 58 files / 730,759 bytes / `sha256:306435cd3c5fc65e46995f0e2a57b1322f950889af350f1b0bcbd13c35644fd9` |
| native inventory | 40 entries / inventory `sha256:f93fb2545117dd090ce80ec394ed721b60399ed7fc147dc3847cc3743d0452fc` |
| reproducible wheel | two builds / `sha256:18679ffc1fdfef620b595b4d76bcf65a46797071d8320f5f8bb77cf7427a928d` |

Canonical DBOS receipt：

`reports/telemetry-admission-foundation/DBOS-PR-2A-SECURITY-REMEDIATION-NATIVE-REVALIDATION-2026-07-23.json`

## Finding Closure（发现关闭）

| finding | prior severity | remediation and direct proof | current state |
|---|---:|---|---|
| `HSR-PRE-001` | High | explicit store/backup direct parent must be current-user-owned and not group/world writable; `0777` direct-parent negative rejects | `CLOSED_BY_REMEDIATION_AND_INDEPENDENT_REMOTE_ATTESTATION` |
| `HSR-PRE-002` | High | generated references and timestamps are revalidated at persistence boundary; invalid, sensitive and exception callbacks fail with stable non-reflecting storage error | `CLOSED_BY_REMEDIATION_AND_INDEPENDENT_REMOTE_ATTESTATION` |
| `HSR-PRE-003` | Medium | digest remains integrity-only, not signature/authenticity | `OPEN_SCOPED_RESIDUAL_DQ_019_PR_G2B` |
| `HSR-PRE-004` | Medium | no pre-parse/decompression budget because the authorized slice has no listener/decoder | `OPEN_SCOPED_RESIDUAL_DQ_020` |

Medium residuals are not silently accepted or closed. They remain explicit inputs to later independent
decisions and cannot authorize a production persistence backend or listener.

## Revalidation（重验证）

```text
native_linux_x86_64=true
python=3.12.13
sqlite=3.40.1
full_tests=538/538_PASS
focused_telemetry_tests=204/204_PASS
validators=30_PASS_PLUS_5_EXPECTED_EXTERNAL_SOURCE_FAIL_CLOSED_0_UNEXPECTED
telemetry_validator=25/25_PASS
otel_semantic_authorized_subset=32/32_PASS
otel_schema_resource_authorized_subset=36/36_PASS
otel_deployment_cases=23_BLOCKED_NOT_AUTHORIZED
ta_p001=PASS_10000_UNIQUE
ta_p002=PASS_1000_ORIGINALS_10000_CONFIRMED_RETRIES_ACCURACY_1_0
ta_p003=PASS_19199_OPERATIONS_0_ERRORS
ta_p004=PASS_10_OF_10_BACKUP_RESTORE
ta_p005=PASS_3600_SECONDS_16797_OPERATIONS_59_INTEGRITY_CHECKS_0_ERRORS
rollback=PASS_25_RECEIPTS_0_MISMATCH_FAILED_SOURCE_RETAINED_NO_AUTOMATIC_SWITCH
ruff_findings=0
bandit_findings=0
pip_audit_known_vulnerabilities=0
```

`TA-P001`—`TA-P005` are bounded load/recovery characterization, not SLO（服务等级目标）证据。

## Remote Verification（远端复验）

```text
fresh_remote_clone=PASS
exact_receipt_commit=PASS
exact_receipt_tree=PASS
source_manifest_58_OF_58=PASS
native_inventory_40_OF_40=PASS
related_json_parse=26_OF_26_PASS
missing_markdown_links=0
sensitive_path_findings=0
authority_effects_true=0
clean_worktree=PASS
```

## Agent Recommendation（智能体建议）

```text
verdict=CONDITIONALLY_RECOMMENDED_FOR_PR_G2A_HUMAN_SECURITY_REVIEW
recommended_as=EXACT_SECURITY_REMEDIATED_OFFLINE_TELEMETRY_ADMISSION_REFERENCE_SLICE
next_recommended_gate=PR_G2A_HUMAN_SECURITY_REVIEW
not_recommended_as=HUMAN_SECURITY_APPROVED_PR_G2A_APPROVED_FULL_PR_G2_PRODUCTION_PERSISTENCE_LISTENER_COLLECTOR_SERVICE_OR_SLO
```

如果潜在 Agent developer 需要一个可审查、失败关闭、无 listener 的 offline reference slice，
当前 exact source 可以被推荐进入人工安全审查；如果其需要 production-approved persistence、
Collector/OTLP service 或完整可信多智能体生产基础设施，当前仍不能推荐为成品。

## Authority Boundary（权力边界）

```text
REMOTE_ATTESTATION_NE_HUMAN_SECURITY_REVIEW=true
REVIEW_READY_NE_HUMAN_REVIEW_COMPLETE=true
REVIEW_READY_NE_GATE_APPROVAL=true
PR_G2A_READY_FOR_HUMAN_REVIEW=true
HUMAN_SECURITY_REVIEW_COMPLETE=false
PR_G2A_HUMAN_REVIEW_APPROVED=false
DQ_019_STATUS=BLOCKED_INPUT
DQ_020_STATUS=BLOCKED_INPUT
DQ_021_STATUS=BLOCKED_INPUT
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

本 attestation 不授权 PR、merge、main、release、deployment、Collector、listener、production
database、Agent、Runtime、Entity、Permission、canonical Evidence 或 SAEE output。
