# TITMAS Agent-Native Standards Community

中文：TITMAS 智能体原生标准社区。

> Agent-Native Open Standards Community for Trusted Multi-Agent Infrastructure

TITMAS develops machine-readable open specifications, conformance assets,
reference boundaries and contribution protocols for trustworthy multi-agent
infrastructure. It is not an Agent Framework, Agent Platform, Runtime,
executor, certification authority or central control plane.

The compatibility names **TITMAS Developer Standards Community** and
**TITMAS Infrastructure Developer Community** remain valid human-facing
aliases. No fourth community name is created.

## Start here

- Agent entry: [`../agent-index.json`](../agent-index.json)
- Machine status: [`community/community-status.json`](community/community-status.json)
- Human quick start: [`QUICKSTART.md`](QUICKSTART.md)
- First contribution: [`FIRST_CONTRIBUTION.md`](FIRST_CONTRIBUTION.md)
- Contribution policy: [`community/CONTRIBUTING.md`](community/CONTRIBUTING.md)
- GitHub activation package: [`community/github-activation-templates/README.md`](community/github-activation-templates/README.md)
- Specification registry: [`specifications/registry.yaml`](specifications/registry.yaml)
- Conformance: [`conformance/README.md`](conformance/README.md)
- Reference implementation boundary: [`reference/README.md`](reference/README.md)
- Adapter entry: [`adapters/README.md`](adapters/README.md)
- Research archive index: [`research/agent-native-ecology-box-001/README.md`](research/agent-native-ecology-box-001/README.md)
- Private commercialization boundary:
  [`private-governance/source-classification-registry.json`](private-governance/source-classification-registry.json)
- Private Agent customer evaluation candidate:
  [`private-customer-evaluation/README.md`](private-customer-evaluation/README.md)
- Private Stage 5 standards contribution preview:
  [`private-stage5-pilot/README.md`](private-stage5-pilot/README.md)
- Private Stage 5 protocol surface:
  [`private-stage5-protocol-surface/README.md`](private-stage5-protocol-surface/README.md)
- Minimal private Stage 5 Python SDK:
  [`private-stage5-sdk/python/README.md`](private-stage5-sdk/python/README.md)

## Local validation

From `digital-biosphere-architecture/`:

```bash
python3 TITMAS/conformance/harness.py
python3 -m unittest discover -s TITMAS/conformance/tests -v
python3 -m unittest discover -s TITMAS/agent-native/tests -v
python3 -m unittest discover \
  -s TITMAS/private-customer-evaluation/gateway/tests -p 'test_*.py' -v
python3 -m unittest discover \
  -s TITMAS/private-stage5-sdk/python/tests -p 'test_*.py' -v
python3 -m unittest discover \
  -s TITMAS/private-stage5-pilot/tests -p 'test_*.py' -v
python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
python3 TITMAS/reference/minimal-python/titmas_reference.py \
  TITMAS/reference/minimal-python/example-input.json
```

Conformance validates a bounded Development surface. A pass is not Truth,
Authorization, Adoption, Certification, Release or production readiness.

## Current state

```text
COMMUNITY_STATUS=PRIVATE_COMMERCIALIZATION_BOUNDARY
CORE_REPOSITORY_VISIBILITY=PRIVATE
PRIVATE_CORE_IS_CANONICAL=true
CODE_OF_CONDUCT_HISTORICAL_ADOPTION_RETAINED=true
SECURITY_PROCESS_DEFINED=true
SECURITY_TRANSPORT_ACTIVE=false
SECURITY_TRANSPORT_VERIFIED=false
INTERIM_MAINTAINER_REF=zhangbin
INTERIM_ROLE_EXPIRES=2026-09-30T23:59:59+08:00
PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
PUBLIC_CONTRIBUTION_TEMPLATES_DEVELOPED=true
PUBLIC_CONTRIBUTION_TEMPLATES_INSTALLED=true
PUBLIC_CONTRIBUTION_SURFACE_ACTIVE=false
PUBLIC_LAUNCH_AUTHORIZED=false
PUBLIC_LAUNCH_MODE=PRIVATE_COMMERCIALIZATION_BOUNDARY
OPEN_STANDARDS_COMMUNITY_INFRASTRUCTURE_DEVELOPED=true
OPEN_STANDARDS_COMMUNITY_OPERATION_ACTIVE=false
PRIVATE_AGENT_CUSTOMER_READINESS_ACTIVE=true
PRIVATE_STAGE5_CONTRIBUTION_INFRASTRUCTURE_READY=true
PRIVATE_STAGE5_PROGRAMMATIC_PILOT_PASS=true
PRIVATE_STAGE5_REAL_MODEL_CALL_COUNT=0
PRIVATE_STAGE5_HUMAN_DISPOSITION_REQUIRED=true
COMMUNITY_ESTABLISHED=false
EXTERNAL_CONTRIBUTOR_COUNT=0
EXTERNAL_ADOPTER_COUNT=0
```

The temporary assignment is revocable and limited to this integration
candidate. It does not grant DBA, DBOS, SAEE, Evidence Truth, Certification,
Commercial, Release, automatic merge or Stable-promotion authority.

The community core, PR #41, Activation PR #42, entry-repair PR #45 and Welcome
Issue #43 remain historical facts. The current repository is private; public
Issue/PR operation and public Security Transport are not active. The historical
public phase is not erased, and it does not authorize a new public export,
Release, Stable promotion or external Authority.

## Core boundaries

```text
SPECIFICATION_NE_IMPLEMENTATION=true
REFERENCE_IMPLEMENTATION_NE_STANDARD_AUTHORITY=true
CONFORMANCE_PASS_NE_ADOPTION=true
COMMUNITY_REVIEW_NE_ARCHITECTURE_DECISION=true
AGENT_REVIEW_NE_HUMAN_AUTHORITY=true
EVIDENCE_NE_TRUTH=true
VERIFICATION_NE_AUTHORIZATION=true
AGENT_NATIVE_NE_AUTONOMOUS_AUTHORITY=true
```

Ecology Box, Operational Calibration and Candidate Grounding remain supporting
validation. Only the generalized, local contribution-grounding controls are
present in the community conformance surface; experiment runners, raw run
assets and Calibration v0.3 are excluded.
