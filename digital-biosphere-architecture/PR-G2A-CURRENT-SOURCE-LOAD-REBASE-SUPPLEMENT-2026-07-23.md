# PR-G2A Current-source Load Rebase Supplement

```text
supplement_id=TMAI-PR-G2A-CURRENT-SOURCE-LOAD-REBASE-SUPPLEMENT-20260723-009
decision_reference=DQ-018
review_gate=PR-G2A
dbos_remote_receipt_verified=true
current_source_full_ta_p001_to_ta_p005_rebase_complete=true
execution_mode=EMULATED_LINUX_AMD64_ON_ARM64_HOST
native_linux_x86_64_validated=false
pr_g2a_current_source_packet_refresh_required=true
pr_g2a_ready_for_human_review=false
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

DBOS current exact source `23c8f08…` 已在固定 `linux/amd64` 镜像、measurement contract
`0.1.1` 和 implementation manifest `43382e42…` 上完成 `TA-P001`—`TA-P005` 全套
load characterization（负载表征）重基线。五项 integrity/source binding 均为 `PASS`，
全部 authority effects 为 false。

这关闭了“current source 的 P001/P002/P004/P005 未重跑”缺口，但没有关闭原生 Linux
x86_64、Windows、production backend、容量 SLO、独立安全审查或 PR-G2A Human Approval。
因此 `PR_G2A_CURRENT_SOURCE_PACKET_REFRESH_REQUIRED=true` 和
`PR_G2A_READY_FOR_HUMAN_REVIEW=false` 均保持不变。

## Exact DBOS Remote Binding（DBOS 精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-os.git` |
| branch | `codex/telemetry-admission-foundation` |
| implementation source / tree | `23c8f0878058f29e733b6f164572ac157c6c7d1c` / `27703ed64d6e885a2933a5a39139a59bab83c3c1` |
| implementation manifest | 58 files / 726,068 bytes / `sha256:43382e42…bc8c` |
| receipt commit / tree | `3f5b848fa42a4e35770d5534f36f509f02eb7bf7` / `81321436a1619ee6fdad7edd16df11fc4c649fb5` |
| DBOS report Markdown | 6,239 bytes / `sha256:f48856a2…c793` |
| DBOS report JSON | 8,127 bytes / `sha256:49fe1b84…695a` |
| new raw directory bytes | 141,217 bytes；P001/P002/P004/P005 results + receipts + index |
| remote clean clone | `PASS`；75 local links；all report/raw digest bindings `PASS` |

## Current-source Load Results（当前源码负载结果）

| case | observed result | boundary |
|---|---|---|
| `TA-P001` | 10,000 ops；301.217s；p95 35.770ms；integrity/source `PASS` | serial reference |
| `TA-P002` | 10,000 confirmed retries；duplicate accuracy 1.0；lifecycle growth 0；integrity/source `PASS` | idempotency reference |
| `TA-P003` | 18,953 ops；errors `{}`；63.076 ops/s；p95 276.034ms；integrity/source `PASS` | observer-effect hardened emulation |
| `TA-P004` | 10/10 restore；writer errors `[]`；integrity/source `PASS` | restore reference |
| `TA-P005` | 13,532 ops；59/59 periodic + final `PASS`；errors `{}`；p95 70.085ms | one-hour integrity reference, not SLO |

`TA-P005` 原始结果没有 observed-rate 字段；DBOS 报告仅把
`13,532 / 3,600.194 = 3.758686 ops/s` 标记为派生描述值。该缺失没有被写成 0 或伪装成
原始字段。

## Agent Recommendation and Boundary（智能体建议与边界）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CURRENT_EXACT_SOURCE_OFFLINE_OBSERVER_EFFECT_HARDENED_EMULATED_AMD64_LOAD_CHARACTERIZATION
NOT_RECOMMENDED_AS=NATIVE_X86_64_CAPACITY_SLO_PRODUCTION_DURABILITY_OR_PRODUCTION_READINESS_EVIDENCE
REFERENCE_SUPPLEMENT_NE_APPROVAL=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
DQ_020_REMAINS_BLOCKED_INPUT=true
DQ_021_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

规范 SSH alias `hongyan-4cj` 仍在 key exchange 前被服务端关闭；未认证、未进入主机、未产生
远程写入。因此下一证据缺口是 native Linux x86_64，不是 Human Decision 或后继生产阶段。
