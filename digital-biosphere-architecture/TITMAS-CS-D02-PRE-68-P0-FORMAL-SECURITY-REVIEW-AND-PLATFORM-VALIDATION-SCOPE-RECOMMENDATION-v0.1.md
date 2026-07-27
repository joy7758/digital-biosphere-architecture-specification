# TITMAS CS-D02 PRE-68 P0 Formal Security Review and Platform Validation Scope Recommendation v0.1

## 1. Recommendation

```text
DECISION_CANDIDATE=CS-D02-PRE-68
RECOMMENDATION=CONDITIONALLY_RECOMMENDED
EXACT_RECOMMENDED_ACTION=AUTHORIZE_TWO_PUBLIC_SAFE_AGENT_ASSISTED_STATIC_REVIEWS_AND_TWO_PINNED_NETWORK_DISABLED_LINUX_X86_64_VALIDATIONS_WITH_FORMAL_HUMAN_SECURITY_REVIEW_REMAINING_SEPARATE
PRIMARY_REPOSITORY=digital-biosphere-architecture
TARGET_REPOSITORY=joy7758/titmas-integrations
TARGET_COMMIT=0030077f29c37145a306b72e7083345eb76b504a
DECISION_RECORDED=false
EXECUTION_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

Recommend one bounded next action: after an independent Decision, collect two
public-safe agent-assisted static security reviews of the exact PRE-67 source
and run the unchanged offline suite in two pinned, network-disabled Linux
x86_64 environments. Treat both lanes as review inputs only. A named human
reviewer and a separate decision remain required before
`FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE` can become true.

This Recommendation does not authorize the proposed model requests, image
pulls, container execution, credential access, target changes, real DNS/TCP,
formal review, contract adoption, merge, release, or Provider claim.

Machine-readable scope:

- [`pre68-security-and-platform-scope.v0.1.json`](commercialization-standards-p0-security-and-platform-scope/pre68-security-and-platform-scope.v0.1.json)
- [`pre68-security-and-platform-scope.schema.v0.1.json`](commercialization-standards-p0-security-and-platform-scope/pre68-security-and-platform-scope.schema.v0.1.json)

```text
SCOPE_SHA256=c1706e8d6d4cca6f8dfe140096c0d41534370f6ed9e7398e388be5f34bb5b07d
SCOPE_SCHEMA_SHA256=f4ab489afd28d4a70cded04dd3a181e9517b44462808f078669fce5d7c5f9bdf
```

## 2. Why this is the recommended next step

PRE-65 provided the required pre-development agent consultation. Both distinct
Provider lanes returned `REVISE` / `CONDITIONAL`, primarily because the
deadline mechanism was not executable and DNS rebinding/continuity controls
were not proven.

PRE-67 corrected part of that gap:

- a bounded POSIX P0 reference implementation now exists;
- 92/92 offline tests and 7/7 independent-path cases pass locally and in a
  remote clean clone;
- selected-address continuity, bounded IPC, destination-policy rejection,
  child termination and negative boundaries have executable tests;
- the target records 0 real DNS, TCP, TLS, HTTP or credential reads during
  validation.

The project is now recommendable as a Development candidate for further
review. It is still not recommendable as a production-safe, cross-platform,
Provider-supported or Standard-ready component.

## 3. Why implementation should not advance directly

The current code uses `os.fork()` and executes Python operations in the child.
Python's current documentation states that:

- `fork()` is POSIX-only and unavailable or behaviorally different on several
  platforms;
- mixing `fork()` with threads has never been safe on POSIX, even when Python
  cannot detect every thread;
- macOS warns that `fork()` is unsafe when mixed with higher-level system APIs;
- TLS/OpenSSL state adds a separate multiprocessing concern.

Therefore `threading.active_count() == 1` is a useful fail-closed precondition,
not proof that no native or extension thread exists and not a formal fork-safety
argument.

The IANA special-purpose registries also state that a listed prefix is not
guaranteed routable in a particular context. Their `Destination` and
`Globally Reachable` fields are valid policy inputs, not network truth.

These unresolved issues make “keep implementing P1/P2 now” the wrong next
step. The correct next step is to decide whether the P0 mechanism should be
retained, revised or replaced based on bounded review evidence.

## 4. Exact review target

The target is immutable for PRE-68:

| Field | Exact value |
|---|---|
| Repository | `joy7758/titmas-integrations` |
| Branch | `codex/rb0-governance-baseline` |
| Commit | `0030077f29c37145a306b72e7083345eb76b504a` |
| `origin/main` | `e8eeccbf19e5e1d1f01ab9ad8796a53591a38dc8` |
| Public-safe inputs | 10 hash-bound files |
| Target writes | `0` |
| Test changes | `0` |
| Implementation changes | `0` |

Input drift, a different target commit, a model substitution, an unpinned
container manifest or a writable source mount must stop the execution.

## 5. Security review questions

The two advisory reviewers must answer the same sixteen questions:

| ID | Required review question |
|---|---|
| `SR-001` | Can the process prove that no Python, native or extension thread makes `fork()` unsafe? |
| `SR-002` | Are all child-side Python and libc operations defensible after `fork()`? |
| `SR-003` | Does the macOS high-level API warning require macOS rejection or mechanism replacement? |
| `SR-004` | Can inherited OpenSSL or TLS state affect P0 now or future P2 composition? |
| `SR-005` | Is inherited file-descriptor closure complete, bounded and resistant to resource exhaustion? |
| `SR-006` | Can clearing `os.environ` race, leak or corrupt parent/child state? |
| `SR-007` | Are timeout, kill, wait and reap paths complete for every child state? |
| `SR-008` | Are monotonic deadline and late-result semantics internally consistent without claiming an absolute bound? |
| `SR-009` | Can the pipe payload exceed, fragment, deadlock or bypass the 512-byte canonical boundary? |
| `SR-010` | Can hostname, numeric address, exception, credential or authorization data leak through observations or errors? |
| `SR-011` | Does first-address selection plus the destination policy fail closed for every IPv4/IPv6 class? |
| `SR-012` | Are policy snapshot provenance, update, stale-data and IANA non-routability semantics stated correctly? |
| `SR-013` | Are lowercase ASCII hostname and exact allowlist rules sufficient, including IDNA and trailing-dot cases? |
| `SR-014` | Are raw results, prefix matching, file limits, CPU time and memory use bounded against denial of service? |
| `SR-015` | Can signal handlers, audit hooks, subinterpreters or process state invalidate the child-safety assumptions? |
| `SR-016` | Does the transient binding actually prevent P1 re-resolution and preserve original-hostname P2 verification? |

Each reviewer must return one of:

```text
RETAIN
REVISE
REPLACE
REJECT
```

with findings, severity, directly affected symbols, proposed tests and explicit
non-claims. A transport/schema pass does not make the verdict favorable.

## 6. Advisory review lane

Exactly two sequential public-safe sessions are proposed:

1. `BAIDU_QIANFAN / ernie-4.5-turbo-20260402`
   as `IMPLEMENTATION_SECURITY_REVIEWER_CANDIDATE`;
2. `ALIBABA_CLOUD_MODEL_STUDIO / qwen3.7-plus`
   as `INDEPENDENT_SECURITY_REVIEWER_CANDIDATE`.

Both receive the same hash-bound public-safe package. No private path, secret
value, customer data, real endpoint, Agent instance, Runtime state, Evidence
truth or unpublished Provider material may enter a prompt.

The future execution cap is two model requests total:

```text
RETRY=0
FALLBACK=0
MODEL_SUBSTITUTION=0
RESPONSE_EXTRACTION_OR_REPAIR=0
FORMAL_REVIEW_CLAIM=false
```

The existing standing directive cannot itself execute these API/network
actions because the canonical standing record keeps API/runtime/network
resources behind a future exact packet and preserves
`automatic_gate_approval=false`.

## 7. Platform-validation lane

The unchanged source and tests are proposed for two exact Linux x86_64
observations:

| ID | Exact image | Linux/amd64 manifest digest |
|---|---|---|
| `PFM-LINUX-311` | `docker.io/library/python:3.11.15-slim-bookworm` | `sha256:28255a3ace7eb4c48bc1b57b90af29e1bc82b4fd6c60614a8e3dce61b87ff941` |
| `PFM-LINUX-314` | `docker.io/library/python:3.14.6-slim-bookworm` | `sha256:f70215e5dbe2a47dee6d23f9c6d358bf3c148f59cce2fd165b61118e9d80f2bb` |

The digest candidates were resolved through read-only public Docker registry
metadata during Recommendation preparation. No image was pulled or executed.
This metadata lookup is not platform validation.

Future execution must use:

```text
PLATFORM=linux/amd64
CONTAINER_NETWORK=none
SOURCE_MOUNT=read-only
DEPENDENCY_INSTALL=0
TARGET_WRITE=0
REAL_DNS_TCP_TLS_HTTP=0
```

For each environment:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
python3 -m unittest discover -s tests -v
```

The current 92/92 unit suite, 7/7 independent-path rehearsal, four machine
Schema pairs, nine declared hashes and two frozen IANA byte inputs must all
pass. Any unplanned warning, lingering child, modified source, cache write or
network use fails closed.

A Linux result is only an observation for that exact image, digest,
architecture and Python version. Two environments do not prove all Linux,
cross-platform support or production safety.

## 8. Formal human review boundary

```text
FORMAL_HUMAN_REVIEW_REQUIRED=true
HUMAN_REVIEWER_REF=null
HUMAN_REVIEWER_ASSIGNED=false
HUMAN_REVIEW_EXECUTION_AUTHORIZED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
```

Agent reviews and automated tests can produce review evidence. They cannot
take Human Security Accountability or approve their own findings. Until a
named reviewer is independently assigned and records a decision, the formal
review gate remains open.

If no qualified human reviewer is available, the truthful result is:

```text
AUTOMATED_AND_AGENT_REVIEW_INPUT_MAY_BE_COMPLETE
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
STANDARD_READY=false
```

## 9. Success and failure gates

The future bounded action passes only if:

1. both pinned Linux environments run the unchanged target;
2. both produce 92/92 tests and 7/7 rehearsal results;
3. all machine instances and hashes validate;
4. no test-subject network activity or target write occurs;
5. both exact agent sessions return direct Schema-valid responses;
6. all findings, including `REVISE`, `REPLACE` or `REJECT`, are retained;
7. the result explicitly keeps formal human review and Standard readiness
   false.

It fails closed on the first scope, hash, image, network, model, Schema,
authority or result-retention violation.

## 10. Required independent Decision

This Recommendation is canonical and exact, but not self-executing. The next
artifact, if the Human Program Authority chooses to proceed, must be an
independent Decision record that binds:

- the exact action string;
- the ten target input hashes;
- the two Provider/model/role bindings;
- the two image manifest digests;
- the network-disabled and read-only execution contract;
- request and image caps;
- stop conditions;
- result packet and rollback requirements;
- formal human review remaining separate.

No Decision may silently add real DNS/TCP/TLS, P1/P2, Provider binding, target
changes, formal-review completion, Standard adoption, merge, release or
commercial claims.

## 11. Primary review sources

The future reviewers must use these primary sources as review inputs, not as
evidence that the implementation conforms:

- Python `os.fork()` availability, thread and macOS warnings:
  <https://docs.python.org/3.14/library/os.html#os.fork>
- Python multiprocessing start-method and fork-safety guidance:
  <https://docs.python.org/3.14/library/multiprocessing.html#contexts-and-start-methods>
- Python TLS/OpenSSL multiprocessing warning:
  <https://docs.python.org/3.14/library/ssl.html#multi-processing>
- Python `socket.getaddrinfo()` system-dependent behavior:
  <https://docs.python.org/3.14/library/socket.html#socket.getaddrinfo>
- IANA IPv4 special-purpose registry:
  <https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml>
- IANA IPv6 special-purpose registry:
  <https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml>
- Docker Official Image metadata for Python:
  <https://hub.docker.com/_/python>

Source text may change. PRE-68 must record the observed version/date and must
not treat an external document as an implementation result.

## 12. Truth boundary

```text
RECOMMENDATION != DECISION
AGENT_REVIEW != FORMAL_HUMAN_SECURITY_REVIEW
PLATFORM_TEST != SECURITY_APPROVAL
LINUX_AMD64_OBSERVATION != ALL_LINUX_SUPPORT
NETWORK_NONE_TEST != REAL_NETWORK_CONFORMANCE
FORK_PREFLIGHT != NATIVE_THREAD_SAFETY_PROOF
IANA_POLICY_INPUT != ROUTABILITY_TRUTH
REFERENCE_IMPLEMENTATION != STANDARD
COMMIT != RELEASE
```
