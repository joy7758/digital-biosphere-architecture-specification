import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { resolveReleaseContext, routeMarkers } from "../scripts/release-mode.mjs";

async function currentResources() {
  const root = new URL("../public/", import.meta.url);
  const [status, agentIndex, agentCustomerPackage, dbosPackage] = await Promise.all([
    readFile(new URL("status.json", root), "utf8").then(JSON.parse),
    readFile(new URL("agent-index.json", root), "utf8").then(JSON.parse),
    readFile(new URL("agent-customer-package.json", root), "utf8").then(JSON.parse),
    readFile(new URL("dbos-public-package-manifest.json", root), "utf8").then(JSON.parse),
  ]);
  return { status, agentIndex, agentCustomerPackage, dbosPackage };
}

test("defaults to the fail-closed candidate release context", async () => {
  const context = resolveReleaseContext({}, await currentResources());
  assert.deepEqual(context, {
    mode: "candidate",
    deploymentState: "candidate_not_released",
    developerPreviewReleased: false,
    releaseDecisionReference: null,
    releasedByRef: null,
    publicReleaseTag: null,
    dbosWheelUrl: null,
  });
  assert.match(routeMarkers(context.mode).zhStatus[0], /当前不是正式发布/);
});

test("rejects unknown release modes", async () => {
  const resources = await currentResources();
  assert.throws(
    () => resolveReleaseContext({ RELEASE_MODE: "production" }, resources),
    /RELEASE_MODE must be one of/,
  );
});

test("rejects formal release mode without explicit decision inputs", async () => {
  const resources = await currentResources();
  assert.throws(
    () => resolveReleaseContext({ RELEASE_MODE: "formal" }, resources),
    /RELEASE_DECISION_REF is required/,
  );
});

test("rejects formal release mode while public truth surfaces remain candidates", async () => {
  const resources = await currentResources();
  assert.throws(
    () =>
      resolveReleaseContext(
        {
          RELEASE_MODE: "formal",
          RELEASE_DECISION_REF: "architecture/ADR-PLACEHOLDER.md",
          RELEASED_BY_REF: "release-owner",
          PUBLIC_RELEASE_TAG: "v0.1-developer-preview",
          DBOS_WHEEL_URL: "https://example.invalid/dbos.whl",
        },
        resources,
      ),
    /formal export requires status\.release_claim=true/,
  );
});

test("accepts formal mode only when every machine truth surface and input agree", async () => {
  const resources = structuredClone(await currentResources());
  const wheelUrl = "https://github.com/example/releases/download/v0.1/dbos.whl";
  resources.status.release_claim = true;
  resources.status.gates.DEVELOPER_PREVIEW_RELEASED = true;
  resources.status.gates.DBOS_PUBLIC_SAFE_WHEEL_PUBLISHED = true;
  resources.status.gates.DQ_016_DBOS_DISTRIBUTION_DECIDED = true;
  resources.agentIndex.released = true;
  resources.agentCustomerPackage.released = true;
  resources.dbosPackage.release_authorized = true;
  resources.dbosPackage.status = "PUBLISHED";
  resources.dbosPackage.public_download_url = wheelUrl;

  const context = resolveReleaseContext(
    {
      RELEASE_MODE: "formal",
      RELEASE_DECISION_REF: "architecture/ADR-022-developer-preview-release.md",
      RELEASED_BY_REF: "release-owner",
      PUBLIC_RELEASE_TAG: "v0.1-developer-preview",
      DBOS_WHEEL_URL: wheelUrl,
    },
    resources,
  );

  assert.equal(context.deploymentState, "developer_preview_released");
  assert.equal(context.developerPreviewReleased, true);
  assert.equal(context.dbosWheelUrl, wheelUrl);
  assert.match(routeMarkers(context.mode).enStatus[0], /is released/);
});
