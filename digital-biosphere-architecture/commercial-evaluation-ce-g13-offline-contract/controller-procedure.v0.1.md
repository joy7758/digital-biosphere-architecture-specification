# CE-G13 Controller Procedure v0.1

## Status

`FROZEN_NOT_AUTHORIZED_NOT_EXECUTED`

This is an offline execution contract, not an executable controller. It defines the sequence a
future, separately authorized controller must follow.

## Preconditions

1. A Human Decision explicitly authorizes CE-G13 execution.
2. The frozen 28-file package passes offline validation without modification.
3. The requested and returned model identity is exactly `qwen3.7-max`.
4. The public source root, request ceiling, byte ceiling and same-origin restriction match the
   frozen execution plan.
5. No customer data, private repository, credential value or hidden answer key is admitted.

## Future execution sequence

1. Freeze the package digest set and create an empty request-capture ledger.
2. Retrieve the public root and same-origin references within the frozen budget.
3. Persist a snapshot manifest and retrieval receipt. Fail closed on origin, size, transport,
   parsing, sanitization or budget violations.
4. Bind the same immutable public snapshot to five isolated role sessions.
5. Execute sessions in order S01 through S05. Each role receives only its declared inputs.
6. Accept only a raw, direct JSON response that validates against the role schema. Do not extract,
   repair, retry, substitute models or fall back.
7. Record a request-capture contract for every attempted session, including failed attempts.
8. Validate the website-only reuse plan without starting a Runtime, creating an Agent or granting
   Permission.
9. If separately authorized, run no more than one clean, synthetic technical-reuse check and record
   its bounded receipt. A passing receipt is not production or customer evidence.
10. Produce the composite result and apply the frozen scoring rules.
11. Preserve all failures. Any critical boundary failure yields `FAIL_CLOSED`.

## Isolation and ordering

- S01 receives no project name, known filename, repository link, earlier response or answer key.
- S02 receives the public snapshot only.
- S03 receives the public snapshot only.
- S04 receives the public snapshot and the validated bounded reuse-plan result.
- S05 receives the public snapshot and the four preceding role responses.
- Sessions do not share conversation state.

## Hard boundaries

```text
Observation != Evidence
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Contract != Implementation
```

The procedure creates no Agent, Runtime, Entity, Permission, commercial offering, certification,
customer adoption, production claim or Evidence Truth.
