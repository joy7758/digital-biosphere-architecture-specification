# Baidu Cloud deployment boundary

Target host: `180.76.115.193` (`hongyan-4cj`)

Target layout:

```text
/srv/tmai/
├── releases/<source_revision>/
└── current -> releases/<source_revision>/
```

The website is exported with:

```bash
SOURCE_REVISION="$(git rev-parse HEAD)" npm run release:static
```

Deployment copies only the generated `out/` directory to a new immutable release
directory. The `current` symlink changes only after manifest verification and
`nginx -t` pass. Rollback repoints `current` to the previous release and reloads
Nginx.

The checked-in Nginx configuration references only the certificate and private
key that exist under `/etc/letsencrypt/live/redcrag.cn/`; it does not assume
Certbot helper files that are absent on the current Baidu Cloud host.

Deployment truth:

```text
STATIC_EXPORT_NE_RELEASE=true
DEPLOYMENT_NE_DEVELOPER_PREVIEW_RELEASE=true
RELEASE_MANIFEST_REQUIRED=true
NGINX_VALIDATION_REQUIRED=true
HEALTH_CHECK_REQUIRED=true
ROLLBACK_VALIDATION_REQUIRED=true
```
