import Link from "next/link";
import { ArrowRight, Search, Building2, Code2, MessageSquare } from "lucide-react";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";

export const metadata = generatePageMetadata({
  title: "Guides",
  description:
    "In-depth guides that walk law firms through winning in AI search — from AI search optimization fundamentals to schema, entity SEO, and AI chatbots.",
  slug: "resources/guides",
});

const guides = [
  {
    icon: Search,
    title: "The Complete Guide to AI Search Optimization for Law Firms",
    description:
      "A start-to-finish playbook for getting your firm cited by ChatGPT, Gemini, Perplexity, and Google AI Overviews — covering entity signals, content, and measurement.",
    href: "/services/ai-search-optimization",
  },
  {
    icon: Code2,
    title: "Structured Data & Schema Markup: A Law Firm's Technical Foundation",
    description:
      "How to implement LegalService, Attorney, and FAQ schema to unlock rich results and make your firm unmistakable to AI engines.",
    href: "/services/structured-data",
  },
  {
    icon: Building2,
    title: "Entity SEO for Law Firms: Becoming a Recognized Authority",
    description:
      "Build a consistent, trusted entity across your site, directories, and the knowledge graph so AI models confidently recommend you.",
    href: "/services/entity-seo",
  },
  {
    icon: MessageSquare,
    title: "Converting AI Search Traffic with Chatbots & AI Receptionists",
    description:
      "Capturing visibility is only half the battle — learn how 24/7 AI chat and receptionist systems turn AI-driven visitors into booked consultations.",
    href: "/services/ai-chatbots",
  },
];

export default function GuidesPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Guides | LexScale.ai",
          "In-depth AI search guides for law firms.",
          `${SITE_URL}/resources/guides`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <p className="mb-4 text-sm font-bold uppercase tracking-[0.2em] text-pu3">
            Resources
          </p>
          <h1 className="mx-auto max-w-[760px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Guides for winning AI search
          </h1>
          <p className="mx-auto mt-6 max-w-[600px] text-[17px] leading-relaxed text-white/70">
            Practical, step-by-step playbooks built specifically for law firms
            navigating the shift to AI-driven search.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-6 md:grid-cols-2">
            {guides.map((g) => {
              const Icon = g.icon;
              return (
                <Link
                  key={g.title}
                  href={g.href}
                  className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-200 hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(11,21,54,.14)]"
                >
                  <span className="mb-5 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Icon size={24} />
                  </span>
                  <h2 className="text-[20px] font-extrabold leading-snug tracking-tight text-navy">
                    {g.title}
                  </h2>
                  <p className="mt-3 flex-1 text-[15px] leading-relaxed text-slate-600">
                    {g.description}
                  </p>
                  <span className="mt-5 inline-flex items-center gap-1.5 text-[14px] font-bold text-pu">
                    Read Guide
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
              Prefer expert help over DIY?
            </h2>
            <p className="mx-auto mt-4 max-w-[520px] text-[16px] leading-relaxed text-white/70">
              Our team implements everything in these guides for you. Book a free
              strategy call to see what AI search could do for your firm.
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
