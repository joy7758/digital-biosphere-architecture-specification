---
document_id: TITMAS-AGENT-NATIVE-STANDARDS-COMMUNITY-OPENING-REPORT-1.0
title: TITMAS Agent-Native Standards Community Core Merge and Public Opening Report v1.0
title_zh: TITMAS 智能体原生标准社区核心合并与公共开放报告 v1.0
status: activation-pr-candidate
maturity: Development
normative: false
owner_ref: zhangbin
decision_reference: TITMAS-COMMUNITY-CORE-MERGE-AND-OPENING-D01
---

# TITMAS Community Core Merge and Public Opening Report v1.0

## Core merge

```text
core_pr=41
core_pr_head=922f2b088287a9ee026e931357ecdc343a468566
core_decision_record_head=7ac40ea01a48160c8f38af7478c01229f7ec8f21
core_merge_commit=3ce0b2008db1433db7c24375f81cfa422fabb7e3
main_after_core_merge=3ce0b2008db1433db7c24375f81cfa422fabb7e3
```

PR #41 passed the six Human Owner review lanes and was merged with an exact
head binding. This was not an independent third-party review.

## Security Transport

```text
security_transport_before=false
security_activation_method=GITHUB_PRIVATE_VULNERABILITY_REPORTING_API_PUT
security_activation_http_status=204
security_transport_after=true
security_transport_verified=true
```

No token, Authorization header, private report content or invented mailbox is
stored. The enabled route is not a security audit, certification, SLA or
zero-vulnerability claim.

## Activation candidate

```text
activation_branch=codex/titmas-community-public-contribution-activation-v0-1
activation_pr=42
activation_pr_head=8a1c114186d3fb3cb613a2e1f423d1a33e760416
activation_merge_commit=PENDING_MERGE
main_after_activation=PENDING_MERGE
```

Five templates are installed on the non-default Activation branch:

- `.github/ISSUE_TEMPLATE/bug.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/integration.yml`
- `.github/ISSUE_TEMPLATE/proposal.yml`
- `.github/pull_request_template.md`

Their hashes are bound by
`TITMAS/community/github-activation-templates/activation-manifest.json`.
They remain inactive until the Activation PR merges.

## Welcome and public entry

```text
welcome_issue=PENDING_ACTIVATION_MERGE
public_entry_points=TITMAS/README.md,agent-index.json,CONTRIBUTING.md
conformance_command=python3 TITMAS/conformance/harness.py
```

## Validation

The candidate must pass TITMAS Conformance, unit tests, Agent-native tests,
Candidate Grounding, reference tests, JSON/YAML parsing, Issue Form and Pull
Request template structure, active/dormant hash binding, Markdown links,
secret/private-path scans, site tests/build/lint, production dependency audit
and `git diff --check`. GitHub CI and the exact Activation PR head are recorded
after PR creation.

## Limitations and deferred decisions

- `COMMUNITY_ESTABLISHED=false`;
- no external contributor or adopter is yet recorded;
- no Foundation, Certification, Stable standard, Release tag, deployment or
  commercial product is authorized;
- no GitHub Organization is created;
- no independent Human Reviewer is assigned;
- Calibration v0.3 and Formal Ecology Box remain unauthorized;
- contribution submission does not mean acceptance or Authority.

## Rollback

If activation fails before merge, keep the PR Draft and leave `main` without
the templates. If Security Transport becomes inactive, do not merge. After
merge, a serious activation defect should first remove the active templates and
close the limited contribution surface; the community core is reverted only if
the core itself is affected. No automatic revert is authorized by this report.
