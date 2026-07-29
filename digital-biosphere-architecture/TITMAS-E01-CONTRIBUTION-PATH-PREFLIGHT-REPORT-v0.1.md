---
document_id: TITMAS-E01-CONTRIBUTION-PATH-PREFLIGHT-REPORT-0.1
title: TITMAS E01 Contribution-Path Preflight Report v0.1
title_zh: TITMAS E01 贡献路径预检报告 v0.1
status: complete-private-fork-path-confirmed
maturity: Development
normative: false
owner_ref: zhangbin
decision_reference: TITMAS-E01-CONTRIBUTION-PATH-AND-GITHUB-PROMOTION-D01
participant_id: TITMAS-EXT-DEV-001
observed_at: 2026-07-29T21:11:03+08:00
---

# TITMAS E01 Contribution-Path Preflight Report

## Decision and scope

```text
DECISION_ID=TITMAS-E01-CONTRIBUTION-PATH-AND-GITHUB-PROMOTION-D01
DECISION=ACCEPT_BOUNDED_PREFLIGHT_AND_PROFILE_UPDATE
DECIDED_BY_REF=zhangbin

PARTICIPANT_GITHUB_USERNAME=lizuyi-6
TRIAL_REPOSITORY=joy7758/titmas-private-developer-trial
CORE_REPOSITORY=joy7758/digital-biosphere-architecture-specification
```

This preflight uses repository settings, collaborator permissions, branch
protection, Fork inventory and GitHub's published contribution rules. It does
not authenticate as the participant and does not create a participant branch,
Fork, contribution or Pull Request.

## Access facts

Live GitHub API reads returned:

```text
CORE_REPOSITORY_PERMISSION=NONE
TRIAL_REPOSITORY_PERMISSION=read
TRIAL_REPOSITORY_ROLE_NAME=read
INVITATION_ACCEPTED=true
```

The core collaborator endpoint returned `404`. The trial collaborator
permission endpoint returned `read`. The trial repository remains private and
is owned by the `joy7758` personal account.

## Path A — direct upstream branch

```text
CLONE_TRIAL_REPOSITORY=AVAILABLE
CREATE_LOCAL_NON_MAIN_BRANCH=AVAILABLE
PUSH_UPSTREAM_NON_MAIN_BRANCH=NOT_AVAILABLE_WITH_CURRENT_READ_ROLE
OPEN_PULL_REQUEST_FROM_UPSTREAM_BRANCH=NOT_AVAILABLE

DIRECT_BRANCH_CONTRIBUTION_PATH=NOT_AVAILABLE
```

The live participant role is the authoritative current access fact. GitHub's
repository-role documentation separately describes `Write` as the role for
contributors who actively push to a repository. No controller-side push was
attempted with participant credentials.

## Path B — private Fork Pull Request

The live repository record returned `allow_forking=true`, `forks_count=0` and
`network_count=0`. GitHub documents that a user with access to a private
repository may fork it to a personal account when the owner permits forking,
and may submit a Pull Request from that Fork.

```text
PRIVATE_FORKING_ENABLED=true
PARTICIPANT_CAN_CREATE_PRIVATE_FORK=not_assessed
FORK_PULL_REQUEST_PATH=available
EXISTING_PARTICIPANT_FORK=false
```

`PARTICIPANT_CAN_CREATE_PRIVATE_FORK=not_assessed` preserves the distinction
between a platform path that is available and a participant action that has
not yet occurred. The controller is prohibited from creating the Fork on the
participant's behalf.

GitHub reference:

- <https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks>

## Main-branch controls

The live `main` branch protection record confirms:

```text
DEFAULT_BRANCH_DIRECT_PUSH_BLOCKED=true
FORCE_PUSH_BLOCKED=true
BRANCH_DELETION_BLOCKED=true
SELF_APPROVAL_BLOCKED=true
PULL_REQUEST_REQUIRED=true
REQUIRED_APPROVING_REVIEW_COUNT=1
REQUIRE_LAST_PUSH_APPROVAL=true
DISMISS_STALE_REVIEWS=true
REQUIRED_CONVERSATION_RESOLUTION=true
REQUIRED_LINEAR_HISTORY=true
REQUIRED_STATUS_CHECK=trial-conformance
MERGE_WITHOUT_TRIAL_CONFORMANCE_BLOCKED=true
```

Branch protection constrains `main`; it does not grant the participant a new
permission or prove that a future contribution is correct.

## Final path classification

```text
E01_CONTRIBUTION_PATH=PRIVATE_FORK_PULL_REQUEST
E01_CONTRIBUTION_PATH_CONFIRMED=true
E01_WAITING_FOR_PARTICIPANT_ACTION=true
E01_WAITING_STATE_VALID=true

OPTION_A_GRANT_WRITE_ACCESS=NOT_REQUIRED_FOR_CONFIRMED_PATH
OPTION_B_TRANSFER_TO_ORGANIZATION=LONG_TERM_RECOMMENDATION_ONLY
OPTION_C_CLOSE_E01_INCOMPLETE=NOT_TRIGGERED
```

The classification confirms a technically documented Pull Request route while
keeping the upstream trial role read-only. It does not assert that the
participant has created a Fork, branch, contribution or Pull Request.

## Owner start entry

The first Issue creation attempt failed because Issues were disabled. The
owner enabled Issues on the still-private trial repository and created:

```text
OWNER_START_ISSUE_NUMBER=1
OWNER_START_ISSUE_TITLE=E01 Start Here — Negative Test Vector Trial
OWNER_START_ISSUE_CREATED=true
PARTICIPANT_MENTIONED=true
STANDARD_ANSWER_INCLUDED=false
PREBUILT_CONTRIBUTION_INCLUDED=false
```

The Issue instructs the participant to read the entry surfaces, use the
private-Fork path, choose `TRIAL-01-NEGATIVE-TEST-VECTOR`, avoid private,
customer and production data, create their own contribution, run preflight,
open one Pull Request, wait for `trial-conformance`, submit feedback and avoid
requesting core source.

## Monitoring correction

The active E01 monitor was revised to inspect both:

- branches and Pull Requests in the upstream trial repository; and
- private Fork inventory plus Pull Requests originating from the participant's
  Fork.

The monitor cannot see or claim private local participant activity that GitHub
does not expose to the repository owner.

## Closed boundaries

```text
PARTICIPANT_CONTENT_CREATION_AUTHORIZED=false
PARTICIPANT_BRANCH_CREATION_BY_CONTROLLER=false
PARTICIPANT_FORK_CREATION_BY_CONTROLLER=false
PARTICIPANT_PR_CREATION_BY_CONTROLLER=false

CORE_REPOSITORY_ACCESS_CHANGE_AUTHORIZED=false
CORE_REPOSITORY_PERMISSION=NONE
TRIAL_REPOSITORY_PUBLICATION_AUTHORIZED=false
TRIAL_REPOSITORY_VISIBILITY=PRIVATE

FORMAL_STANDARD_CHANGE_AUTHORIZED=false
COMMERCIAL_ACCESS_GRANTED=false
FIRST_EXTERNAL_HUMAN_DEVELOPER_TRIAL_COMPLETE=false
```

## Audit-branch validation

```text
CANONICAL_CONFORMANCE=PASS
PYTHON_TEST_DOMAINS=8
PYTHON_TESTS=167/167_PASS
GIT_DIFF_CHECK=PASS
AUDIT_BOUNDARY_SCAN=PASS
```

These checks cover the final audit candidate. They do not execute or validate a
participant contribution.

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
