import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowRight, CalendarDays, Sparkles } from "lucide-react";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import { CATEGORIES, CATEGORY_SLUGS, humanizeCategory } from "../data";

export function generateStaticParams() {
  return CATEGORY_SLUGS.map((category) => ({ category }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ category: string }>;
}) {
  const { category } = await params;
  const data = CATEGORIES[category];
  const name = humanizeCategory(category);
  return generatePageMetadata({
    title: `${name} Insights for Law Firms`,
    slug: `insights/${category}`,
    description:
      data?.description ??
      `AI search insights and playbooks on ${name} for law firms.`,
  });
}

function formatDate(date: string): string {
  return new Date(date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export default async function CategoryPage({
  params,
}: {
  params: Promise<{ category: string }>;
}) {
  const { category } = await params;
  const data = CATEGORIES[category];

  if (!data) {
    notFound();
  }

  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          `${data.name} Insights for Law Firms`,
          data.description,
          `${SITE_URL}/insights/${category}`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Link
            href="/insights"
            className="mb-6 inline-flex items-center gap-1.5 text-[13px] font-semibold text-pu3 hover:text-white"
          >
            <Sparkles size={14} /> All Insights
          </Link>
          <h1 className="max-w-[760px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            {data.name}{" "}
            <span className="text-grad-gold">for Law Firms</span>
          </h1>
          <p className="mt-6 max-w-[640px] text-[17px] leading-relaxed text-slate-300">
            {data.description}
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <h2 className="mb-8 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Latest articles
          </h2>
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {data.articles.map((article) => (
              <Link
                key={article.slug}
                href={`/insights/${category}/${article.slug}`}
                className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 hover:border-pu/40"
              >
                <span className="mb-4 inline-flex w-fit items-center gap-1.5 rounded-full border border-pu/20 bg-pu/8 px-3 py-1 text-[11px] font-bold uppercase tracking-wide text-pu">
                  {data.name}
                </span>
                <h3 className="text-[18px] font-extrabold leading-snug tracking-tight text-navy">
                  {article.title}
                </h3>
                <p className="mt-3 flex-1 text-[14px] leading-relaxed text-slate-600">
                  {article.excerpt}
                </p>
                <div className="mt-5 flex items-center justify-between">
                  <span className="inline-flex items-center gap-1.5 text-[12px] text-slate-400">
                    <CalendarDays size={13} />
                    {formatDate(article.date)}
                  </span>
                  <span className="inline-flex items-center gap-1 text-[13px] font-bold text-pu">
                    Read
                    <ArrowRight
                      size={14}
                      className="transition-transform group-hover:translate-x-1"
                    />
                  </span>
                </div>
              </Link>
            ))}
          </div>

          <div className="mt-16 rounded-3xl border border-pu/10 bg-gradient-to-br from-pu/5 to-gold/5 p-10 text-center">
            <h3 className="text-[24px] font-extrabold tracking-tight text-navy">
              Want to see where your firm stands in AI search?
            </h3>
            <p className="mx-auto mt-3 max-w-[520px] text-[15px] text-slate-600">
              Get a free AI visibility check and a strategy call tailored to
              your practice areas.
            </p>
            <div className="mt-6 flex justify-center">
              <Button
                href="/tools/ai-visibility-checker"
                variant="primary"
                size="lg"
              >
                Get a Free Strategy Call
              </Button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
