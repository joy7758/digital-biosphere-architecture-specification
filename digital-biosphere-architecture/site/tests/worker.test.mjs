import test, { mock } from "node:test";
import assert from "node:assert/strict";

mock.module("vinext/server/image-optimization", {
  namedExports: {
    handleImageOptimization: mock.fn(async (request, handlers, allowedWidths) => {
      // Simulate successful optimization to test handlers
      if (handlers.fetchAsset) {
        await handlers.fetchAsset("test.jpg");
      }
      if (handlers.transformImage) {
        await handlers.transformImage(new ReadableStream(), { width: 100, format: "webp", quality: 80 });
      }
      return new Response("optimized-image");
    }),
    DEFAULT_DEVICE_SIZES: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    DEFAULT_IMAGE_SIZES: [16, 32, 48, 64, 96, 128, 256, 384],
  }
});

mock.module("vinext/server/app-router-entry", {
  defaultExport: {
    fetch: mock.fn(async (request, env, ctx) => {
      return new Response("app-router-response");
    })
  }
});

const { default: worker } = await import("../worker/index.ts");

test("Worker handles regular requests", async () => {
  const request = new Request("http://localhost/");
  const env = {};
  const ctx = {};

  const response = await worker.fetch(request, env, ctx);
  const text = await response.text();
  assert.strictEqual(text, "app-router-response");
});

test("Worker handles image optimization requests", async () => {
  const request = new Request("http://localhost/_vinext/image");
  let assetFetched = false;
  let imageTransformed = false;

  const env = {
    ASSETS: {
      fetch: async (req) => {
        assetFetched = true;
        return new Response("asset");
      }
    },
    IMAGES: {
      input: (stream) => ({
        transform: (options) => ({
          output: async (options) => {
            imageTransformed = true;
            return {
              response: () => new Response("transformed")
            };
          }
        })
      })
    }
  };
  const ctx = {};

  const response = await worker.fetch(request, env, ctx);
  const text = await response.text();
  assert.strictEqual(text, "optimized-image");
  assert.ok(assetFetched, "Expected fetchAsset to be called");
  assert.ok(imageTransformed, "Expected transformImage to be called");
});
