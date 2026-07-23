# PR-G2A Native Linux x86_64 Validation Supplement

```text
supplement_id=TMAI-PR-G2A-NATIVE-LINUX-X86-64-VALIDATION-SUPPLEMENT-20260723-013
decision_reference=DQ-018
review_gate=PR-G2A
dbos_source_commit=23c8f0878058f29e733b6f164572ac157c6c7d1c
dbos_receipt_commit=ff1752cb3bb01ff67538bb04b3c7517fbcee3269
implementation_manifest=sha256:43382e4274c19ef6b10ee6e76f36ddddc18f05b7dfaedfdca43ddd8d3f2abc8c
native_linux_x86_64_direct_validation=PASS
dbos_receipt_remote_verified=true
dba_supplement_remote_attested=false
human_security_review_complete=false
pr_g2a_ready_for_human_review=false
pr_g2a_human_review_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

DBOS current source 已在 native Linux x86_64（原生 Linux x86_64）主机上使用架构锁定的
Python 3.12.13 immutable amd64 image、exact-hash dependency locks 和 `--network none` 完成
直接验证。DBOS receipt commit `ff1752c…` 已推送，并从 GitHub fresh clean clone 复验。

验证包括 534/534 全仓测试、200/200 telemetry tests、25/25 Telemetry validator、OTel
授权子集 32/32 + 36/36、TA-P001—TA-P005、rollback、可重复 wheel 和隔离安装。五个跨项目
validator 在隔离 checkout 中因外部绝对路径不可用而按设计 fail closed；准确结果是
`30 PASS + 5 EXPECTED_EXTERNAL_SOURCE_FAIL_CLOSED + 0 unexpected`。

本 supplement 关闭 native x86_64 direct-validation blocker，但 DBA supplement 自身尚未
remote attested，Human Security Review 也未完成，所以 PR-G2A 仍不是 review ready 或
approved。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| DBOS repository / branch | `joy7758/digital-biosphere-os` / `codex/telemetry-admission-foundation` |
| DBOS receipt commit / tree | `ff1752cb3bb01ff67538bb04b3c7517fbcee3269` / `2efc9dbb25e91d726771a7ae4ee4d532c4bf8d6e` |
| implementation source / tree | `23c8f0878058f29e733b6f164572ac157c6c7d1c` / `27703ed64d6e885a2933a5a39139a59bab83c3c1` |
| implementation manifest | 58 files / 726,068 bytes / `sha256:43382e42…abc8c` |
| DBOS report Markdown | 6,011 bytes / `sha256:c39c315b…f15b` |
| DBOS report JSON | 3,712 bytes / `sha256:e9f68c03…ab73` |
| raw inventory | 32 entries / 316,531 bytes / file `sha256:f434c833…b06a` |
| native summary | 2,888 bytes / `sha256:34b1024c…08b5` |

## Direct Results（直接结果）

| evidence | result | gate interpretation |
|---|---|---|
| exact-hash runtime/build locks | `PASS`; `pip check` clean | exact environment only |
| full/focused tests | `534/534` / `200/200 PASS` | synthetic/offline |
| validators | 30 pass + 5 expected external-source fail closed | unexpected `0`; no source fabrication |
| Telemetry validator | `25/25 PASS` | zero live authority effects |
| OTel authorized subsets | `32/32 + 36/36 PASS` | 23 deployment cases remain `BLOCKED` |
| TA-P001—TA-P005 | all integrity/source binding `PASS` | native x86_64 characterization, not SLO |
| TA-P003 | 19,200 operations / 0 errors | QEMU observer-effect error not reproduced |
| TA-P005 | 3,600 s / 16,787 operations / 59 checks / 0 errors | one-hour characterization, not SLO |
| rollback | 25 receipts / 0 mismatch / failed source retained | no automatic switch |
| wheel | byte-identical `sha256:03190078…155af9` | no publication/release |
| GitHub fresh clone | 190/190 JSON、32/32 inventory、5/5 receipts | DBOS receipt remote verified |

## Agent Recommendation（智能体建议）

```text
verdict=CONDITIONALLY_RECOMMENDED
recommended_as=CURRENT_SOURCE_OFFLINE_TELEMETRY_ADMISSION_REFERENCE_SLICE_WITH_NATIVE_X86_64_DIRECT_VALIDATION
next_recommended_gate=PUSH_DBA_SUPPLEMENT_AND_REMOTE_ATTESTATION_THEN_HUMAN_SECURITY_REVIEW
not_recommended_as=PR_G2A_APPROVED_FULL_PR_G2_PRODUCTION_SERVICE_SLO_HA_OR_DURABILITY_EVIDENCE
```

## Authority Boundary（权力边界）

```text
NATIVE_VALIDATION_NE_SLO=true
NATIVE_VALIDATION_NE_HUMAN_SECURITY_REVIEW=true
NATIVE_VALIDATION_NE_GATE_APPROVAL=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_HUMAN_REVIEW_APPROVED=false
DQ_019_STATUS=BLOCKED_INPUT
DQ_020_STATUS=BLOCKED_INPUT
DQ_021_STATUS=BLOCKED_INPUT
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

本 supplement 不授权 PR、merge、main、release、deployment、Collector、listener、production
database、Agent、DBOS Runtime、Entity、Permission、canonical Evidence 或 SAEE output。
