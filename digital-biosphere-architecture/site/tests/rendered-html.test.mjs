import assert from "node:assert/strict";
import { access, readFile, readdir } from "node:fs/promises";
import test from "node:test";
import { resolveReleaseContext, routeMarkers } from "../scripts/release-mode.mjs";
import {
  selectActiveAnnouncement,
  validateUpdatesCatalog,
} from "../scripts/update-contract.mjs";

const publicRoot = new URL("../public/", import.meta.url);
const [publicStatus, publicAgentIndex, publicAgentCustomerPackage, publicDbosPackage, publicTitmasCommunity] = await Promise.all([
  readFile(new URL("status.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("agent-index.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("agent-customer-package.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("dbos-public-package-manifest.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("titmas-community.json", publicRoot), "utf8").then(JSON.parse),
]);
const releaseContext = resolveReleaseContext(process.env, {
  status: publicStatus,
  agentIndex: publicAgentIndex,
  agentCustomerPackage: publicAgentCustomerPackage,
  dbosPackage: publicDbosPackage,
});
const expectedMarkers = routeMarkers(releaseContext.mode);

assert.equal(publicTitmasCommunity.brand, "TITMAS");
assert.equal(publicTitmasCommunity.community_state.community_established, false);
assert.equal(publicTitmasCommunity.community_state.public_contribution_enabled, false);

async function render(pathname = "/") {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}-${pathname}`);
  const { default: worker } = await import(workerUrl.href);

  return worker.fetch(
    new Request(`http://localhost${pathname}`, { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
}

test("renders equivalent Chinese and English public entry points", async () => {
  const [zhResponse, enResponse] = await Promise.all([render("/"), render("/en")]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);

  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /TITMAS 可信多智能体基础设施开发者社区/);
  assert.match(en, /trust infrastructure layer for autonomous AI agent ecosystems/i);
  for (const marker of expectedMarkers.zhHome) assert.match(zh, new RegExp(marker));
  for (const marker of expectedMarkers.enHome) assert.match(en, new RegExp(marker));
  assert.match(zh, /Evidence/);
  assert.match(en, /Evidence/);
  assert.match(zh, /10 分钟判断 TITMAS/);
  assert.match(en, /Evaluate TITMAS for your multi-agent system in 10 minutes/);
  assert.match(zh, /医疗证据基础设施/);
  assert.match(en, /Medical Evidence Infrastructure/);
  assert.match(zh, /href="\/industry\/medical-evidence\//);
  assert.match(en, /href="\/en\/industry\/medical-evidence\//);
  assert.match(zh, /href="\/demo\/medical-evidence\//);
  assert.match(en, /href="\/en\/demo\/medical-evidence\//);
  assert.match(zh, /TITMAS_PUBLIC_DOMAIN/);
  assert.match(en, /TITMAS_GITHUB_SLUG/);
  assert.match(zh, /\/status\//);
  assert.match(en, /\/en\/status\//);
  assert.match(zh, /晋ICP备2026006409号-1/);
  assert.match(en, /晋ICP备2026006409号-1/);
  assert.match(zh, /https:\/\/beian\.miit\.gov\.cn\//);
  if (releaseContext.mode === "candidate") {
    assert.match(zh, /Developer Preview Candidate/);
    assert.match(en, /Developer Preview Candidate/);
    assert.doesNotMatch(zh, /production-ready|现已正式发布|已经正式发布/);
    assert.doesNotMatch(en, /production-ready|now released/i);
  } else {
    assert.doesNotMatch(zh, /Developer Preview Candidate/);
    assert.doesNotMatch(en, /Developer Preview Candidate/);
  }
});

test("renders OpenAI-inspired peer surfaces without an empty product shelf", async () => {
  const [zhResearchResponse, enResearchResponse, zhIndexResponse, enIndexResponse, zhApplicationsResponse, enApplicationsResponse, zhDemosResponse, enDemosResponse] = await Promise.all([
    render("/research"),
    render("/en/research"),
    render("/research/index"),
    render("/en/research/index"),
    render("/applications"),
    render("/en/applications"),
    render("/demos"),
    render("/en/demos"),
  ]);
  for (const response of [zhResearchResponse, enResearchResponse, zhIndexResponse, enIndexResponse, zhApplicationsResponse, enApplicationsResponse, zhDemosResponse, enDemosResponse]) {
    assert.equal(response.status, 200);
  }
  const [zhResearch, enResearch, zhIndex, enIndex, zhApplications, enApplications, zhDemos, enDemos] = await Promise.all([
    zhResearchResponse.text(),
    enResearchResponse.text(),
    zhIndexResponse.text(),
    enIndexResponse.text(),
    zhApplicationsResponse.text(),
    enApplicationsResponse.text(),
    zhDemosResponse.text(),
    enDemosResponse.text(),
  ]);
  assert.match(zhResearch, /从研究框架到可验证基础设施/);
  assert.match(enResearch, /Evidence Governance/);
  assert.match(zhIndex, /PUBLISHED_ARCHITECTURE_BASELINE/);
  assert.match(enIndex, /DEVELOPER_PREVIEW_RELEASED/);
  assert.match(zhApplications, /医疗证据基础设施/);
  assert.match(enApplications, /Manufacturing AI Agent Ecosystem/);
  assert.match(zhDemos, /SYNTHETIC_DATA=true/);
  assert.match(enDemos, /CLINICAL_VALIDATION=false/);
  for (const html of [zhResearch, enResearch, zhIndex, enIndex, zhApplications, enApplications, zhDemos, enDemos]) {
    assert.doesNotMatch(html, /href="(?:\/en)?\/products\//);
  }
});

test("renders bilingual updates, one active announcement, and the website update constitution", async () => {
  const [zhHomeResponse, enHomeResponse, zhUpdatesResponse, enUpdatesResponse, zhDetailResponse, enDetailResponse, zhConstitutionResponse, enConstitutionResponse] = await Promise.all([
    render("/"),
    render("/en"),
    render("/updates"),
    render("/en/updates"),
    render("/updates/information-architecture-v0-1"),
    render("/en/updates/information-architecture-v0-1"),
    render("/updates/constitution"),
    render("/en/updates/constitution"),
  ]);
  for (const response of [zhHomeResponse, enHomeResponse, zhUpdatesResponse, enUpdatesResponse, zhDetailResponse, enDetailResponse, zhConstitutionResponse, enConstitutionResponse]) {
    assert.equal(response.status, 200);
  }
  const [zhHome, enHome, zhUpdates, enUpdates, zhDetail, enDetail, zhConstitution, enConstitution] = await Promise.all([
    zhHomeResponse.text(),
    enHomeResponse.text(),
    zhUpdatesResponse.text(),
    enUpdatesResponse.text(),
    zhDetailResponse.text(),
    enDetailResponse.text(),
    zhConstitutionResponse.text(),
    enConstitutionResponse.text(),
  ]);
  assert.match(zhHome, /当前公告/);
  assert.match(enHome, /Current announcement/);
  assert.match(zhHome, /网站结构已更新/);
  assert.match(enHome, /Site structure updated/);
  assert.equal((zhHome.match(/class="announcement-bar"/g) || []).length, 1);
  assert.equal((enHome.match(/class="announcement-bar"/g) || []).length, 1);
  assert.match(zhUpdates, /每次变化，都要说明发生了什么/);
  assert.match(enUpdates, /Every change should explain what changed/);
  assert.match(zhDetail, /AVAILABLE_PRODUCTS=0/);
  assert.match(enDetail, /PRODUCTION_READY=false/);
  assert.match(zhConstitution, /TITMAS 网站更新宪法/);
  assert.match(enConstitution, /TITMAS Website Update Constitution/);
  assert.match(zhConstitution, /OpenAI：面向受众的信息架构/);
  assert.match(enConstitution, /OpenTelemetry: open-specification lifecycle/);
  assert.match(zhConstitution, /REFERENCE_NE_ADOPTION/);
  assert.match(enConstitution, /REFERENCE_NE_ENDORSEMENT/);
});

test("enforces deterministic announcement selection and update provenance", async () => {
  const updates = await readFile(new URL("../public/updates.json", import.meta.url), "utf8").then(JSON.parse);
  assert.equal(validateUpdatesCatalog(updates), true);
  assert.equal(selectActiveAnnouncement(updates.items, new Date("2026-07-28T13:20:00+08:00")).slug, "information-architecture-v0-1");
  assert.equal(selectActiveAnnouncement(updates.items, new Date("2026-09-01T00:00:00+08:00")), null);

  const selectionFixtures = [
    {
      slug: "release",
      category: "RELEASE_NOTE",
      status: "PUBLISHED",
      is_announcement: true,
      severity: null,
      effective_date: "2026-07-28T10:00:00+08:00",
      expires_at: "2026-08-20T00:00:00+08:00",
    },
    {
      slug: "maintenance",
      category: "MAINTENANCE_NOTICE",
      status: "PUBLISHED",
      is_announcement: true,
      severity: "high",
      effective_date: "2026-07-27T10:00:00+08:00",
      expires_at: "2026-08-10T00:00:00+08:00",
    },
  ];
  assert.equal(selectActiveAnnouncement(selectionFixtures, new Date("2026-07-29T00:00:00+08:00")).slug, "maintenance");

  const invalidSupersedes = structuredClone(updates);
  invalidSupersedes.items[0].supersedes = "missing-update";
  assert.throws(() => validateUpdatesCatalog(invalidSupersedes), /SUPERSEDES_TARGET_NOT_FOUND/);
});

test("renders bilingual commercial evaluation entry with fail-closed truth", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/commercial-evaluation"),
    render("/en/commercial-evaluation"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /商业评估包 v0\.2/);
  assert.match(en, /Commercial Evaluation Pack v0\.2/);
  assert.match(zh, /4\/4 智能体推荐用于离线评估/);
  assert.match(en, /4\/4 recommend offline evaluation/);
  assert.match(zh, /AVAILABLE_OFFERING=false/);
  assert.match(en, /PASS ≠ TRUTH/);
});

test("renders complete bilingual TITMAS community entry points", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/community"),
    render("/en/community"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);

  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /共同建设可信多智能体基础设施/);
  assert.match(en, /Build trustworthy multi-agent infrastructure together/);
  assert.match(zh, /Organization 未创建/);
  assert.match(en, /organization that does not exist/i);
  assert.match(zh, /COMMUNITY_ESTABLISHED=false/);
  assert.match(en, /PUBLIC_CONTRIBUTION_ENABLED=false/);
});

test("renders clickable bilingual industry application entry points", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/industries"),
    render("/en/industries"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /智能制造智能体生态/);
  assert.match(zh, /TITMAS 不提供/);
  assert.match(en, /Manufacturing AI Agent Ecosystem/);
  assert.match(en, /TITMAS does not provide/);
  assert.match(zh, /href="\/digital-cell\//);
  assert.match(en, /href="\/en\/digital-cell\//);
  assert.match(zh, /href="\/industry\/medical-evidence\//);
  assert.match(en, /href="\/en\/industry\/medical-evidence\//);
});

test("renders bilingual medical evidence industry application with explicit infrastructure positioning", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/industry/medical-evidence"),
    render("/en/industry/medical-evidence"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /医疗证据基础设施/);
  assert.match(en, /Medical Evidence Infrastructure/);
  assert.match(zh, /未来医疗系统不是缺少数据/);
  assert.match(en, /Future medical systems will not lack data/);
  assert.match(zh, /INDEPENDENT_MEDICAL_PLATFORM=false/);
  assert.match(en, /INDEPENDENT_MEDICAL_PLATFORM=false/);
  assert.match(zh, /DIRECTION_ONLY/);
  assert.match(en, /DIRECTION_ONLY/);
  assert.match(zh, /href="\/demo\/medical-evidence\//);
  assert.match(en, /href="\/en\/demo\/medical-evidence\//);
});

test("renders bilingual synthetic medical evidence reference demo with explicit boundaries", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/demo/medical-evidence"),
    render("/en/demo/medical-evidence"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /UDI-DICOM Evidence Validator Demo/);
  assert.match(en, /UDI-DICOM Evidence Validator Demo/);
  assert.match(zh, /SYNTHETIC_DATA_ONLY/);
  assert.match(en, /REAL_REGISTRY_LOOKUP=false/);
  assert.match(zh, /VALIDATOR_IMPLEMENTED_HERE=false/);
  assert.match(en, /VALIDATOR_IMPLEMENTED_HERE=false/);
  assert.match(zh, /不执行医疗 Validator/);
  assert.match(en, /does not implement a medical validator/);
  assert.match(zh, /不构成监管认证或合规背书/);
  assert.match(en, /No regulatory certification or compliance endorsement/);
  assert.match(zh, /href="\/industry\/medical-evidence\//);
  assert.match(en, /href="\/en\/industry\/medical-evidence\//);
});

test("renders bilingual Digital Cell pages with shared return navigation", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/digital-cell"),
    render("/en/digital-cell"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /REFERENCE_COMPLETE/);
  assert.match(en, /REFERENCE_COMPLETE/);
  assert.match(zh, /href="\/industries\//);
  assert.match(en, /href="\/en\/industries\//);
  assert.match(zh, /href="\/"/);
  assert.match(en, /href="\/en\/"/);
  assert.match(zh, /NO PRODUCTION CERTIFICATION/);
  assert.match(en, /NO PRODUCTION CERTIFICATION/);
});

test("renders bilingual status pages with fail-closed truth", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/status"),
    render("/en/status"),
  ]);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  for (const marker of expectedMarkers.zhStatus) assert.match(zh, new RegExp(marker.replace(".", "\\.")));
  for (const marker of expectedMarkers.enStatus) assert.match(en, new RegExp(marker.replace(".", "\\.")));
  assert.match(zh, /AGENT_CUSTOMER_VALIDATION_BASELINE/);
  assert.match(en, /AGENT_CUSTOMER_VALIDATION_BASELINE/);
  assert.match(zh, /PASS/);
  assert.match(en, /PASS/);
  assert.match(zh, /PARTIAL/);
  assert.match(en, /PARTIAL/);
  assert.match(zh, /cd3f867c4379/);
  assert.match(en, /2173c258f91a/);
});

test("ships agent-readable and discovery resources", async () => {
  const root = new URL("../public/", import.meta.url);
  await Promise.all([
    access(new URL("llms.txt", root)),
    access(new URL("site-catalog.json", root)),
    access(new URL("updates.json", root)),
    access(new URL("WEBSITE-UPDATE-CONSTITUTION-v0.1.json", root)),
    access(new URL("WEBSITE-UPDATE-CONSTITUTION-v0.1.md", root)),
    access(new URL("agent-index.json", root)),
    access(new URL("status.json", root)),
    access(new URL("agent-customer-package.json", root)),
    access(new URL("dbos-public-package-manifest.json", root)),
    access(new URL("titmas-community.json", root)),
    access(new URL("robots.txt", root)),
    access(new URL("sitemap.xml", root)),
    access(new URL("medical-evidence-demo.json", root)),
    access(new URL("TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.json", root)),
    access(new URL("TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json", root)),
    access(new URL("TITMAS-EXTERNAL-AGENT-FIRST-RUN-VALIDATION-REPORT-v0.1.md", root)),
    access(new URL("TITMAS-FIRST-RUN-v0.1.md", root)),
    access(new URL("architecture/schemas/titmas-commercial-evaluation-pack.schema.v0.1.json", root)),
    access(new URL("architecture/schemas/titmas-commercial-evaluation-pack.schema.v0.2.json", root)),
    access(new URL("commercial-evaluation-agent-first-run/composite-result.v0.1.json", root)),
    access(new URL("examples/titmas-first-run/entity-object.synthetic.v0.1.json", root)),
  ]);

  const [agentIndex, status, agentCustomerPackage, dbosPackage, titmasCommunity, medicalEvidence, siteCatalog, updatesCatalog, websiteConstitution, llms] = await Promise.all([
    readFile(new URL("agent-index.json", root), "utf8").then(JSON.parse),
    readFile(new URL("status.json", root), "utf8").then(JSON.parse),
    readFile(new URL("agent-customer-package.json", root), "utf8").then(JSON.parse),
    readFile(new URL("dbos-public-package-manifest.json", root), "utf8").then(JSON.parse),
    readFile(new URL("titmas-community.json", root), "utf8").then(JSON.parse),
    readFile(new URL("medical-evidence-demo.json", root), "utf8").then(JSON.parse),
    readFile(new URL("site-catalog.json", root), "utf8").then(JSON.parse),
    readFile(new URL("updates.json", root), "utf8").then(JSON.parse),
    readFile(new URL("WEBSITE-UPDATE-CONSTITUTION-v0.1.json", root), "utf8").then(JSON.parse),
    readFile(new URL("llms.txt", root), "utf8"),
  ]);
  assert.equal(agentIndex.entrypoints.site_catalog, "/site-catalog.json");
  assert.equal(agentIndex.entrypoints.research_zh, "/research/");
  assert.equal(agentIndex.entrypoints.applications_en, "/en/applications/");
  assert.equal(agentIndex.entrypoints.demos_zh, "/demos/");
  assert.equal(agentIndex.entrypoints.updates_zh, "/updates/");
  assert.equal(agentIndex.entrypoints.updates_machine, "/updates.json");
  assert.equal(agentIndex.entrypoints.website_update_constitution_machine, "/WEBSITE-UPDATE-CONSTITUTION-v0.1.json");
  assert.equal(updatesCatalog.announcement_policy.maximum_visible, 1);
  assert.equal(updatesCatalog.items[0].source_commit.length, 40);
  assert.equal(updatesCatalog.items[0].truth_boundaries[0].scope, "PRODUCT_AVAILABILITY");
  assert.equal(websiteConstitution.default_decision_rule, "WHEN_WEBSITE_CHOICE_IS_REQUIRED_REFER_TO_OPENAI_AND_OPENTELEMETRY_FIRST");
  assert.equal(websiteConstitution.effects.openai_affiliation, false);
  assert.equal(websiteConstitution.effects.opentelemetry_affiliation, false);
  assert.equal(websiteConstitution.effects.release_authorization, false);
  assert.equal(agentIndex.website_update_governance.reference_creates_affiliation, false);
  assert.match(llms, /WHEN_WEBSITE_CHOICE_IS_REQUIRED_REFER_TO_OPENAI_AND_OPENTELEMETRY_FIRST/);
  assert.match(llms, /ANNOUNCEMENT_NE_RELEASE_AUTHORIZATION=true/);
  assert.equal(siteCatalog.public_surfaces.products.enabled, false);
  assert.equal(siteCatalog.public_surfaces.products.available_products, 0);
  assert.equal(siteCatalog.truth.future_placeholder_items_published, 0);
  assert.equal(siteCatalog.commercial_evaluation.engagement_type, "consultation");
  assert.equal(siteCatalog.published_items.demos[1].synthetic_data, true);
  assert.equal(siteCatalog.published_items.demos[1].clinical_validation, false);
  assert.equal(agentIndex.released, releaseContext.developerPreviewReleased);
  assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, true);
  assert.equal(status.public_front_door.future_primary_domain, "https://titmas.cn/");
  assert.equal(status.public_front_door.future_domain_live, false);
  assert.equal(status.public_front_door.selected_github_organization_slug, "titmas-cn");
  assert.equal(status.public_front_door.github_organization_created, false);
  assert.equal(agentIndex.public_brand, "TITMAS");
  assert.equal(agentIndex.developer_community.community_established, false);
  assert.equal(agentIndex.entrypoints.titmas_community, "/titmas-community.json");
  assert.equal(agentIndex.entrypoints.commercial_evaluation_zh, "/commercial-evaluation/");
  assert.equal(agentIndex.entrypoints.commercial_evaluation_manifest, "/TITMAS-COMMERCIAL-EVALUATION-PACK-v0.2.json");
  assert.equal(agentIndex.entrypoints.industries_zh, "/industries/");
  assert.equal(agentIndex.entrypoints.industries_en, "/en/industries/");
  assert.equal(agentIndex.entrypoints.medical_evidence_industry_zh, "/industry/medical-evidence/");
  assert.equal(agentIndex.entrypoints.medical_evidence_industry_en, "/en/industry/medical-evidence/");
  assert.equal(agentIndex.entrypoints.medical_evidence_demo_zh, "/demo/medical-evidence/");
  assert.equal(agentIndex.entrypoints.medical_evidence_demo_en, "/en/demo/medical-evidence/");
  assert.equal(medicalEvidence.application_positioning, "TITMAS_INDUSTRY_APPLICATION_NOT_MEDICAL_SOFTWARE");
  assert.equal(medicalEvidence.status, "STATIC_SYNTHETIC_UI_DEMO");
  assert.equal(medicalEvidence.direction_status, "DEVELOPMENT_DIRECTION");
  assert.equal(medicalEvidence.vertical_development_direction, true);
  assert.equal(medicalEvidence.independent_medical_platform, false);
  assert.equal(medicalEvidence.data_policy.patient_data_used, false);
  assert.equal(medicalEvidence.boundaries.validator_implemented_here, false);
  assert.equal(medicalEvidence.boundaries.clinical_validation, false);
  assert.equal(medicalEvidence.boundaries.regulatory_certification_claim, false);
  assert.equal(titmasCommunity.public_front_door.future_domain_filing_status, "PENDING");
  assert.equal(titmasCommunity.github.organization_created, false);
  assert.equal(titmasCommunity.community_state.public_contribution_enabled, false);
  assert.equal(titmasCommunity.effects.authority, false);
  assert.equal(status.gates.DQ_010_SUPERSEDED_FOR_PRIMARY_ROUTE, true);
  assert.equal(status.gates.AGENT_CUSTOMER_VALIDATION_BASELINE_CONDITIONAL, true);
  assert.equal(status.gates.AGENT_CUSTOMER_VALIDATION_RERUN_PASS, true);
  assert.equal(status.gates.COMMERCIAL_EVALUATION_PACKAGE_REMOTE_VALIDATED, true);
  assert.equal(status.agent_customer_validation.api_sessions_completed, 12);
  assert.equal(status.agent_customer_validation.result, "PASS");
  assert.equal(status.agent_customer_validation.open_web_discovery, "NOT_ASSESSED");
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
  assert.equal(dbosPackage.public_safe_boundary.absolute_user_path_matches, 0);
  assert.equal(status.gates.DBOS_PUBLIC_SAFE_WHEEL_VALIDATED, true);
  assert.equal(status.license.selected, true);
  assert.equal(status.license.identifier, "Apache-2.0");
  assert.equal(status.public_website.deployed, true);
  assert.equal(status.public_website.rollback_validated, true);
  assert.equal(status.public_website.icp_filing.approved, true);
  assert.equal(status.public_website.icp_filing.record_number, "晋ICP备2026006409号-1");
  assert.deepEqual(status.public_website.icp_filing.covered_domains, ["redcrag.cn", "www.redcrag.cn"]);
  assert.equal(agentIndex.public_website.icp_filing_approved, true);
  assert.equal(agentIndex.public_website.icp_record_number, "晋ICP备2026006409号-1");
  assert.match(llms, /ICP filing: APPROVED/);
  assert.match(llms, /ICP record number: 晋ICP备2026006409号-1/);
  assert.equal(status.production_path.otlp_reference_candidate_version, "1.11.0");
  assert.equal(status.production_path.otlp_reference_version_status, "ADOPTED_REFERENCE_NOT_RUNTIME_PROOF");
  assert.equal(status.production_path.dq_022_status, "DECIDED_REFERENCE_ADOPTED");
  assert.equal(status.production_path.dq_022_human_decision_recorded, true);
  assert.equal(status.production_path.otlp_reference_adoption_recommended_by_two_agents, true);
  assert.equal(status.production_path.opentelemetry_production_alignment_matrix_defined, true);
  assert.equal(status.production_path.production_gate_evidence_manifest_contract_defined, true);
  assert.equal(status.production_path.production_gate_evidence_profile_registry_status, "PROPOSED_NOT_ADOPTED");
  assert.equal(status.production_path.production_gate_evidence_validator_implemented, false);
  assert.equal(status.production_path.any_production_gate_pass_created, false);
  assert.equal(status.production_path.production_evidence_contract_agent_review_complete, true);
  assert.equal(status.production_path.s0_architecture_contract_freeze_recommended_by_two_agents, true);
  assert.equal(status.production_path.s0_architecture_freeze_design_blockers, 0);
  assert.equal(
    agentIndex.production_path.otlp_reference_candidate_version,
    status.production_path.otlp_reference_candidate_version,
  );
  assert.equal(agentIndex.production_path.otlp_reference_version_adopted, true);
  assert.equal(agentIndex.production_path.dq_022_status, "DECIDED_REFERENCE_ADOPTED");
  assert.equal(agentIndex.production_path.production_gate_evidence_manifest_contract_defined, true);
  assert.equal(agentIndex.production_path.production_gate_evidence_validator_implemented, false);
  assert.equal(agentIndex.production_path.any_production_gate_pass_created, false);
  assert.equal(agentIndex.production_path.s0_architecture_contract_freeze_recommended_by_two_agents, true);
  assert.match(llms, /Recommendation != Decision/);
  assert.match(llms, /Future domain status: SELECTED, FILING_PENDING, NOT_LIVE/);
  assert.match(llms, /Selected GitHub organization slug: titmas-cn/);
  assert.match(llms, /production-gate-evidence-manifest-specification/);
  assert.match(llms, /production-gate-evidence-manifest\.schema\.v0\.1\.json/);
  assert.match(llms, /DQ_022_STATUS=DECIDED_REFERENCE_ADOPTED/);
  assert.match(llms, /OTLP_REFERENCE_VERSION_ADOPTED=true/);
  assert.match(llms, /DBOS records -> SAEE evaluation\/recommendation -> Governance Decision review\/adoption -> DBOS authorized execution/);
  assert.match(llms, /OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY/);
  assert.match(llms, /COMMERCIAL_EVALUATION_PACKAGE_PREPARED=true/);
  assert.match(llms, /EXTERNAL_AGENT_FIRST_RUN_VALIDATION=PASS/);
  assert.match(llms, /EVALUATION_RECOMMENDED=4\/4/);
  assert.match(llms, /PRODUCTION_NOT_RECOMMENDED=4\/4/);
  assert.match(
    llms,
    releaseContext.mode === "candidate"
      ? /DBOS_PUBLIC_SAFE_WHEEL=VALIDATED_NOT_PUBLISHED/
      : /DBOS_PUBLIC_SAFE_WHEEL=PUBLISHED/,
  );
});

test("removes the disposable starter preview", async () => {
  const root = new URL("../", import.meta.url);
  await assert.rejects(access(new URL("app/_sites-preview", root)));
  const packageJson = await readFile(new URL("package.json", root), "utf8");
  const page = await readFile(new URL("app/page.tsx", root), "utf8");
  assert.doesNotMatch(packageJson, /react-loading-skeleton/);
  assert.doesNotMatch(page, /codex-preview|SkeletonPreview/);
});

test("does not retain stale generated font assets", async () => {
  const assetsRoot = new URL("../dist/client/assets/", import.meta.url);
  const entries = await readdir(assetsRoot);
  assert.equal(entries.some((entry) => entry.startsWith("_vinext_fonts")), false);
});
