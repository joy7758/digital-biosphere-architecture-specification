---
report_id: DBA-FORMAL-RELEASE-READINESS-AUDIT-2026-07-21
title: Trusted Multi-Agent Infrastructure Formal Release Readiness Audit
title_zh: 可信多智能体基础设施正式发布就绪审计
status: formal-release-ready-authorized-execution-in-progress
observed_at: 2026-07-22T01:54:00+08:00
formal_release_ready: true
developer_preview_released: false
---

# Formal Release Readiness Audit（正式发布就绪审计）

## Outcome

All formal release prerequisites and explicit Human decisions are satisfied.
`ADR-022` authorizes the exact GitHub and Baidu Cloud release transaction. This
readiness audit remains distinct from the post-release external verification.

## Requirement audit

| Requirement | Authoritative evidence | Result |
|---|---|---|
| DBA public source | `origin/main`; public GitHub repository | `PASS` |
| Bilingual public website | `https://redcrag.cn/`, `/en/` | `PASS` |
| Agent-readable website | `/llms.txt`, `/agent-index.json`, `/status.json` | `PASS` |
| Agent customer package | `/agent-customer-package.json` | `PUBLIC_CANDIDATE_DEPLOYED_PASS_NOT_RUNTIME` |
| Agent customer validation baseline | `TMAI-ACV-20260721-001`；12/12 sessions；2 providers；4 models | `CONDITIONAL_REMEDIATION_REQUIRED` |
| Agent customer validation rerun | `TMAI-ACV-20260722-002`；same thresholds；12/12 sessions；0 failed thresholds | `PASS_NOT_RELEASE_AUTHORIZATION` |
| Open-web discovery observation | `TMAI-OWD-20260722-001`；GitHub full-description match；canonical English／Chinese and public-web queries still no match | `PARTIAL_METADATA_ONLY_CANONICAL_RECHECK_REQUIRED` |
| Website artifact integrity | `/release-manifest.json`; remote `sha256sum -c` | `PASS` |
| HTTPS and security headers | Public response and origin checks | `PASS` |
| Website rollback | Atomic switch to previous artifact and restore | `PASS` |
| GitHub website artifact | `v0.1-public-website-candidate.7`; `1c4bf032`; anonymous download hash PASS；prerelease | `PASS_CANDIDATE_ONLY` |
| DBA clean clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `PASS` |
| DBOS clean clone | `main@cd3f867`；334 tests、34 validators、two demos | `PASS_PRIVATE_ACCESS` |
| DBOS public-safe wheel | `TMAI-DBOS-WHEEL-CANDIDATE-20260722-001`；0 path／Gitleaks findings；clean install and validation PASS | `PASS_VALIDATED_NOT_PUBLISHED` |
| SAEE public clean clone | public smoke/demo、8/8 Adapter tests | `PASS` |
| SAEE ↔ DBOS public adapter | public `main@2173c25`；read-only pipeline | `PASS_ADVISORY_ONLY` |
| SAEE adapter extraction | `SAEE-PUBLIC-SAFE-EXTRACTION-REVIEW.md`；exact 19/19 blobs | `PASS_IMPLEMENTED_PUBLIC_SAFE_PROJECTION` |
| Cross-project clean clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `PASS` |
| Public license | 三仓库根 `LICENSE`；与 Apache 官方 `LICENSE-2.0.txt` 一致 | `PASS_OWNER_CREATED_SURFACES` |
| Website dependency audit | `TMAI-WEB-DEPENDENCY-REVIEW-20260722-001`：0 critical、0 high、2 moderate；5/5 tests、lint、静态导出通过；服务器只部署静态 `out/` | `PASS_WITH_BOUNDED_RESIDUAL_DISCLOSED` |
| DBOS anonymous access | exact public-safe wheel URL fixed by `ADR-022`；whole repository remains `PRIVATE` | `AUTHORIZED_EXTERNAL_VERIFICATION_REQUIRED` |
| DBOS trial access decision | `PRIVATE_COLLABORATOR_TRIAL` selected；repository remains private | `PASS_FOR_TRIAL_NO_COLLABORATORS_ADDED` |
| Trial package | `TMAI-DP-v0.1-TRIAL-20260721-001` | `TECHNICAL_FREEZE_PASS_DISTRIBUTION_BLOCKED` |
| Human developer trial | 0 participants；`ADR-021` retains it as an optional secondary study | `SUPERSEDED_AS_PRIMARY_GATE_NOT_EXECUTED` |
| Human Developer Preview release decision | `ADR-022`；`released_by_ref=zhangbin` | `PASS_AUTHORIZED` |

## Release classification

```text
PUBLIC_WEBSITE_DEPLOYED=true
GITHUB_WEBSITE_PRERELEASE_PUBLISHED=true
WEBSITE_CANDIDATE_PUBLISHED=true
TRUSTED_MULTI_AGENT_INFRASTRUCTURE_DEVELOPER_PREVIEW_RELEASED=false
FORMAL_RELEASE_READY=true
RELEASE_AUTHORIZED=true
RELEASE_DECISION_REF=architecture/ADR-022-developer-preview-release.md
```

## Remaining implementation and external evidence

1. Publish the exact wheel and verify anonymous SHA-256, byte size and clean installation.
2. Publish `v0.1-developer-preview` as a non-draft, non-prerelease GitHub Release.
3. Deploy the formal static artifact to Baidu Cloud and verify manifest, Nginx,
   public routes, security headers and rollback preservation.
4. Reconfirm DBOS repository visibility remains `PRIVATE`.
5. Record the post-release evidence without upgrading `PARTIAL_METADATA_ONLY`,
   `R-015`, customer adoption or production-readiness claims.

No local test, model recommendation, website deployment, prerelease tag, or
synthetic demo replaces the external execution evidence still required after authorization.
