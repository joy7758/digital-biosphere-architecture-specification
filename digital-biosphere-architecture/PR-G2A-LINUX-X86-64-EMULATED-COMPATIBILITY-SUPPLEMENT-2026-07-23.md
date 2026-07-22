# PR-G2A Linux x86_64 Emulated Compatibility Supplement

```text
supplement_id=TMAI-PR-G2A-LINUX-X86-64-EMULATED-SUPPLEMENT-20260723-005
decision_reference=DQ-018
review_gate=PR-G2A
dbos_remote_receipt_verified=true
execution_mode=EMULATED_LINUX_AMD64_ON_ARM64_HOST
compatibility_result=PARTIAL
native_linux_x86_64_validated=false
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

DBOS DQ-018 Telemetry Admission reference slice（遥测准入参考切片）已新增一个精确绑定的
Linux amd64 emulated compatibility（模拟兼容）回执。DBOS 远端分支的 implementation
source、receipt commit、机器可读报告和 25 个公开安全原始产物已通过 fresh clean clone
（全新干净检出）复验。

该结果是 `PARTIAL`：534/534 tests、200/200 telemetry tests、失败关闭 validators、静态安全、
恢复和一小时完整性均通过，但 `TA-P003` 在 QEMU 模拟环境记录 426 个
`TA_STORAGE_UNAVAILABLE`。它可能受模拟开销影响，在真实 x86_64 原生主机重跑前不得归因
结案，也不得写成原生平台通过。

本文件是现有 `PR-G2A` hardened human-review packet（加固人工审查包）的 reference-only
supplement（仅参考补充），不是 Decision、Authorization 或 Gate Approval。原审查包、Linux
arm64 原生补充与历史回执均保留。

## Exact DBOS Remote Binding（DBOS 精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-os.git` |
| branch | `codex/telemetry-admission-foundation` |
| implementation source | `d62b411845b18af3ec79af67622666e96d1baed3` |
| implementation tree | `109b2a9dcad86d1ff882ac472394a140f0dc5169` |
| implementation manifest | 58 files / 723,949 bytes / `sha256:6d1bcbbf…d6e4` |
| receipt commit | `8c6ddd7b5c790214cea9a42a34ed9f4df44fda2b` |
| receipt tree | `cfc1919bec82ea65159cf8997b0e96aff4c3c0be` |
| Markdown report | 7,646 bytes / `sha256:ee645cec…d118` |
| JSON report | 9,075 bytes / `sha256:5f987f11…cc9c` |
| public-safe raw artifact files | 25 |

## Validation Results（验证结果）

- exact CPython `3.12.13` / Linux glibc x86_64 lock and amd64 image digest；
- full tests `534/534 PASS`，focused telemetry tests `200/200 PASS`；
- 35 validators：30 `PASS` + 5 external-source fail closed，0 unexpected failures；
- Ruff 0 findings / format `PASS`，Bandit 5,363 LOC / 0 findings，pip-audit 7 deps /
  0 vulnerabilities；
- `TA-P001`、`TA-P002`、`TA-P004`、`TA-P005` integrity/source binding `PASS`；
- `TA-P003` integrity/source binding `PASS`，但 426 个 `TA_STORAGE_UNAVAILABLE`，overall
  characterization `PARTIAL`；
- `TA-P005` 运行 `3600.144s`、13,171 operations、59/59 periodic integrity checks `PASS`，
  final integrity `PASS`，errors `{}`；
- Agent、Runtime、Entity、Capability、Permission、Execution、canonical Evidence、Verification、
  Collector、listener、SAEE call 和 gate change 均为 0/false。

以上为 `EMULATED_CHARACTERIZATION_NOT_NATIVE_NOT_SLO`。它为 `R-042` 增加兼容材料但不缓解
原生 Linux x86_64 缺口；Windows、真实 production backend、人类安全审查和 Human rollback
switch 仍未完成。

## Agent Recommendation Gate（智能体推荐闸门）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=OFFLINE_EMULATED_AMD64_COMPATIBILITY_AND_FAILURE_DISCOVERY_MATERIAL
NOT_RECOMMENDED_AS=NATIVE_X86_64_OR_PRODUCTION_READINESS_EVIDENCE
```

## Human Decision Boundary（人工决策边界）

```text
RECOMMENDATION_NE_DECISION=true
EMULATED_COMPATIBILITY_NE_NATIVE_VALIDATION=true
REFERENCE_SUPPLEMENT_NE_APPROVAL=true
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
DQ_020_REMAINS_BLOCKED_INPUT=true
DQ_021_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

下一状态提升仍只能由独立人工审查后记录 exact `PR-G2A` decision token 与
`decided_by_ref`。本 supplement 不提供或推断该 token。
