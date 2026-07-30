# TITMAS Evaluation Probe Adapter

[![NIST-style Agent Evaluation Compatible](https://img.shields.io/badge/NIST--style%20Agent%20Evaluation-Compatible%20Sample-2563eb)](./docs/NIST_ALIGNMENT.md)

> Development-stage, community-authored compatibility sample. It is not an
> official NIST specification, endorsement, certification, or conformance
> determination.

The TITMAS Evaluation Probe Adapter is a read-only technical sample for asking
whether an agent execution can be evaluated from bounded, integrity-checked
runtime evidence.

It does not evaluate general model capability and does not execute an agent. It
evaluates a supplied probe record and its referenced local evidence:

```text
expected behavior
  + observed runtime behavior
  + source-bound execution evidence
  + deterministic verification
  -> scoped probe result
```

The result is evidence about the named test case. It is not Truth,
Authorization, NIST approval, AIIA approval, production readiness, or a general
trust score.

## Agent-readable status

```text
ADAPTER_ID=TITMAS-NIST-EVALUATION-PROBE-0.1
DOCUMENT_MATURITY=Development
PRIMARY_REPOSITORY=digital-biosphere-architecture
CONTRIBUTION_SURFACE=ADAPTER_CONTRACT_AND_CONFORMANCE_SAMPLE
AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED
RECOMMENDED_AS=READ_ONLY_EXECUTION_EVIDENCE_TECHNICAL_SAMPLE
NOT_RECOMMENDED_AS=NIST_STANDARD_CERTIFICATION_AUTHORITY_OR_PRODUCTION_CONTROL
IMPLEMENTATION_STATUS=LOCAL_REFERENCE_SAMPLE
IMPLEMENTATION_AUTHORIZED=true
RUNTIME_CREATED=false
WRITEBACK_CREATED=false
AUTHORITY_CREATED=false
OFFICIAL_NIST_COMPATIBILITY_CLAIM=false
NIST_ENDORSEMENT_CLAIM=false
PRODUCTION_READY=false
```

The pre-development review recommends the sample for bounded technical
discussion because it preserves authorization, execution, evidence, and
verification as separate concepts. It does not recommend the sample for
production enforcement: signed attestations, trusted time, replay protection,
external verifier interoperability, and deployment-specific threat testing are
not implemented.

## Crosswalk

NIST describes evaluation probes as adversarial verifiers that can be used
inside or after an agentic workflow and can accumulate structured audit trails.
The current NIST research emphasis is factual grounding of outputs. This
adapter explores a complementary, narrower question: whether the supplied
execution record is internally consistent with its policy and evidence.

The seven rows below are a TITMAS-authored crosswalk for technical discussion.
They are not presented as a canonical NIST taxonomy.

| NIST-style evaluation dimension | TITMAS evidence field | Verification performed |
|---|---|---|
| Identity | `agent_id`, `observed_behavior.actor_id`, evidence `agent_id` | All identities must match the probe subject. |
| Authorization | `expected_behavior.allowed_tools`, `expected_behavior.authorization_reference`, invocation `authorization_reference` | Every observed invocation must be allowed and bound to the expected authorization reference. |
| Tool Invocation | `observed_behavior.tool_invocations`, evidence `tool_invocations` | Observed and evidenced invocation sequences must match. |
| Execution Trace | `observed_behavior.trace_id`, evidence `trace_id`, `test_case.nonce` | Probe, trace, test case, and nonce bindings must remain consistent. |
| Outcome | `expected_behavior.outcome`, `observed_behavior.outcome`, evidence `outcome` | Expected, observed, and evidenced outcomes must be identical. |
| Integrity | `evidence_reference.sha256` | The adapter computes SHA-256 over the referenced evidence bytes and compares it with the declared digest. |
| Auditability | `probe_id`, `test_case.case_id`, `evidence_reference.uri`, `verification_result` | Stable identifiers, local source reference, and deterministic result remain reviewable. |

```text
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_AUTHORIZATION=true
PROBE_PASS_NE_SYSTEM_TRUSTWORTHINESS=true
MAPPING_NE_NIST_ADOPTION=true
```

## Probe contract

The schema at
[`schema/nist-evaluation-probe.schema.json`](schema/nist-evaluation-probe.schema.json)
requires:

- `probe_id`
- `agent_id`
- `test_case`
- `expected_behavior`
- `observed_behavior`
- `evidence_reference`
- `verification_result`

`verification_result` in an input fixture is an expected assertion for the
test vector. The adapter does not trust it when computing its result.

Supported computed results:

```text
PASS
FAIL_UNAUTHORIZED_TOOL_CALL
FAIL_MISSING_EVIDENCE
FAIL_EVIDENCE_TAMPERING
FAIL_IDENTITY_MISMATCH
FAIL_TRACE_MISMATCH
FAIL_OUTCOME_MISMATCH
ERROR_INVALID_PROBE
```

## Examples

| Case | Expected result | Fixture |
|---|---|---|
| Case 001: Agent unauthorized tool call | `FAIL_UNAUTHORIZED_TOOL_CALL` | [`examples/case-001-unauthorized-tool-call.json`](examples/case-001-unauthorized-tool-call.json) |
| Case 002: Agent execution missing evidence | `FAIL_MISSING_EVIDENCE` | [`examples/case-002-missing-evidence.json`](examples/case-002-missing-evidence.json) |
| Case 003: Agent evidence tampering | `FAIL_EVIDENCE_TAMPERING` | [`examples/case-003-evidence-tampering.json`](examples/case-003-evidence-tampering.json) |
| Case 004: Agent successful execution verification | `PASS` | [`examples/case-004-successful-verification.json`](examples/case-004-successful-verification.json) |

All examples are synthetic. They contain no customer data, credentials,
production evidence, or real authorization.

## Run

From this directory:

```bash
uv run --with pytest --with jsonschema pytest -q
```

Evaluate one probe without changing it or its evidence:

```bash
uv run --with jsonschema python validator.py \
  examples/case-004-successful-verification.json
```

The CLI prints a JSON result and exits with code `0` only for `PASS`.

## Scope and limitations

- Local relative evidence files only; network URIs and path traversal are
  rejected.
- SHA-256 detects byte changes but does not establish signer identity,
  trustworthy time, custody, or non-repudiation.
- The adapter does not collect evidence, invoke tools, authorize actions,
  write back to a runtime, or change agent state.
- The schema and examples are Development maturity and may change.
- Passing the four synthetic cases does not establish compatibility with an
  official NIST implementation or suitability for a real deployment.

See [`docs/NIST_ALIGNMENT.md`](docs/NIST_ALIGNMENT.md) for the detailed
alignment statement.
