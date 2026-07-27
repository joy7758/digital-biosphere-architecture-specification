import assert from "node:assert/strict";
import { copyFile, mkdir, readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repositoryRoot = resolve(siteRoot, "..");
const publicRoot = join(siteRoot, "public");

const artifacts = [
  ["TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.md", "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.md"],
  ["TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.json", "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.json"],
  ["TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1-VALIDATION-REPORT.md", "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1-VALIDATION-REPORT.md"],
  ["TITMAS-FIRST-RUN-v0.1.md", "TITMAS-FIRST-RUN-v0.1.md"],
  [
    "architecture/schemas/titmas-commercial-evaluation-pack.schema.v0.1.json",
    "architecture/schemas/titmas-commercial-evaluation-pack.schema.v0.1.json",
  ],
  [
    "examples/titmas-first-run/entity-object.synthetic.v0.1.json",
    "examples/titmas-first-run/entity-object.synthetic.v0.1.json",
  ],
];

const manifest = JSON.parse(
  await readFile(join(repositoryRoot, "TITMAS-COMMERCIAL-EVALUATION-PACK-v0.1.json"), "utf8"),
);
assert.equal(
  manifest.status,
  "COMMERCIAL_EVALUATION_PACKAGE_PREPARED_NOT_AVAILABLE_OFFERING",
);
assert.equal(manifest.commercial_truth.evaluation_package_prepared, true);
assert.equal(manifest.commercial_truth.available_offering, false);
assert.equal(manifest.commercial_truth.production_ready, false);
assert.equal(manifest.effects.authority, false);
assert.equal(manifest.effects.permission, false);
assert.equal(manifest.effects.runtime, false);
assert.equal(manifest.effects.agent, false);

for (const [source, target] of artifacts) {
  const destination = join(publicRoot, target);
  await mkdir(dirname(destination), { recursive: true });
  await copyFile(join(repositoryRoot, source), destination);
}

console.log(`COMMERCIAL_EVALUATION_ARTIFACTS_SYNCED=${artifacts.length}`);
