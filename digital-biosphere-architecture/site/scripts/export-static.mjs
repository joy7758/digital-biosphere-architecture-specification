import { createHash } from "node:crypto";
import { cp, mkdir, readdir, readFile, rm, stat, writeFile } from "node:fs/promises";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { resolveReleaseContext, routeMarkers } from "./release-mode.mjs";

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const outputRoot = join(siteRoot, "out");
const clientRoot = join(siteRoot, "dist", "client");
const serverEntry = join(siteRoot, "dist", "server", "index.js");
const sourceRevision = process.env.SOURCE_REVISION || "working-tree";
const generatedAt = new Date().toISOString();

const [status, agentIndex, agentCustomerPackage, dbosPackage] = await Promise.all([
  readFile(join(siteRoot, "public", "status.json"), "utf8").then(JSON.parse),
  readFile(join(siteRoot, "public", "agent-index.json"), "utf8").then(JSON.parse),
  readFile(join(siteRoot, "public", "agent-customer-package.json"), "utf8").then(JSON.parse),
  readFile(join(siteRoot, "public", "dbos-public-package-manifest.json"), "utf8").then(JSON.parse),
]);
const releaseContext = resolveReleaseContext(process.env, {
  status,
  agentIndex,
  agentCustomerPackage,
  dbosPackage,
});
const markers = routeMarkers(releaseContext.mode);

const routes = [
  { request: "/", output: "index.html", markers: markers.zhHome },
  { request: "/en", output: "en/index.html", markers: markers.enHome },
  { request: "/research", output: "research/index.html", markers: ["从研究框架到可验证基础设施", "Evidence Governance", "Evidence ≠ Truth"] },
  { request: "/en/research", output: "en/research/index.html", markers: ["From research frames to verifiable infrastructure", "Evidence Governance", "Evidence ≠ Truth"] },
  { request: "/research/index", output: "research/index/index.html", markers: ["研究索引", "PUBLISHED_ARCHITECTURE_BASELINE", "DEVELOPER_PREVIEW_RELEASED"] },
  { request: "/en/research/index", output: "en/research/index/index.html", markers: ["Research index", "PUBLISHED_ARCHITECTURE_BASELINE", "DEVELOPER_PREVIEW_RELEASED"] },
  { request: "/applications", output: "applications/index.html", markers: ["可信基础设施如何进入行业", "Space Agent Evidence Profile", "PUBLISHED_RESEARCH_PROFILE"] },
  { request: "/en/applications", output: "en/applications/index.html", markers: ["How trust infrastructure enters industries", "Space Agent Evidence Profile", "PUBLISHED_RESEARCH_PROFILE"] },
  { request: "/demos", output: "demos/index.html", markers: ["用可检查的演示理解基础设施", "REFERENCE_COMPLETE", "CLINICAL_VALIDATION=false"] },
  { request: "/en/demos", output: "en/demos/index.html", markers: ["Understand the infrastructure through inspectable demos", "REFERENCE_COMPLETE", "CLINICAL_VALIDATION=false"] },
  { request: "/updates", output: "updates/index.html", markers: ["每次变化，都要说明发生了什么", "RELEASE_NOTE", "网站更新宪法"] },
  { request: "/en/updates", output: "en/updates/index.html", markers: ["Every change should explain what changed", "RELEASE_NOTE", "Website Update Constitution"] },
  { request: "/updates/information-architecture-v0-1", output: "updates/information-architecture-v0-1/index.html", markers: ["网站结构已更新", "AVAILABLE_PRODUCTS=0", "6a30da9c3e4ea52885ba911da50320a06191fd6f"] },
  { request: "/en/updates/information-architecture-v0-1", output: "en/updates/information-architecture-v0-1/index.html", markers: ["Site structure updated", "AVAILABLE_PRODUCTS=0", "6a30da9c3e4ea52885ba911da50320a06191fd6f"] },
  { request: "/updates/constitution", output: "updates/constitution/index.html", markers: ["TITMAS 网站更新宪法", "REFERENCE_NE_ADOPTION", "OpenTelemetry"] },
  { request: "/en/updates/constitution", output: "en/updates/constitution/index.html", markers: ["TITMAS Website Update Constitution", "REFERENCE_NE_ENDORSEMENT", "OpenTelemetry"] },
  { request: "/community", output: "community/index.html", markers: ["共同建设可信多智能体基础设施", "COMMUNITY_ESTABLISHED=false"] },
  { request: "/en/community", output: "en/community/index.html", markers: ["Build trustworthy multi-agent infrastructure together", "COMMUNITY_ESTABLISHED=false"] },
  { request: "/industries", output: "industries/index.html", markers: ["智能制造智能体生态", "TITMAS 不提供", "Space Agent Evidence Profile"] },
  { request: "/en/industries", output: "en/industries/index.html", markers: ["Manufacturing AI Agent Ecosystem", "TITMAS does not provide", "Space Agent Evidence Profile"] },
  { request: "/industry/medical-evidence", output: "industry/medical-evidence/index.html", markers: ["医疗证据基础设施", "INDEPENDENT_MEDICAL_PLATFORM=false", "Medical Agent Evidence"] },
  { request: "/en/industry/medical-evidence", output: "en/industry/medical-evidence/index.html", markers: ["Medical Evidence Infrastructure", "INDEPENDENT_MEDICAL_PLATFORM=false", "Medical Agent Evidence"] },
  { request: "/industry/space-agent-evidence", output: "industry/space-agent-evidence/index.html", markers: ["自主航天智能体可信执行", "SAEP_STATUS=RESEARCH_PROTOTYPE", "FLIGHT_CERTIFICATION_CLAIM=false"] },
  { request: "/en/industry/space-agent-evidence", output: "en/industry/space-agent-evidence/index.html", markers: ["Space Agent Evidence Profile", "SAEP_STATUS=RESEARCH_PROTOTYPE", "FLIGHT_CERTIFICATION_CLAIM=false"] },
  { request: "/demo/medical-evidence", output: "demo/medical-evidence/index.html", markers: ["UDI-DICOM Evidence Validator Demo", "SYNTHETIC_DATA_ONLY", "REAL_REGISTRY_LOOKUP=false"] },
  { request: "/en/demo/medical-evidence", output: "en/demo/medical-evidence/index.html", markers: ["UDI-DICOM Evidence Validator Demo", "SYNTHETIC_DATA_ONLY", "REAL_REGISTRY_LOOKUP=false"] },
  { request: "/medical-evidence", output: "medical-evidence/index.html", markers: ["UDI-DICOM Evidence Validator Demo", "SYNTHETIC_DATA_ONLY", "REAL_REGISTRY_LOOKUP=false"] },
  { request: "/en/medical-evidence", output: "en/medical-evidence/index.html", markers: ["UDI-DICOM Evidence Validator Demo", "SYNTHETIC_DATA_ONLY", "REAL_REGISTRY_LOOKUP=false"] },
  { request: "/digital-cell", output: "digital-cell/index.html", markers: ["TITMAS Digital Cell Demo", "REFERENCE_COMPLETE", "NO DIGITAL LIFE CLAIM"] },
  { request: "/commercial-evaluation", output: "commercial-evaluation/index.html", markers: ["商业评估包 v0.2", "AGENT_FIRST_RUN_VALIDATED"] },
  { request: "/en/commercial-evaluation", output: "en/commercial-evaluation/index.html", markers: ["Commercial Evaluation Pack v0.2", "AGENT_FIRST_RUN_VALIDATED"] },
  { request: "/en/digital-cell", output: "en/digital-cell/index.html", markers: ["Make agent execution", "REFERENCE_COMPLETE", "NO DIGITAL LIFE CLAIM"] },
  { request: "/status", output: "status/index.html", markers: markers.zhStatus },
  { request: "/en/status", output: "en/status/index.html", markers: markers.enStatus },
];

await rm(outputRoot, { recursive: true, force: true });
await mkdir(outputRoot, { recursive: true });
await cp(clientRoot, outputRoot, { recursive: true });

const workerUrl = pathToFileURL(serverEntry);
workerUrl.searchParams.set("export", `${process.pid}-${Date.now()}`);
const { default: worker } = await import(workerUrl.href);

for (const route of routes) {
  const response = await worker.fetch(
    new Request(`https://redcrag.cn${route.request}`, {
      headers: { accept: "text/html" },
    }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );

  if (response.status !== 200) {
    throw new Error(`Cannot export ${route.request}: HTTP ${response.status}`);
  }

  const html = await response.text();
  for (const marker of route.markers) {
    if (!html.includes(marker)) {
      throw new Error(`Cannot export ${route.request}: expected marker is absent: ${marker}`);
    }
  }

  const target = join(outputRoot, route.output);
  await mkdir(dirname(target), { recursive: true });
  await writeFile(target, html, "utf8");
}

await writeFile(
  join(outputRoot, "release.json"),
  `${JSON.stringify(
    {
      schema_version: "0.1",
      artifact: "titmas-infrastructure-developer-community-website",
      source_revision: sourceRevision,
      generated_at: generatedAt,
      release_mode: releaseContext.mode,
      deployment_state: releaseContext.deploymentState,
      developer_preview_released: releaseContext.developerPreviewReleased,
      release_decision_reference: releaseContext.releaseDecisionReference,
      released_by_ref: releaseContext.releasedByRef,
      public_release_tag: releaseContext.publicReleaseTag,
      dbos_public_package_url: releaseContext.dbosWheelUrl,
      routes: routes.map((route) => route.request),
    },
    null,
    2,
  )}\n`,
  "utf8",
);

async function listFiles(root, current = root) {
  const entries = await readdir(current, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const absolute = join(current, entry.name);
    if (entry.isDirectory()) files.push(...(await listFiles(root, absolute)));
    else if (entry.isFile() && entry.name !== "release-manifest.json") files.push(absolute);
  }
  return files;
}

const manifestFiles = [];
for (const absolute of (await listFiles(outputRoot)).sort()) {
  const bytes = await readFile(absolute);
  const metadata = await stat(absolute);
  manifestFiles.push({
    path: relative(outputRoot, absolute),
    bytes: metadata.size,
    sha256: createHash("sha256").update(bytes).digest("hex"),
  });
}

await writeFile(
  join(outputRoot, "release-manifest.json"),
  `${JSON.stringify(
    {
      schema_version: "0.1",
      source_revision: sourceRevision,
      generated_at: generatedAt,
      files: manifestFiles,
    },
    null,
    2,
  )}\n`,
  "utf8",
);

console.log(`Static export created: ${outputRoot}`);
console.log(`Source revision: ${sourceRevision}`);
console.log(`Files: ${manifestFiles.length + 1}`);
