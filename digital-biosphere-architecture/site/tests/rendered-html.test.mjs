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

  const [zhRaw, enRaw] = await Promise.all([zhResponse.text(), enResponse.text()]);
  const zh = zhRaw.replace(/<html lang="[^"]+">/, '<html lang="zh-CN">');
  const en = enRaw.replace(/<html lang="[^"]+">/, '<html lang="en">');

  assert.match(zh, /TITMAS 可信多智能体基础设施开发者社区/);
  assert.match(zh, /夏日之海/);
  assert.match(zh, /\/summersea-logo\.png/);
  assert.match(en, /TITMAS Infrastructure Developer Community/);
  for (const marker of expectedMarkers.zhHome) assert.match(zh, new RegExp(marker));
  for (const marker of expectedMarkers.enHome) assert.match(en, new RegExp(marker));
  assert.match(zh, /Evidence/);
  assert.match(en, /Evidence/);
  assert.match(zh, /共同建设 Agent 时代的可信基础设施/);
  assert.match(en, /Build trustworthy infrastructure for the agent era/);
  assert.match(zh, /Community Review ≠ Architecture Decision/);
  assert.match(en, /Contribution ≠ Authority/);
  assert.match(zh, /PUBLIC CONTRIBUTION/);
  assert.match(en, /NOT ESTABLISHED/);
  assert.match(zh, /第一个可信闭环：设计完成，尚未执行/);
  assert.match(en, /The first trustworthy loop is designed—not executed/);
  assert.match(zh, /Observation ≠ Evidence/);
  assert.match(en, /Evaluation ≠ Authorization/);
  assert.match(zh, /E01 Human Compatibility Observation/);
  assert.match(en, /E01 Human Compatibility Observation/);
  assert.match(zh, /查看智能体基准证据/);
  assert.match(en, /Read the agent benchmark evidence/);
  assert.match(zh, /24\/24/);
  assert.match(en, /24\/24/);
  assert.match(zh, /AGENT START HERE/);
  assert.match(en, /Understand TITMAS at a glance/);
  assert.match(zh, /商业基础设施候选已上线，成熟度验证仍在进行/);
  assert.match(en, /commercial infrastructure candidate is live; maturity validation continues/);
  assert.match(zh, /COMMERCIAL_TECHNICAL_READY=false/);
  assert.match(en, /PAID_BETA_READY=false/);
  assert.match(zh, /TITMAS Digital Cell Demo/);
  assert.match(en, /Bring trust infrastructure into medical evidence/);
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
  const [zhRaw, enRaw] = await Promise.all([zhResponse.text(), enResponse.text()]);
  const zh = zhRaw.replace(/<html lang="[^"]+">/, '<html lang="zh-CN">');
  const en = enRaw.replace(/<html lang="[^"]+">/, '<html lang="en">');

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
  assert.match(zh, /E01_STATUS/);
  assert.match(en, /E01_STATUS/);
  assert.match(zh, /COMPENSATED_HUMAN_TRIAL_STRATEGY/);
  assert.match(en, /COMPENSATED_HUMAN_TRIAL_STRATEGY/);
});

test("returns 404 for an unknown route", async () => {
  const response = await render("/this-route-does-not-exist");
  assert.equal(response.status, 404);
});

test("ships agent-readable and discovery resources", async () => {
  const root = new URL("../public/", import.meta.url);
  await Promise.all([
    access(new URL("llms.txt", root)),
    access(new URL("agent-index.json", root)),
    access(new URL("site-catalog.json", root)),
    access(new URL("titmas-community.json", root)),
    access(new URL("updates.json", root)),
    access(new URL("status.json", root)),
    access(new URL("agent-customer-package.json", root)),
    access(new URL("dbos-public-package-manifest.json", root)),
    access(new URL("robots.txt", root)),
    access(new URL("sitemap.xml", root)),
    access(new URL("summersea-logo.png", root)),
    access(new URL("evidence/stage5-7/aggregate-results.json", root)),
    access(new URL("evidence/stage5-7/agent-selection-audit.json", root)),
    access(new URL("evidence/stage5-7/evidence-manifest.json", root)),
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
  assert.equal(status.gates.TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED, true);
  assert.equal(status.gates.TITMAS_CONTRIBUTOR_ENTRY_PREPARED, true);
  assert.equal(status.gates.TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED, false);
  assert.equal(status.gates.TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED, false);
  assert.equal(status.gates.TITMAS_CODE_OF_CONDUCT_ADOPTED, false);
  assert.equal(status.gates.TITMAS_MAINTAINER_ASSIGNED, false);
  assert.equal(status.gates.TITMAS_FOUNDATION_IN_SCOPE, false);
  assert.equal(status.community.current_state, "CONTRIBUTOR_ENTRY_PREPARED");
  assert.equal(status.community.public_contribution_surface_authorized, false);
  assert.deepEqual(status.community.maintainers, []);
  assert.equal(agentIndex.name, "TITMAS Infrastructure Developer Community");
  assert.equal(agentIndex.display_name_zh, "夏日之海");
  assert.equal(agentIndex.abbreviation, "TITMAS");
  assert.equal(agentIndex.community.direction_adopted, true);
  assert.equal(agentIndex.community.public_submission_invitation, false);
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
  assert.match(llms, /Recommendation != Decision/);
  assert.match(llms, /TITMAS Infrastructure Developer Community/);
  assert.match(llms, /TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false/);
  assert.match(llms, /Community Review != Architecture Decision/);
  assert.match(llms, /TITMAS_TECHNICAL_VALIDATION_DESIGN_COMPLETE=true/);
  assert.match(llms, /TITMAS_PILOT_EXECUTION_AUTHORIZED=false/);
  assert.match(llms, /Observation != Evidence/);
  assert.match(llms, /FIRST_EXTERNAL_ROLE=REVIEWER/);
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
