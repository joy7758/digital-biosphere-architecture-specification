import assert from "node:assert/strict";
import { access, readFile, readdir } from "node:fs/promises";
import test from "node:test";
import { resolveReleaseContext, routeMarkers } from "../scripts/release-mode.mjs";

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
  assert.match(zh, /<title>[^<]*第一版商业评估包 v0\.2[^<]*<\/title>/);
  assert.match(en, /<title>[^<]*Commercial Evaluation Pack v0\.2[^<]*<\/title>/);
  assert.match(zh, /href="\/TITMAS-COMMERCIAL-EVALUATION-PACK-v0\.2\.json"/);
  assert.match(en, /href="\/TITMAS-COMMERCIAL-EVALUATION-PACK-v0\.2\.json"/);
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
  assert.match(zh, /href="\/medical-evidence\//);
  assert.match(en, /href="\/en\/medical-evidence\//);
});

test("renders bilingual synthetic medical evidence demo with explicit boundaries", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/medical-evidence"),
    render("/en/medical-evidence"),
  ]);
  assert.equal(zhResponse.status, 200);
  assert.equal(enResponse.status, 200);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /UDI-DICOM 证据链验证器/);
  assert.match(en, /UDI-DICOM Evidence Chain Validator/);
  assert.match(zh, /SYNTHETIC_DATA_ONLY/);
  assert.match(en, /REAL_REGISTRY_LOOKUP=false/);
  assert.match(zh, /VALIDATOR_IMPLEMENTED_HERE=false/);
  assert.match(en, /VALIDATOR_IMPLEMENTED_HERE=false/);
  assert.match(zh, /不执行医疗 Validator/);
  assert.match(en, /does not implement a medical validator/);
  assert.match(zh, /不构成监管认证或合规背书/);
  assert.match(en, /No regulatory certification or compliance endorsement/);
  assert.match(zh, /href="\/industries\//);
  assert.match(en, /href="\/en\/industries\//);
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

  const [agentIndex, status, agentCustomerPackage, dbosPackage, titmasCommunity, medicalEvidence, llms] = await Promise.all([
    readFile(new URL("agent-index.json", root), "utf8").then(JSON.parse),
    readFile(new URL("status.json", root), "utf8").then(JSON.parse),
    readFile(new URL("agent-customer-package.json", root), "utf8").then(JSON.parse),
    readFile(new URL("dbos-public-package-manifest.json", root), "utf8").then(JSON.parse),
    readFile(new URL("titmas-community.json", root), "utf8").then(JSON.parse),
    readFile(new URL("medical-evidence-demo.json", root), "utf8").then(JSON.parse),
    readFile(new URL("llms.txt", root), "utf8"),
  ]);
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
  assert.equal(agentIndex.entrypoints.medical_evidence_demo_zh, "/medical-evidence/");
  assert.equal(agentIndex.entrypoints.medical_evidence_demo_en, "/en/medical-evidence/");
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
