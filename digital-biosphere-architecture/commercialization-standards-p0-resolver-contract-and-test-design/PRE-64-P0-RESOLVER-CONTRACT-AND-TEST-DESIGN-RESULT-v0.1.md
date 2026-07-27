# PRE-64 P0 Resolver Contract and Test Design Result v0.1

```text
RESULT=PASS_OFFLINE_P0_RESOLVER_CONTRACT_AND_TEST_DESIGN
POSITIVE_DESIGN_CASES=6
NEGATIVE_DESIGN_CASES=24
MUTATION_NEGATIVES_REJECTED=12
NETWORK_MODEL_CREDENTIAL_TARGET_DEPENDENCY_IMPLEMENTATION_ACTIONS=0
P0_RESOLVER_IMPLEMENTED=false
FORMAL_HUMAN_SECURITY_REVIEW_COMPLETE=false
IMPLEMENTATION_AUTHORIZED=false
STANDARD_READY=false
```

## Result

PRE-64 defines a Development candidate for separating P0 DNS resolution from P1 TCP connect.
It freezes:

- one exact allowlisted hostname and port `443`;
- one `getaddrinfo(AF_UNSPEC, SOCK_STREAM, IPPROTO_TCP, flags=0)` invocation;
- a 5,000 ms required deadline, with the implementation mechanism intentionally unresolved;
- at most 64 raw and 64 unique usable results;
- `FIRST_UNIQUE_IN_RESOLVER_ORDER_V1`;
- one selected address, one P1 socket creation and one P1 connect;
- an in-memory `ResolvedEndpoint` with an opaque continuity handle;
- original-hostname TLS identity;
- sanitized P0 metadata and nine failure categories;
- 6 positive and 24 negative offline test-design cases.

## Important Limits

Python resolver order can vary by platform. The selection rule is deterministic only for a given
ordered input. `getaddrinfo()` has no per-call timeout parameter, and the deadline mechanism is not
selected. The single-address profile intentionally provides no address failover.

The default HTTPCore 1.0.9 sync backend is not treated as conformant because its `connect_tcp()`
delegates to `socket.create_connection()`, which may resolve and try multiple addresses.

## Current Truth

```text
CONTRACT_CANDIDATE_CREATED=true
CONTRACT_ADOPTED=false
TEST_DESIGN_CREATED=true
TESTS_IMPLEMENTED=false
TESTS_EXECUTED=false
AGENT_REVIEW_INPUT_PREPARED=true
AGENT_REVIEW_AUTHORIZED=false
P0_RESOLVER_IMPLEMENTED=false
TARGET_REPOSITORY_CHANGED=false
PROVIDER_SUPPORTED=false
PROVIDER_CONFORMANCE_EXECUTED=false
RELEASE_AUTHORIZED=false
```

## Next Action

```text
NEXT_ACTION=FORM_PRE65_P0_RESOLVER_CONTRACT_MULTI_PROVIDER_AGENT_REVIEW_RECOMMENDATION
```

That review must assess deadline implementability, platform dependence, privacy, P0/P1 continuity,
TLS identity and fail-closed behavior. It remains AI-assisted review input, not formal Human
Security Review or implementation authorization.
