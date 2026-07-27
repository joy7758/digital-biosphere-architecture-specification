import type { Metadata } from "next";
import { MedicalEvidencePage } from "../medical-evidence-page";

export const metadata: Metadata = {
  title: "UDI-DICOM 医疗证据链 Demo",
  description: "使用模拟 UDI 查看设备身份、影像对象与外部证据的结构闭合；不构成安全、认证或生产声明。",
  alternates: {
    canonical: "/medical-evidence/",
    languages: { "zh-CN": "/medical-evidence/", en: "/en/medical-evidence/" },
  },
};

export default function MedicalEvidence() {
  return <MedicalEvidencePage locale="zh" />;
}
