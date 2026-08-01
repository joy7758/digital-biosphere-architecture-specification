import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const publicRoot = new URL("../public/", import.meta.url);
const canonicalRoot = new URL("../../TITMAS/research/gbz-185-alignment/", import.meta.url);

const [mapping, canonicalMapping, schema, canonicalSchema, agentIndex, siteCatalog, status, updates] = await Promise.all([
  readFile(new URL("gbz-185-mapping.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("gbz-185-titmas-mapping-v0.1.json", canonicalRoot), "utf8").then(JSON.parse),
  readFile(new URL("schemas/gbz-185-mapping.schema.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("gbz-185-titmas-mapping-v0.1.schema.json", canonicalRoot), "utf8").then(JSON.parse),
  readFile(new URL("agent-index.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("site-catalog.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("status.json", publicRoot), "utf8").then(JSON.parse),
  readFile(new URL("updates.json", publicRoot), "utf8").then(JSON.parse),
]);

async function render(pathname) {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("gbz-185-test", `${process.pid}-${Date.now()}-${pathname}`);
  const { default: worker } = await import(workerUrl.href);
  return worker.fetch(
    new Request(`http://localhost${pathname}`, { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
}

test("GBZ-01 canonical and public mapping copies remain identical", () => {
  assert.deepEqual({ ...mapping, $schema: undefined }, { ...canonicalMapping, $schema: undefined });
  assert.equal(mapping.$schema, "/schemas/gbz-185-mapping.schema.json");
  assert.deepEqual(schema, canonicalSchema);
  assert.equal(mapping.schema_version, "0.1.0");
  assert.equal(mapping.mapping_status, "MAPPING_IMPLEMENTED_LOCAL_VALIDATED");
  assert.equal(mapping.publication_status.local_implementation_validated, true);
  assert.equal(mapping.publication_status.ready_for_publication, true);
  assert.equal(mapping.publication_status.publication_authorized, false);
  assert.equal(mapping.publication_status.publicly_deployed, false);
  assert.equal(mapping.publication_status.public_launch_authorized, false);
  assert.equal(mapping.publication_status.update_status, "READY_FOR_RELEASE");
  assert.match(mapping.observed_at, /[+-]\d{2}:\d{2}$/);
  assert.deepEqual(mapping.parts.map((part) => part.part), [1, 2, 3, 4, 5, 6, 7, 8]);
  assert.equal(mapping.parts.slice(0, 7).every((part) => part.official_status === "CURRENT"), true);
  assert.equal(mapping.parts[7].standard_id, "20264195-Z-469");
  assert.equal(mapping.parts[7].official_status, "DRAFTING");
  assert.equal(mapping.parts.every((part) => part.conformance_assessed === false), true);
  assert.equal(mapping.non_claims.gbz_185_conformance_assessed, false);
  assert.equal(mapping.non_claims.gbz_185_official_affiliation, false);
  assert.equal(mapping.non_claims.conformance_assessed, false);
  assert.equal(mapping.non_claims.official_affiliation, false);
  assert.equal(mapping.non_claims.adoption_claimed, false);
  assert.equal(mapping.next_validation_slice.status, "DEFINED_NOT_EXECUTED");
  assert.equal(mapping.next_validation_slice.scenarios.length, 8);
  assert.equal(mapping.next_validation_slice.scenarios.every((scenario) => scenario.status === "DEFINED_NOT_EXECUTED"), true);
});

test("GBZ-02 agent and site discovery surfaces register the bounded mapping", () => {
  assert.equal(agentIndex.entrypoints.gbz_185_alignment_zh, "/standards/gbz-185/");
  assert.equal(agentIndex.entrypoints.gbz_185_alignment_en, "/en/standards/gbz-185/");
  assert.equal(agentIndex.entrypoints.gbz_185_mapping, "/gbz-185-mapping.json");
  assert.equal(agentIndex.standards_alignment.gbz_185.status, "MAPPING_IMPLEMENTED_LOCAL_VALIDATED");
  assert.equal(agentIndex.standards_alignment.gbz_185.local_implementation_validated, true);
  assert.equal(agentIndex.standards_alignment.gbz_185.ready_for_publication, true);
  assert.equal(agentIndex.standards_alignment.gbz_185.publication_authorized, false);
  assert.equal(agentIndex.standards_alignment.gbz_185.publicly_deployed, false);
  assert.equal(agentIndex.standards_alignment.gbz_185.acps_adapter_implemented, false);
  assert.equal(agentIndex.standards_alignment.gbz_185.conformance_assessed, false);
  assert.equal(agentIndex.standards_alignment.gbz_185.official_affiliation, false);
  assert.equal(agentIndex.standards_alignment.gbz_185.adoption_claimed, false);
  assert.equal(siteCatalog.public_surfaces.standards_alignment.machine_entry, "/gbz-185-mapping.json");
  assert.ok(siteCatalog.agent_front_door.machine_entries.includes("/gbz-185-mapping.json"));
  assert.ok(siteCatalog.release_candidates.research.some((item) => item.id === "gbz-185-alignment"));
  assert.equal(siteCatalog.published_items.research.some((item) => item.id === "gbz-185-alignment"), false);
  assert.equal(status.gates.LOCAL_IMPLEMENTATION_VALIDATED, true);
  assert.equal(status.gates.GBZ_185_MAPPING_READY_FOR_PUBLICATION, true);
  assert.equal(status.gates.GBZ_185_MAPPING_PUBLICLY_DEPLOYED, false);
  assert.equal(status.gates.PUBLIC_LAUNCH_AUTHORIZED, false);
  assert.equal(status.gates.GBZ_185_CONFORMANCE_ASSESSED, false);
  assert.equal(status.gates.ACPS_ADAPTER_IMPLEMENTED, false);
  assert.equal(status.production_ready, false);
  assert.equal(status.public_protocol_released, false);
  assert.equal(status.formal_standard_change_authorized, false);
  const update = updates.items.find((item) => item.slug === "gbz-185-alignment-v0-1");
  assert.equal(update.category, "RESEARCH_UPDATE");
  assert.equal(update.status, "READY_FOR_RELEASE");
  assert.equal(update.publication_authorized, false);
  assert.equal(update.publicly_deployed, false);
  assert.equal(update.expires_at, null);
});

test("GBZ-03 bilingual pages preserve parity, language links, metadata, and boundaries", async () => {
  const [zhResponse, enResponse, zhUpdateResponse, enUpdateResponse] = await Promise.all([
    render("/standards/gbz-185"),
    render("/en/standards/gbz-185"),
    render("/updates/gbz-185-alignment-v0-1"),
    render("/en/updates/gbz-185-alignment-v0-1"),
  ]);
  for (const response of [zhResponse, enResponse, zhUpdateResponse, enUpdateResponse]) assert.equal(response.status, 200);
  const [zh, en, zhUpdate, enUpdate] = await Promise.all([
    zhResponse.text(),
    enResponse.text(),
    zhUpdateResponse.text(),
    enUpdateResponse.text(),
  ]);
  assert.match(zh, /GB\/Z 185 智能体互联与 TITMAS/);
  assert.match(en, /GB\/Z 185 Agent Interconnection and TITMAS/);
  for (const html of [zh, en]) {
    assert.match(html, /GBZ_185_CONFORMANCE_ASSESSED=false/);
    assert.match(html, /OFFICIAL_AFFILIATION=false/);
    assert.match(html, /PART8_CONTRIBUTION_SUBMITTED=false/);
    assert.match(html, /Mapping ≠ Compliance/);
    assert.match(html, /"isBasedOn"/);
  }
  assert.match(zh, /href="\/en\/standards\/gbz-185\//);
  assert.match(en, /href="\/standards\/gbz-185\//);
  assert.match(zh, /rel="canonical" href="https:\/\/redcrag.cn\/standards\/gbz-185\//);
  assert.match(en, /rel="canonical" href="https:\/\/redcrag.cn\/en\/standards\/gbz-185\//);
  assert.match(zhUpdate, /READY_FOR_RELEASE/);
  assert.match(enUpdate, /READY_FOR_RELEASE/);
  assert.match(zhUpdate, /PUBLICLY_DEPLOYED=false/);
  assert.match(enUpdate, /PUBLICLY_DEPLOYED=false/);
});

test("GBZ-04 source and public text contain no prohibited positive claim phrases", async () => {
  const texts = await Promise.all([
    readFile(new URL("gbz-185-mapping.json", publicRoot), "utf8"),
    readFile(new URL("agent-index.json", publicRoot), "utf8"),
    readFile(new URL("site-catalog.json", publicRoot), "utf8"),
    readFile(new URL("llms.txt", publicRoot), "utf8"),
  ]);
  const combined = texts.join("\n");
  const prohibited = [
    /已符合 GB\/Z 185/,
    /通过 GB\/Z 185 认证/,
    /GB\/Z 185 官方实现/,
    /国家标准认证/,
    /官方合作伙伴/,
    /参与第8部分起草/,
    /已被第8部分采纳/,
    /GB\/Z 185 compliant/i,
    /GB\/Z 185 certified/i,
    /official implementation/i,
    /official partner/i,
    /standard adopted TITMAS/i,
    /GBZ_185_MAPPING_PUBLISHED\s*[=:]\s*true/i,
    /\bPUBLISHED_MAPPING\b/,
    /\bMAPPING_PUBLISHED(?:_NO_CONFORMANCE)?\b/,
  ];
  for (const pattern of prohibited) assert.doesNotMatch(combined, pattern);
});
