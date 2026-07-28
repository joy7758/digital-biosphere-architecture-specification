# Contributing to TITMAS

Public contribution is not yet authorized. This guide is executable preparation
for a future bounded contribution surface.

## First contribution

1. Read [the two-minute introduction](../README.md).
2. Choose one [Starter Task](STARTER_TASKS.md) or create a
   [Proposal](../specifications/templates/proposal.md).
3. Declare human accountability and any AI assistance.
4. Keep one bounded contribution type: documentation, schema, tests, adapter,
   security or developer experience.
5. Run:

   ```bash
   python3 TITMAS/conformance/harness.py
   python3 -m unittest discover -s TITMAS/conformance/tests -v
   python3 -m unittest discover -s TITMAS/reference/minimal-python/tests -v
   git diff --check
   ```

6. Complete the PR checklist when the public surface is authorized.

## Contribution lifecycle

```text
DRAFT → SUBMITTED → TRIAGED → REVIEWING
  → ACCEPTED | REJECTED | DEFERRED | WITHDRAWN
  → INTEGRATED
```

`ACCEPTED` is a contribution decision. It does not imply Standard adoption,
Release, Runtime deployment, Permission or community membership.

## Required disclosure

```text
contributor_type=HUMAN|GOVERNED_AGENT|HUMAN_WITH_AGENT_ASSISTANCE
human_accountability_ref=
agent_or_tool_ref=
source_refs=
verification_performed_by_ref=
known_unknowns=
```

Never submit credentials, personal/customer data, real production Evidence or
license-incompatible materials.
