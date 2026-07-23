import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { resolveReleaseContext } from "./release-mode.mjs";

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
  "agent-customer-package.json",
  "dbos-public-package-manifest.json",
  "release.json",
  "release-manifest.json",
  "robots.txt",
  "sitemap.xml",
  "favicon.svg",
  "og.png",
];

await Promise.all(requiredFiles.map((file) => access(join(outputRoot, file))));

const [zh, en, zhStatus, enStatus, status, agentCustomerPackage, dbosPackage, release, manifest] = await Promise.all([
  readFile(join(outputRoot, "index.html"), "utf8"),
  readFile(join(outputRoot, "en/index.html"), "utf8"),
  readFile(join(outputRoot, "status/index.html"), "utf8"),
  readFile(join(outputRoot, "en/status/index.html"), "utf8"),
  readFile(join(outputRoot, "status.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "agent-customer-package.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "dbos-public-package-manifest.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "release.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "release-manifest.json"), "utf8").then(JSON.parse),
]);
const agentIndex = await readFile(join(outputRoot, "agent-index.json"), "utf8").then(JSON.parse);
const releaseContext = resolveReleaseContext(process.env, {
  status,
  agentIndex,
  agentCustomerPackage,
  dbosPackage,
});

assert.match(zh, /TITMAS 可信多智能体基础设施开发者社区/);
assert.match(en, /TITMAS Infrastructure Developer Community/);
assert.match(zh, /<html lang="zh-CN">/);
assert.match(zhStatus, /<html lang="zh-CN">/);
assert.match(en, /<html lang="en">/);
assert.match(enStatus, /<html lang="en">/);
assert.match(zh, /共同建设 Agent 时代的可信基础设施/);
assert.match(en, /Build trustworthy infrastructure for the agent era/);
assert.match(zh, /Community Review ≠ Architecture Decision/);
assert.match(en, /Contribution ≠ Authority/);
if (releaseContext.mode === "candidate") {
  assert.match(zhStatus, /当前不是正式发布/);
  assert.match(enStatus, /This is not a release/);
} else {
  assert.match(zhStatus, /可信多智能体基础设施开发者预览版 v0\.1 已发布/);
  assert.match(enStatus, /Trusted Multi-Agent Infrastructure Developer Preview v0\.1 is released/);
}
assert.match(zh, /SAEE_DBOS_ADAPTER_PASS/);
assert.match(en, /SAEE_DBOS_ADAPTER_PASS/);
assert.match(zh, /第一个可信闭环：设计完成，尚未执行/);
assert.match(en, /The first trustworthy loop is designed—not executed/);
assert.match(zh, /Observation ≠ Evidence/);
assert.match(en, /Evaluation ≠ Authorization/);
assert.doesNotMatch(zh, /codex-preview|Your site is taking shape/);
assert.doesNotMatch(en, /codex-preview|Your site is taking shape/);
assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, true);
assert.equal(status.gates.TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED, true);
assert.equal(status.gates.TITMAS_CONTRIBUTOR_ENTRY_PREPARED, true);
assert.equal(status.gates.TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED, false);
assert.equal(status.gates.TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED, false);
assert.equal(status.gates.TITMAS_CODE_OF_CONDUCT_ADOPTED, false);
assert.equal(status.gates.TITMAS_MAINTAINER_ASSIGNED, false);
assert.equal(status.gates.TITMAS_FOUNDATION_IN_SCOPE, false);
assert.equal(status.community.current_state, "CONTRIBUTOR_ENTRY_PREPARED");
assert.equal(status.community.public_contribution_surface_authorized, false);
assert.equal(agentIndex.name, "TITMAS Infrastructure Developer Community");
assert.equal(agentIndex.abbreviation, "TITMAS");
assert.equal(agentIndex.community.public_submission_invitation, false);
assert.equal(status.gates.DQ_010_SUPERSEDED_FOR_PRIMARY_ROUTE, true);
assert.equal(status.gates.AGENT_CUSTOMER_VALIDATION_BASELINE_CONDITIONAL, true);
assert.equal(status.gates.AGENT_CUSTOMER_VALIDATION_RERUN_PASS, true);
assert.equal(status.agent_customer_validation.api_sessions_completed, 12);
assert.equal(status.agent_customer_validation.open_web_discovery, "NOT_ASSESSED");
assert.equal(status.agent_customer_validation.result, "PASS");
assert.equal(status.open_web_discovery.observation_id, "TMAI-OWD-20260722-001");
assert.equal(status.open_web_discovery.result, "PARTIAL_METADATA_ONLY");
assert.equal(status.open_web_discovery.public_web_exact_match_observed, false);
assert.equal(status.open_web_discovery.canonical_name_match_observed, false);
assert.equal(status.open_web_discovery.github_metadata_description_match_observed, true);
assert.equal(status.open_web_discovery.github_metadata_remediated, true);
assert.equal(status.open_web_discovery.github_metadata_indexing_signal_observed, true);
assert.equal(agentCustomerPackage.intended_customer, "AI_AGENT");
assert.equal(agentCustomerPackage.released, releaseContext.developerPreviewReleased);
assert.equal(agentCustomerPackage.validation_truth.rerun_result, "PASS");
assert.equal(dbosPackage.package_id, "TMAI-DBOS-WHEEL-CANDIDATE-20260722-001");
assert.equal(dbosPackage.source.source_revision, "cd3f867c4379ec555c45e7d554088ad12ce08a24");
assert.equal(dbosPackage.public_safe_boundary.absolute_user_path_matches, 0);
assert.equal(dbosPackage.public_safe_boundary.gitleaks_findings, 0);
assert.equal(status.gates.DBOS_PUBLIC_SAFE_WHEEL_VALIDATED, true);
assert.equal(status.gates.TITMAS_ADOPTION_VALIDATION_FRAMEWORK_DEFINED, true);
assert.equal(status.gates.TITMAS_ADOPTION_VALIDATION_READY, false);
assert.equal(status.gates.TITMAS_TECHNICAL_VALIDATION_DESIGN_COMPLETE, true);
assert.equal(status.gates.TITMAS_PILOT_EXECUTION_AUTHORIZED, false);
assert.equal(status.gates.COMPLETE_VERTICAL_SLICE_EXECUTED, false);
assert.equal(status.technical_validation.conformance_cases_defined, 14);
assert.equal(status.technical_validation.conformance_cases_executed, 0);
assert.equal(status.technical_validation.first_external_role, "REVIEWER");
assert.equal(status.technical_validation.public_materials.demo, "NOT_CREATED");
assert.equal(status.technical_validation.adoption_claimed, false);
assert.equal(agentIndex.technical_validation.design_complete, true);
assert.equal(agentIndex.technical_validation.execution_authorized, false);
assert.equal(agentIndex.technical_validation.vertical_slice_executed, false);
assert.equal(agentIndex.technical_validation.first_external_role, "REVIEWER");
assert.equal(release.release_mode, releaseContext.mode);
assert.equal(release.developer_preview_released, releaseContext.developerPreviewReleased);
assert.equal(release.deployment_state, releaseContext.deploymentState);
assert.equal(release.release_decision_reference, releaseContext.releaseDecisionReference);
assert.equal(release.released_by_ref, releaseContext.releasedByRef);
assert.equal(release.public_release_tag, releaseContext.publicReleaseTag);
assert.equal(release.dbos_public_package_url, releaseContext.dbosWheelUrl);
assert.ok(manifest.files.length >= 10);
assert.equal(manifest.source_revision, release.source_revision);

console.log("STATIC_EXPORT_PASS=true");
console.log("ZH_EN_CONTENT_PARITY_PASS=true");
console.log("TRUTH_BOUNDARY_VALIDATION_PASS=true");
console.log(`RELEASE_MODE=${releaseContext.mode}`);
console.log(`SOURCE_REVISION=${release.source_revision}`);
console.log(`MANIFEST_FILES=${manifest.files.length}`);
