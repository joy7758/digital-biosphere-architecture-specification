import assert from "node:assert/strict";
import test from "node:test";
import { serializeJsonLd } from "../app/json-ld.ts";

test("serializes JSON-LD without a script-closing sequence", () => {
  const serialized = serializeJsonLd({
    description: "</script><script>alert('xss')</script>",
  });

  assert.doesNotMatch(serialized, /</);
  assert.match(serialized, /\\u003c\/script>/);
  assert.deepEqual(JSON.parse(serialized), {
    description: "</script><script>alert('xss')</script>",
  });
});

test("serializes undefined as 'null'", () => {
  const serialized = serializeJsonLd(undefined);
  assert.equal(serialized, "null");
});

test("serializes null correctly", () => {
  const serialized = serializeJsonLd(null);
  assert.equal(serialized, "null");
  assert.deepEqual(JSON.parse(serialized), null);
});

test("serializes primitives correctly", () => {
  assert.equal(serializeJsonLd(42), "42");
  assert.equal(serializeJsonLd("hello <world>"), '"hello \\u003cworld>"');
  assert.equal(serializeJsonLd(true), "true");
});

test("serializes arrays correctly", () => {
  const serialized = serializeJsonLd(["<test>"]);
  assert.equal(serialized, '["\\u003ctest>"]');
  assert.deepEqual(JSON.parse(serialized), ["<test>"]);
});
