---
document_id: TITMAS-STAGE-5-2-EXTERNAL-DEVELOPER-TRIAL-E01-REPORT-1.0
title: TITMAS Stage 5.2 First External Developer Trial E01 Report v1.0
title_zh: TITMAS Stage 5.2 首位外部开发者试用 E01 报告 v1.0
status: access-revoked-expired-incomplete
maturity: Development
normative: false
owner_ref: zhangbin
decision_reference: TITMAS-STAGE-5-2-FIRST-EXTERNAL-DEVELOPER-TRIAL-E01
participant_id: TITMAS-EXT-DEV-001
observed_at: 2026-08-02T04:04:48+08:00
---

# TITMAS Stage 5.2 First External Developer Trial E01 Report

## Scope and Human Decision

This report records the bounded first external human developer trial. It is an
audit record of an invitation and future participant activity. It is not
customer adoption, community establishment, market validation, formal standard
change, Release or Deployment.

```text
DECISION_ID=TITMAS-STAGE-5-2-FIRST-EXTERNAL-DEVELOPER-TRIAL-E01
DECISION=ACCEPT_ONCE
DECIDED_BY_REF=zhangbin

PARTICIPANT_ID=TITMAS-EXT-DEV-001
PARTICIPANT_GITHUB_USERNAME=lizuyi-6
PARTICIPANT_SOURCE=HUMAN_OWNER_NOMINATED_TRUSTED_EXTERNAL_DEVELOPER
SELECTED_TRIAL_TASK=TRIAL-01-NEGATIVE-TEST-VECTOR

ACCESS_REPOSITORY=joy7758/titmas-private-developer-trial
ACCESS_DURATION_HOURS=72
ACCESS_EXPIRES_AT=2026-08-01T20:00:00+08:00
TRIAL_ACKNOWLEDGEMENT_CONFIRMED=true
```

The Human Owner confirmed the required trial terms before invitation. This
confirmation does not assert that the participant has accepted the GitHub
invitation or separately confirmed deletion of a future local clone.

## Live pre-invitation facts

The following facts were read from the GitHub API immediately before the
invitation:

```text
PARTICIPANT_ACCOUNT_EXISTS=true
PARTICIPANT_IS_JOY7758=false
PARTICIPANT_CORE_COLLABORATOR=false
PARTICIPANT_TRIAL_COLLABORATOR=false
PARTICIPANT_PENDING_INVITATION=false
PARTICIPANT_OPEN_TRIAL_PULL_REQUEST=false

CORE_REPOSITORY=joy7758/digital-biosphere-architecture-specification
CORE_REPOSITORY_VISIBILITY=PRIVATE
TRIAL_REPOSITORY=joy7758/titmas-private-developer-trial
TRIAL_REPOSITORY_VISIBILITY=PRIVATE
TRIAL_REPOSITORY_IS_FORK=false
TRIAL_REPOSITORY_DEFAULT_BRANCH=main
TRIAL_REPOSITORY_ROOT_COMMIT=cb824621189262c4e4bc9f12840f1de08d615cb9
TRIAL_REPOSITORY_CURRENT_MAIN=cb824621189262c4e4bc9f12840f1de08d615cb9
```

The trial repository still had only `main`, no open Pull Request, no Release
and no Tag. Its only collaborator was `joy7758`.

## Repository protection

GitHub branch protection was read back from the live trial repository:

```text
BRANCH_PROTECTION_VERIFIED=true
DEFAULT_BRANCH_DIRECT_PUSH_BLOCKED=true
FORCE_PUSH_BLOCKED=true
BRANCH_DELETION_BLOCKED=true
PULL_REQUEST_REQUIRED=true
REQUIRED_APPROVING_REVIEW_COUNT=1
REQUIRE_LAST_PUSH_APPROVAL=true
DISMISS_STALE_REVIEWS=true
REQUIRED_CONVERSATION_RESOLUTION=true
REQUIRED_LINEAR_HISTORY=true
REQUIRED_STATUS_CHECK=trial-conformance
REQUIRED_STATUS_CHECK_STATE=success
```

The successful status is bound to trial repository commit
`cb824621189262c4e4bc9f12840f1de08d615cb9`. Its status description states that
the allowlist, manifest, clean clone and Conformance checks passed. This is a
technical baseline, not participant completion or standard adoption.

## Invitation state

GitHub accepted a read-only collaborator invitation for the exact participant.
The first post-invitation check found it pending and unexpired. A later live
check found no pending invitation, returned `204` for the trial-repository
collaborator check and reported the participant's role as `read`. This proves
that repository access became active; it does not identify the exact GitHub
acceptance timestamp.

```text
INVITATION_SENT=true
INVITATION_SENT_AT=2026-07-29T20:38:37+08:00
INVITATION_PERMISSION=read
INVITATION_ACCEPTED=true
INVITATION_ACCEPTED_OBSERVED_AT=2026-07-29T20:44:10+08:00
INVITATION_PENDING=false
INVITATION_EXPIRED=false

EXTERNAL_ACCESS_GRANTED=true
EXTERNAL_ACCESS_ROLE=read
CORE_REPOSITORY_ACCESS=false
CORE_SOURCE_ACCESS=false
PRIVATE_GOVERNANCE_ACCESS=false
```

`INVITATION_SENT=true` records GitHub accepting the invitation request. It does
not by itself prove acceptance; the later collaborator and permission reads
provide that separate evidence.

## Participant task boundary

The participant receives only `TRIAL-01-NEGATIVE-TEST-VECTOR`: prepare one
negative Test Vector that describes an input that must be rejected, declares
the expected `FAIL` result, exposes a public Reason Code and states the failure
boundary.

Contribution-path preflight found the direct upstream-branch route unavailable
with the live `read` role. The repository permits private Forks, so the
confirmed route is:

```text
E01_CONTRIBUTION_PATH=PRIVATE_FORK_PULL_REQUEST
OWNER_START_ISSUE_NUMBER=1
OWNER_START_ISSUE_CREATED=true
```

The participant must independently read the repository entry surfaces,
install the trial SDK, select the task, create their own private Fork and
branch, prepare the Test Vector, run preflight, push to their Fork, open one
Pull Request to upstream `main`, wait for `trial-conformance` and submit
feedback.

No standard answer, internal test, core source, hidden expected field, private
conversation or prior Agent answer may be supplied.

## Initial measurements

No participant behavior has yet been observed. Unknown values are preserved
rather than inferred from the invitation.

```text
time_to_repository_acceptance=OBSERVED_WITHIN_00:05:33
repository_acceptance_observed_at=2026-07-29T20:44:10+08:00
time_to_first_clone=NOT_OBSERVED
time_to_sdk_install=NOT_OBSERVED
time_to_task_selection=NOT_OBSERVED
time_to_first_preflight=NOT_OBSERVED
time_to_pull_request=NOT_OBSERVED

installation_failures=NOT_OBSERVED
documentation_questions=NOT_OBSERVED
human_help_count=0

task_understanding=NOT_ASSESSED
sdk_usability=NOT_ASSESSED
conformance_clarity=NOT_ASSESSED
boundary_understanding=NOT_ASSESSED

core_access_requests=0
authority_confusion_count=0
private_context_exposure_count=0

trial_completion=false
submission_quality=NOT_ASSESSED
```

These fields must not be populated from private participant data or
unauthorized terminal contents.

## Audit-branch validation

The canonical TITMAS Development Conformance harness and all eight Python test
domains were run from a clean checkout after the two audit records were
created.

```text
CANONICAL_CONFORMANCE=PASS
PYTHON_TEST_DOMAINS=8
PYTHON_TESTS=167/167_PASS
GIT_DIFF_CHECK=PASS
REAL_MODEL_CALL_COUNT=0
REAL_PROVIDER_CALL_COUNT=0
```

These local checks validate the bounded audit change. They do not represent
participant activity or replace the trial repository's required
`trial-conformance` check.

## Maintainer and access gates

No participant Pull Request exists and no Human Maintainer disposition can yet
be made. A valid negative Test Vector can receive
`CONFORMANCE_STATUS=CONFORMANCE_PASS` while still requiring Human disposition;
the status means that the contribution follows the negative-test contribution
format, not that the rejected input passed.

Access must be revoked on expiry, trial completion, participant withdrawal,
core-access request, data-scope violation, Human Owner stop or security
exception. Revocation must be verified through GitHub. Local clone deletion can
only be reported from participant confirmation.

```text
ACCESS_REVOKED=true
ACCESS_REVOCATION_REASON=TRIAL_EXPIRY
ACCESS_EXPIRED_AT=2026-08-01T20:00:00+08:00
ACCESS_REVOKED_OBSERVED_AT=2026-08-02T04:04:48+08:00
POST_REVOCATION_PERMISSION=none
POST_REVOCATION_COLLABORATOR_CHECK=404_NOT_FOUND
POST_REVOCATION_PENDING_INVITATION_COUNT=0
LOCAL_CLONE_DELETION_CONFIRMED_BY_PARTICIPANT=unknown
```

The expiry check was executed after the declared expiry time. GitHub returned
`permission=none`, the direct collaborator check returned `404`, the pending
invitation list was empty and the remaining collaborator list contained only
the repository owner. These reads verify that repository permission no longer
exists. They do not prove deletion of any participant-side local clone.

## Expiry-state observation

The owner-visible repository surfaces were read without modifying participant
content:

```text
OWNER_START_ISSUE_NUMBER=1
OWNER_START_ISSUE_STATE=OPEN
OWNER_START_ISSUE_COMMENT_COUNT=0
PARTICIPANT_PRIVATE_FORK_OBSERVED_BY_OWNER_API=false
PARTICIPANT_UPSTREAM_BRANCH_OBSERVED=false
PARTICIPANT_PULL_REQUEST_EXISTS=false
PARTICIPANT_CONTRIBUTION_OBSERVED=false
PARTICIPANT_FEEDBACK_RECEIVED=false
CORE_ACCESS_REQUESTS_OBSERVED=0
DATA_SCOPE_VIOLATIONS_OBSERVED=0
SECURITY_EXCEPTIONS_OBSERVED=0
PARTICIPANT_TRIAL_CONFORMANCE_RESULT=NOT_ASSESSED
BASELINE_TRIAL_CONFORMANCE_STATE=success
BASELINE_TRIAL_CONFORMANCE_SHA=cb824621189262c4e4bc9f12840f1de08d615cb9
```

The Fork value means that the owner API returned no visible Fork record at the
observation time; it is not a claim about an unobservable participant-local
clone. The successful `trial-conformance` status remains the repository
baseline status and must not be attributed to the participant.

## Current outcome

```text
TRIAL_PREFLIGHT_STATUS=PASS
TRIAL_EXECUTION_STATUS=ACCESS_EXPIRED_NO_PARTICIPANT_CONTRIBUTION
FIRST_EXTERNAL_HUMAN_DEVELOPER_TRIAL_COMPLETE=false
HUMAN_DISPOSITION_STATUS=PENDING

CUSTOMER_ADOPTION=false
COMMUNITY_ESTABLISHED=false
MARKET_VALIDATED=false
PRODUCTION_READY=false
```

## Closed boundaries

```text
CORE_REPOSITORIES_PRIVATE=true
EXTERNAL_DEVELOPER_CORE_ACCESS=false
FORMAL_STANDARD_CHANGE_AUTHORIZED=false
AUTOMATIC_MERGE_AUTHORIZED=false
PUBLIC_EXPORT_AUTHORIZED=false
PUBLIC_PROTOCOL_RELEASED=false
COMMERCIAL_ACCESS_GRANTED=false
RELEASE_AUTHORIZED=false
TAG_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
REAL_MODEL_CALL_AUTHORIZED=false
REAL_PROVIDER_CALL_AUTHORIZED=false
TITMAS_COMMUNITY_ESTABLISHED=false
COMMERCIAL_ECOSYSTEM_ESTABLISHED=false
```

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
