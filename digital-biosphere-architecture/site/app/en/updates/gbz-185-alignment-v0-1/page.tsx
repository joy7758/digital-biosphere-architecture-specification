import type { Metadata } from "next";
import { UpdateDetailPage } from "../../../update-detail-page";

export const metadata: Metadata = {
  title: "GB/Z 185 and TITMAS Alignment Matrix v0.1 Published",
  description: "A research update mapping GB/Z 185.1–185.7, the drafting Part 8 project, and TITMAS trusted-execution, evidence, and audit extensions.",
  alternates: {
    canonical: "/en/updates/gbz-185-alignment-v0-1/",
    languages: { "zh-CN": "/updates/gbz-185-alignment-v0-1/", en: "/en/updates/gbz-185-alignment-v0-1/" },
  },
};

export default function EnglishGbz185AlignmentUpdate() {
  return <UpdateDetailPage locale="en" slug="gbz-185-alignment-v0-1" />;
}
