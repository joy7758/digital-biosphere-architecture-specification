import type { Metadata } from "next";
import { PortalPage } from "../portal-page";

export const metadata: Metadata = {
  title: "TITMAS Infrastructure Developer Community",
  description:
    "A trust infrastructure layer for autonomous AI agent ecosystems; manufacturing and other industries are application examples.",
  alternates: {
    canonical: "/en/",
    languages: { "zh-CN": "/", en: "/en/" },
  },
};

export default function EnglishHome() {
  return <PortalPage locale="en" />;
}
