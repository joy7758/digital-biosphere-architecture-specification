import 'global-jsdom/register'
import { test } from "node:test";
import assert from "node:assert";
import { render, screen } from "@testing-library/react";
import { Brand, Header, Footer } from "../app/site-shell.tsx";
import { content } from "../app/site-content.ts";
import { createElement } from 'react';

test("Brand component renders correctly", () => {
    const { container } = render(createElement(Brand));
    assert.match(container.innerHTML, /TITMAS/);
});

test("Header component renders correctly for 'zh' locale and 'home' section", () => {
    const { container } = render(createElement(Header, { locale: "zh", section: "home" }));
    assert.match(container.innerHTML, /<nav.*主导航/);
    assert.ok(container.innerHTML.includes('href="/#community"'));
});

test("Header component renders correctly for 'en' locale and 'status' section", () => {
    const { container } = render(createElement(Header, { locale: "en", section: "status" }));
    assert.match(container.innerHTML, /<nav.*Primary navigation/);
    assert.ok(container.innerHTML.includes('href="/en/#community"'));
});

test("Footer component renders correctly for 'zh' locale", () => {
    const { container } = render(createElement(Footer, { locale: "zh" }));
    assert.match(container.innerHTML, /机器可读/);
    assert.match(container.innerHTML, /社区方向/);
});

test("Footer component renders correctly for 'en' locale", () => {
    const { container } = render(createElement(Footer, { locale: "en" }));
    assert.match(container.innerHTML, /Machine-readable/);
    assert.match(container.innerHTML, /Community direction/);
});
