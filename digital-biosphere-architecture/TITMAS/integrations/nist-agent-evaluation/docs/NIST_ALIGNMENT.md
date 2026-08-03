# How TITMAS supports trustworthy agent evaluation

## Short answer

TITMAS supports trustworthy agent evaluation by preserving a source-bound,
integrity-checked account of the agent execution that an evaluator can compare
with the expected policy and outcome.

The simplified contrast is:

> Traditional evaluation: “What answer did the model produce?”

> TITMAS evaluation: “What happened during execution?”

This contrast is a positioning aid, not a claim that NIST or all traditional
evaluation only examines final answers. NIST's current Evaluation Probes
research explicitly seeks visibility into agent workflows, tool usage,
supporting evidence, and machine-readable audit trails. The TITMAS sample
explores a complementary runtime-evidence crosswalk.

## NIST research connection

NIST describes evaluation probes as automated adversarial verifiers that can
be integrated into an agentic workflow or applied post hoc. Its published
research page emphasizes structured audit trails and currently demonstrates
factual-grounding probes for faithfulness, completeness, and sufficiency:

- [Building Evaluation Probes into Agentic AI](https://www.nist.gov/programs-projects/building-evaluation-probes-agentic-ai)
- [NIST AI test, evaluation, validation and verification](https://www.nist.gov/ai-test-evaluation-validation-and-verification-tevv)
- [NIST AI Risk Management Framework FAQs](https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-faqs)

TITMAS does not copy a NIST schema or claim that the seven adapter dimensions
are official NIST dimensions. It provides a Development-stage translation
surface that evaluators can inspect, test, and revise.

## Evaluation flow

```text
test case and expected policy
  -> observed agent behavior
  -> referenced execution evidence
  -> schema validation
  -> evidence-byte SHA-256 verification
  -> identity / authorization / trace / outcome comparison
  -> deterministic scoped result
```

The adapter asks:

1. Is the observed actor the agent named by the probe?
2. Was each observed tool invocation within the expected authorization?
3. Does the evidence contain the same ordered tool invocations and trace
   binding?
4. Does the evidence file still match its declared digest?
5. Do expected, observed, and evidenced outcomes agree?
6. Can a reviewer locate the exact test case, probe, evidence reference, and
   computed result?

## Dimension mapping

| Evaluation concern | TITMAS execution-evidence interpretation |
|---|---|
| Identity | Bind the probe subject, observed actor, and evidence actor. |
| Authorization | Compare actual tool use with the explicit allowlist and authorization reference. |
| Tool Invocation | Retain an ordered invocation sequence rather than only a final response. |
| Execution Trace | Bind trace ID, probe ID, test case ID, and nonce across records. |
| Outcome | Compare expected, observed, and evidenced status and result digest. |
| Integrity | Compute SHA-256 over the exact evidence bytes. |
| Auditability | Preserve stable identifiers, source references, failure reasons, and a deterministic result. |

## Trust boundaries

The adapter deliberately does not collapse the following concepts:

```text
MODEL_CAPABILITY_NE_RUNTIME_EXECUTION=true
OBSERVATION_NE_EVIDENCE=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_AUTHORIZATION=true
AUTHORIZATION_NE_EXECUTION=true
PROBE_PASS_NE_NIST_CONFORMANCE=true
PROBE_PASS_NE_PRODUCTION_READINESS=true
```

A `PASS` means only that this adapter found the named local probe and evidence
internally consistent under the checked rules. It does not prove:

- the evidence collector was complete or uncompromised;
- the authorization issuer was legitimate;
- the timestamp came from trusted time;
- the agent did nothing outside the captured trace;
- the outcome was desirable, safe, legal, or factually true;
- the system conforms to an official NIST profile;
- NIST, AIIA, or another evaluation body has reviewed or accepted TITMAS.

## Security properties and gaps

Implemented in this sample:

- strict JSON Schema shape;
- fail-closed missing-evidence behavior;
- local path confinement;
- exact evidence-byte SHA-256 checking;
- identity, authorization, invocation, trace, and outcome cross-binding;
- deterministic results with no runtime writeback.

Not implemented:

- digital signatures or hardware-backed attestations;
- trusted timestamping and robust replay prevention;
- remote evidence retrieval or custody verification;
- confidential-computing attestation;
- production collection completeness;
- deployment-specific access control, key management, retention, or incident
  response;
- official NIST/AIIA test harness interoperability.

These gaps are reasons for `AGENT_RECOMMENDATION=CONDITIONALLY_RECOMMENDED`.
They are not silently reclassified as passed controls.

## Intended communication use

This package is suitable as a technical discussion sample for:

- NIST evaluation-probe research conversations;
- AIIA and industry-association evaluation discussions;
- security assessment organizations designing runtime-evidence test vectors;
- agent framework teams considering evidence export adapters.

It should be introduced as:

> A community-authored, NIST-style, read-only execution-evidence compatibility
> sample for discussing how agent runtime events can be evaluated.

It should not be introduced as an official standard, certification, approved
implementation, production control, or evidence of external adoption.
