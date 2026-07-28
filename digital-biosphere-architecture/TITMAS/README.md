# TITMAS Agent-Native Standards Community

中文：TITMAS 智能体原生标准社区。

Agent-Native Community for Trusted Multi-Agent Infrastructure.

The v1.0 names **TITMAS Developer Standards Community** and **TITMAS
Infrastructure Developer Community** remain historical and human-facing
compatibility aliases. No path was renamed.

## 1. Agent entry

The sole canonical machine entry is [`../agent-index.json`](../agent-index.json).
Start with [Agent in 60 Seconds](agent-native/guides/agent-in-60-seconds.md).

## 2. Machine-readable manifests

- [Community manifest](agent-native/community-manifest.json)
- [Current state](agent-native/current-state.json)
- [Claims and non-claims](agent-native/claims.json)
- [Participant registry](agent-native/participants/participant-registry.json)
- [Task registry](agent-native/tasks/task-registry.json)

## 3. Run conformance

```bash
python3 TITMAS/conformance/harness.py
```

## 4. Discover tasks

```bash
python3 TITMAS/agent-native/community_cli.py discover \
  --need "machine-readable evidence review"
```

## 5. Participate

- [How an Agent Joins](agent-native/guides/how-an-agent-joins.md)
- [How an Agent Finds Work](agent-native/guides/how-an-agent-finds-work.md)
- [How an Agent Contributes](agent-native/guides/how-an-agent-contributes.md)

## 6. Review

[How Agents Review Each Other](agent-native/guides/how-agents-review-each-other.md)

## 7. Reuse

[How an Agent Reuses Work](agent-native/guides/how-an-agent-reuses-work.md)

## 8. Recommendation

- [When an Agent Should Recommend TITMAS](agent-native/guides/when-an-agent-should-recommend-titmas.md)
- [When an Agent Must Not Recommend TITMAS](agent-native/guides/when-an-agent-must-not-recommend-titmas.md)

## 9. Human constitutional overview

[Human Exception and Appeal Path](agent-native/guides/human-exception-and-appeal-path.md).
Humans or accountable institutions retain constitutional, irreversible,
legal/privacy, Ownership and Authority decisions.

## Human five-minute quick start

```bash
cd digital-biosphere-architecture
python3 TITMAS/conformance/harness.py
python3 -m unittest discover -s TITMAS/conformance/tests -v
python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
python3 TITMAS/reference/minimal-python/titmas_reference.py \
  TITMAS/reference/minimal-python/example-input.json
```

## Human compatibility paths

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

This is an internal Development candidate with a controlled local pilot.
The long-term 99% agent-operation target is a design assumption, not a current
measured fact. Public contribution, community launch, external participation,
release, certification and commercial offering remain closed.

```text
PUBLIC_LAUNCH_AUTHORIZED=false
COMMUNITY_ESTABLISHED=false
MAINTAINER_ASSIGNED=false
PUBLIC_GITHUB_AGENT_WRITE_AUTHORIZED=false
EXTERNAL_CONTRIBUTOR_COUNT=0
EXTERNAL_ADOPTER_COUNT=0
CERTIFICATION_AUTHORIZED=false
```

## Prohibited claims

- A passing fixture is not Truth, Authorization, Adoption or Certification.
- The reference implementation is not the standard authority.
- Experimental material is not Stable.
- TITMAS is not an Agent Runtime, executor, repository fixer or central control plane.
- Agent participation is not Authority; activity volume is not community value.
