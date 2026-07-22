# PR-G2A Human Review Packet Remote Attestation

```text
attestation_id=TMAI-PR-G2A-PACKET-ATTESTATION-20260722-001
observed_at=2026-07-22T20:38:36+08:00
packet_attested_remote=true
pr_g2a_ready_for_human_decision=true
pr_g2a_approved=false
full_pr_g2_ready=false
production_ready=false
```

## Outcome（结果）

`PR-G2A` Human Review Packet（人工审查包）及其站点供应链加固记录已经从 GitHub 远端
分支执行 fresh clean clone（全新干净检出）并复验通过。该证明绑定一个已经存在的远端前驱
提交，不把证明文件本身放入被证明的哈希集合，因此没有 self-reference（自引用）循环。

本证明只说明“审查材料来自远端且可复验”。它不批准 `PR-G2A`，不关闭完整 `PR-G2`，也
不授权 PR、merge、main、release、deployment、Collector、listener、database、Agent、
Runtime、Entity、Permission、canonical Evidence 或 SAEE output。

## Exact Remote Binding（精确远端绑定）

| surface | exact binding |
|---|---|
| repository | `https://github.com/joy7758/digital-biosphere-architecture-specification.git` |
| branch | `codex/production-observability-baseline` |
| attested predecessor commit | `7eea3d0e49e0ef2ab15170a3b5dcf83fd67e5f35` |
| attested predecessor tree | `f21c0b5018da37439b2a76d6c68e579c427b0a19` |
| packet Markdown | 5533 bytes / `sha256:cb0cbdb544f38731dd40307114572828ce72b06f37917d43d6a34a4aa496a0ce` |
| packet JSON | 2913 bytes / `sha256:3979eccd2d20d246b42308ecdd9718083a959a29bff28f9451aa58fd5d63c2a9` |
| site package | `sha256:e78a322a1580090e4dab22458d4e1df9572d5ae66557793a4cd0d04efd0ae136` |
| site lock | `sha256:4f179b1107a3a3f18aa906ebd19f952a9a4d190b1ad7123cba0a6884e3a312fd` |

## Clean Clone Validation（干净检出验证）

```text
git_head_match=PASS
git_tree_match=PASS
git_status_clean_before_and_after=PASS
json_parse=64/64_PASS
markdown_files=163
local_links=856
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

## DBOS Evidence Binding（DBOS 证据绑定）

| surface | exact binding |
|---|---|
| DBOS source | `5c52c1c2f44767c0b13b4ac9670425721b9ea0dd` |
| DBOS receipt | `aa6440e83f35cc63483f487367ccb573bba7681a` |
| implementation manifest | 56 files / 714335 bytes / `sha256:fdda745c3907e35ac92769740f07afc81483be674568879a3c0314c2a09baa51` |
| reproducible wheel | `sha256:240828497ab265d3703f60ce5d71c2d49bc623c092ad607d8b2f8762ffc42e41` |
| validation | 531/531 tests; 197/197 telemetry tests; 35/35 validators; 68/68 authorized OTel cases |
| fail-closed boundary | 23 `DQ-020` cases blocked; no listener, Collector, SAEE call or authority effect |

## Decision Boundary（决策边界）

Agent recommendation（智能体建议）仍为：

```text
PR-G2A=APPROVE_DQ_018_OFFLINE_TELEMETRY_ADMISSION_REFERENCE_SLICE
```

该 token 只是审查包中的 recommended option（推荐选项）。当前没有记录 `selected_token` 或
`decided_by_ref`，因此：

```text
RECOMMENDATION_NE_DECISION=true
PACKET_ATTESTATION_NE_APPROVAL=true
PR_G2A_APPROVED=false
DQ_019_REMAINS_BLOCKED_INPUT=true
FULL_PR_G2_READY=false
PRODUCTION_READY=false
```
