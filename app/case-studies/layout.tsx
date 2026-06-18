import { ReactNode } from "react";
import Breadcrumb from "@/components/layout/Breadcrumb";

export default function CaseStudiesLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <>
      <Breadcrumb />
      {children}
    </>
  );
}
