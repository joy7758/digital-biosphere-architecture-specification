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

test("serializes null as 'null'", () => {
  const serialized = serializeJsonLd(null);
  assert.equal(serialized, "null");
});

test("serializes primitive types", () => {
  assert.equal(serializeJsonLd(42), "42");
  assert.equal(serializeJsonLd("hello"), '"hello"');
  assert.equal(serializeJsonLd(true), "true");
});

test("serializes functions as 'null'", () => {
  const serialized = serializeJsonLd(() => {});
  assert.equal(serialized, "null");
});
