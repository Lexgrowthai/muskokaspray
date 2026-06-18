import { ReactNode } from "react";
import Breadcrumb from "@/components/layout/Breadcrumb";

export default function ToolsLayout({ children }: { children: ReactNode }) {
  return (
    <>
      <Breadcrumb />
      {children}
    </>
  );
}
