import Link from "next/link";
import { ArrowRight, Sparkles } from "lucide-react";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import { INSIGHTS_ITEMS } from "@/lib/navigation";

export const metadata = generatePageMetadata({
  title: "AI Search Insights for Law Firms",
  slug: "insights",
  description:
    "Strategy, research, and playbooks on how law firms win visibility across ChatGPT, Gemini, Perplexity, AI Overviews, and the new generation of AI search engines.",
});

type Accent = "purple" | "gold" | "blue";

const ACCENTS: Accent[] = ["purple", "gold", "blue"];

const ACCENT_STYLES: Record<
  Accent,
  { ring: string; badge: string; icon: string; bar: string }
> = {
  purple: {
    ring: "hover:border-pu/40",
    badge: "bg-pu/8 text-pu border-pu/20",
    icon: "bg-pu/10 text-pu",
    bar: "from-pu to-pu2",
  },
  gold: {
    ring: "hover:border-gold/40",
    badge: "bg-gold/10 text-gold3 border-gold/30",
    icon: "bg-gold/10 text-gold3",
    bar: "from-gold3 to-gold2",
  },
  blue: {
    ring: "hover:border-sky-400/40",
    badge: "bg-sky-500/10 text-sky-600 border-sky-500/20",
    icon: "bg-sky-500/10 text-sky-600",
    bar: "from-sky-500 to-sky-400",
  },
};

// Hardcoded article counts per category slug.
const ARTICLE_COUNTS: Record<string, number> = {
  chatgpt: 6,
  gemini: 5,
  perplexity: 4,
  "ai-overviews": 7,
  "entity-seo": 5,
  "structured-data": 6,
  "semantic-search": 4,
  geo: 8,
  "knowledge-graphs": 3,
  "voice-search": 4,
  "future-of-search": 6,
};

function slugFromHref(href: string): string {
  return href.replace("/insights/", "");
}

export default function InsightsHubPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "AI Search Insights for Law Firms",
          "Strategy, research, and playbooks on how law firms win visibility across ChatGPT, Gemini, Perplexity, and AI Overviews.",
          `${SITE_URL}/insights`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <span className="mb-5 inline-flex items-center gap-2 rounded-full border border-pu/30 bg-pu/10 px-4 py-1.5 text-[12px] font-bold uppercase tracking-wide text-pu3">
            <Sparkles size={14} /> Insights
          </span>
          <h1 className="mx-auto max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            AI Search Insights for{" "}
            <span className="text-grad-gold">Law Firms</span>
          </h1>
          <p className="mx-auto mt-6 max-w-[640px] text-[17px] leading-relaxed text-slate-300">
            Search is moving from blue links to AI answers. Explore our research
            and playbooks on getting your firm cited across every AI engine that
            matters — from ChatGPT and Gemini to Perplexity and Google&apos;s AI
            Overviews.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {INSIGHTS_ITEMS.map((item, i) => {
              const accent = ACCENTS[i % ACCENTS.length];
              const styles = ACCENT_STYLES[accent];
              const slug = slugFromHref(item.href);
              const count = ARTICLE_COUNTS[slug] ?? 4;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className={`group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 ${styles.ring}`}
                >
                  <div
                    className={`mb-5 flex h-11 w-11 items-center justify-center rounded-xl ${styles.icon}`}
                  >
                    <Sparkles size={20} />
                  </div>
                  <div className="mb-3 flex items-center gap-2">
                    <h2 className="text-[19px] font-extrabold tracking-tight text-navy">
                      {item.label}
                    </h2>
                    <span
                      className={`rounded-full border px-2.5 py-0.5 text-[11px] font-bold ${styles.badge}`}
                    >
                      {count} articles
                    </span>
                  </div>
                  <p className="flex-1 text-[14px] leading-relaxed text-slate-600">
                    {item.description}
                  </p>
                  <span className="mt-5 inline-flex items-center gap-1.5 text-[13px] font-bold text-pu">
                    Explore category
                    <ArrowRight
                      size={15}
                      className="transition-transform group-hover:translate-x-1"
                    />
                  </span>
                  <div
                    className={`mt-5 h-1 w-full rounded-full bg-gradient-to-r ${styles.bar} opacity-70`}
                  />
                </Link>
              );
            })}
          </div>
        </div>
      </section>
    </>
  );
}
