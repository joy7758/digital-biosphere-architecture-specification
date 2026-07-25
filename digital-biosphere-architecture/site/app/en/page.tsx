import type { Metadata } from "next";
import { PortalPage } from "../portal-page";

export const metadata: Metadata = {
  title: "TITMAS Infrastructure Developer Community",
  description:
    "Build the shared trust layer for long-running multi-agent systems.",
  alternates: {
    canonical: "/en/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function EnglishHome() {
  return <PortalPage locale="en" />;
}
