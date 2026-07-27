import type { Metadata } from "next";
import { MedicalEvidencePage } from "../../medical-evidence-page";

export const metadata: Metadata = {
  title: "UDI-DICOM Medical Evidence Demo",
  description: "Use a synthetic UDI to inspect structural closure across device identity, an imaging object, and external evidence; no safety, certification, or production claim.",
  alternates: {
    canonical: "/en/medical-evidence/",
    languages: { "zh-CN": "/medical-evidence/", en: "/en/medical-evidence/" },
  },
};

export default function EnglishMedicalEvidence() {
  return <MedicalEvidencePage locale="en" />;
}
