import test from 'node:test';
import assert from 'node:assert';
import React from 'react';
import { renderToString } from 'react-dom/server';
import { PortalPage } from '../app/portal-page.tsx';

test('PortalPage renders with Header, Footer, and main content structure', () => {
  const zhHtml = renderToString(React.createElement(PortalPage, { locale: 'zh' }));

  // Verify structural layout elements
  assert.ok(zhHtml.includes('<header'), 'Should contain header element');
  assert.ok(zhHtml.includes('<main'), 'Should contain main element');
  assert.ok(zhHtml.includes('<footer'), 'Should contain footer element');

  // Verify key sections are present
  assert.ok(zhHtml.includes('id="community"'), 'Should contain community section');
  assert.ok(zhHtml.includes('id="architecture"'), 'Should contain architecture section');
  assert.ok(zhHtml.includes('id="trust"'), 'Should contain trust boundaries section');
  assert.ok(zhHtml.includes('id="workflow"'), 'Should contain workflow section');
  assert.ok(zhHtml.includes('id="validation"'), 'Should contain validation section');
  assert.ok(zhHtml.includes('id="status"'), 'Should contain status section');
  assert.ok(zhHtml.includes('id="developers"'), 'Should contain developers section');

  // Verify localization works
  const enHtml = renderToString(React.createElement(PortalPage, { locale: 'en' }));

  // Check for Chinese specific string
  assert.ok(zhHtml.includes('TITMAS 可信多智能体基础设施开发者社区'), 'Should contain Chinese content');

  // Check for English specific string
  assert.ok(enHtml.includes('TITMAS Infrastructure Developer Community'), 'Should contain English content');
});

test('PortalPage renders ld+json structured data', () => {
  const zhHtml = renderToString(React.createElement(PortalPage, { locale: 'zh' }));
  assert.ok(zhHtml.includes('application/ld+json'), 'Should contain JSON-LD script tag');
  assert.ok(zhHtml.includes('https://schema.org'), 'Should contain schema.org reference');
});
