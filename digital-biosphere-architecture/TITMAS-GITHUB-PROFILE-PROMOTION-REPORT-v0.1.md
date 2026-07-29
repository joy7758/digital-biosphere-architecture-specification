---
document_id: TITMAS-GITHUB-PROFILE-PROMOTION-REPORT-0.1
title: TITMAS GitHub Profile Promotion Report v0.1
title_zh: TITMAS GitHub 主页推广报告 v0.1
status: complete-profile-main-verified
maturity: Development
normative: false
owner_ref: zhangbin
decision_reference: TITMAS-E01-CONTRIBUTION-PATH-AND-GITHUB-PROMOTION-D01
observed_at: 2026-07-29T21:11:03+08:00
---

# TITMAS GitHub Profile Promotion Report

## Decision and repository

```text
DECISION_ID=TITMAS-E01-CONTRIBUTION-PATH-AND-GITHUB-PROMOTION-D01
DECISION=ACCEPT_BOUNDED_PREFLIGHT_AND_PROFILE_UPDATE
DECIDED_BY_REF=zhangbin

PROFILE_REPOSITORY=joy7758/joy7758
PROFILE_REPOSITORY_VISIBILITY=PUBLIC
PROFILE_DEFAULT_BRANCH=main
PROFILE_BASE_COMMIT=2f2c3b31910665c1bb890d114f807b54581958cb
```

The Profile repository is the public GitHub Profile README source. The core and
trial repositories remained private throughout this change.

## Developer-first public entry

The first screen now states:

```text
TITMAS
Trusted Multi-Agent Infrastructure Standards and Developer Community

Build your Agent product with:
Specification + SDK + Sandbox + scoped access

Confidential core remains private.
Private developer trials are now available by invitation.
```

The README gives first-time developers three explicit entry points:

1. `What TITMAS solves`;
2. `How developers build on TITMAS`;
3. `Apply for a bounded private developer trial`.

It describes the surfaces available to developers as standards, schemas, SDK,
synthetic examples, Sandbox and time-limited scoped trial access. It states
that confidential core source, internal tests, private governance, automatic
standard authority, automatic merge and Deployment authority are not included.

## Trial discovery boundary

The public CTA records:

```text
Private Trial Status: Invite-only
Current Trial: E01 in progress
Next Trial Slots: not yet authorized
TRIAL_APPLICATION_ENTRY=PREPARED_NOT_PUBLISHED
```

No formal application page was invented. The README directs non-binding
interest to the already public RedCrag website and existing public project
email. It requests only a GitHub username, Agent framework or Runtime, a short
non-confidential scenario and confirmation that no personal, customer,
confidential or production data will be submitted.

The private trial repository URL is not present in the public README.

## Current maturity truth

The Profile now publishes:

```text
TITMAS_STAGE_5_PRIVATE_PREVIEW_OPERATIONAL=true
TITMAS_STAGE_5_1_PRIVATE_TRIAL_CHANNEL_READY=true

FIRST_EXTERNAL_HUMAN_DEVELOPER_TRIAL_COMPLETE=false
PUBLIC_PROTOCOL_RELEASED=false
COMMERCIAL_ECOSYSTEM_ESTABLISHED=false
TITMAS_COMMUNITY_ESTABLISHED=false
```

The README expressly separates `ready`, `operational`, `in progress`,
`complete`, `released`, `adopted` and `production ready`.

## Validation

The final candidate passed:

```text
PROFILE_README_LINK_CHECK=PASS
PROFILE_README_CURRENT_STATE_CONSISTENT=true
OUTDATED_PUBLIC_STATE_CLAIMS=0
PRIVATE_REPOSITORY_URL_FINDINGS=0
CORE_SOURCE_DISCLOSURE_FINDINGS=0
SECRET_FINDINGS=0
MARKDOWN_RENDERING_CHECK=PASS
GIT_DIFF_CHECK=PASS
```

All nine unique public HTTPS targets returned HTTP `200`. GitHub's Markdown API
rendered the candidate and contained the required first-screen and private
trial status text.

## Pull Request and merge

```text
PROFILE_BRANCH=codex/titmas-e01-profile-promotion-v0-1
PROFILE_HEAD_COMMIT=b1267fc06e4aff4a148d4d1aa0e75c022b091af1
PROFILE_PULL_REQUEST=14
PROFILE_PULL_REQUEST_STATE=MERGED
PROFILE_PULL_REQUEST_MERGEABLE_BEFORE_MERGE=MERGEABLE
PROFILE_PULL_REQUEST_MERGE_STATE_BEFORE_MERGE=CLEAN
PROFILE_PULL_REQUEST_CHECK_FAILURES=0
PROFILE_PULL_REQUEST_REVIEW_FINDINGS=0
PROFILE_MERGE_COMMIT=e999ee9c1a3e9c4a3b1cb450c1c0776b005feda0
PROFILE_MERGED_AT=2026-07-29T21:09:52+08:00
PROFILE_REMOTE_BRANCH_DELETED=true
```

The Pull Request modified only `README.md`. The public GitHub Profile page,
GitHub Contents API and an uncached raw-content request were read after merge.
The Contents API and raw response matched byte-for-byte with SHA-256
`426f7507f1a8060d1e719ff3e35c0a004b8ffff929c230afc31211131e0a54fa`.

```text
PROFILE_MAIN_SOURCE_VERIFIED=true
PROFILE_MAIN_RENDER_VERIFIED=true
PROFILE_README_BLOB_SHA=53de6ea38e85aaa8df22406de7ae126add6ba29d
TITMAS_GITHUB_PROFILE_CURRENT=true
TITMAS_PRIVATE_TRIAL_DISCOVERY_ENTRY_READY=true
```

## Closed boundaries

```text
CORE_REPOSITORIES_PRIVATE=true
TRIAL_REPOSITORY_VISIBILITY=PRIVATE
PUBLIC_EXPORT_AUTHORIZED=false
FORMAL_STANDARD_CHANGE_AUTHORIZED=false
CORE_REPOSITORY_ACCESS_CHANGE_AUTHORIZED=false
COMMERCIAL_ACCESS_GRANTED=false
FIRST_EXTERNAL_HUMAN_DEVELOPER_TRIAL_COMPLETE=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
```

The Profile update changed public navigation and current-state communication;
it did not change the formal Specification Registry, trial participant
permission, core source, Runtime, Release or commercial status.

## TITMAS Drift Check

```text
TITMAS_DRIFT_CHECK

CORE_INTEROPERABILITY_OBJECTIVE_PRESERVED=true
NEW_CONTROL_AUTHORITY_CREATED=false
NEW_TRUTH_SOURCE_CREATED=false
DUPLICATE_EVIDENCE_OR_VERIFICATION_CREATED=false
RUNTIME_OR_EXECUTOR_CREATED=false
CURRENT_CAPABILITY_OVERCLAIMED=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false

TITMAS_DRIFT_CHECK_RESULT=PASS_WITH_RECORDED_LIMITATIONS
```
