import assert from "node:assert/strict";
import test from "node:test";

test("Worker - standard route fallback", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}-1`);
  const { default: worker } = await import(workerUrl.href);

  const request = new Request("http://localhost/");
  const env = {
    ASSETS: { fetch: async () => new Response("Asset not found", { status: 404 }) },
    DB: {},
    IMAGES: {}
  };
  const ctx = {
    waitUntil() {},
    passThroughOnException() {}
  };

  const response = await worker.fetch(request, env, ctx);
  assert.ok(response instanceof Response);
});

test("Worker - image optimization route", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}-2`);
  const { default: worker } = await import(workerUrl.href);

  const request = new Request("http://localhost/_vinext/image?url=/test.png&w=256&q=75", {
    headers: { accept: "image/webp" }
  });

  let assetFetched = false;
  let transformCalled = false;
  let outputCalled = false;

  const env = {
    ASSETS: {
      fetch: async (req) => {
        assetFetched = true;
        assert.equal(req.url, "http://localhost/test.png");
        return new Response(new ReadableStream({
          start(controller) {
            controller.enqueue(new Uint8Array([1, 2, 3]));
            controller.close();
          }
        }), {
          headers: { "Content-Type": "image/png" } // mock image content type so isSafeImageContentType passes
        });
      }
    },
    DB: {},
    IMAGES: {
      input: (stream) => {
        return {
          transform: (options) => {
            transformCalled = true;
            assert.deepEqual(options, { width: 256 });
            return {
              output: async (options) => {
                outputCalled = true;
                assert.equal(options.quality, 75);
                assert.equal(options.format, "image/webp");
                return {
                  response: () => new Response("optimized-image", {
                    headers: { "Content-Type": "image/webp" }
                  })
                };
              }
            };
          }
        };
      }
    }
  };
  const ctx = {
    waitUntil() {},
    passThroughOnException() {}
  };

  const response = await worker.fetch(request, env, ctx);
  assert.equal(assetFetched, true, "Asset should be fetched");
  assert.equal(transformCalled, true, "Transform should be called");
  assert.equal(outputCalled, true, "Output should be called");
  assert.equal(await response.text(), "optimized-image", "Response text should match");
});
