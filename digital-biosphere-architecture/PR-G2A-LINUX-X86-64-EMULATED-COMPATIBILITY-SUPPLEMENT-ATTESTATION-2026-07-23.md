# PR-G2A Linux x86_64 Emulated Compatibility Supplement Remote Attestation

```text
attestation_id=TMAI-PR-G2A-LINUX-X86-64-EMULATED-SUPPLEMENT-ATTESTATION-20260723-006
attested_predecessor_commit=ca694720481f91bdd36a109a11a480f0616a4029
remote_clean_clone_pass=true
supplement_remote_attested=true
compatibility_result=PARTIAL
native_linux_x86_64_validated=false
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

`PR-G2A` Linux x86_64 emulated compatibility supplement（模拟兼容补充）已从 GitHub
远端分支执行 fresh clean clone（全新干净检出）并复验通过。本证明只绑定 predecessor
commit `ca69472…` 及其 tree `37ac787…`，不把本证明放入被证明的哈希集合，因此没有
self-reference（自引用）循环。

被证明材料的结论仍为 `PARTIAL`：它确认 DBOS amd64 模拟兼容材料、失败记录和 DBA
治理表面可以从远端重现，但不证明 native Linux x86_64（原生 Linux x86_64）通过。
`TA-P003` 的 426 个 `TA_STORAGE_UNAVAILABLE` 仍被保留。

本证明不批准 `PR-G2A`，不关闭完整 `PR-G2`，也不授权 PR、merge、main、release、
deployment、Collector、listener、database、Agent、Runtime、Entity、Permission、canonical
Evidence 或 SAEE output。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-architecture-specification.git` |
| branch | `codex/production-observability-baseline` |
| attested predecessor commit | `ca694720481f91bdd36a109a11a480f0616a4029` |
| attested predecessor tree | `37ac78750aaa3c3d7815f49aab9420993e72715f` |
| supplement Markdown | 4,030 bytes / `sha256:132a0835…22a` |
| supplement JSON | 4,404 bytes / `sha256:3d39314f…898` |
| site package | `sha256:e78a322a…136` |
| site lock | `sha256:4f179b11…12fd` |

## Clean Clone Validation（干净检出验证）

```text
git_head_match=PASS
git_tree_match=PASS
git_status_clean_before_and_after=PASS
json_parse=70/70_PASS
markdown_files=169
local_links=865
missing_links=0
npm_ci=PASS
npm_audit=0_TOTAL
site_build=PASS
site_tests=11/11_PASS
site_lint=PASS
node=v26.0.0
npm=11.12.1
platform=Darwin-25.5.0-arm64
```

Audit 是 `observed_at` 时点的供应链观察，不是永久无漏洞承诺。未来构建仍须重新执行
clean install、audit、build、tests 与 lint。

## Agent Recommendation and Decision Boundary（智能体建议与决策边界）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=OFFLINE_EMULATED_AMD64_COMPATIBILITY_AND_FAILURE_DISCOVERY_MATERIAL
NOT_RECOMMENDED_AS=NATIVE_X86_64_OR_PRODUCTION_READINESS_EVIDENCE
SUPPLEMENT_ATTESTATION_NE_APPROVAL=true
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
DQ_020_REMAINS_BLOCKED_INPUT=true
DQ_021_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

当前仍没有记录 PR-G2A 的 `selected_token` 或新的 `decided_by_ref`。下一状态提升只能来自
独立人工审查后的显式 Decision。
