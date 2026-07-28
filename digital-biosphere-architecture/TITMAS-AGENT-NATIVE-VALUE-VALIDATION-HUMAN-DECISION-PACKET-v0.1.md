# TITMAS Agent-Native Value Validation Human Decision Packet v0.1

本 Packet 仅为 Human Decision（人类决策）准备。所有项目均为 `UNDECIDED`；推荐意见不会
执行操作。每项只允许 `ACCEPT`、`REJECT` 或 `DEFER`，不得从其他 Decision 推导。

共同证据：

- [verified baseline](architecture/titmas-agent-native-value-validation-baseline-v0.1.md)；
- [framework](architecture/titmas-agent-native-value-validation-framework-v0.1.md)；
- [Ecology Box 001](architecture/titmas-agent-native-ecology-box-001-v0.1.md)；
- [metrics](architecture/titmas-agent-native-value-metrics-v0.1.md)。

## HD-VV-01 — Run formal Ecology Box 001

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=one matched ten-task low-risk internal experiment
prohibited_scope=real Git writes, external data, Authority changes, Release
term=one pre-registered batch
revocation=source drift, scope breach, privacy or comparability failure
required_evidence=frozen source, allocation, rubric, budget, reviewer and stop rules
```

## HD-VV-02 — Allow real agent candidate contribution

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=one unadopted contribution candidate inside an accepted experiment
prohibited_scope=merge, adoption, release, self-approval
term=one task lease
revocation=boundary breach or missing provenance
required_evidence=HD-VV-01 ACCEPT plus exact contribution scope
```

## HD-VV-03 — Allow bounded agent access to real Git

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=REJECT
scope=none in current v0.1 design
prohibited_scope=branch write, commit, push, Issue, PR, merge, tag, Release
term=until a future exact repository and path authorization
revocation=not applicable while rejected
required_evidence=clean-room write trial, rollback rehearsal, named effector and expiry
```

## HD-VV-04 — Allow public experiment report

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=public-safe methods, aggregate results, limitations and negative evidence
prohibited_scope=raw private prompts, credentials, adoption, standard-complete or value-proven claim
term=one reviewed version
revocation=privacy, provenance or claims defect
required_evidence=completed experiment, public-safe extraction review and owner approval
```

## HD-VV-05 — Enter commercial value validation

```text
decision=UNDECIDED
options=ACCEPT|REJECT|DEFER
recommended_disposition=DEFER
scope=future problem validation only
prohibited_scope=offer, customer data, certification, pricing, deployment
term=separate future gate
revocation=insufficient value evidence or unresolved risk
required_evidence=repeatable positive result across independent lineages and real low-risk scenarios
```

## Current decision state

```text
HUMAN_DECISIONS_RECORDED=0
ECOLOGY_BOX_EXECUTION_AUTHORIZED=false
REAL_AGENT_CONTRIBUTION_AUTHORIZED=false
REAL_GIT_ACCESS_AUTHORIZED=false
PUBLIC_EXPERIMENT_REPORT_AUTHORIZED=false
COMMERCIAL_VALUE_VALIDATION_AUTHORIZED=false
```

