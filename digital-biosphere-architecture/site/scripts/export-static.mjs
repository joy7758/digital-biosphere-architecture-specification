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
  { request: "/", output: "index.html", markers: markers.zhHome, lang: "zh-CN" },
  { request: "/en", output: "en/index.html", markers: markers.enHome, lang: "en" },
  { request: "/status", output: "status/index.html", markers: markers.zhStatus, lang: "zh-CN" },
  { request: "/en/status", output: "en/status/index.html", markers: markers.enStatus, lang: "en" },
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

  const renderedHtml = await response.text();
  const html = renderedHtml.replace(
    /<html lang="[^"]+">/,
    `<html lang="${route.lang}">`,
  );
  if (!html.includes(`<html lang="${route.lang}">`)) {
    throw new Error(`Cannot export ${route.request}: document language was not set to ${route.lang}`);
  }
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
      artifact: "trusted-multi-agent-infrastructure-website",
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
