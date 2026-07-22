import assert from "node:assert/strict";
import { access, readFile, readdir } from "node:fs/promises";
import test from "node:test";
import { resolveReleaseContext, routeMarkers } from "../scripts/release-mode.mjs";

const publicRoot = new URL("../public/", import.meta.url);
const [publicStatus, publicAgentIndex, publicAgentCustomerPackage, publicDbosPackage] = await Promise.all([
  readFile(new URL("status.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("agent-index.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("agent-customer-package.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("dbos-public-package-manifest.json", publicRoot), "utf8").then(JSON.parse),
]);
const releaseContext = resolveReleaseContext(process.env, {
  status: publicStatus,
  agentIndex: publicAgentIndex,
  agentCustomerPackage: publicAgentCustomerPackage,
  dbosPackage: publicDbosPackage,
});
const expectedMarkers = routeMarkers(releaseContext.mode);

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
  assert.match(zh, /面向长期、协作和可验证数字主体的基础设施|面向长期运行、协作和可验证数字主体的基础设施/);
  assert.match(en, /Infrastructure for long-running, collaborative, and verifiable digital entities/);
  for (const marker of expectedMarkers.zhHome) assert.match(zh, new RegExp(marker));
  for (const marker of expectedMarkers.enHome) assert.match(en, new RegExp(marker));
  assert.match(zh, /Evidence/);
  assert.match(en, /Evidence/);
  assert.match(zh, /SAEE_DBOS_ADAPTER_PASS/);
  assert.match(en, /SAEE_DBOS_ADAPTER_PASS/);
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
    access(new URL("robots.txt", root)),
    access(new URL("sitemap.xml", root)),
  ]);

  const [agentIndex, status, agentCustomerPackage, dbosPackage, llms] = await Promise.all([
    readFile(new URL("agent-index.json", root), "utf8").then(JSON.parse),
    readFile(new URL("status.json", root), "utf8").then(JSON.parse),
    readFile(new URL("agent-customer-package.json", root), "utf8").then(JSON.parse),
    readFile(new URL("dbos-public-package-manifest.json", root), "utf8").then(JSON.parse),
    readFile(new URL("llms.txt", root), "utf8"),
  ]);
  assert.equal(agentIndex.released, releaseContext.developerPreviewReleased);
  assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, true);
  assert.equal(status.gates.DQ_010_SUPERSEDED_FOR_PRIMARY_ROUTE, true);
  assert.equal(status.gates.AGENT_CUSTOMER_VALIDATION_BASELINE_CONDITIONAL, true);
  assert.equal(status.gates.AGENT_CUSTOMER_VALIDATION_RERUN_PASS, true);
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
  assert.match(llms, /production-gate-evidence-manifest-specification/);
  assert.match(llms, /production-gate-evidence-manifest\.schema\.v0\.1\.json/);
  assert.match(llms, /DQ_022_STATUS=DECIDED_REFERENCE_ADOPTED/);
  assert.match(llms, /OTLP_REFERENCE_VERSION_ADOPTED=true/);
  assert.match(llms, /DBOS records -> SAEE evaluation\/recommendation -> Governance Decision review\/adoption -> DBOS authorized execution/);
  assert.match(llms, /OPEN_WEB_DISCOVERY=PARTIAL_METADATA_ONLY/);
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
