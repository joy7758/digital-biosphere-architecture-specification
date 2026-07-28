# TITMAS Developer Standards Community

中文：TITMAS 可信多智能体基础设施开发者社区。

TITMAS provides open interoperability rules for identity references, boundary
declarations, execution-evidence bindings, verification-result references and
evaluation handoffs across multi-agent systems.

## Start in five minutes

```bash
cd digital-biosphere-architecture
python3 TITMAS/conformance/harness.py
python3 -m unittest discover -s TITMAS/conformance/tests -v
python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
python3 TITMAS/reference/minimal-python/titmas_reference.py \
  TITMAS/reference/minimal-python/example-input.json
```

## Choose one path

- [Understand the positioning](../architecture/titmas-developer-infrastructure-positioning-v1.0.md)
- [Read the first-contribution guide](community/CONTRIBUTING.md)
- [Propose a specification](specifications/templates/proposal.md)
- [Read the specification lifecycle](specifications/lifecycle.md)
- [Run conformance tests](conformance/README.md)
- [Run the minimal reference](reference/minimal-python/README.md)
- [Prepare an Adapter](adapters/README.md)
- [Pick a Starter Task](community/STARTER_TASKS.md)
- [Read the launch-readiness assessment](../architecture/titmas-developer-standard-community-launch-readiness-v1.0.md)
- [Read the completion report](../TITMAS-DEVELOPER-STANDARD-COMMUNITY-COMPLETION-REPORT-v1.0.md)
- [Review the Human Owner decision packet](../TITMAS-DEVELOPER-STANDARD-COMMUNITY-HUMAN-OWNER-DECISION-PACKET-v1.0.md)

## Current maturity

This is an internal public-launch-ready candidate. The infrastructure can be
reviewed and executed locally, but public contribution, community launch,
maintainer assignment, release, certification and commercial offering remain
closed.

```text
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
MAINTAINER_ASSIGNED=false
EXTERNAL_CONTRIBUTOR_COUNT=0
EXTERNAL_ADOPTER_COUNT=0
CERTIFICATION_AUTHORIZED=false
```

## Prohibited claims

- A passing fixture is not Truth, Authorization, Adoption or Certification.
- The reference implementation is not the standard authority.
- Experimental material is not Stable.
- TITMAS is not an Agent Runtime, executor, repository fixer or central control plane.
