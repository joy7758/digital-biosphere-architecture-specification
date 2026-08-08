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
  "products/gate/index.html",
  "en/products/gate/index.html",
  "products/receipt/index.html",
  "en/products/receipt/index.html",
  "products/audit/index.html",
  "en/products/audit/index.html",
  "products/health/index.html",
  "en/products/health/index.html",
  "design-partner/index.html",
  "en/design-partner/index.html",
  "private-evaluation/index.html",
  "en/private-evaluation/index.html",
  "monitor-pilot/index.html",
  "en/monitor-pilot/index.html",
  "enforce-pilot/index.html",
  "en/enforce-pilot/index.html",
  "request-access/index.html",
  "en/request-access/index.html",
  "security/index.html",
  "en/security/index.html",
  "trust-center/index.html",
  "en/trust-center/index.html",
  "privacy/index.html",
  "en/privacy/index.html",
  "terms/index.html",
  "en/terms/index.html",
  "research/index.html",
  "en/research/index.html",
  "research/index/index.html",
  "en/research/index/index.html",
  "applications/index.html",
  "en/applications/index.html",
  "demos/index.html",
  "en/demos/index.html",
  "community/index.html",
  "en/community/index.html",
  "updates/index.html",
  "en/updates/index.html",
  "updates/constitution/index.html",
  "en/updates/constitution/index.html",
  "industries/index.html",
  "en/industries/index.html",
  "industry/media-evidence/index.html",
  "en/industry/media-evidence/index.html",
  "industry/medical-evidence/index.html",
  "en/industry/medical-evidence/index.html",
  "industry/space-agent-evidence/index.html",
  "en/industry/space-agent-evidence/index.html",
  "demo/medical-evidence/index.html",
  "en/demo/medical-evidence/index.html",
  "demo/media-evidence/index.html",
  "en/demo/media-evidence/index.html",
  "digital-cell/index.html",
  "en/digital-cell/index.html",
  "commercial-evaluation/index.html",
  "en/commercial-evaluation/index.html",
  "status/index.html",
  "en/status/index.html",
  "llms.txt",
  "TITMAS-FIRST-RUN-v0.1.md",
  "agent-index.json",
  "product-catalog.json",
  "solution-catalog.json",
  "proof-catalog.json",
  "commercial-offerings.json",
  "deployment-options.json",
  "recommendation-policy.json",
  "site-catalog.json",
  "media-evidence-profile.json",
  "media-evidence-reproduction.md",
  "titmas-community.json",
  "updates.json",
  "status.json",
  "architecture/cr01-ledger-transition-design-v1.0.json",
  "agent-customer-package.json",
  "dbos-public-package-manifest.json",
  "release.json",
  "release-manifest.json",
  "robots.txt",
  "sitemap.xml",
  "favicon.svg",
  "favicon.png",
  "titmas-logo.png",
  "summersea-logo.png",
  "digital-cell.json",
  "digital-cell/digital-cell-architecture.png",
  "medical-evidence-demo.json",
  "space-agent-evidence-profile.json",
  "og.png",
  "og-media-evidence.png",
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
const llms = await readFile(join(outputRoot, "llms.txt"), "utf8");
const releaseContext = resolveReleaseContext(process.env, {
  status,
  agentIndex,
  agentCustomerPackage,
  dbosPackage,
});

assert.match(zh, /<h1>为自主 AI 系统构建可信基础设施<\/h1>/);
assert.match(en, /<h1>Building trustworthy infrastructure for autonomous AI systems<\/h1>/);
assert.match(zh, /DCELL · RESEARCH_DIRECTION/);
assert.match(en, /DCELL · RESEARCH_DIRECTION/);
assert.match(zh, /verifiable-agent-demo/);
assert.match(en, /titmas-agent-action-gate/);
assert.match(zh, /早期工程种子和第一个实验实例/);
assert.match(en, /early engineering seed and first experimental instance/);
assert.doesNotMatch(zh, /\/titmas-logo\.png|\/summersea-logo\.png/);
assert.doesNotMatch(en, /\/titmas-logo\.png|\/summersea-logo\.png/);
assert.match(zh, /<title>Bin Zhang · DCELL 研究方向<\/title>/);
assert.match(en, /<title>Bin Zhang · DCELL Research Direction<\/title>/);
assert.match(zh, /网站运营主体[^<]*：山西游骑兵电子商务有限公司/);
assert.match(en, /Website operator[^<]*：山西游骑兵电子商务有限公司/);
assert.match(zh, /晋ICP备2026006409号-1/);
assert.match(en, /晋ICP备2026006409号-1/);
assert.match(zh, /href="https:\/\/beian\.miit\.gov\.cn"[^>]*>工业和信息化部备案管理系统/);
assert.match(en, /href="https:\/\/beian\.miit\.gov\.cn"[^>]*>工业和信息化部备案管理系统/);
assert.match(zh, /<html lang="zh-CN">/);
assert.match(zhStatus, /<html lang="zh-CN">/);
assert.match(en, /<html lang="en">/);
assert.match(enStatus, /<html lang="en">/);
assert.match(zh, /Evidence ≠ Truth/);
assert.match(en, /Evaluation ≠ Authority/);
assert.match(zhStatus, /DCELL 是研究方向，公开工程证据保持有界/);
assert.match(enStatus, /DCELL is a research direction; public engineering evidence remains bounded/);
assert.doesNotMatch(zh, /AVAILABLE OFFERINGS|申请访问/);
assert.doesNotMatch(en, /AVAILABLE OFFERINGS|Request access/);
assert.doesNotMatch(zh, /codex-preview|Your site is taking shape/);
assert.doesNotMatch(en, /codex-preview|Your site is taking shape/);
assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, true);
assert.equal(status.public_focus, "DCELL_RESEARCH_DIRECTION");
assert.equal(status.website_alignment.dcell_maturity, "RESEARCH_DIRECTION");
assert.equal(agentIndex.public_focus, "DCELL_RESEARCH_DIRECTION");
assert.equal(agentIndex.public_identity.name, "Bin Zhang");
assert.equal(agentIndex.research_direction.complete_system_implemented, false);
assert.equal(status.gates.TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED, true);
assert.equal(status.gates.TITMAS_CONTRIBUTOR_ENTRY_PREPARED, true);
assert.equal(status.gates.TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED, false);
assert.equal(status.gates.TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED, false);
assert.equal(status.gates.TITMAS_CODE_OF_CONDUCT_ADOPTED, false);
assert.equal(status.gates.TITMAS_MAINTAINER_ASSIGNED, false);
assert.equal(status.gates.TITMAS_FOUNDATION_IN_SCOPE, false);
assert.equal(status.community.direction_adopted, false);
assert.equal(status.community.historical_direction_recorded, true);
assert.equal(status.community.current_state, "HISTORICAL_NON_CURRENT");
assert.equal(status.community.canonical_name_en, "titmas");
assert.equal(status.community.canonical_name_zh, "夏日之海");
assert.equal(status.community.public_brand_logo, "/titmas-logo.png");
assert.equal(status.community.technical_project_identifier, "TITMAS");
assert.equal(status.community.public_contribution_surface_authorized, false);
assert.equal(agentIndex.name, "TITMAS Commercial Agent Infrastructure");
assert.equal(agentIndex.display_name_zh, "夏日之海");
assert.equal(agentIndex.display_name_en, "titmas");
assert.equal(agentIndex.public_brand, "titmas");
assert.equal(agentIndex.public_brand_zh, "夏日之海");
assert.equal(agentIndex.public_brand_logo, "/titmas-logo.png");
assert.equal(agentIndex.technical_project_identifier, "TITMAS");
assert.equal(agentIndex.abbreviation, "TITMAS");
assert.equal(agentIndex.website_operator_legal_name, "山西游骑兵电子商务有限公司");
assert.equal(agentIndex.public_website.operator_legal_name, "山西游骑兵电子商务有限公司");
assert.equal(agentIndex.public_website.icp_record_number, "晋ICP备2026006409号-1");
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
assert.equal(status.current_stage, "DCELL_RESEARCH_DIRECTION_ALIGNMENT");
assert.equal(status.retained_titmas_stage, "TITMAS_AGENT_NATIVE_COMMERCIAL_MATURITY_PROGRAM");
assert.equal(status.e01_status, "IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION");
assert.equal(status.e01_participant_access_authorized, true);
assert.equal(status.e01_core_repository_access, false);
assert.equal(status.new_external_participant_invitation_authorized, false);
assert.equal(status.public_protocol_released, false);
assert.equal(status.commercial_access_granted, false);
assert.equal(status.production_ready, false);
assert.equal(status.public_website.operator_legal_name, "山西游骑兵电子商务有限公司");
assert.equal(status.public_website.icp_record_number, "晋ICP备2026006409号-1");
assert.match(llms, /Website operator legal name: 山西游骑兵电子商务有限公司/);
assert.match(llms, /ICP record number: 晋ICP备2026006409号-1/);
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
assert.equal(release.routes.length, 64);
assert.ok(manifest.files.length >= 80);
assert.equal(manifest.source_revision, release.source_revision);

console.log("STATIC_EXPORT_PASS=true");
console.log("ZH_EN_CONTENT_PARITY_PASS=true");
console.log("TRUTH_BOUNDARY_VALIDATION_PASS=true");
console.log(`RELEASE_MODE=${releaseContext.mode}`);
console.log(`SOURCE_REVISION=${release.source_revision}`);
console.log(`MANIFEST_FILES=${manifest.files.length}`);
