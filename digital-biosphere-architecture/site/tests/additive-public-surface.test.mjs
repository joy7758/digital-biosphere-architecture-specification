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
  "/products/gate",
  "/en/products/gate",
  "/products/receipt",
  "/en/products/receipt",
  "/products/audit",
  "/en/products/audit",
  "/products/health",
  "/en/products/health",
  "/design-partner",
  "/en/design-partner",
  "/private-evaluation",
  "/en/private-evaluation",
  "/monitor-pilot",
  "/en/monitor-pilot",
  "/enforce-pilot",
  "/en/enforce-pilot",
  "/request-access",
  "/en/request-access",
  "/security",
  "/en/security",
  "/trust-center",
  "/en/trust-center",
  "/privacy",
  "/en/privacy",
  "/terms",
  "/en/terms",
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

test("keeps historical surfaces while promoting the DCELL research direction", async () => {
  const [homeResponse, statusResponse, communityResponse] = await Promise.all([render("/"), render("/status"), render("/community")]);
  const [home, status, community] = await Promise.all([homeResponse.text(), statusResponse.text(), communityResponse.text()]);

  assert.match(home, /为自主 AI 系统构建可信基础设施/);
  assert.match(home, /DCELL · RESEARCH_DIRECTION/);
  assert.match(home, /verifiable-agent-demo/);
  assert.match(home, /SAEE/);
  assert.match(home, /titmas-agent-action-gate/);
  assert.match(home, /早期工程种子和第一个实验实例/);
  assert.match(status, /DCELL 是研究方向/);
  assert.match(status, /LOCAL_CANDIDATE_NOT_DEPLOYED/);
  assert.match(status, /Stage 5\.7 结果/);
  assert.match(status, /IN_PROGRESS_WAITING_FOR_PARTICIPANT_ACTION/);
  assert.match(community, /HISTORICAL_NON_CURRENT/);
  assert.match(community, /社区从未建立/);
});

test("does not restore private-core or deprecated product routes", async () => {
  for (const route of ["/products/agent-immune", "/en/products/agent-immune"]) {
    const response = await render(route);
    assert.equal(response.status, 404);
  }
});
