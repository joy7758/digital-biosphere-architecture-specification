# PR-G2A Current-source Load Rebase Supplement Remote Attestation

```text
attestation_id=TMAI-PR-G2A-CURRENT-SOURCE-LOAD-REBASE-SUPPLEMENT-ATTESTATION-20260723-010
attested_predecessor_commit=c57983b9135bf2ee3c90cf29b9d1a1759dcc20fb
attested_predecessor_tree=32c3e0e0f45d481e21a735233c3074ea4fe53286
remote_clean_clone_pass=true
supplement_remote_attested=true
current_source_full_ta_p001_to_ta_p005_rebase_complete=true
native_linux_x86_64_validated=false
pr_g2a_ready_for_human_review=false
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

`PR-G2A` current-source load rebase supplement 已从 GitHub 远端分支执行 fresh clean clone
（全新干净检出）并复验通过。本证明只绑定 predecessor commit `c57983b…` 及其 tree
`32c3e0e…`，不把本证明放入被证明的哈希集合，因此没有 self-reference（自引用）循环。

被证明材料确认 current DBOS source 的 P001—P005 模拟重基线可从远端追溯，五项
integrity/source binding 全部 `PASS`，authority effects 全部 false。原生 Linux x86_64
仍未验证，current-source independent review packet 仍未形成，所以本证明不把 `PR-G2A`
升级为 review-ready 或 approved。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-architecture-specification.git` |
| branch | `codex/production-observability-baseline` |
| attested predecessor commit | `c57983b9135bf2ee3c90cf29b9d1a1759dcc20fb` |
| attested predecessor tree | `32c3e0e0f45d481e21a735233c3074ea4fe53286` |
| supplement Markdown | 3,751 bytes / `sha256:aa5fdbb8…9712` |
| supplement JSON | 4,066 bytes / `sha256:fe1b4889…d53f` |
| site package | `sha256:e78a322a…136` |
| site lock | `sha256:4f179b11…12fd` |

## Clean Clone Validation（干净检出验证）

```text
git_head_match=PASS
git_tree_match=PASS
git_status_clean_before_and_after=PASS
tracked_json_parse=74/74_PASS
markdown_files=173
local_links=860
missing_links=0
npm_ci=PASS
npm_audit=0_TOTAL
site_build=PASS
site_tests=11/11_PASS
site_lint=PASS
```

## Authority Boundary（权力边界）

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=CURRENT_EXACT_SOURCE_OFFLINE_OBSERVER_EFFECT_HARDENED_EMULATED_AMD64_LOAD_CHARACTERIZATION
NOT_RECOMMENDED_AS=NATIVE_X86_64_CAPACITY_SLO_PRODUCTION_DURABILITY_OR_PRODUCTION_READINESS_EVIDENCE
SUPPLEMENT_ATTESTATION_NE_APPROVAL=true
PR_G2A_READY_FOR_HUMAN_REVIEW=false
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
DQ_020_REMAINS_BLOCKED_INPUT=true
DQ_021_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```

本证明不授权 PR、merge、main、release、deployment、Collector、listener、database、Agent、
Runtime、Entity、Permission、canonical Evidence 或 SAEE output。下一状态仍是原生 Linux
x86_64 直接验证，不是 Human Decision。
