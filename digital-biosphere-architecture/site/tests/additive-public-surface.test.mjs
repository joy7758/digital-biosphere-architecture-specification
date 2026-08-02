import assert from "node:assert/strict";
import test from "node:test";

const restoredRoutes = [
  "/research",
  "/en/research",
  "/research/index",
  "/en/research/index",
  "/applications",
  "/en/applications",
  "/demos",
  "/en/demos",
  "/community",
  "/en/community",
  "/updates",
  "/en/updates",
  "/updates/information-architecture-v0-1",
  "/en/updates/information-architecture-v0-1",
  "/updates/constitution",
  "/en/updates/constitution",
  "/industries",
  "/en/industries",
  "/industry/media-evidence",
  "/en/industry/media-evidence",
  "/industry/medical-evidence",
  "/en/industry/medical-evidence",
  "/industry/space-agent-evidence",
  "/en/industry/space-agent-evidence",
  "/demo/medical-evidence",
  "/en/demo/medical-evidence",
  "/demo/media-evidence",
  "/en/demo/media-evidence",
  "/medical-evidence",
  "/en/medical-evidence",
  "/digital-cell",
  "/en/digital-cell",
  "/commercial-evaluation",
  "/en/commercial-evaluation",
];

async function render(pathname) {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("additive-surface-test", `${process.pid}-${Date.now()}-${pathname}`);
  const { default: worker } = await import(workerUrl.href);
  return worker.fetch(
    new Request(`http://localhost${pathname}`, { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
}

test("keeps all established bilingual surfaces reachable", async () => {
  for (const route of restoredRoutes) {
    const response = await render(route);
    assert.equal(response.status, 200, `expected ${route} to remain reachable`);
    assert.match(response.headers.get("content-type") ?? "", /text\/html/);
  }
});

test("keeps historical E01 while promoting the agent-native mainline", async () => {
  const [homeResponse, statusResponse] = await Promise.all([render("/"), render("/status")]);
  const [home, status] = await Promise.all([homeResponse.text(), statusResponse.text()]);

  assert.match(home, /AGENT START HERE/);
  assert.match(home, /夏日之海/);
  assert.match(home, /\/titmas-logo\.png/);
  assert.doesNotMatch(home, /\/summersea-logo\.png/);
  assert.match(home, /TITMAS Digital Cell Demo/);
  assert.match(home, /E01 Human Compatibility Observation/);
  assert.match(home, /Stage 5\.7 Agent-Native Selection/);
  assert.match(status, /TITMAS 商业基础设施成熟度计划进行中/);
  assert.match(status, /Stage 5\.7 结果/);
  assert.match(status, /IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION/);
});

test("does not restore private-core or deprecated product routes", async () => {
  for (const route of ["/products/agent-immune", "/en/products/agent-immune"]) {
    const response = await render(route);
    assert.equal(response.status, 404);
  }
});
