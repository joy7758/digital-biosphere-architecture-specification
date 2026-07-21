import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const outputRoot = join(siteRoot, "out");
const requiredFiles = [
  "index.html",
  "en/index.html",
  "status/index.html",
  "en/status/index.html",
  "llms.txt",
  "agent-index.json",
  "status.json",
  "release.json",
  "release-manifest.json",
  "robots.txt",
  "sitemap.xml",
  "og.png",
];

await Promise.all(requiredFiles.map((file) => access(join(outputRoot, file))));

const [zh, en, zhStatus, enStatus, status, release, manifest] = await Promise.all([
  readFile(join(outputRoot, "index.html"), "utf8"),
  readFile(join(outputRoot, "en/index.html"), "utf8"),
  readFile(join(outputRoot, "status/index.html"), "utf8"),
  readFile(join(outputRoot, "en/status/index.html"), "utf8"),
  readFile(join(outputRoot, "status.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "release.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "release-manifest.json"), "utf8").then(JSON.parse),
]);

assert.match(zh, /面向多智能体系统的可信基础设施/);
assert.match(en, /Trust infrastructure for multi-agent systems/);
assert.match(zhStatus, /当前不是正式发布/);
assert.match(enStatus, /This is not a release/);
assert.match(zh, /SAEE_DBOS_ADAPTER_PASS/);
assert.match(en, /SAEE_DBOS_ADAPTER_PASS/);
assert.doesNotMatch(zh, /codex-preview|Your site is taking shape/);
assert.doesNotMatch(en, /codex-preview|Your site is taking shape/);
assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, true);
assert.equal(status.gates.DQ_010_EFFECTIVE, false);
assert.equal(status.external_trial.participant_source_confirmed, false);
assert.equal(status.gates.DEVELOPER_PREVIEW_RELEASED, false);
assert.equal(release.developer_preview_released, false);
assert.equal(release.deployment_state, "candidate_not_released");
assert.ok(manifest.files.length >= 10);
assert.equal(manifest.source_revision, release.source_revision);

console.log("STATIC_EXPORT_PASS=true");
console.log("ZH_EN_CONTENT_PARITY_PASS=true");
console.log("TRUTH_BOUNDARY_VALIDATION_PASS=true");
console.log(`SOURCE_REVISION=${release.source_revision}`);
console.log(`MANIFEST_FILES=${manifest.files.length}`);
