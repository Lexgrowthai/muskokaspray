import Link from "next/link";
import { ArrowRight, Bot, Search, Sparkles, Phone } from "lucide-react";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";

export const metadata = generatePageMetadata({
  title: "Comparisons",
  description:
    "Clear, unbiased comparisons to help law firms make confident decisions — ChatGPT vs Gemini, AI SEO vs traditional SEO, AISO vs SEO, and AI chatbot vs receptionist.",
  slug: "resources/comparisons",
});

const comparisons = [
  {
    icon: Bot,
    title: "ChatGPT vs Gemini",
    description:
      "Two of the most-used AI assistants for finding services. We break down how each surfaces and cites law firms, what signals each weighs, and where your firm should focus to win on both.",
    href: "/services/chatgpt-optimization",
  },
  {
    icon: Search,
    title: "AI SEO vs Traditional SEO",
    description:
      "Where classic SEO ends and AI SEO begins. Understand what carries over, what's new, and why optimizing for AI answers requires entity and structured-data work that traditional SEO ignores.",
    href: "/services/ai-seo",
  },
  {
    icon: Sparkles,
    title: "AISO vs SEO",
    description:
      "AI Search Optimization targets being cited inside answers; SEO targets ranking in a list of links. See how the goals, signals, and metrics differ — and why modern firms need both.",
    href: "/services/ai-search-optimization",
  },
  {
    icon: Phone,
    title: "AI Chatbot vs AI Receptionist",
    description:
      "Both capture leads after hours, but they solve different problems. Compare conversational website chat against an AI receptionist that answers and qualifies calls, and learn which your firm needs.",
    href: "/services/ai-receptionists",
  },
];

export default function ComparisonsPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Comparisons | LexScale.ai",
          "Unbiased comparisons of AI platforms and strategies for law firms.",
          `${SITE_URL}/resources/comparisons`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <p className="mb-4 text-sm font-bold uppercase tracking-[0.2em] text-pu3">
            Resources
          </p>
          <h1 className="mx-auto max-w-[760px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Comparisons to guide your decisions
          </h1>
          <p className="mx-auto mt-6 max-w-[600px] text-[17px] leading-relaxed text-white/70">
            Side-by-side breakdowns of the platforms and strategies shaping AI
            search — so your firm can invest with confidence.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-6 md:grid-cols-2">
            {comparisons.map((c) => {
              const Icon = c.icon;
              return (
                <Link
                  key={c.title}
                  href={c.href}
                  className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-200 hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(11,21,54,.14)]"
                >
                  <span className="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Icon size={24} />
                  </span>
                  <h2 className="text-[21px] font-extrabold tracking-tight text-navy">
                    {c.title}
                  </h2>
                  <p className="mt-3 flex-1 text-[15px] leading-relaxed text-slate-600">
                    {c.description}
                  </p>
                  <span className="mt-5 inline-flex items-center gap-1.5 text-[14px] font-bold text-pu">
                    Read Comparison
                    <ArrowRight
                      size={16}
                      className="transition-transform duration-200 group-hover:translate-x-1"
                    />
                  </span>
                </Link>
              );
            })}
          </div>

          <div className="mt-16 rounded-2xl bg-navy p-10 text-center shadow-[0_6px_28px_rgba(11,21,54,.16)]">
            <h2 className="text-[clamp(22px,2.4vw,30px)] font-extrabold tracking-tight text-white">
              Not sure which approach fits your firm?
            </h2>
            <p className="mx-auto mt-4 max-w-[520px] text-[16px] leading-relaxed text-white/70">
              We'll assess your situation and recommend the right mix on a free
              strategy call — no pressure, just a clear plan.
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
