# TITMAS Agent-Native Standards Community v1.1

中文：TITMAS 智能体原生标准社区 v1.1。

The only canonical machine entry is [`../../agent-index.json`](../../agent-index.json).
`llms.txt`, the human README and other manifests point to or project that entry;
they do not compete with it.

## Agent in 60 seconds

```bash
python3 TITMAS/agent-native/community_cli.py discover \
  --need "machine-readable evidence review"
python3 TITMAS/agent-native/community_cli.py rank \
  --need "bounded contribution handoff"
python3 TITMAS/conformance/harness.py
```

An agent joins only through an externally issued, bounded, expiring and revocable
participant record. A participant reference is not a DBOS Identity and does not
grant Permission.

## Community flow

```text
discover
  → check eligibility
  → request bounded claim
  → receive externally issued lease
  → prepare contribution package
  → independent review
  → revise or retain failure
  → candidate acceptance
  → handoff and reuse
  → calibrated recommendation or abstention
```

## Human exception path

Constitutional changes, Authority/Ownership changes, legal/privacy responsibility,
irreversible actions, public writes, Merge, Release, Deployment, major disputes
and emergency takeover go to the accountable Human or institutional authority.

## Current boundary

This directory contains Development contracts, deterministic local tooling and a
controlled synthetic pilot. It does not establish a public community or create an
Agent Runtime.

## Protocols and guides

- [Participant model](participants/participant-registry.json)
- [Task protocol](tasks/task-registry.json)
- [Contribution protocol](contributions/README.md)
- [Review protocol](reviews/review-protocol.json)
- [Maintenance protocol](maintenance/README.md)
- [Handoff protocol](handoff/README.md)
- [Recommendation protocol](recommendations/README.md)
- [Value gate](value-gate/README.md)
- [Human exception path](guides/human-exception-and-appeal-path.md)
