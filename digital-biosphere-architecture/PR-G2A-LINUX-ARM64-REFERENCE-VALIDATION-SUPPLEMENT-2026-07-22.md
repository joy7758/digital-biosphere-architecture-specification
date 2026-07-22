# PR-G2A Linux arm64 Reference Validation Supplement

```text
supplement_id=TMAI-PR-G2A-LINUX-ARM64-SUPPLEMENT-20260722-003
decision_reference=DQ-018
review_gate=PR-G2A
dbos_remote_receipt_verified=true
linux_arm64_reference_validation=PASS
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

DBOS DQ-018 Telemetry Admission reference slice（遥测准入参考切片）已新增一个精确绑定的
Linux arm64 验证环境。远端分支的 source commit、receipt commit、机器可读报告和 25 个公开
安全原始产物已通过 fresh clean clone（全新干净检出）复验。

本文件是现有 `PR-G2A` hardened human-review packet（加固人工审查包）的 reference-only
supplement（仅参考补充），不是新的 Decision、Authorization 或 Gate Approval。原审查包与
历史回执均保留，不被改写。

## Exact DBOS Remote Binding（DBOS 精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-os.git` |
| branch | `codex/telemetry-admission-foundation` |
| implementation source | `57c7b9e55dfcab84e81e7c5f61e9d8ea61045dbe` |
| implementation tree | `a044e54841f856df49e682f8a7a07d9b64a0db8b` |
| implementation manifest | 57 files / 720,322 bytes / `sha256:d0951d6c…9710` |
| receipt commit | `1c8f3d949f7b9686567b43bc8ebc316597ce9cfc` |
| receipt tree | `11ee76e503db9046c5bc28d58ec16c0e08ab32f1` |
| Markdown report | 6,330 bytes / `sha256:e9143932…85c6` |
| JSON report | 8,570 bytes / `sha256:bd352df7…e54c` |
| public-safe raw artifact files | 25 |

## Linux arm64 Results（Linux arm64 结果）

- exact CPython `3.12.13` / Linux glibc arm64 lock and image digest；
- full tests `533/533 PASS`，focused telemetry tests `199/199 PASS`；
- 35 validators：30 `PASS` + 5 external-source fail closed，0 unexpected failures；
- Ruff 0 findings / format `PASS`，Bandit 5,360 LOC / 0 findings，pip-audit 7 deps / 0 vulnerabilities；
- `TA-P001`—`TA-P005` integrity/source binding `PASS`；
- `TA-P005` 运行 `3600.033s`、17,410 operations、59/59 periodic integrity checks `PASS`，
  final integrity `PASS`，errors `{}`；
- Agent、Runtime、Entity、Capability、Permission、Execution、canonical Evidence、Verification、
  Collector、listener、SAEE call 和 gate change 均为 0/false。

这些数字是 `CHARACTERIZATION_NOT_SLO`。Linux arm64 reference pass 只局部缓解 `R-042`；
Linux x86_64、Windows、真实 production backend、人类安全审查和 Human rollback switch 仍未
完成。

## Human Decision Boundary（人工决策边界）

```text
RECOMMENDATION_NE_DECISION=true
REFERENCE_VALIDATION_NE_APPROVAL=true
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
DQ_020_REMAINS_BLOCKED_INPUT=true
DQ_021_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

下一状态提升仍只能由独立人工审查后记录 exact `PR-G2A` decision token 与
`decided_by_ref`。本 supplement 不提供或推断该 token。
