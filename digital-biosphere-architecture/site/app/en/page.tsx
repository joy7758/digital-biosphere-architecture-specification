import type { Metadata } from "next";
import { PortalPage } from "../portal-page";

export const metadata: Metadata = {
  title: "TITMAS Infrastructure Developer Community",
  description:
    "A developer community for open specifications, adapter contracts, conformance tests, and reference boundaries for trusted multi-agent infrastructure.",
  alternates: {
    canonical: "/en/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function EnglishHome() {
  return <PortalPage locale="en" />;
}
