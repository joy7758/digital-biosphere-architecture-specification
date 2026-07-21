---
report_id: DBA-FORMAL-RELEASE-READINESS-AUDIT-2026-07-21
title: Trusted Multi-Agent Infrastructure Formal Release Readiness Audit
title_zh: 可信多智能体基础设施正式发布就绪审计
status: owner-decisions-recorded-technical-and-trial-evidence-blocked
observed_at: 2026-07-21T19:28:00+08:00
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
| GitHub website artifact | `v0.1-public-website-candidate`; prerelease | `PASS_CANDIDATE_ONLY` |
| DBA clean clone | `CLEAN-CLONE-VALIDATION-REPORT.md` | `PASS` |
| DBOS clean clone | 331 tests, 34 validators, two demos | `PASS_PRIVATE_ACCESS` |
| SAEE public clean clone | public smoke/demo | `PASS_ADAPTER_MISSING` |
| SAEE ↔ DBOS public adapter | public `main` lacks required adapter | `FAIL` |
| SAEE adapter extraction preflight | `SAEE-PUBLIC-SAFE-EXTRACTION-REVIEW.md`; isolated 8/8 tests, exact 19-file closure and `ADR-020` authorization | `PASS_AUTHORIZED_IMPLEMENTATION_PENDING` |
| Cross-project clean clone | `CROSS_PROJECT_CLEAN_CLONE_PASS=false` | `FAIL` |
| Public license decision | `ADR-020`; `Apache-2.0` selected for Owner-created public surfaces | `PASS_DECISION_IMPLEMENTATION_IN_PROGRESS` |
| DBOS anonymous access | GitHub visibility is `PRIVATE` | `FAIL` |
| DBOS trial access decision | `DBOS-PUBLIC-VISIBILITY-PREFLIGHT.md`; `PRIVATE_COLLABORATOR_TRIAL` selected; repository remains private | `PASS_DECISION_NO_COLLABORATORS_ADDED` |
| External developer trial | 0 participants; `DQ-010=AUTHORIZE_AFTER_CLEAN_CLONE_PASS`; real `participant_source` missing | `CONDITIONALLY_AUTHORIZED_NOT_EFFECTIVE` |
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

1. Adopt `Apache-2.0` in DBA, DBOS and SAEE while preserving third-party licenses.
2. Implement and verify only the authorized 19-file SAEE public-safe extraction.
3. Keep DBOS private and freeze the exact collaborator-trial source commit.
4. Rerun full clean-clone
   validation.
5. Freeze `trial_package_id`, privacy notice and stop rules; replace the
   `participant_source` placeholder with 3–5 real external Agent Developers or
   an explicit recruitment channel, then make the conditional `DQ-010` effective.
6. `DQ-009`: record an explicit Human Release Decision with `released_by_ref`.

No local test, website deployment, prerelease tag, or synthetic demo can replace
these decisions and external-trial evidence.
