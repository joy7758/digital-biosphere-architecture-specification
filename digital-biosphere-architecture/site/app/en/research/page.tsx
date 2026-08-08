import type { Metadata } from "next";
import { DirectoryPage } from "../../directory-page";

export const metadata: Metadata = {
  title: "DCELL Research Direction",
  description: "Trustworthy-infrastructure research for autonomous AI systems across agents, infrastructure, environments, evaluations, and autonomous experimental loops.",
  alternates: {
    canonical: "/en/research/",
    languages: { "zh-CN": "/research/", en: "/en/research/" },
  },
};

export default function EnglishResearch() {
  return <DirectoryPage locale="en" section="research" />;
}
