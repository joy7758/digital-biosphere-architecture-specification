# TITMAS Private Evaluation Gateway v0.1

This directory implements a local, loopback-only and one-session black-box
evaluation facade for deterministic synthetic validation.

```text
PRIVATE_EVALUATION_FACADE=true
LOCAL_EPHEMERAL_SERVICE=true
BLACK_BOX_CUSTOMER_SURFACE=true
NETWORK_SCOPE=LOOPBACK_ONLY
SERVICE_LIFETIME=ONE_EVALUATION_SESSION
PUBLIC_NETWORK_EXPOSURE=false

NEW_AGENT_RUNTIME=false
NEW_CONTROL_PLANE=false
NEW_TRUTH_SOURCE=false
PUBLIC_API_SERVICE=false
PRODUCTION_SERVICE=false
REAL_MODEL_CALL_COUNT=0
REAL_PROVIDER_CALL_COUNT=0
```

The customer workspace is reconstructed from an explicit nine-file contract
allowlist. The `gateway/` directory, repository metadata, private governance,
core source and internal tests are never copied into that workspace.

The gateway reuses
[`response_capture.py`](../../agent-native/customer-cycle/response_capture.py)
for atomic request/response envelope capture. It does not create a second
response-capture authority.

Run the deterministic tests:

```bash
python3 -m unittest discover \
  -s TITMAS/private-customer-evaluation/gateway/tests \
  -p 'test_*.py' -v
```
