# TITMAS Developer Standards Community

**Open trusted interoperability infrastructure for multi-agent systems.**

中文：**面向多智能体系统的开放可信互操作基础设施。**

TITMAS gives developers shared, testable interfaces for Identity References,
Boundary Declarations, Execution Evidence Bindings, Verification Results and
Evaluation Handoffs. It is not an Agent Runtime, executor, repository fixer,
certification authority or truth store.

## Developer entry

- [Start here](digital-biosphere-architecture/TITMAS/README.md)
- [Five-minute quickstart](digital-biosphere-architecture/TITMAS/QUICKSTART.md)
- [First contribution](digital-biosphere-architecture/TITMAS/FIRST_CONTRIBUTION.md)
- [Core Development proposal](digital-biosphere-architecture/TITMAS/specifications/proposals/titmas-core-developer-interoperability-surface-v0.1.md)
- [Conformance harness](digital-biosphere-architecture/TITMAS/conformance/README.md)
- [Minimal Python reference](digital-biosphere-architecture/TITMAS/reference/minimal-python/README.md)
- [DBA governance cockpit](digital-biosphere-architecture/README.md)

```bash
cd digital-biosphere-architecture
python3 TITMAS/conformance/harness.py
python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
```

## Current status

This branch prepares a public-launch-ready candidate. It does not launch a
community, publish a standard, create a Foundation, assign a Maintainer or
authorize a commercial offer, certification or Release.

```text
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
FOUNDATION_CREATED=false
COMMERCIAL_OFFER_AUTHORIZED=false
CERTIFICATION_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```
