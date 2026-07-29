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
- Dormant GitHub templates: [`community/github-activation-templates/README.md`](community/github-activation-templates/README.md)
- Specification registry: [`specifications/registry.yaml`](specifications/registry.yaml)
- Conformance: [`conformance/README.md`](conformance/README.md)
- Reference implementation boundary: [`reference/README.md`](reference/README.md)
- Adapter entry: [`adapters/README.md`](adapters/README.md)
- Research archive index: [`research/agent-native-ecology-box-001/README.md`](research/agent-native-ecology-box-001/README.md)

## Local validation

From `digital-biosphere-architecture/`:

```bash
python3 TITMAS/conformance/harness.py
python3 -m unittest discover -s TITMAS/conformance/tests -v
python3 -m unittest discover -s TITMAS/agent-native/tests -v
python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
python3 TITMAS/reference/minimal-python/titmas_reference.py \
  TITMAS/reference/minimal-python/example-input.json
```

Conformance validates a bounded Development surface. A pass is not Truth,
Authorization, Adoption, Certification, Release or production readiness.

## Current state

```text
COMMUNITY_STATUS=CANONICAL_INTEGRATION_CANDIDATE
CODE_OF_CONDUCT_ADOPTED_FOR_INTEGRATION_CANDIDATE=true
SECURITY_PROCESS_DEFINED=true
SECURITY_TRANSPORT_ACTIVE=false
INTERIM_MAINTAINER_REF=zhangbin
INTERIM_ROLE_EXPIRES=2026-09-30T23:59:59+08:00
PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
PUBLIC_CONTRIBUTION_TEMPLATES_DEVELOPED=true
PUBLIC_CONTRIBUTION_TEMPLATES_INSTALLED=false
PUBLIC_CONTRIBUTION_SURFACE_ACTIVE=false
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
EXTERNAL_CONTRIBUTOR_COUNT=0
EXTERNAL_ADOPTER_COUNT=0
```

The temporary assignment is revocable and limited to this integration
candidate. It does not grant DBA, DBOS, SAEE, Evidence Truth, Certification,
Commercial, Release, automatic merge or Stable-promotion authority.

The contribution workflow is developed, but its GitHub templates are dormant
and not installed in `.github`. Public Issues or PRs are not an authorized
TITMAS contribution path. A future activation requires an active Security
Transport, a separate Human Decision and an independent Activation PR.

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
