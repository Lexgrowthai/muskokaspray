import type { Metadata } from "next";
import {
  ScanSearch,
  PhoneMissed,
  TrendingUp,
  Code2,
  Search,
  Quote,
  ArrowRight,
} from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, breadcrumbSchema, softwareApplicationSchema, SITE_URL } from "@/lib/schema";
import { TOOLS_ITEMS } from "@/lib/navigation";

export const metadata: Metadata = generatePageMetadata({
  title: "Free AI Tools for Law Firms",
  description:
    "Free tools for law firms — check your AI visibility across ChatGPT, Gemini, and Perplexity, calculate revenue lost to missed calls, and project your growth ROI.",
  slug: "tools",
});

const ICONS: Record<
  string,
  React.ComponentType<{ size?: number; className?: string }>
> = {
  ScanSearch,
  PhoneMissed,
  TrendingUp,
  Code2,
  Search,
  Quote,
};

export default function ToolsPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Free AI Tools for Law Firms",
          "Free tools for law firms to measure AI visibility, missed-call revenue, and growth ROI.",
          `${SITE_URL}/tools`
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Tools", url: `${SITE_URL}/tools` },
        ])}
      />
      <SchemaScript
        schema={softwareApplicationSchema(
          "AI Visibility Checker for Law Firms",
          "Check how visible your law firm is across ChatGPT, Gemini, and Perplexity.",
          `${SITE_URL}/tools/ai-visibility-checker`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 text-center md:px-10">
          <Tag variant="purple">FREE TOOLS</Tag>
          <h1 className="mt-5 text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Free AI Tools for Law Firms
          </h1>
          <p className="mx-auto mt-5 max-w-[680px] text-[17px] leading-relaxed text-white/70">
            See how AI engines rank your firm, calculate the revenue you&apos;re
            losing to missed calls, and project the ROI of an AI growth system —
            no signup required.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {TOOLS_ITEMS.map((tool) => {
              const Icon = ICONS[tool.iconName ?? "ScanSearch"] ?? ScanSearch;
              return (
                <div
                  key={tool.label}
                  className="flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-200 hover:-translate-y-1 hover:shadow-[0_14px_40px_rgba(11,21,54,.14)]"
                >
                  <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-pu to-pu2 text-white shadow-[0_4px_20px_rgba(106,92,255,.35)]">
                    <Icon size={22} />
                  </div>
                  <h2 className="mt-5 text-[20px] font-extrabold tracking-tight text-navy">
                    {tool.label}
                  </h2>
                  <p className="mt-2 flex-1 text-[15px] leading-relaxed text-slate-600">
                    {tool.description}
                  </p>
                  <div className="mt-6">
                    <Button href={tool.href} variant="ghost" size="sm">
                      Launch Tool <ArrowRight size={15} />
                    </Button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>
    </>
  );
}
