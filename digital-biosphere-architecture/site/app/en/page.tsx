import type { Metadata } from "next";
import { PortalPage } from "../portal-page";

export const metadata: Metadata = {
  title: { absolute: "山西游骑兵电子商务有限公司" },
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
