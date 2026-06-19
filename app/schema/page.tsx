import Link from "next/link";
import { ArrowRight, Clock, Sparkles } from "lucide-react";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";
import { SILO_META, ARTICLES } from "./data";

export const metadata = generatePageMetadata({
  title: "Schema & Structured Data for Law Firms: Complete Guide for Law Firms",
  slug: "schema",
  description: "Schema markup is the language AI engines trust. Learn which structured data types help law firms get understood, trusted, and cited across all AI platforms.",
});

function formatDate(date: string): string {
  return new Date(date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export default function SiloHubPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Schema & Structured Data for Law Firms: Complete Guide for Law Firms",
          SILO_META.description,
          `${SITE_URL}/${SILO_META.slug}`
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: SILO_META.name, url: `${SITE_URL}/${SILO_META.slug}` },
        ])}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <span className="mb-5 inline-flex items-center gap-2 rounded-full border border-pu/30 bg-pu/10 px-4 py-1.5 text-[12px] font-bold uppercase tracking-wide text-pu3">
            <Sparkles size={14} /> {SILO_META.name}
          </span>
          <h1 className="mx-auto max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            {SILO_META.name}{" "}
            <span className="text-grad-gold">for Law Firms</span>
          </h1>
          <p className="mx-auto mt-6 max-w-[640px] text-[17px] leading-relaxed text-slate-300">
            {SILO_META.description}
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mb-12 text-center">
            <h2 className="text-[clamp(24px,3vw,36px)] font-extrabold tracking-tight text-navy">
              {ARTICLES.length} in-depth guides for law firms
            </h2>
          </div>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-2">
            {ARTICLES.map((article) => (
              <Link
                key={article.slug}
                href={`/${SILO_META.slug}/${article.slug}`}
                className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 hover:border-pu/40"
              >
                <div className="mb-4 flex items-center gap-3">
                  <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Sparkles size={18} />
                  </div>
                  <div className="flex items-center gap-2 text-[12px] text-slate-400">
                    <Clock size={12} />
                    <span>{article.readTime}</span>
                    <span className="mx-1">·</span>
                    <span>{formatDate(article.date)}</span>
                  </div>
                </div>
                <h2 className="mb-2 text-[18px] font-extrabold leading-snug tracking-tight text-navy transition-colors group-hover:text-pu">
                  {article.title}
                </h2>
                <p className="flex-1 text-[14px] leading-relaxed text-slate-600">
                  {article.description}
                </p>
                <span className="mt-5 inline-flex items-center gap-1.5 text-[13px] font-bold text-pu">
                  Read guide
                  <ArrowRight
                    size={15}
                    className="transition-transform group-hover:translate-x-1"
                  />
                </span>
                <div className="mt-5 h-1 w-full rounded-full bg-gradient-to-r from-pu to-pu2 opacity-70" />
              </Link>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-slate-50/60">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="rounded-3xl border border-pu/10 bg-gradient-to-br from-navy to-navy/90 p-10 text-center text-white shadow-[0_12px_40px_rgba(11,21,54,.2)]">
            <h2 className="mx-auto max-w-[600px] text-[clamp(24px,3vw,36px)] font-extrabold leading-tight tracking-tight">
              See Where Your Firm Stands in AI Search
            </h2>
            <p className="mx-auto mt-4 max-w-[480px] text-[16px] leading-relaxed text-slate-300">
              Get a free AI visibility check and find out exactly how AI platforms describe and cite your firm.
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
              <Button variant="gold" size="lg" href="/tools/ai-visibility-checker">
                Check My AI Visibility Free
                <ArrowRight size={18} className="ml-2" />
              </Button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
