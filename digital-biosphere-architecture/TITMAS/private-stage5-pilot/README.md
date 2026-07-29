# TITMAS Stage 5 Programmatic Pilot

This private, deterministic gate exercises five synthetic scenarios before any
real model call is permitted. It reuses the existing loopback Gateway,
Conformance harness, Response Capture boundary and the minimal Stage 5 SDK.

The persisted output contains sanitized audit facts only. It contains no
Sandbox Key, provider credential, raw provider response, customer data,
standard adoption or release authorization.

```text
PROGRAMMATIC_PILOT_NE_AGENT_PILOT=true
PILOT_ACCEPTANCE_NE_STANDARD_ADOPTION=true
REAL_MODEL_CALLS_REQUIRE_PROGRAMMATIC_PASS=true
```
