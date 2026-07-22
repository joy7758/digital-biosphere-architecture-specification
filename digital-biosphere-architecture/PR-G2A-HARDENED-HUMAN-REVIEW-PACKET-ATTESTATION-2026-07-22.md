# PR-G2A Hardened Human Review Packet Remote Attestation

```text
attestation_id=TMAI-PR-G2A-HARDENED-PACKET-ATTESTATION-20260722-002
observed_at=2026-07-22T23:28:26+08:00
hardened_packet_attested_remote=true
pr_g2a_ready_for_human_decision=true
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

`PR-G2A` hardened successor packet（加固后继审查包）已经从 GitHub 远端分支执行 fresh clean
clone（全新干净检出）并复验通过。本证明只绑定已存在的 predecessor packet commit，不把本证明
文件放进被证明的哈希集合，因此没有 self-reference（自引用）循环。

本证明只说明“加固审查材料来自远端且可复验”。它不批准 `PR-G2A`，不关闭完整 `PR-G2`，也
不授权 PR、merge、main、release、deployment、Collector、listener、database、Agent、Runtime、
Entity、Permission、canonical Evidence 或 SAEE output。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-architecture-specification.git` |
| branch | `codex/production-observability-baseline` |
| attested predecessor commit | `07e9c49a5042b06ca8a3e5c5ebe80727af7f9f90` |
| attested predecessor tree | `06af08eba4a181c76833dd87a15c1a4c81330d11` |
| hardened packet Markdown | 5,893 bytes / `sha256:7a623ce5adf1273965e2ca5733123fca1cd788a048a40d0232c39d7707013e7b` |
| hardened packet JSON | 3,767 bytes / `sha256:003ac58beafd0ed97b678a6894716ec896b7f69d36d46a9ec6de3a8c36cc8986` |
| site package | `sha256:e78a322a1580090e4dab22458d4e1df9572d5ae66557793a4cd0d04efd0ae136` |
| site lock | `sha256:4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd` |

## Clean Clone Validation（干净检出验证）

```text
git_head_match=PASS
git_tree_match=PASS
git_status_clean_before_and_after=PASS
json_parse=66/66_PASS
markdown_files=165
local_links=862
missing_links=0
npm_ci=PASS
npm_audit=0_TOTAL
site_build=PASS
site_tests=11/11_PASS
site_lint=PASS
node=v26.0.0
npm=11.12.1
platform=Darwin-arm64
```

Audit 结果是 `observed_at` 时点的供应链观察，不是永久无漏洞承诺。未来每次构建仍必须重新
执行 clean install、audit、build、tests 和 lint。

## DBOS Hardened Evidence Binding（DBOS 加固证据绑定）

| surface | exact binding |
|---|---|
| DBOS exact source | `3a63161d3e04d785b4b04feadd4a0712bf6314fc` |
| DBOS hardening receipt | `bf1b3b6ebf2c905f94c8f4ddaf447964a07dd183` |
| implementation manifest | 56 files / 716,453 bytes / `sha256:b6c03faf50bfab4ce25edaeb39b7ae36d2525df32519f82a8108c164162bd9fc` |
| reproducible wheel | `sha256:0319007826990d53addee8392be257d68966565c2242cde71e66b01ade155af9` / not published |
| validation | 532/532 tests; 198/198 telemetry tests; 35/35 validators; 68/68 authorized OTel cases |
| characterization | TA-P001—P005 PASS; one-hour 59 periodic checks + final PASS; all authority effects false |
| fail-closed boundary | 23 `DQ-020` cases blocked; no listener, Collector, SAEE call or authority effect |

## Decision Boundary（决策边界）

Agent recommendation（智能体建议）仍为：

```text
PR-G2A=APPROVE_DQ_018_OFFLINE_TELEMETRY_ADMISSION_REFERENCE_SLICE
```

该 token 只是 hardened packet 中的 recommended option（推荐选项）。当前没有记录
`selected_token` 或 `decided_by_ref`，因此：

```text
RECOMMENDATION_NE_DECISION=true
PACKET_ATTESTATION_NE_APPROVAL=true
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```
