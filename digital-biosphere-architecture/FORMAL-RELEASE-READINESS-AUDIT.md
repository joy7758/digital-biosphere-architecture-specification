---
report_id: DBA-FORMAL-RELEASE-READINESS-AUDIT-2026-07-21
title: Trusted Multi-Agent Infrastructure Formal Release Readiness Audit
title_zh: 可信多智能体基础设施正式发布就绪审计
status: website-candidate-published-formal-release-blocked
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
| Cross-project clean clone | `CROSS_PROJECT_CLEAN_CLONE_PASS=false` | `FAIL` |
| Public license | no root `LICENSE` in DBA, DBOS, or SAEE | `MISSING_DECISION` |
| DBOS anonymous access | GitHub visibility is `PRIVATE` | `FAIL` |
| External developer trial | 0 participants; DQ-010 not authorized | `NOT_STARTED` |
| Human Developer Preview release decision | DQ-009 `BLOCKED_INPUT` | `MISSING` |

## Release classification

```text
PUBLIC_WEBSITE_DEPLOYED=true
GITHUB_WEBSITE_PRERELEASE_PUBLISHED=true
WEBSITE_CANDIDATE_PUBLISHED=true
TRUSTED_MULTI_AGENT_INFRASTRUCTURE_DEVELOPER_PREVIEW_RELEASED=false
FORMAL_RELEASE_READY=false
```

## Required decisions and external evidence

1. `DQ-011`: approve or reject `A_PUBLIC_SAFE_EXTRACTION` for the SAEE adapter.
2. `DQ-012`: select `Apache-2.0`, another license, or withhold a license.
3. `DQ-014`: choose DBOS public timing or controlled collaborator trial access.
4. Repair the chosen public adapter/access path and rerun full clean-clone
   validation.
5. `DQ-010`: authorize a named coordinator and 3–5 real external Agent
   Developers, then execute and record the trial.
6. `DQ-009`: record an explicit Human Release Decision with `released_by_ref`.

No local test, website deployment, prerelease tag, or synthetic demo can replace
these decisions and external-trial evidence.
