import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { resolveReleaseContext } from "./release-mode.mjs";
import { validateUpdatesCatalog } from "./update-contract.mjs";

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const outputRoot = join(siteRoot, "out");
const requiredFiles = [
  "index.html",
  "en/index.html",
  "research/index.html",
  "en/research/index.html",
  "research/index/index.html",
  "en/research/index/index.html",
  "applications/index.html",
  "en/applications/index.html",
  "demos/index.html",
  "en/demos/index.html",
  "updates/index.html",
  "en/updates/index.html",
  "updates/information-architecture-v0-1/index.html",
  "en/updates/information-architecture-v0-1/index.html",
  "updates/constitution/index.html",
  "en/updates/constitution/index.html",
  "community/index.html",
  "en/community/index.html",
  "industries/index.html",
  "en/industries/index.html",
  "industry/medical-evidence/index.html",
  "en/industry/medical-evidence/index.html",
  "demo/medical-evidence/index.html",
  "en/demo/medical-evidence/index.html",
  "medical-evidence/index.html",
  "en/medical-evidence/index.html",
  "medical-evidence-demo.json",
  "digital-cell/index.html",
  "en/digital-cell/index.html",
  "digital-cell.json",
  "digital-cell/digital-cell-architecture.png",
  "digital-cell/digital-cell-lifecycle.png",
  "digital-cell/digital-cell-report.png",
  "digital-cell/digital-cell-repository-structure.png",
  "commercial-evaluation/index.html",
  "en/commercial-evaluation/index.html",
  "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.md",
  "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.json",
  "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1-VALIDATION-REPORT.md",
  "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.md",
  "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json",
  "TITMAS-EXTERNAL-AGENT-FIRST-RUN-VALIDATION-PROTOCOL-v0.1.md",
  "TITMAS-EXTERNAL-AGENT-FIRST-RUN-VALIDATION-REPORT-v0.1.md",
  "TITMAS-FIRST-RUN-v0.1.md",
  "TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json",
  "TITMAS-AGENT-EVALUATION-ENTRY-VALIDATION-REPORT-v0.1.md",
  "architecture/titmas-agent-evaluation-entry-contract-v0.1.md",
  "architecture/schemas/titmas-agent-evaluation-entry.schema.v0.1.json",
  "architecture/schemas/titmas-commercial-evaluation-pack.schema.v0.1.json",
  "architecture/schemas/titmas-commercial-evaluation-pack.schema.v0.2.json",
  "commercial-evaluation-agent-first-run/composite-result.v0.1.json",
  "commercial-evaluation-agent-first-run/composite-result.schema.v0.1.json",
  "commercial-evaluation-agent-first-run/technical-first-run-receipt.v0.1.json",
  "commercial-evaluation-agent-first-run/technical-first-run-receipt.schema.v0.1.json",
  "examples/titmas-first-run/entity-object.synthetic.v0.1.json",
  "status/index.html",
  "en/status/index.html",
  "llms.txt",
  "site-catalog.json",
  "updates.json",
  "WEBSITE-UPDATE-CONSTITUTION-v0.1.json",
  "WEBSITE-UPDATE-CONSTITUTION-v0.1.md",
  "agent-index.json",
  "status.json",
  "titmas-community.json",
  "agent-customer-package.json",
  "dbos-public-package-manifest.json",
  "release.json",
  "release-manifest.json",
  "robots.txt",
  "sitemap.xml",
];

await Promise.all(requiredFiles.map((file) => access(join(outputRoot, file))));
await Promise.all([
  "products/agent-immune/index.html",
  "en/products/agent-immune/index.html",
  "products/agent-immune.json",
].map((file) => assert.rejects(access(join(outputRoot, file)))));

const [zh, en, zhCommunity, enCommunity, zhStatus, enStatus, status, titmasCommunity, agentCustomerPackage, dbosPackage, release, manifest, siteCatalog, updatesCatalog, websiteConstitution] = await Promise.all([
  readFile(join(outputRoot, "index.html"), "utf8"),
  readFile(join(outputRoot, "en/index.html"), "utf8"),
  readFile(join(outputRoot, "community/index.html"), "utf8"),
  readFile(join(outputRoot, "en/community/index.html"), "utf8"),
  readFile(join(outputRoot, "status/index.html"), "utf8"),
  readFile(join(outputRoot, "en/status/index.html"), "utf8"),
  readFile(join(outputRoot, "status.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "titmas-community.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "agent-customer-package.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "dbos-public-package-manifest.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "release.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "release-manifest.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "site-catalog.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "updates.json"), "utf8").then(JSON.parse),
  readFile(join(outputRoot, "WEBSITE-UPDATE-CONSTITUTION-v0.1.json"), "utf8").then(JSON.parse),
]);
validateUpdatesCatalog(updatesCatalog);
const [zhUpdates, enUpdates, zhUpdateDetail, enUpdateDetail, zhConstitution, enConstitution] = await Promise.all([
  readFile(join(outputRoot, "updates/index.html"), "utf8"),
  readFile(join(outputRoot, "en/updates/index.html"), "utf8"),
  readFile(join(outputRoot, "updates/information-architecture-v0-1/index.html"), "utf8"),
  readFile(join(outputRoot, "en/updates/information-architecture-v0-1/index.html"), "utf8"),
  readFile(join(outputRoot, "updates/constitution/index.html"), "utf8"),
  readFile(join(outputRoot, "en/updates/constitution/index.html"), "utf8"),
]);
const [zhResearch, enResearch, zhResearchIndex, enResearchIndex, zhApplications, enApplications, zhDemos, enDemos] = await Promise.all([
  readFile(join(outputRoot, "research/index.html"), "utf8"),
  readFile(join(outputRoot, "en/research/index.html"), "utf8"),
  readFile(join(outputRoot, "research/index/index.html"), "utf8"),
  readFile(join(outputRoot, "en/research/index/index.html"), "utf8"),
  readFile(join(outputRoot, "applications/index.html"), "utf8"),
  readFile(join(outputRoot, "en/applications/index.html"), "utf8"),
  readFile(join(outputRoot, "demos/index.html"), "utf8"),
  readFile(join(outputRoot, "en/demos/index.html"), "utf8"),
]);
const [zhIndustries, enIndustries, medicalIndustryPage, enMedicalIndustryPage, medicalEvidencePage, enMedicalEvidencePage, digitalCellPage, enDigitalCellPage] = await Promise.all([
  readFile(join(outputRoot, "industries/index.html"), "utf8"),
  readFile(join(outputRoot, "en/industries/index.html"), "utf8"),
  readFile(join(outputRoot, "industry/medical-evidence/index.html"), "utf8"),
  readFile(join(outputRoot, "en/industry/medical-evidence/index.html"), "utf8"),
  readFile(join(outputRoot, "demo/medical-evidence/index.html"), "utf8"),
  readFile(join(outputRoot, "en/demo/medical-evidence/index.html"), "utf8"),
  readFile(join(outputRoot, "digital-cell/index.html"), "utf8"),
  readFile(join(outputRoot, "en/digital-cell/index.html"), "utf8"),
]);
const digitalCell = await readFile(join(outputRoot, "digital-cell.json"), "utf8").then(JSON.parse);
const medicalEvidence = await readFile(join(outputRoot, "medical-evidence-demo.json"), "utf8").then(JSON.parse);
const commercialZh = await readFile(join(outputRoot, "commercial-evaluation/index.html"), "utf8");
const commercialEn = await readFile(join(outputRoot, "en/commercial-evaluation/index.html"), "utf8");
const commercialPack = await readFile(join(outputRoot, "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json"), "utf8").then(JSON.parse);
const agentEvaluationEntry = await readFile(join(outputRoot, "TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json"), "utf8").then(JSON.parse);
const commercialAgentResult = await readFile(join(outputRoot, "commercial-evaluation-agent-first-run/composite-result.v0.1.json"), "utf8").then(JSON.parse);
const commercialFixture = await readFile(join(outputRoot, "examples/titmas-first-run/entity-object.synthetic.v0.1.json"), "utf8").then(JSON.parse);
const agentIndex = await readFile(join(outputRoot, "agent-index.json"), "utf8").then(JSON.parse);
const llms = await readFile(join(outputRoot, "llms.txt"), "utf8");
const robots = await readFile(join(outputRoot, "robots.txt"), "utf8");
const sitemap = await readFile(join(outputRoot, "sitemap.xml"), "utf8");
const releaseContext = resolveReleaseContext(process.env, {
  status,
  agentIndex,
  agentCustomerPackage,
  dbosPackage,
});

assert.match(zh, /面向自治 AI 智能体生态的可信基础设施层/);
assert.match(en, /trust infrastructure layer for autonomous AI agent ecosystems/i);
assert.match(zh, /晋ICP备2026006409号-1/);
assert.match(en, /晋ICP备2026006409号-1/);
assert.match(zh, /https:\/\/beian\.miit\.gov\.cn\//);
assert.match(zh, /href="\/research\//);
assert.match(en, /href="\/en\/research\//);
for (const html of [zh, en]) {
  const prefix = html.slice(0, 50_000);
  assert.match(prefix, /id="agent-start"/);
  assert.match(prefix, /AGENT START HERE/);
  assert.match(prefix, /href="\/llms\.txt"/);
  assert.match(prefix, /href="\/agent-index\.json"/);
  assert.match(prefix, /href="\/site-catalog\.json"/);
  assert.match(html, /rel="alternate"[^>]+type="text\/plain"[^>]+llms\.txt/);
  assert.match(html, /rel="alternate"[^>]+type="application\/json"[^>]+agent-index\.json/);
  assert.match(html, /rel="alternate"[^>]+type="application\/json"[^>]+site-catalog\.json/);
  assert.match(html, /"hasPart":\[/);
}
assert.match(zh.slice(0, 50_000), /一眼理解 RedCrag/);
assert.match(en.slice(0, 50_000), /Understand RedCrag at a glance/);
assert.ok(llms.indexOf("## Agent start here") < 1_500);
assert.match(robots, /User-agent: OAI-SearchBot\s+Allow: \//);
assert.equal(siteCatalog.agent_front_door.position, "IMMEDIATELY_AFTER_HERO");
assert.equal(siteCatalog.agent_front_door.javascript_required, false);
assert.equal(agentIndex.agent_front_door.maximum_expected_source_prefix_bytes, 50_000);
assert.equal(agentIndex.agent_front_door.runtime_created, false);
assert.equal(agentIndex.agent_front_door.permission_created, false);
assert.match(zhResearch, /Evidence Governance/);
assert.match(enResearch, /Evidence ≠ Truth/);
assert.match(zhResearchIndex, /PUBLISHED_ARCHITECTURE_BASELINE/);
assert.match(enResearchIndex, /DEVELOPER_PREVIEW_RELEASED/);
assert.match(zhApplications, /医疗证据基础设施/);
assert.match(enApplications, /Manufacturing AI Agent Ecosystem/);
assert.match(zhDemos, /SYNTHETIC_DATA=true/);
assert.match(enDemos, /CLINICAL_VALIDATION=false/);
assert.match(zh, /网站结构已更新/);
assert.match(en, /Site structure updated/);
assert.match(zhUpdates, /每次变化，都要说明发生了什么/);
assert.match(enUpdates, /Every change should explain what changed/);
assert.match(zhUpdateDetail, /AVAILABLE_PRODUCTS=0/);
assert.match(enUpdateDetail, /PRODUCTION_READY=false/);
assert.match(zhConstitution, /TITMAS 网站更新宪法/);
assert.match(enConstitution, /TITMAS Website Update Constitution/);
assert.match(zhConstitution, /OpenAI/);
assert.match(zhConstitution, /OpenTelemetry/);
assert.equal(updatesCatalog.items[0].source_commit, "6a30da9c3e4ea52885ba911da50320a06191fd6f");
assert.equal(updatesCatalog.items[0].severity, null);
assert.equal(updatesCatalog.items[0].truth_boundaries.length, 3);
assert.equal(updatesCatalog.items[1].slug, "constitution");
assert.equal(updatesCatalog.items[1].source_commit, "07f69964b9b2568944bdbb0f2b2038b49c6dff93");
assert.equal(updatesCatalog.items[1].is_announcement, false);
assert.equal(websiteConstitution.default_decision_rule, "WHEN_WEBSITE_CHOICE_IS_REQUIRED_REFER_TO_OPENAI_AND_OPENTELEMETRY_FIRST");
assert.equal(websiteConstitution.effects.openai_affiliation, false);
assert.equal(websiteConstitution.effects.opentelemetry_affiliation, false);
assert.equal(websiteConstitution.effects.release_authorization, false);
assert.equal(siteCatalog.public_surfaces.products.enabled, false);
assert.equal(siteCatalog.public_surfaces.products.available_products, 0);
assert.equal(siteCatalog.public_surfaces.products.public_navigation, false);
assert.equal(siteCatalog.public_surfaces.products.sitemap_visible, false);
assert.equal(siteCatalog.extension_interfaces.products.publication_precondition, "AVAILABLE_PRODUCTS_GT_0");
assert.equal(siteCatalog.truth.available_products, 0);
assert.equal(siteCatalog.published_items.demos[1].synthetic_data, true);
assert.equal(siteCatalog.published_items.demos[1].clinical_validation, false);
assert.equal(siteCatalog.commercial_evaluation.engagement_type, "consultation");
assert.equal(siteCatalog.commercial_evaluation.product, false);
assert.match(zhCommunity, /共同建设可信多智能体基础设施/);
assert.match(enCommunity, /Build trustworthy multi-agent infrastructure together/);
assert.match(digitalCellPage, /TITMAS Digital Cell Demo/);
assert.match(digitalCellPage, /NO DIGITAL LIFE CLAIM/);
assert.match(digitalCellPage, /href="\/industries\//);
assert.match(enDigitalCellPage, /Make agent execution/);
assert.match(enDigitalCellPage, /href="\/en\/industries\//);
assert.match(zhIndustries, /TITMAS 不提供/);
assert.match(enIndustries, /TITMAS does not provide/);
assert.match(zh, /href="\/industry\/medical-evidence\//);
assert.match(en, /href="\/en\/industry\/medical-evidence\//);
assert.match(zh, /href="\/demo\/medical-evidence\//);
assert.match(en, /href="\/en\/demo\/medical-evidence\//);
assert.match(zhIndustries, /href="\/industry\/medical-evidence\//);
assert.match(enIndustries, /href="\/en\/industry\/medical-evidence\//);
assert.match(medicalIndustryPage, /医疗证据基础设施/);
assert.match(enMedicalIndustryPage, /Medical Evidence Infrastructure/);
assert.match(medicalIndustryPage, /INDEPENDENT_MEDICAL_PLATFORM=false/);
assert.match(enMedicalIndustryPage, /DIRECTION_ONLY/);
assert.match(medicalEvidencePage, /UDI-DICOM Evidence Validator Demo/);
assert.match(enMedicalEvidencePage, /UDI-DICOM Evidence Validator Demo/);
assert.match(medicalEvidencePage, /REAL_REGISTRY_LOOKUP=false/);
assert.match(enMedicalEvidencePage, /REAL_REGISTRY_LOOKUP=false/);
assert.match(medicalEvidencePage, /VALIDATOR_IMPLEMENTED_HERE=false/);
assert.match(enMedicalEvidencePage, /VALIDATOR_IMPLEMENTED_HERE=false/);
assert.equal(medicalEvidence.status, "STATIC_SYNTHETIC_UI_DEMO");
assert.equal(medicalEvidence.direction_status, "DEVELOPMENT_DIRECTION");
assert.equal(medicalEvidence.vertical_development_direction, true);
assert.equal(medicalEvidence.independent_medical_platform, false);
assert.equal(medicalEvidence.data_policy.real_registry_lookup, false);
assert.equal(medicalEvidence.boundaries.validator_implemented_here, false);
assert.equal(medicalEvidence.boundaries.clinical_validation, false);
assert.equal(medicalEvidence.boundaries.production_ready, false);
assert.equal(digitalCell.status, "REFERENCE_COMPLETE");
assert.equal(digitalCell.boundaries.production_claim, false);
assert.equal(agentIndex.entrypoints.digital_cell_demo, "/digital-cell/");
assert.equal(agentIndex.site_information_architecture.products_public_navigation, false);
assert.equal(agentIndex.site_information_architecture.available_products, 0);
assert.equal(agentIndex.products, undefined);
assert.doesNotMatch(zh, /Agent Immune|agent-health|products\/agent-immune/i);
assert.doesNotMatch(en, /Agent Immune|agent-health|products\/agent-immune/i);
assert.doesNotMatch(llms, /Agent Immune|agent-health|products\/agent-immune/i);
assert.doesNotMatch(sitemap, /Agent Immune|agent-health|products\/agent-immune/i);
assert.equal(agentIndex.entrypoints.medical_evidence_industry_zh, "/industry/medical-evidence/");
assert.equal(agentIndex.entrypoints.medical_evidence_industry_en, "/en/industry/medical-evidence/");
assert.equal(agentIndex.entrypoints.medical_evidence_demo_zh, "/demo/medical-evidence/");
assert.equal(agentIndex.entrypoints.medical_evidence_demo_en, "/en/demo/medical-evidence/");
assert.equal(agentIndex.medical_evidence_demo.real_registry_lookup, false);
assert.match(commercialZh, /商业评估包 v0\.2/);
assert.match(commercialEn, /Commercial Evaluation Pack v0\.2/);
assert.equal(commercialPack.commercial_truth.evaluation_package_prepared, true);
assert.equal(commercialPack.commercial_truth.evaluation_entry_agent_recommendable, true);
assert.equal(commercialPack.commercial_truth.available_offering, false);
assert.equal(commercialPack.commercial_truth.production_ready, false);
assert.equal(agentEvaluationEntry.evaluation_only, true);
assert.equal(agentEvaluationEntry.artifact.no_deps_allowed, false);
assert.equal(agentEvaluationEntry.discovery.contract_site_deployed, false);
assert.equal(agentEvaluationEntry.recommendation_policy.production_result, "DO_NOT_RECOMMEND_FOR_PRODUCTION");
assert.equal(agentEvaluationEntry.availability_observation.sla_defined, false);
assert.equal(agentEvaluationEntry.effects.runtime, false);
assert.equal(agentEvaluationEntry.effects.permission, false);
assert.equal(agentEvaluationEntry.effects.commercial_offer, false);
assert.equal(commercialAgentResult.status, "PASS_EVALUATION_ENTRY_AGENT_RECOMMENDABLE");
assert.equal(commercialAgentResult.agent_result.sessions_executed, 4);
assert.equal(commercialAgentResult.agent_result.distinct_providers, 2);
assert.equal(commercialAgentResult.agent_result.critical_boundary_failures, 0);
assert.equal(commercialFixture.lifecycle_state, "PROPOSED");
assert.equal(agentIndex.entrypoints.commercial_evaluation_zh, "/commercial-evaluation/");
assert.equal(agentIndex.entrypoints.commercial_evaluation_manifest, "/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json");
assert.equal(agentIndex.entrypoints.agent_evaluation_entry_contract, "/TITMAS-AGENT-EVALUATION-ENTRY-v0.1.json");
assert.equal(agentIndex.agent_evaluation_entry_contract.website_deployed, false);
if (releaseContext.mode === "candidate") {
  assert.match(zhStatus, /当前不是正式发布/);
  assert.match(enStatus, /This is not a release/);
} else {
  assert.match(zhStatus, /可信多智能体基础设施开发者预览版 v0\.1 已发布/);
  assert.match(enStatus, /Trusted Multi-Agent Infrastructure Developer Preview v0\.1 is released/);
}
assert.match(zh, /TITMAS_PUBLIC_DOMAIN/);
assert.match(en, /TITMAS_GITHUB_SLUG/);
assert.doesNotMatch(zh, /codex-preview|Your site is taking shape/);
assert.doesNotMatch(en, /codex-preview|Your site is taking shape/);
assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, true);
assert.equal(status.gates.COMMERCIAL_EVALUATION_PACKAGE_REMOTE_VALIDATED, true);
assert.equal(status.public_front_door.future_domain_live, false);
assert.equal(status.public_front_door.github_organization_created, false);
assert.equal(status.public_website.icp_filing.approved, true);
assert.equal(status.public_website.icp_filing.record_number, "晋ICP备2026006409号-1");
assert.equal(agentIndex.public_website.icp_filing_approved, true);
assert.equal(agentIndex.public_website.icp_record_number, "晋ICP备2026006409号-1");
assert.equal(titmasCommunity.github.selected_organization_slug, "titmas-cn");
assert.equal(titmasCommunity.github.organization_created, false);
assert.equal(titmasCommunity.community_state.community_established, false);
assert.equal(titmasCommunity.effects.public_contribution, false);
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
