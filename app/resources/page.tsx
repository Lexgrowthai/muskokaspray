import { HelpCircle, BookOpen, FileText, GitCompare, ArrowRight } from "lucide-react";
import Link from "next/link";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";

export const metadata = generatePageMetadata({
  title: "Resources",
  description:
    "Free resources to help law firms understand and win in AI search — FAQs, a plain-English glossary, in-depth guides, and head-to-head comparisons.",
  slug: "resources",
});

const categories = [
  {
    icon: HelpCircle,
    title: "FAQ",
    description:
      "Straight answers to the questions law firms ask most about AI search, our services, getting started, and pricing.",
    href: "/resources/faq",
  },
  {
    icon: BookOpen,
    title: "Glossary",
    description:
      "An A–Z glossary of AI search and SEO terms — from AI Overviews and entity SEO to schema markup and topical authority.",
    href: "/resources/glossary",
  },
  {
    icon: FileText,
    title: "Guides",
    description:
      "Step-by-step playbooks that walk you through optimizing your firm for ChatGPT, Gemini, Perplexity, and Google AI.",
    href: "/resources/guides",
  },
  {
    icon: GitCompare,
    title: "Comparisons",
    description:
      "Clear, unbiased breakdowns comparing platforms and strategies so you can make confident decisions for your firm.",
    href: "/resources/comparisons",
  },
];

export default function ResourcesPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Resources | LexScale.ai",
          "Free AI search and SEO resources for law firms.",
          `${SITE_URL}/resources`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <p className="mb-4 text-sm font-bold uppercase tracking-[0.2em] text-pu3">
            Knowledge Hub
          </p>
          <h1 className="mx-auto max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Everything law firms need to understand AI search
          </h1>
          <p className="mx-auto mt-6 max-w-[640px] text-[17px] leading-relaxed text-white/70">
            AI is rewriting how clients find lawyers. Our resource library gives
            you the definitions, guides, and comparisons to keep your firm
            visible everywhere clients are searching.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-6 md:grid-cols-2">
            {categories.map((cat) => {
              const Icon = cat.icon;
              return (
                <Link
                  key={cat.href}
                  href={cat.href}
                  className="group rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-200 hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(11,21,54,.14)]"
                >
                  <span className="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Icon size={24} />
                  </span>
                  <h2 className="text-[22px] font-extrabold tracking-tight text-navy">
                    {cat.title}
                  </h2>
                  <p className="mt-3 text-[15px] leading-relaxed text-slate-600">
                    {cat.description}
                  </p>
                  <span className="mt-5 inline-flex items-center gap-1.5 text-[14px] font-bold text-pu">
                    Explore
                    <ArrowRight
                      size={16}
                      className="transition-transform duration-200 group-hover:translate-x-1"
                    />
                  </span>
                </Link>
              );
            })}
          </div>

          <div className="mt-16 rounded-2xl bg-navy p-10 text-center shadow-[0_6px_28px_rgba(11,21,54,.16)] md:p-14">
            <h2 className="text-[clamp(24px,2.6vw,34px)] font-extrabold tracking-tight text-white">
              Want to see how your firm shows up in AI search?
            </h2>
            <p className="mx-auto mt-4 max-w-[560px] text-[16px] leading-relaxed text-white/70">
              Run a free AI visibility check and find out exactly where you
              stand across ChatGPT, Gemini, Perplexity, and Google AI Overviews.
            </p>
            <div className="mt-8 flex justify-center">
              <Button
                href="/tools/ai-visibility-checker"
                variant="gold"
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
