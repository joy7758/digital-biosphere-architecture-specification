---
report_id: DBA-WEB-DEPLOY-002
title: Trusted Multi-Agent Infrastructure Public Website Deployment Report
title_zh: 可信多智能体基础设施公开网站部署报告
status: pass-candidate-deployed-not-released
observed_at: 2026-07-21T23:36:23+08:00
public_url: https://redcrag.cn/
github_prerelease_url: https://github.com/joy7758/digital-biosphere-architecture-specification/releases/tag/v0.1-public-website-candidate.2
github_prerelease_tag: v0.1-public-website-candidate.2
github_prerelease_published: true
host: 180.76.115.193
initial_validated_source_revision: 6e05f8d383f409ed5790390da440890fd9603c48
current_validated_source_revision: bc7ba49a357ebc007e2a4c9dc01178a37e74d2d8
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
| `/release.json` | Active artifact source and state | `200` |
| `/release-manifest.json` | SHA-256 artifact inventory | `200` |
| `/og.png` | Social preview asset | `200` |

## Artifact integrity

The current validated deployment was generated from source revision
`bc7ba49a357ebc007e2a4c9dc01178a37e74d2d8`. The initial validated deployment
`6e05f8d383f409ed5790390da440890fd9603c48` and the immediately previous active
artifact `ec2fd06cabc36de5422019103cf8d6f092600fc8` remain preserved. The authoritative
active revision is the value returned by `https://redcrag.cn/release.json`.

Every file listed in `release-manifest.json` passed an on-host SHA-256 and byte-size
manifest verifier before Nginx activation.

For the current artifact, all 19 manifest entries passed byte-size and SHA-256
verification before the atomic switch. All nine public health routes returned
HTTP 200 under bounded retry. One intermediate TLS probe returned a transient
`SSL_ERROR_SYSCALL`; the complete route set then passed. This event is retained
and is not rewritten as an uninterrupted first-attempt pass.

## Transport and security

- HTTP redirects to `https://redcrag.cn/`.
- The Let's Encrypt certificate is valid from `2026-07-11` to `2026-10-09`.
- Nginx accepts TLS 1.2 and TLS 1.3.
- HSTS, CSP, `nosniff`, frame denial, referrer policy, and permissions policy
  headers were observed on the public HTML response.
- SSH, Docker, fail2ban, Certbot, firewall, and certificate material were
  preserved during the old-site cleanup.

## Rollback validation

The `/srv/tmai/current` symlink was atomically switched from
`bc7ba49a357ebc007e2a4c9dc01178a37e74d2d8` to the previous verified artifact
`ec2fd06cabc36de5422019103cf8d6f092600fc8`, its `release.json` was read from the
local TLS origin, and the symlink was then atomically restored to `bc7ba49…`.

```text
ROLLBACK_VALIDATED=true
ROLLBACK_MECHANISM=ATOMIC_SYMLINK_SWITCH
```

## Truth boundary

Website deployment does not satisfy the remaining Developer Preview release
gates. In particular:

- `SAEE_DBOS_ADAPTER_PASS=true` only for the frozen read-only advisory path
- `CROSS_PROJECT_CLEAN_CLONE_PASS=true` does not equal external trial completion
- `DBOS` remains private; no trial collaborator has been added
- `participant_source` is still pending and `DQ_010_EFFECTIVE=false`
- the external developer trial has not been executed
- dependency risk `R-015` still requires review before formal release
- no GitHub Developer Preview Release exists

No Agent, Runtime, Permission, Digital Entity instance, or scientific Evidence
was created by this deployment.

## GitHub website candidate

The same source revision is tagged and published as an explicit GitHub
prerelease:

- Tag: `v0.1-public-website-candidate.2`
- Release title: `TMAI Public Website Candidate v0.1.2`
- Source revision: `bc7ba49a357ebc007e2a4c9dc01178a37e74d2d8`
- Asset: `tmai-public-website-candidate-bc7ba49.tar.gz`
- Asset SHA-256:
  `6eaae585fbc40564f39f9ecc9ab5dbc9759986d895916e46713184dd2aa56b29`
- GitHub state: `prerelease=true`, `draft=false`

This GitHub prerelease distributes the website candidate artifact. It is not a
Developer Preview release and does not resolve DBOS trial access, participant,
external-trial, dependency-review, or Human Release Decision gates. The previous
website candidate prerelease remains historical and has not been retagged.
