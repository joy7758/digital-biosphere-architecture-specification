import type { Metadata } from "next";
import { UpdateDetailPage } from "../../update-detail-page";

export const metadata: Metadata = {
  title: "发布 GB/Z 185 与 TITMAS 衔接矩阵 v0.1",
  description: "GB/Z 185.1—185.7、第8部分起草项目与 TITMAS 可信执行、证据和审计扩展关系的研究更新。",
  alternates: {
    canonical: "/updates/gbz-185-alignment-v0-1/",
    languages: { "zh-CN": "/updates/gbz-185-alignment-v0-1/", en: "/en/updates/gbz-185-alignment-v0-1/" },
  },
};

export default function Gbz185AlignmentUpdate() {
  return <UpdateDetailPage locale="zh" slug="gbz-185-alignment-v0-1" />;
}
