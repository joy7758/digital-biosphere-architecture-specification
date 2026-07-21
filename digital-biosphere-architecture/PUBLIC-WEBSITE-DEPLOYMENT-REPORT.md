---
report_id: DBA-WEB-DEPLOY-002
title: Trusted Multi-Agent Infrastructure Public Website Deployment Report
title_zh: 可信多智能体基础设施公开网站部署报告
status: pass-candidate-deployed-not-released
observed_at: 2026-07-22T01:17:50+08:00
public_url: https://redcrag.cn/
github_prerelease_url: https://github.com/joy7758/digital-biosphere-architecture-specification/releases/tag/v0.1-public-website-candidate.6
github_prerelease_tag: v0.1-public-website-candidate.6
github_prerelease_published: true
host: 180.76.115.193
initial_validated_source_revision: 6e05f8d383f409ed5790390da440890fd9603c48
current_validated_source_revision: ac5374ad326e95a71a326da4b2d9ec74880c608f
deployment_state: candidate-deployed-not-released
developer_preview_released: false
production_ready: false
agent_created: false
runtime_created: false
permission_created: false
---

# Trusted Multi-Agent Infrastructure Public Website Deployment Report

## Conclusion

`https://redcrag.cn/` now serves the bilingual, agent-readable TMAI public
website from an immutable Baidu Cloud release directory. This is a deployed
website candidate, not the Trusted Multi-Agent Infrastructure Developer Preview
release.

```text
PUBLIC_WEBSITE_DEPLOYED=true
PUBLIC_WEBSITE_HEALTH_PASS=true
PUBLIC_WEBSITE_SECURITY_HEADERS_PASS=true
PUBLIC_WEBSITE_ROLLBACK_VALIDATED=true
DEVELOPER_PREVIEW_RELEASED=false
PRODUCTION_READY=false
```

## Published routes

| Route | Role | Result |
|---|---|---|
| `/` | 中文首页 | `200` |
| `/en/` | English home | `200` |
| `/status/` | 中文状态页 | `200` |
| `/en/status/` | English status | `200` |
| `/llms.txt` | LLM-readable project entry | `200` |
| `/agent-index.json` | Agent discovery index | `200` |
| `/status.json` | Machine-readable program status | `200` |
| `/agent-customer-package.json` | Agent recommendation, composition and boundary package | `200` |
| `/release.json` | Active artifact source and state | `200` |
| `/release-manifest.json` | SHA-256 artifact inventory | `200` |
| `/og.png` | Social preview asset | `200` |

## Artifact integrity

The current validated deployment was generated from source revision
`ac5374ad326e95a71a326da4b2d9ec74880c608f`. The initial validated deployment
`6e05f8d383f409ed5790390da440890fd9603c48`, the preceding public candidates
`bc7ba49a357ebc007e2a4c9dc01178a37e74d2d8` and
`f217831c287b9b09f0a56f54374ec16d91fa5070` and
`6fd94a62f5eea26b7edd9d2f66a9dde99ab7832f` and
`7fe88e8bb267b141c43f3132155714c1e110e172`, and the pre-rerun remediation candidate
`a0f014d4bb0454f7612c6bd899e9f0b83fb0be2f` remain preserved. The authoritative
active revision is the value returned by `https://redcrag.cn/release.json`.

Every file listed in `release-manifest.json` passed an on-host SHA-256 and byte-size
manifest verifier before Nginx activation.

For the current artifact, all 20 manifest entries passed byte-size and SHA-256
verification before the atomic switch. All 10 primary public health routes
returned HTTP 200 on the first post-switch check. Earlier second-attempt health
events remain recorded in deployment history rather than being rewritten.

GNU tar reported ignored `LIBARCHIVE.xattr.com.apple.provenance` extended-header
keywords while extracting the macOS-created archive. All declared bytes and
SHA-256 values still passed. The warning is retained as a packaging-portability
signal and is not treated as content corruption or silently rewritten as absent.

## Transport and security

- HTTP redirects to `https://redcrag.cn/`.
- The Let's Encrypt certificate is valid from `2026-07-11` to `2026-10-09`.
- Nginx accepts TLS 1.2 and TLS 1.3.
- HSTS, CSP, `nosniff`, frame denial, referrer policy, and permissions policy
  headers were observed on the public HTML response.
- SSH, Docker, fail2ban, Certbot, firewall, and certificate material were
  preserved during the old-site cleanup.

## Rollback validation

The rollback mechanism was previously validated by an actual atomic switch and
restore. The current update used the same immutable release-directory and atomic
symlink mechanism, preserving `a0f014d…`, `bc7ba49…`, `f217831…`, `6fd94a62…`,
`7fe88e8…` and older verified artifacts.

```text
ROLLBACK_VALIDATED=true
ROLLBACK_MECHANISM=ATOMIC_SYMLINK_SWITCH
```

## Truth boundary

Website deployment does not satisfy the remaining Developer Preview release
gates. In particular:

- `SAEE_DBOS_ADAPTER_PASS=true` only for the frozen read-only advisory path
- `AGENT_CUSTOMER_VALIDATION_RERUN_RESULT=PASS` does not equal customer adoption or release authorization
- all 12 rerun verdicts are boundary-aware `CONDITIONAL`, not unconditional production recommendations
- `DBOS` remains private; no public Runtime, package or API is claimed
- `OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY`; GitHub's full new description finds the project, while canonical English／Chinese names and public-search queries still do not
- dependency risk `R-015` review is complete with 0 high／critical and 2 disclosed moderate residuals
- no GitHub Developer Preview Release exists

No Agent, Runtime, Permission, Digital Entity instance, or scientific Evidence
was created by this deployment.

## GitHub website candidate

The same source revision is tagged and published as an explicit GitHub
prerelease:

- Tag: `v0.1-public-website-candidate.6`
- Release title: `Trusted Multi-Agent Infrastructure public website candidate 6`
- Source revision: `ac5374ad326e95a71a326da4b2d9ec74880c608f`
- Asset: `tmai-public-website-candidate-ac5374ad326e95a71a326da4b2d9ec74880c608f.tar.gz`
- Asset SHA-256:
  `35a01d42856edb03a040b9a89afced4d73d3b3271db3725aa8285e981740f00f`
- GitHub state: `prerelease=true`, `draft=false`

This GitHub prerelease distributes the website candidate artifact. It is not a
Developer Preview release and does not resolve DBOS agent access, open-web
discovery or Human Release Decision gates. Previous website
candidate prereleases remain historical and have not been retagged.
