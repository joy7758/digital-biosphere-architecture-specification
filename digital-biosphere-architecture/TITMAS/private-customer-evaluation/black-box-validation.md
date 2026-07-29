# Black-box Validation Candidate

Only synthetic local files may be used in the current stage.

```bash
python3 -m json.tool TITMAS/private-customer-evaluation/agent-service-discovery.json >/dev/null
python3 -m json.tool TITMAS/private-customer-evaluation/api-contract.json >/dev/null
python3 -m json.tool TITMAS/private-customer-evaluation/synthetic-request.json >/dev/null
python3 -m json.tool TITMAS/private-customer-evaluation/synthetic-response.json >/dev/null
python3 -m json.tool TITMAS/private-customer-evaluation/error-codes.json >/dev/null
```

These commands validate syntax only. They do not call a service, prove value,
create Evidence Truth or authorize a real evaluation.
