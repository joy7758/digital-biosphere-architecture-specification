---
report_id: DBA-FORMAL-RELEASE-READINESS-AUDIT-2026-07-21
title: Trusted Multi-Agent Infrastructure Formal Release Readiness Audit
title_zh: 可信多智能体基础设施正式发布就绪审计
status: clean-clone-pass-external-trial-and-release-decision-blocked
observed_at: 2026-07-21T23:17:11+08:00
formal_release_ready: false
developer_preview_released: false
---

# Formal Release Readiness Audit（正式发布就绪审计）

## Outcome

The public website and its GitHub website artifact are published as an explicit
candidate. The full Trusted Multi-Agent Infrastructure Developer Preview v0.1
is not ready for formal release.

## Requirement audit

| Requirement | Authoritative evidence | Result |
|---|---|---|
| DBA public source | `origin/main`; public GitHub repository | `PASS` |
| Bilingual public website | `https://redcrag.cn/`, `/en/` | `PASS` |
| Agent-readable website | `/llms.txt`, `/agent-index.json`, `/status.json` | `PASS` |
| Website artifact integrity | `/release-manifest.json`; remote `sha256sum -c` | `PASS` |
| HTTPS and security headers | Public response and origin checks | `PASS` |
| Website rollback | Atomic switch to previous artifact and restore | `PASS` |
| GitHub website artifact | `v0.1-public-website-candidate.2`; `bc7ba49`; prerelease | `PASS_CANDIDATE_ONLY` |
| DBA clean clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `PASS` |
| DBOS clean clone | 331 tests, 34 validators, two demos | `PASS_PRIVATE_ACCESS` |
| SAEE public clean clone | public smoke/demo、8/8 Adapter tests | `PASS` |
| SAEE ↔ DBOS public adapter | public `main@2173c25`；read-only pipeline | `PASS_ADVISORY_ONLY` |
| SAEE adapter extraction | `SAEE-PUBLIC-SAFE-EXTRACTION-REVIEW.md`；exact 19/19 blobs | `PASS_IMPLEMENTED_PUBLIC_SAFE_PROJECTION` |
| Cross-project clean clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `PASS` |
| Public license | 三仓库根 `LICENSE`；与 Apache 官方 `LICENSE-2.0.txt` 一致 | `PASS_OWNER_CREATED_SURFACES` |
| Website dependency audit | `npm audit`：12 total；production tree 2 moderate；服务器只部署静态 `out/` | `REVIEW_REQUIRED_BEFORE_FORMAL_RELEASE` |
| DBOS anonymous access | GitHub visibility is `PRIVATE` | `FAIL` |
| DBOS trial access decision | `PRIVATE_COLLABORATOR_TRIAL` selected；repository remains private | `PASS_FOR_TRIAL_NO_COLLABORATORS_ADDED` |
| Trial package | `TMAI-DP-v0.1-TRIAL-20260721-001` | `TECHNICAL_FREEZE_PASS_DISTRIBUTION_BLOCKED` |
| External developer trial | 0 participants；real `participant_source` missing | `CONDITIONALLY_AUTHORIZED_NOT_EFFECTIVE` |
| Human Developer Preview release decision | DQ-009 `BLOCKED_INPUT` | `MISSING` |

## Release classification

```text
PUBLIC_WEBSITE_DEPLOYED=true
GITHUB_WEBSITE_PRERELEASE_PUBLISHED=true
WEBSITE_CANDIDATE_PUBLISHED=true
TRUSTED_MULTI_AGENT_INFRASTRUCTURE_DEVELOPER_PREVIEW_RELEASED=false
FORMAL_RELEASE_READY=false
```

## Remaining implementation and external evidence

1. Replace the `participant_source` placeholder with 3–5 real external Agent
   Developers or an explicit recruitment channel.
2. Make the conditional `DQ-010` effective, grant per-participant minimum DBOS
   collaborator access, and execute the frozen trial without changing metrics.
3. Produce an External Developer Trial Result Report retaining failures,
   intervention levels and comprehension scoring.
4. Decide the post-trial DBOS distribution model; private trial access is not
   anonymous Developer Preview availability.
5. Resolve or explicitly review `R-015` against a non-breaking upstream dependency
   update; do not use `npm audit fix --force` as an unreviewed release action.
6. `DQ-009`: record an explicit Human Release Decision with `released_by_ref`.

No local test, website deployment, prerelease tag, or synthetic demo can replace
these decisions and external-trial evidence.
