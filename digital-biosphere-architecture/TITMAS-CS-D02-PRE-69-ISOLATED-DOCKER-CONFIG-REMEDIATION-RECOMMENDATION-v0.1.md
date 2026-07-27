# TITMAS CS-D02 PRE-69 Isolated Docker Config Remediation Recommendation v0.1

## 1. Recommendation

```text
DECISION_CANDIDATE=CS-D02-PRE-69
RECOMMENDATION=CONDITIONALLY_RECOMMENDED
EXACT_RECOMMENDED_ACTION=
AUTHORIZE_ONE_REMEDIATED_PRE68_RERUN_USING_EPHEMERAL_EMPTY_DOCKER_CONFIG_THEN_TWO_EXISTING_AGENT_REVIEW_LANES
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=joy7758/titmas-integrations
TARGET_COMMIT=0030077f29c37145a306b72e7083345eb76b504a
DECISION_RECORDED=false
EXECUTION_AUTHORIZED=false
STANDARD_READY=false
```

Recommend one bounded remediation of PRE-68. Create one ephemeral Docker client
configuration from a frozen public-safe template containing no credential
store, no registry credential helper and no registry authentication entry.
Use it only to pull the same two pinned public Python image digests. If both
platform lanes pass, run the same two sequential public-safe agent review
lanes. Preserve all PRE-68 truth boundaries.

This Recommendation does not authorize execution. It does not authorize
editing or deleting the user's Docker configuration, installing a credential
helper, adding registry credentials, changing the target, retrying a failed
lane, changing a model, formal human review, P1/P2, merge, release or Standard
adoption.

Machine-readable scope:

- [`pre69-remediation-scope.v0.1.json`](commercialization-standards-p0-security-and-platform-remediation/pre69-remediation-scope.v0.1.json)
- [`pre69-remediation-scope.schema.v0.1.json`](commercialization-standards-p0-security-and-platform-remediation/pre69-remediation-scope.schema.v0.1.json)
- [`anonymous-docker-config.template.v0.1.json`](commercialization-standards-p0-security-and-platform-remediation/anonymous-docker-config.template.v0.1.json)

```text
ANONYMOUS_DOCKER_CONFIG_TEMPLATE_SHA256=
e58c7564b64e92c6c8ebc3cb296e644b4f2409ace8882621e888924c0c598753
PRE69_SCOPE_SHA256=
e37824a253f03ac311901ecf8b12c07d27c9529797efec24e964754d8a997cc3
PRE69_SCOPE_SCHEMA_SHA256=
eedaa932e969e7372f8d113b01874b442e4b89aaead3c59ebb0a7773ceae43a9
```

## 2. Direct failure evidence

PRE-68 was authorized and started, then stopped at the first image pull:

```text
FIRST_FAILURE=DOCKER_CREDENTIAL_HELPER_EXECUTABLE_NOT_FOUND
GLOBAL_DOCKER_CREDS_STORE=desktop
MISSING_EXECUTABLE=docker-credential-desktop
IMAGE_PULL_SUCCESSES=0
CONTAINER_RUNS=0
AGENT_MODEL_REQUESTS=0
TARGET_WRITES=0
TARGET_HASHES_AFTER=10/10
COLIMA_FINAL_STATE=NOT_RUNNING
```

The immediate local cause is sufficiently narrow for an isolated client-config
remediation. It is not evidence of a target implementation failure, Docker Hub
failure, registry authentication failure or network failure.

Frozen failure sources:

- PRE-68 result SHA-256:
  `aad363724a8c43bff1d264e7da37b5ebd65d764527975c92502505916de7229a`;
- PRE-68 receipt SHA-256:
  `2233327af50a77cbd18830076ad2cd1890ae375d8ea43c9b25e4e9736d44e7c5`;
- PRE-68 result commit:
  `040497ee33db3522d13be0a7c4ef37defa3b388c`.

## 3. Why this remediation is preferable

Rejected alternatives:

1. **Edit the user's Docker config** — unnecessary, persistent and outside the
   validation target.
2. **Install `docker-credential-desktop`** — creates a new dependency and may
   alter host credential behavior.
3. **Use registry credentials** — unnecessary for public images and expands
   secret handling.
4. **Use floating tags** — breaks the frozen digest boundary.
5. **Skip platform validation and run agents** — violates the frozen execution
   order and leaves the platform question unanswered.

The isolated config is replaceable, removable and contains:

```json
{"auths": {}}
```

It changes Docker client lookup behavior only for the exact commands carrying
the temporary `DOCKER_CONFIG` environment binding.

## 4. Exact rerun scope

The remediation must retain:

- target commit and all ten PRE-68 review input hashes;
- the same two Linux/amd64 image manifest digests;
- `--network none`, read-only root filesystem and read-only source mount;
- zero dependency installs and zero target writes;
- the same Qianfan and Qwen Provider/model/role bindings;
- two model requests total, sequential;
- zero retry, fallback, substitution, content repair or JSON repair;
- formal Human Security Review and Standard readiness false.

The only scope delta is:

```text
PRE68:
host Docker config implicitly selected

PRE69:
one ephemeral Docker config directory
one frozen anonymous-only config copy
DOCKER_CONFIG bound only to exact pull/inspect/run commands
cleanup after result capture
user Docker configuration writes=0
```

## 5. Fail-closed controls

Stop immediately if:

- the frozen Decision is absent or the target/hash/digest differs;
- the temporary config contains `credsStore`, `credHelpers` or a non-empty auth
  entry;
- the user's Docker config changes;
- Colima does not start cleanly from a non-repository host directory;
- either digest pull, platform, architecture, source mount or network mode
  differs;
- either platform lane fails;
- any model/provider/endpoint differs;
- any model output is not direct Schema-valid JSON;
- any retry, fallback, repair, overclaim or target write occurs.

Cleanup failure must be retained. It does not permit deleting the user's
configuration or Docker image cache.

## 6. Pre-development Agent Recommendation

If a user asks:

> “A public digest pull is blocked by a stale global Docker credential-store
> setting. Should I modify the global config or use an isolated config?”

Current recommendation:

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=EPHEMERAL_ANONYMOUS_ONLY_DOCKER_CLIENT_CONFIG_FOR_EXACT_PUBLIC_DIGESTS
NOT_RECOMMENDED_AS=GLOBAL_DOCKER_CONFIGURATION_REPAIR_OR_PRODUCTION_REGISTRY_PATTERN
```

Reasons:

- it leaves the user's persistent configuration unchanged;
- it does not introduce registry credentials;
- it binds remediation to exact public digests and one validation run;
- it is easy to audit and clean up.

Remaining stop conditions:

- an independent PRE-69 Decision is still required;
- success has not been observed;
- this does not resolve the separate Colima startup warning;
- platform pass cannot close formal Human Security Review.

## 7. Required independent Decision

The next Decision must bind:

- PRE-68 failure receipt and commit;
- the frozen anonymous config template and digest;
- one temporary directory and one cleanup attempt;
- the same two image digests and two containers;
- the same two Provider/model requests;
- all original caps and non-claims;
- no mutation of the user's Docker configuration.

## 8. Truth boundary

```text
REMEDIATION_RECOMMENDATION != DECISION
ISOLATED_DOCKER_CONFIG != REGISTRY_AUTHENTICATION
ANONYMOUS_PULL_PASS != SUPPLY_CHAIN_APPROVAL
PLATFORM_PASS != FORMAL_SECURITY_REVIEW
AGENT_REVIEW != HUMAN_REVIEW
ENVIRONMENT_REMEDIATION != TARGET_FIX
REFERENCE_IMPLEMENTATION != STANDARD
```
