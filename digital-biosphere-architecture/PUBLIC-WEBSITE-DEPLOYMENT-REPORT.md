---
report_id: DBA-WEB-DEPLOY-001
title: Trusted Multi-Agent Infrastructure Public Website Deployment Report
title_zh: 可信多智能体基础设施公开网站部署报告
status: pass-candidate-deployed-not-released
observed_at: 2026-07-21T19:23:00+08:00
public_url: https://redcrag.cn/
github_prerelease_url: https://github.com/joy7758/digital-biosphere-architecture-specification/releases/tag/v0.1-public-website-candidate
github_prerelease_tag: v0.1-public-website-candidate
github_prerelease_published: true
host: 180.76.115.193
initial_validated_source_revision: 6e05f8d383f409ed5790390da440890fd9603c48
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

The initial validated deployment was generated from source revision
`6e05f8d383f409ed5790390da440890fd9603c48`. The authoritative current revision
is always the value returned by `https://redcrag.cn/release.json`.

Every file listed in `release-manifest.json` passed `sha256sum -c` on the target
host before Nginx activation.

## Transport and security

- HTTP redirects to `https://redcrag.cn/`.
- The Let's Encrypt certificate is valid from `2026-07-11` to `2026-10-09`.
- Nginx accepts TLS 1.2 and TLS 1.3.
- HSTS, CSP, `nosniff`, frame denial, referrer policy, and permissions policy
  headers were observed on the public HTML response.
- SSH, Docker, fail2ban, Certbot, firewall, and certificate material were
  preserved during the old-site cleanup.

## Rollback validation

The `/srv/tmai/current` symlink was atomically switched to the previous verified
artifact, its `release.json` was read successfully, and the symlink was then
atomically restored to the active artifact.

```text
ROLLBACK_VALIDATED=true
ROLLBACK_MECHANISM=ATOMIC_SYMLINK_SWITCH
```

## Truth boundary

Website deployment does not satisfy the remaining Developer Preview release
gates. In particular:

- `SAEE_DBOS_ADAPTER_PASS=false`
- `CROSS_PROJECT_CLEAN_CLONE_PASS=false`
- `DBOS` external trial access remains unvalidated
- the public license decision remains pending
- the external developer trial has not been authorized or executed
- no GitHub Developer Preview Release exists

No Agent, Runtime, Permission, Digital Entity instance, or scientific Evidence
was created by this deployment.

## GitHub website candidate

The same source revision is tagged and published as an explicit GitHub
prerelease:

- Tag: `v0.1-public-website-candidate`
- Release title: `TMAI Public Website Candidate v0.1`
- Source revision: `ec2fd06cabc36de5422019103cf8d6f092600fc8`
- Asset: `tmai-public-website-candidate-ec2fd06.tar.gz`
- Asset SHA-256:
  `ae01c978d9d1940121d27a9c566b87f89d837219c5f1c2b703fcaeaad9326142`
- GitHub state: `prerelease=true`, `draft=false`

This GitHub prerelease distributes the website candidate artifact. It is not a
Developer Preview release and does not resolve the outstanding license,
adapter, access, or external-trial gates.
