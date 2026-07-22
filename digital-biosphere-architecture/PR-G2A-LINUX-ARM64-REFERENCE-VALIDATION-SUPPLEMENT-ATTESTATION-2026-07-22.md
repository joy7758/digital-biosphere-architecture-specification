# PR-G2A Linux arm64 Reference Validation Supplement Remote Attestation

```text
attestation_id=TMAI-PR-G2A-LINUX-ARM64-SUPPLEMENT-ATTESTATION-20260722-004
attested_predecessor_commit=90b3966a5603b6db3c04e581af4a3063822c3250
remote_clean_clone_pass=true
supplement_remote_attested=true
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

`PR-G2A` Linux arm64 reference validation supplement（参考验证补充）已从 GitHub 远端分支
执行 fresh clean clone（全新干净检出）并复验通过。本证明绑定 predecessor commit
`90b3966…`，不把本证明文件放进被证明的哈希集合，因此没有 self-reference（自引用）循环。

本证明只说明 supplement 与驾驶舱状态来自远端、链接完整、站点仍可构建。它不批准
`PR-G2A`，不关闭完整 `PR-G2`，也不授权 PR、merge、main、release、deployment、Collector、
listener、database、Agent、Runtime、Entity、Permission、canonical Evidence 或 SAEE output。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-architecture-specification.git` |
| branch | `codex/production-observability-baseline` |
| attested predecessor commit | `90b3966a5603b6db3c04e581af4a3063822c3250` |
| attested predecessor tree | `ae66a97da8f4172f375241370c404319cdecc5be` |
| supplement Markdown | 3,047 bytes / `sha256:3dfc5bb2…b6ad` |
| supplement JSON | 3,904 bytes / `sha256:6560b33b…a6d` |
| site package | `sha256:e78a322a…136` |
| site lock | `sha256:4f179b11…12fd` |

## Clean Clone Validation（干净检出验证）

```text
git_head_match=PASS
git_tree_match=PASS
git_status_clean_before_and_after=PASS
json_parse=68/68_PASS
markdown_files=169
local_links=869
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

## Decision Boundary（决策边界）

```text
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
