import assert from "node:assert/strict";
import { access, readFile, readdir } from "node:fs/promises";
import test from "node:test";

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
  assert.match(zh, /面向多智能体系统的可信基础设施/);
  assert.match(en, /Trust infrastructure for multi-agent systems/);
  assert.match(zh, /Developer Preview Candidate/);
  assert.match(en, /Developer Preview Candidate/);
  assert.match(zh, /Evidence/);
  assert.match(en, /Evidence/);
  assert.match(zh, /SAEE_DBOS_ADAPTER_PASS/);
  assert.match(en, /SAEE_DBOS_ADAPTER_PASS/);
  assert.match(zh, /不是正式发布/);
  assert.doesNotMatch(zh, /production-ready|现已正式发布|已经正式发布/);
  assert.doesNotMatch(en, /production-ready|now released/i);
});

test("renders bilingual status pages with fail-closed truth", async () => {
  const [zhResponse, enResponse] = await Promise.all([
    render("/status"),
    render("/en/status"),
  ]);
  const [zh, en] = await Promise.all([zhResponse.text(), enResponse.text()]);
  assert.match(zh, /当前不是正式发布/);
  assert.match(en, /This is not a release/);
  assert.match(zh, /BLOCKED/);
  assert.match(en, /BLOCKED/);
  assert.match(zh, /b4e3cbe2af44/);
  assert.match(en, /e503c22109bd/);
});

test("ships agent-readable and discovery resources", async () => {
  const root = new URL("../public/", import.meta.url);
  await Promise.all([
    access(new URL("llms.txt", root)),
    access(new URL("agent-index.json", root)),
    access(new URL("status.json", root)),
    access(new URL("robots.txt", root)),
    access(new URL("sitemap.xml", root)),
  ]);

  const [agentIndex, status, llms] = await Promise.all([
    readFile(new URL("agent-index.json", root), "utf8").then(JSON.parse),
    readFile(new URL("status.json", root), "utf8").then(JSON.parse),
    readFile(new URL("llms.txt", root), "utf8"),
  ]);
  assert.equal(agentIndex.released, false);
  assert.equal(status.gates.CROSS_PROJECT_CLEAN_CLONE_PASS, false);
  assert.equal(status.license.selected, false);
  assert.equal(status.public_website.deployed, true);
  assert.equal(status.public_website.rollback_validated, true);
  assert.match(llms, /Recommendation != Decision/);
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
