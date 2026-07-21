import { createHash } from "node:crypto";
import { cp, mkdir, readdir, readFile, rm, stat, writeFile } from "node:fs/promises";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const outputRoot = join(siteRoot, "out");
const clientRoot = join(siteRoot, "dist", "client");
const serverEntry = join(siteRoot, "dist", "server", "index.js");
const sourceRevision = process.env.SOURCE_REVISION || "working-tree";
const generatedAt = new Date().toISOString();

const routes = [
  { request: "/", output: "index.html", marker: "面向多智能体系统的可信基础设施" },
  { request: "/en", output: "en/index.html", marker: "Trust infrastructure for multi-agent systems" },
  { request: "/status", output: "status/index.html", marker: "当前不是正式发布" },
  { request: "/en/status", output: "en/status/index.html", marker: "This is not a release" },
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
  if (!html.includes(route.marker)) {
    throw new Error(`Cannot export ${route.request}: expected marker is absent`);
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
      deployment_state: "candidate_not_released",
      developer_preview_released: false,
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
