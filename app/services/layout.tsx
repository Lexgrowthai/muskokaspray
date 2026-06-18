import { ReactNode } from "react";
import Breadcrumb from "@/components/layout/Breadcrumb";

export default function ServicesLayout({ children }: { children: ReactNode }) {
  return (
    <>
      <Breadcrumb />
      {children}
    </>
  );
}
