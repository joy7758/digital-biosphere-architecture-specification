---
report_id: DBA-FORMAL-RELEASE-READINESS-AUDIT-2026-07-21
title: Trusted Multi-Agent Infrastructure Formal Release Readiness Audit
title_zh: 可信多智能体基础设施正式发布就绪审计
status: clean-clone-pass-agent-validation-conditional-remediation-and-release-decision-blocked
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
| Agent customer package | `/agent-customer-package.json` | `LOCAL_REMEDIATION_CANDIDATE_PENDING_DEPLOYMENT` |
| Agent customer validation baseline | `TMAI-ACV-20260721-001`；12/12 sessions；2 providers；4 models | `CONDITIONAL_REMEDIATION_REQUIRED` |
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
| Human developer trial | 0 participants；`ADR-021` retains it as an optional secondary study | `SUPERSEDED_AS_PRIMARY_GATE_NOT_EXECUTED` |
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

1. Deploy the remediated agent-readable machine surfaces and rerun under the same
   thresholds with a new validation ID; retain the `CONDITIONAL` baseline.
2. Review the exact-command, canonical-composition, positive-fit, and simple-task
   negative-control results after rerun.
3. Make an explicit Human Owner decision on DBOS agent access or distribution;
   private access is not autonomous AI-agent usability.
4. Assess `OPEN_WEB_DISCOVERY` separately; URL-given comprehension is not natural discovery.
5. Resolve or explicitly review `R-015` against a non-breaking upstream dependency
   update; do not use `npm audit fix --force` as an unreviewed release action.
6. `DQ-009`: record an explicit Human Release Decision with `released_by_ref`.

No local test, model recommendation, website deployment, prerelease tag, or
synthetic demo can replace these decisions or Human Release Authorization.
