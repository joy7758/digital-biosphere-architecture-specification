# TITMAS Agent Front Door Recommendation v0.1

```text
REVIEW_ID=TITMAS-AGENT-FRONT-DOOR-20260728-001
PRIMARY_REPOSITORY=DBA
CHANGE_CLASS=WEBSITE_INFORMATION_ARCHITECTURE
AGENT_CUSTOMER_PROBLEM=HOMEPAGE_ONLY_OR_PREFIX_ONLY_FETCH_PRODUCES_SHALLOW_UNDERSTANDING
FINAL_AGENT_RECOMMENDATION=RECOMMENDED
RECOMMENDATION_MODEL=kimi-k2.6
RECOMMENDATION_PROVIDER=baidu-qianfan
IMPLEMENTATION_AUTHORIZED_BY_RECOMMENDATION=false
PUBLICATION_AUTHORIZED_BY_RECOMMENDATION=false
```

## Customer recommendation

If a potential user asks how to help a homepage-only AI Agent quickly understand
RedCrag, the bounded `Agent Front Door` solution is recommended.

The solution reuses the existing `llms.txt`, `agent-index.json`,
`site-catalog.json`, sitemap, and bilingual public routes. It does not create a
second discovery system. It moves a concise explanation and direct links into
the first static portion of each homepage, adds HTML discovery metadata, and
keeps the complete indexes as canonical machine-readable detail.

## Prior recommendation attempts

Two invalid attempts are retained as failures:

1. A `kimi-k2.6` request returned `provider_timeout_or_network_error`; it
   supplied no recommendation.
2. A local `qwen3.7-max` request returned HTTP `401`; it supplied no
   recommendation and was not retried or silently downgraded.

The later bounded `kimi-k2.6` request returned a valid `RECOMMENDED` result.
That result is advisory external content, not an Architecture Decision,
Implementation Authorization, Release Authorization, customer adoption, or
truth.

## Problems and corrections

| Problem | Correction | Direct evidence required |
|---|---|---|
| Machine indexes exist but appear too late for prefix-only readers | Put a visible, semantic `Agent Start Here` section immediately after the hero | Bilingual rendered HTML contains the section within the first 50,000 bytes |
| Homepage-only readers do not discover machine resources | Link `llms.txt`, `agent-index.json`, and `site-catalog.json` in the front door and HTML head | Static HTML contains all links without JavaScript |
| A crawler cannot infer the relationship between major sections | Add bounded `WebSite.hasPart` JSON-LD records for public surfaces and machine documents | Rendered JSON-LD contains stable absolute URLs and encoding formats |
| Existing `llms.txt` is long | Add a short `Agent start here` map near the beginning without deleting retained detail | The heading begins within the first 1,500 characters |
| Future homepage growth can push the entry too deep | Add a 50,000-byte prefix regression test | Build and static verification fail if the entry moves beyond the limit |
| General crawler permission may be misunderstood | Preserve the wildcard rule and explicitly allow `OAI-SearchBot` | Static `robots.txt` validation passes |

## Remaining gaps and stop conditions

- A local build and static verification must pass before any publication review.
- The current public website must not be changed without a separate explicit
  publication authorization.
- If the front door exceeds the 50,000-byte source prefix, requires JavaScript,
  hides content from humans, or drifts from the machine indexes, the change
  must fail closed.
- If a future public surface is added, its human and machine entries must be
  updated together.

## Non-claims

```text
RUNTIME_CREATED=false
API_CREATED=false
AGENT_CREATED=false
PERMISSION_CREATED=false
AUTHENTICATION_CREATED=false
PRODUCT_CREATED=false
CERTIFICATION_CREATED=false
PRODUCTION_STATUS_CHANGED=false
PUBLICATION_EXECUTED=false
```
