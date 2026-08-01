import type { Metadata } from "next";
import { Gbz185Page } from "../../../gbz-185-page";

export const metadata: Metadata = {
  title: "GB/Z 185 Agent Interconnection and TITMAS Trusted Execution, Evidence, and Audit Alignment",
  description: "A research mapping of GB/Z 185 agent interconnection to TITMAS trusted execution, execution evidence, verification, and agent-audit extensions; no conformance, certification, or official-affiliation claim.",
  alternates: {
    canonical: "/en/standards/gbz-185/",
    languages: { "zh-CN": "/standards/gbz-185/", en: "/en/standards/gbz-185/" },
  },
};

export default function EnglishGbz185Alignment() {
  return <Gbz185Page locale="en" />;
}
