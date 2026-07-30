# Technical input: Runtime execution evidence as an additional probe dimension

> Draft only. Do not submit without human confirmation and replacement of the
> public-reference placeholder below.

## Context

NIST's “Building Evaluation Probes into Agentic AI” project provides a useful
measurement framing: automated probes can act as adversarial verifiers during
an agentic workflow or as post-hoc evaluations, and their structured verdicts
can accumulate into a machine-readable audit trail. The current demonstrator's
faithfulness, completeness, and sufficiency probes make factual-grounding
claims inspectable rather than relying on “the AI said so.”

This input asks a related scope question. In addition to evaluating whether an
agent's output is grounded in source material, could a probe evaluate whether a
claimed runtime action is supported by bounded execution evidence?

The question is motivated by agents that use tools, APIs, repositories,
databases, or domain systems. Their final answer may be plausible and even
factually grounded while the actual execution differs from the expected or
authorized behavior. This input is not a proposal to replace output-focused
probes, and it does not assume that the current demonstrator should become an
enforcement or control system.

## Measurement Gap

Consider an agent that reports: “I queried the approved database, applied the
requested transformation, and stored the result.” Output evaluation can assess
the factual quality of the response or whether cited material supports it. A
different set of questions concerns the execution itself:

- Was the named tool actually invoked?
- Was that invocation within the allowed tool set and bound to the expected
  authorization reference?
- Is required execution evidence present?
- Does the retained evidence still have the same bytes?
- Do the expected, observed, and evidenced outcomes agree?

Without an execution-evidence measurement, an evaluator may be unable to
distinguish a successful authorized action from an unauthorized call, a
missing record, a changed record, or a result that contradicts the retained
trace. These are not necessarily model-capability failures. They are runtime
consistency and evidence-integrity failures.

This gap is intentionally bounded. A matching hash does not prove that a
collector observed all activity. An authorization reference does not prove
that its issuer was legitimate. A consistent outcome does not prove that the
outcome was safe, legal, correct, or desirable. The proposed measurement
should report only the checks it actually performed.

## Proposed Extension

One possible additional dimension is **Runtime Execution Evidence
Consistency**. A probe would compare:

1. a test case describing the expected policy and outcome;
2. observed runtime behavior, including actor, trace, ordered tool invocations,
   and outcome;
3. a source-bound execution-evidence artifact; and
4. deterministic integrity and cross-binding checks.

For a small reference sample, the checks are decomposed into identity,
authorization, tool invocation, execution trace, outcome, integrity, and
auditability. These labels are community-authored and are not presented as an
official NIST taxonomy.

The result is a scoped verdict such as `PASS`,
`FAIL_UNAUTHORIZED_TOOL_CALL`, `FAIL_MISSING_EVIDENCE`,
`FAIL_EVIDENCE_TAMPERING`, or `FAIL_OUTCOME_MISMATCH`. A `PASS` means only that
the supplied record and evidence are internally consistent under the checked
rules. It is not a trust score, certification, authorization, or production
readiness decision.

This appears compatible with the project's extensible probe concept because it
can be implemented as an independent rubric/check without changing the
existing factual-grounding dimensions. It could run immediately after a tool
action or post hoc over retained records.

## Example Failure Cases

**Unauthorized tool invocation.** The test case allows `records.read`, but the
observed trace or evidence contains `shell.exec`, or the invocation carries a
different authorization reference. The probe fails even if the agent's final
answer appears correct.

**Execution missing evidence.** The test case requires execution evidence, but
the reference is missing or the artifact cannot be located. The probe does not
infer success from the agent's narrative or from an expected result field.

**Evidence tampering.** The evidence file exists, but a digest computed over
its exact bytes differs from the declared SHA-256 value. The probe reports an
integrity failure before trusting the evidence content.

**Outcome mismatch.** The expected behavior reports success, while the
observed behavior or evidence reports failure or a different result digest.
The probe retains the inconsistency instead of selecting whichever value is
most favorable.

Positive and negative test vectors are useful here because each failure can be
reproduced without access to a production agent, private data, or a live tool.

## Machine-readable Evidence

A minimal probe record can require seven top-level fields:

```text
probe_id
agent_id
test_case
expected_behavior
observed_behavior
evidence_reference
verification_result
```

The expected behavior contains an allowed-tool set, authorization reference,
required-evidence flag, and expected outcome. The observed behavior contains
the actor, trace, timestamps, ordered tool invocations, and observed outcome.
The evidence reference contains presence status, a local or otherwise governed
URI, media type, and digest.

The input `verification_result` is useful as an expected assertion in a test
vector, but a verifier should recompute its own result and must not accept that
field as self-attestation. A structured output should also include the
dimensions checked and concrete failure reasons so that a reviewer can
reproduce and challenge the result.

## Reference Implementation

A Development-stage, read-only TITMAS sample has been prepared with a strict
JSON Schema, four synthetic cases, local evidence artifacts, a deterministic
Python validator, and pytest coverage. It does not call tools, collect
production evidence, write back to an agent runtime, or grant authority.

Public reference:

```text
PUBLIC_REFERENCE_URL_TO_BE_ADDED_AFTER_PUBLICATION
```

The source repository is currently private. This draft should not be submitted
until the placeholder is replaced with an anonymously accessible,
commit-bound reference and the final package has passed secret and overclaim
review.

## Questions for NIST Team

1. Is runtime execution evidence consistency within the intended scope of the
   evaluation-probe research, or is the near-term scope deliberately limited to
   factual grounding and citation quality?
2. Would NIST view this as a separate probe dimension, an input to the
   structured audit trail, or a concern better handled by another TEVV
   mechanism?
3. Which minimum provenance fields would be useful for a portable runtime
   evidence record without turning the probe into an authorization or control
   plane?
4. How should a probe represent `UNKNOWN` when evidence capture completeness
   cannot be established?
5. Would deterministic negative test vectors for unauthorized calls, missing
   evidence, changed evidence, and outcome mismatch be useful alongside
   model-judge-based probes?

## Scope and Limitations

This input is NIST-style and development-stage. It does not claim NIST
endorsement, certification, formal compatibility, conformance, or adoption. It
does not propose a NIST standard, request that NIST merge the sample, or
represent that NIST uses the seven labels above.

The sample uses synthetic data only. SHA-256 detects byte changes but is not a
signature, trusted timestamp, custody chain, or non-repudiation mechanism. The
sample does not prove evidence-capture completeness, activity outside the
recorded trace, authorization-issuer legitimacy, domain safety, legal
compliance, or production suitability. No official NIST harness
interoperability has been tested.

There is also an existing open issue, “Measurement scope vs execution
conditions in agentic systems” (#1), that raises operational context and
execution trace as first-class measurement elements. This input is narrower:
it supplies concrete, machine-readable negative cases for authorization,
evidence presence, byte integrity, and outcome consistency. To avoid
duplication, a comment on #1 may be more appropriate than a new issue unless
the NIST team prefers a separate reproducible example.

## AI Assistance Disclosure

This draft and the reference sample were prepared with AI assistance from
OpenAI Codex and Alibaba Cloud Qwen models under human direction. AI-generated
content was reviewed against the public NIST project page, official repository,
local tests, source-bound repository metadata, and explicit non-claim
boundaries. A human remains accountable for the final text and any external
submission. No AI agent has submitted this Issue, comment, pull request, or
email to NIST.
