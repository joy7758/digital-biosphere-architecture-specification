import type { Metadata } from "next";
import { PortalPage } from "../portal-page";

export const metadata: Metadata = {
  title: { absolute: "Bin Zhang · DCELL Research Direction" },
  description:
    "Research Engineer building trustworthy infrastructure for autonomous AI systems. DCELL is a research direction grounded in public engineering evidence.",
  alternates: {
    canonical: "/en/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function EnglishHome() {
  return <PortalPage locale="en" />;
}
