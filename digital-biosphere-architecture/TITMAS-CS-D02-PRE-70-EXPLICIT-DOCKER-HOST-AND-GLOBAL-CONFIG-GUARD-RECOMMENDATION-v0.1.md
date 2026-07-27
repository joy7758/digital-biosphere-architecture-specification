# TITMAS CS-D02 PRE-70 Explicit Docker Host and Global Config Guard Recommendation v0.1

## 1. Recommendation

```text
DECISION_CANDIDATE=CS-D02-PRE-70
RECOMMENDATION=CONDITIONALLY_RECOMMENDED
EXACT_RECOMMENDED_ACTION=
AUTHORIZE_ONE_NONACTIVATING_COLIMA_RERUN_WITH_EPHEMERAL_DOCKER_CONFIG_EXPLICIT_DOCKER_HOST_METADATA_GUARD_THEN_EXISTING_PLATFORM_AND_AGENT_LANES
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=joy7758/titmas-integrations
TARGET_COMMIT=0030077f29c37145a306b72e7083345eb76b504a
DECISION_RECORDED=false
EXECUTION_AUTHORIZED=false
STANDARD_READY=false
```

Recommend one new bounded remediation run. Bind the ephemeral anonymous-only
`DOCKER_CONFIG` to Colima start, Docker operations and Colima stop. Start the
existing default profile with:

```text
--activate=false
--save-config=false
--port-forwarder=none
```

Do not depend on Docker context selection. Instead, validate the default-profile
Unix socket and bind it through `DOCKER_HOST` only for the exact Docker pull and
container commands. Compare recursive metadata-only snapshots of the user's
default Docker configuration root before start and after stop. Persist only
whether the snapshots match, never paths, metadata entries or file contents.

This Recommendation does not authorize execution. It does not authorize a
retry of PRE-69, modifying or restoring the user's Docker configuration,
reading credential values, symlinking `/var/run/docker.sock`, changing the
target, using floating tags, changing Provider/model bindings, formal human
review, P1/P2, merge, release or Standard adoption.

Machine-readable scope:

- [`pre70-context-and-config-guard-scope.v0.1.json`](commercialization-standards-p0-security-and-platform-context-remediation/pre70-context-and-config-guard-scope.v0.1.json)
- [`pre70-context-and-config-guard-scope.schema.v0.1.json`](commercialization-standards-p0-security-and-platform-context-remediation/pre70-context-and-config-guard-scope.schema.v0.1.json)

```text
PRE70_SCOPE_SHA256=
be159d945c02cb0f3a17d87dd1aa351d4fd6c7b270a3a14fe1085c285956f077
PRE70_SCOPE_SCHEMA_SHA256=
9714b064974937431dd6f705ef2f4b6df58eacb421861214e4e9538e31acfd7d
```

## 2. Direct failure evidence

PRE-69 completed its isolated config and source checks, then failed before image
transfer:

```text
FIRST_FAILURE=DOCKER_DAEMON_SOCKET_UNAVAILABLE_UNDER_ISOLATED_CONFIG
ISOLATED_CONFIG_VALID=true
ISOLATED_CONFIG_CURRENT_CONTEXT_PRESENT=false
DOCKER_CONTEXT_EXPLICITLY_SELECTED=false
ZERO_USER_DOCKER_CONFIG_WRITE_BOUNDARY_MET=false
IMAGE_PULL_SUCCESSES=0
CONTAINER_RUNS=0
AGENT_MODEL_REQUESTS=0
TARGET_HASHES_AFTER=10/10
COLIMA_FINAL_STATE=NOT_RUNNING
```

Frozen PRE-69 sources:

- result commit:
  `14a044a4ae3c2fa93057d4332e752f6e33ca9638`;
- result SHA-256:
  `b0ff4169c0e3a391abc73da6e64f9aad3bbad55673a0cf14590d4e57e7d6ae53`;
- receipt SHA-256:
  `91d7a0ae4b74c6949088ce184f18e5e4de5cef74ff88dc7a8d12dd72a5186b18`.

PRE-69 did not prove a target implementation defect, registry failure,
platform test failure or agent-review rejection.

## 3. Tool and source basis

The currently installed host tool reports:

```text
COLIMA_VERSION=0.10.1
COLIMA_COMMIT=ed905203afdbc6fd4eae6cc301918099ff31e86e
START_FLAG_ACTIVATE_AVAILABLE=true
START_FLAG_ACTIVATE_DEFAULT=true
START_FLAG_SAVE_CONFIG_AVAILABLE=true
START_FLAG_SAVE_CONFIG_DEFAULT=true
DOCKER_HOST_OPTION_AVAILABLE=true
```

The official Colima FAQ documents both the default-profile socket and
`DOCKER_HOST` as a supported way for clients that do not use Docker contexts:

<https://github.com/abiosoft/colima/blob/main/docs/FAQ.md>

This source basis shows that the remediation is technically plausible. It does
not prove that the exact non-activating run will leave all global Docker
metadata unchanged; that remains an execution gate.

## 4. Exact control delta

PRE-70 retains the PRE-68/PRE-69 target, inputs, images, containers, model
bindings, response schema, caps and truth boundaries. Its only control changes
are:

```text
COLIMA_START_AND_STOP_DOCKER_CONFIG=EPHEMERAL_ANONYMOUS_ONLY
COLIMA_ACTIVATE=false
COLIMA_SAVE_CONFIG=false
COLIMA_PORT_FORWARDER=none
DOCKER_DAEMON_SELECTOR=DOCKER_HOST
DOCKER_CONTEXT_DEPENDENCY=false
DEFAULT_SOCKET_FALLBACK=false
GLOBAL_CONFIG_GUARD=RECURSIVE_LSTAT_METADATA_ONLY
GLOBAL_CONFIG_CONTENT_READS=0
GLOBAL_CONFIG_DIRECT_WRITES=0
GLOBAL_CONFIG_REPAIR_AUTHORIZED=false
```

The socket must:

- exist only after the authorized Colima start;
- be a Unix socket;
- be owned by the current user;
- resolve under the current default-profile Colima home;
- be passed only through the exact process environment;
- never be persisted as a private absolute path.

## 5. Fail-closed order

1. Verify the PRE-70 Decision, target commit, 10 hashes and all frozen digests.
2. Create one temporary root and anonymous Docker config.
3. Take the pre-start metadata-only global Docker config snapshot in memory.
4. Start existing Colima with the isolated config and three frozen flags.
5. Validate the default-profile Unix socket and bind `DOCKER_HOST`.
6. Pull both exact public digests, with no retry.
7. Run both `linux/amd64`, `--network none`, read-only lanes.
8. Only if both pass, run the two sequential agent-assisted review requests.
9. Stop Colima using the same isolated Docker config.
10. Compare the post-stop metadata-only snapshot.
11. Delete only the exact temporary root.
12. Persist sanitized results and all failures.

Stop if the daemon selector, socket, global metadata, source, digest, network,
read-only controls, tests, model binding, direct-JSON contract or cleanup
differs. A metadata mismatch is a failed boundary; it does not authorize
repair.

## 6. Pre-development Agent Recommendation

If a user asks:

> “Should a bounded Colima validation isolate credentials and select the daemon
> explicitly, instead of relying on the user's active Docker context?”

Current answer:

```text
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=BOUNDED_NONACTIVATING_LOCAL_VALIDATION_WITH_EXPLICIT_DAEMON_AND_METADATA_GUARD
NOT_RECOMMENDED_AS=GENERAL_DOCKER_CONFIGURATION_PATTERN_OR_PRODUCTION_RUNTIME
```

Why an agent would recommend it:

- it separates credential lookup from daemon selection;
- it removes dependence on mutable global Docker context;
- it uses official Colima/Docker connection mechanisms;
- it binds all writes to one removable temporary Docker config;
- it preserves failure and does not repair user state silently.

Remaining reasons not to recommend it as complete:

- the exact non-activating lifecycle has not been executed;
- metadata-only comparison cannot prove absence of an in-place write that
  preserves all observed metadata;
- image provenance and supply-chain approval remain out of scope;
- two Linux observations cannot establish cross-platform support;
- agent review cannot close formal Human Security Review.

## 7. Required independent Decision

The next Decision must bind:

- PRE-69 result commit and receipt hashes;
- Colima version and local CLI capabilities;
- official FAQ reference as source evidence, not adoption;
- the same anonymous config template;
- the three exact Colima flags;
- the symbolic default-profile socket and `DOCKER_HOST` binding;
- the metadata-only guard and its limitations;
- the same two image digests, two containers and two Provider/model requests;
- zero retry, target write, credential value read, global config repair,
  P1/P2, Provider binding, release and Standard adoption.

## 8. Truth boundary

```text
REMEDIATION_RECOMMENDATION != DECISION
EXPLICIT_DOCKER_HOST != PRODUCTION_RUNTIME_CONFIGURATION
METADATA_GUARD_PASS != ZERO_WRITE_PROOF
ANONYMOUS_PULL_PASS != SUPPLY_CHAIN_APPROVAL
PLATFORM_PASS != FORMAL_SECURITY_REVIEW
AGENT_REVIEW != HUMAN_REVIEW
ENVIRONMENT_REMEDIATION != TARGET_FIX
REFERENCE_IMPLEMENTATION != STANDARD
```
