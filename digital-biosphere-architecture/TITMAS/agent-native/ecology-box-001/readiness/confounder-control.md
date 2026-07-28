# Ecology Box 001 Confounder Control v0.1

## Matched controls

Both arms use the same frozen source revision, ten-task set, task-specific
inputs, output requirements, rubric, time/revision/review ceilings, local
validation classes and final blind evaluation.

Potential residual confounders must be reported:

- participant prior familiarity;
- Human tool fluency and model/provider prior training;
- modality-specific resource differences;
- failed or repeated Provider calls;
- unequal Human clarification;
- unplanned sensing, memory or recommendation assistance.

## Agent Immune

```text
AGENT_IMMUNE_STRATEGIC_POSITION_CANDIDATE=TITMAS_NATIVE_SENSOR_NODE
AGENT_IMMUNE_ENABLED=false
AGENT_IMMUNE_REQUIRED=false
```

Agent Immune is not required or enabled for Ecology Box 001. If separately
authorized later, its scope is limited to `observe`, `record` and
`export_signal`; it cannot recommend a fix, approve, reject, authorize, modify
or execute.

Both arms must receive equivalent sensing, or the difference must be declared
as a confounder before execution. `Observation` cannot automatically become
Evidence, Evaluation or Decision.

```text
OBSERVATION_NE_EVIDENCE=true
HEALTH_SIGNAL_NE_EVALUATION=true
HEALTH_SIGNAL_NE_DECISION=true
```
