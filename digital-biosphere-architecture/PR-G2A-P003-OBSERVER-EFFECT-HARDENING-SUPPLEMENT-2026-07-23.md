# PR-G2A P003 Observer-effect Hardening Supplement

```text
supplement_id=TMAI-PR-G2A-P003-OBSERVER-EFFECT-SUPPLEMENT-20260723-007
decision_reference=DQ-018
review_gate=PR-G2A
dbos_remote_receipt_verified=true
p003_result=PASS_EMULATED_AMD64_OBSERVER_EFFECT_HARDENED
current_source_full_ta_p001_to_ta_p005_rebase_complete=false
pr_g2a_current_source_packet_refresh_required=true
pr_g2a_ready_for_human_review=false
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

DBOS current source `23c8f08…` 已修正 `TA-P003` 并发 load characterization（负载表征）
中 global `tracemalloc` 对 QEMU amd64 的 observer effect（观察者效应）。同一固定镜像、
Linux tmpfs、32 workers、300 秒、target 64 ops/s 的 successor run 完成 18,953 次成功、
0 errors、63.076 observed ops/s、p95 276.034ms，integrity/source binding 均为 `PASS`。

诊断 A/B 在相同镜像和 tmpfs 中显示：关闭 `tracemalloc` 时 1,853/1,853 成功、0 errors；
开启时只有 734 次成功并出现 38 个 `TA_STORAGE_UNAVAILABLE`，底层异常为
`sqlite3.OperationalError: database is locked`，发生在 `BEGIN IMMEDIATE`。修复没有扩大 SQLite
busy timeout、自动重试失败写入或隐藏错误，只移除了会干扰并发测量的全局 allocation tracing，
并继续记录 process max RSS。

predecessor `d62b411…` 的 426 个错误和完整五项模拟结果继续保留，不被改写。但当前源码只重跑
了 P003；P001、P002、P004 和一小时 P005 仍绑定 predecessor manifest。因此，本补充触发的是
`PR_G2A_CURRENT_SOURCE_PACKET_REFRESH_REQUIRED=true`，不是 gate 升级。

## Exact DBOS Remote Binding（DBOS 精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-os.git` |
| branch | `codex/telemetry-admission-foundation` |
| implementation source | `23c8f0878058f29e733b6f164572ac157c6c7d1c` |
| implementation tree | `27703ed64d6e885a2933a5a39139a59bab83c3c1` |
| implementation manifest | 58 files / 726,068 bytes / `sha256:43382e42…bc8c` |
| receipt commit | `759b69c900368fdf15e319b4503d83fb15374f67` |
| receipt tree | `149138f26b208f65571cde91c5f0919e9e999dea` |
| DBOS report Markdown | 7,123 bytes / `sha256:a73225c5…6e6b` |
| DBOS report JSON | 6,954 bytes / `sha256:229a03e4…90a` |
| raw P003 tmpfs result | 29,092 bytes / `sha256:da031f64…9142` |
| remote clean clone | `PASS` |

## Validation and Security（验证与安全）

- full tests `534/534 PASS`，focused telemetry tests `200/200 PASS`；
- 35 validators：30 `PASS` + 5 external-source fail closed，0 unexpected；
- telemetry admission validator `25/25 PASS`；
- Ruff 0 findings，Bandit `1.9.4` / 4,650 LOC / 0 findings / 0 `nosec`；
- pip-audit `2.10.1` / 7 locked runtime dependencies / 0 known vulnerabilities；
- runtime dependencies 使用 exact Linux x86_64 hash lock 与离线 wheelhouse；
- audit tools 的完整 transitive hash lock 尚未形成，作为供应链剩余缺口保留；
- Agent、Runtime、Entity、Capability、Permission、Execution、canonical Evidence、Verification、
  Collector、listener、SAEE output 和 gate approval 均为 0/false。

## Agent Recommendation Gate（智能体推荐闸门）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=OBSERVER_EFFECT_HARDENED_OFFLINE_EMULATED_CONCURRENCY_CHARACTERIZATION
NOT_RECOMMENDED_AS=NATIVE_X86_64_CAPACITY_SLO_OR_PRODUCTION_READINESS_EVIDENCE
```

## Human Decision Boundary（人工决策边界）

```text
P003_PASS_NE_FULL_WORKLOAD_REBASE=true
REFERENCE_SUPPLEMENT_NE_APPROVAL=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
DQ_020_REMAINS_BLOCKED_INPUT=true
DQ_021_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

下一步必须先在 current source 上重跑 P001/P002/P004/P005，并补充原生 Linux x86_64 直接证据，
再生成新的完整 PR-G2A packet。此 supplement 不提供或推断 Human Decision token。
