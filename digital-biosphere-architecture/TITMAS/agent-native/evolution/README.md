# TITMAS Bounded Discovery and Evolution Layer v2.1

中文：TITMAS 有界发现、自愈与进化层 v2.1。

This directory is the canonical machine-contract surface for D19. It defines
how bounded agents may discover problems, preserve evidence, generate repair
variants, evaluate fitness, request authorization, retain outcomes and record
lineage. It is not a Runtime, executor, semantic owner, truth store or
certification authority.

## Machine entry

- Policy: [`evolution-policy.json`](evolution-policy.json)
- State machine: [`evolution-state-machine.json`](evolution-state-machine.json)
- Risk classes: [`risk-classification.json`](risk-classification.json)
- Fitness: [`fitness-profile.json`](fitness-profile.json)
- ER-1 registry: [`self-healing-registry.json`](self-healing-registry.json)
- Capability and role boundary: [`evolution-capability.json`](evolution-capability.json)
- Canonical owner routing: [`canonical-owner-map.json`](canonical-owner-map.json)
- Retry and mutation limits: [`mutation-limits.json`](mutation-limits.json)
- Object schemas: [`schemas/`](schemas/)
- Deterministic ER-1 demo: [`demo/README.md`](demo/README.md)

## Object reuse boundary

| Existing object | Existing owner / surface | D19 treatment |
|---|---|---|
| Observation | source runtime, adapter or observation producer | referenced, never relabelled as Evidence |
| Evidence Object | DBOS / admitted Evidence contract | referenced, never duplicated |
| Matching Assessment | agent-native task and recommendation surfaces | reused for scoped matching |
| Approval / Authorization | Human Decision and authority registry | referenced; discovery never self-issues |
| Action / Receipt | canonical execution and Receipt owners | referenced; mutation metadata is not a second Receipt |
| Outcome Evidence | admitted Evidence with outcome scope | referenced by lineage |
| Verification | DBOS / conformance surface | consumed, never elevated to Authorization |
| Evaluation | SAEE and bounded fitness profiles | advisory input, never activation authority |

The new schemas cover only semantics that were absent: problem evidence,
evolution proposal, patch variant, fitness evaluation, selection record,
evolution lineage and rollback evidence.

## Local validation

```bash
python3 -m unittest discover \
  -s TITMAS/agent-native/tests \
  -p 'test_evolution.py' \
  -v
python3 TITMAS/agent-native/evolution/evolution.py demo \
  --output /tmp/titmas-d19-evolution-demo
```

Expected D19 result:

```text
EVOLUTION_TESTS=25/25_PASS
SCHEMA_VALIDATION=PASS
DETERMINISTIC_REPLAY=PASS
```

The reference demo operates only on synthetic fixture copies. It does not
change canonical `main`, a live runtime, production data, credentials or
P0-10.
