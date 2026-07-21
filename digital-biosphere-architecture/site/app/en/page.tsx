import type { Metadata } from "next";
import { PortalPage } from "../portal-page";

export const metadata: Metadata = {
  title: "Trusted Multi-Agent Infrastructure",
  description:
    "Trust infrastructure for long-running, collaborative, and verifiably evolving AI agents.",
  alternates: {
    canonical: "/en/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function EnglishHome() {
  return <PortalPage locale="en" />;
}
