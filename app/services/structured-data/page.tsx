import {
  Code2,
  FileJson,
  Star,
  Scale,
  RefreshCcw,
  CheckCircle2,
  Bot,
  Sparkles,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";

const NAME = "Structured Data & Schema Markup for Law Firms";
const DESCRIPTION =
  "Schema markup tells search engines and AI models exactly what your firm's content means. LexScale implements clean, validated structured data that earns rich results and powers AI citations.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/structured-data",
});

const steps = [
  {
    title: "Markup Audit & Validation",
    body: "We crawl your site, surface existing schema, and run it through Google's Rich Results Test and Schema.org validation to find errors, missing types, and untapped opportunities.",
  },
  {
    title: "Schema Architecture",
    body: "We design the right markup map for a law firm — LegalService, Attorney, FAQPage, Review, BreadcrumbList, and Article — and define how they nest and reference each other across your site.",
  },
  {
    title: "Implementation in JSON-LD",
    body: "We deploy clean, Google-preferred JSON-LD, either directly in your templates or via your CMS, so every page emits accurate, machine-readable facts about your firm and content.",
  },
  {
    title: "Entity Linking",
    body: "We connect your schema to the wider web with sameAs references and consistent identifiers, reinforcing your firm's entity so AI models can corroborate and trust your data.",
  },
  {
    title: "Monitor & Maintain",
    body: "Schema standards and Google's supported types evolve. We monitor Search Console for enhancements and errors, then update markup so your rich results and AI eligibility hold steady.",
  },
];

const benefits = [
  {
    icon: Star,
    title: "Win Rich Results",
    body: "Star ratings, FAQs, and breadcrumbs in the search results lift click-through dramatically. Structured data is the only way to qualify for these eye-catching enhancements.",
  },
  {
    icon: Bot,
    title: "Feed the AI Engines",
    body: "ChatGPT, Gemini, and Perplexity parse structured data to understand and cite content. Clean schema makes your pages easier to extract and far more likely to be quoted.",
  },
  {
    icon: Scale,
    title: "Communicate Legal Expertise",
    body: "Law-specific schema like LegalService and Attorney lets you encode practice areas, credentials, and locations precisely — removing ambiguity for both Google and AI.",
  },
  {
    icon: CheckCircle2,
    title: "Validated & Error-Free",
    body: "Broken markup can suppress rich results or mislead AI. We validate every implementation so your structured data is trusted, not ignored.",
  },
];

const faqs = [
  {
    question: "What is structured data and why does my firm need it?",
    answer:
      "Structured data is standardized code (usually JSON-LD using Schema.org vocabulary) that labels what your content means — that this is your firm, these are your practice areas, this is a review. It helps Google show rich results and helps AI models accurately understand and cite your pages.",
  },
  {
    question: "Which schema types matter most for a law firm?",
    answer:
      "The core set is LegalService or Attorney for your firm and lawyers, FAQPage for question content, Review and AggregateRating for testimonials, BreadcrumbList for navigation, and Article for insights. We implement the combination that fits your site and content.",
  },
  {
    question: "Does schema markup directly improve rankings?",
    answer:
      "Schema isn't a direct ranking factor, but it improves how your results appear and how well engines understand your content — which lifts click-through and supports rankings indirectly. For AI search, accurate schema materially improves your odds of being cited.",
  },
  {
    question: "Will rich results show up immediately after implementation?",
    answer:
      "Eligibility begins once Google recrawls and validates the markup, typically within days to a few weeks. Appearance also depends on Google deciding the enhancement is useful for a given query, which we monitor and optimize for.",
  },
  {
    question: "Can you add schema without breaking my website?",
    answer:
      "Yes. JSON-LD is added in the page head or body and is invisible to visitors, so it doesn't affect design or layout. We test in staging and validate before and after deployment to ensure nothing breaks.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/structured-data"
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="green">
            <Code2 size={13} /> Structured Data & Schema
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Speak the Language Search Engines & AI Understand
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            Schema markup turns your content into machine-readable facts. We
            implement clean, validated structured data that earns rich results
            in Google and makes your firm easy for AI engines to understand and
            cite.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button
              href="/tools/ai-visibility-checker"
              variant="gold"
              size="lg"
            >
              Get a Free Strategy Call
            </Button>
            <Button
              href="/services/entity-seo"
              variant="outline"
              size="lg"
              className="border-white/25 text-white hover:border-white hover:text-white"
            >
              See Entity SEO
            </Button>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="green">What We Do</Tag>
          <h2 className="mt-4 max-w-[760px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We make your content unambiguous to machines
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            A page that reads beautifully to a human can still be opaque to a
            machine. Structured data fixes that by explicitly labeling what
            every element is — your firm, your attorneys, your reviews, your
            FAQs. Our schema program designs the right markup architecture for a
            law firm, implements it in Google-preferred JSON-LD, links it to your
            wider entity, and validates every line. The result is eligibility
            for rich results in search and dramatically cleaner data for the AI
            engines deciding which firms to cite.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step schema program
          </h2>
          <div className="mt-10 flex flex-col gap-5">
            {steps.map((step, i) => (
              <div
                key={i}
                className="flex gap-5 rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)]"
              >
                <span className="flex h-11 w-11 flex-shrink-0 items-center justify-center rounded-xl bg-gradient-to-br from-pu to-pu2 text-[17px] font-extrabold text-white">
                  {i + 1}
                </span>
                <div>
                  <h3 className="text-[18px] font-bold text-navy">
                    {step.title}
                  </h3>
                  <p className="mt-1.5 text-[15px] leading-relaxed text-slate-600">
                    {step.body}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="green">Why It Matters</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Clean markup is the price of admission for AI
          </h2>
          <div className="mt-10 grid gap-6 md:grid-cols-2">
            {benefits.map((b, i) => {
              const Icon = b.icon;
              return (
                <div
                  key={i}
                  className="rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)]"
                >
                  <span className="flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Icon size={22} />
                  </span>
                  <h3 className="mt-5 text-[18px] font-bold text-navy">
                    {b.title}
                  </h3>
                  <p className="mt-2 text-[15px] leading-relaxed text-slate-600">
                    {b.body}
                  </p>
                </div>
              );
            })}
          </div>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <FileJson size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Google-preferred JSON-LD
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <CheckCircle2 size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Validated, error-free markup
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Sparkles size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Rich result eligibility
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Implementation & Maintenance
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              Structured data done right for law firms
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              One-time schema implementation starts at $2,500, with ongoing
              maintenance from $400/month. Includes a full audit, JSON-LD
              deployment, validation, and Search Console monitoring.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button
                href="/tools/ai-visibility-checker"
                variant="gold"
                size="lg"
              >
                Get a Free Strategy Call
              </Button>
              <Button
                href="/services/structured-data"
                variant="outline"
                size="lg"
                className="border-white/30 text-white hover:border-white hover:text-white"
              >
                Request an Audit
              </Button>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <FAQ faqs={faqs} title="Structured Data & Schema FAQs" />
        </div>
      </section>
    </>
  );
}
