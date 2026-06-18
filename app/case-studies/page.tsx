import type { Metadata } from "next";
import { MapPin, ArrowRight } from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";

export const metadata: Metadata = generatePageMetadata({
  title: "Law Firm Case Studies",
  description:
    "Real results from law firms using LexScale.ai AI growth systems — see how personal injury, family, criminal, estate, and corporate firms grew leads, traffic, and revenue.",
  slug: "case-studies",
});

interface CaseStudyCard {
  slug: string;
  practiceArea: string;
  location: string;
  firm: string;
  stat: string;
  statLabel: string;
  summary: string;
}

const CASE_STUDIES: CaseStudyCard[] = [
  {
    slug: "personal-injury",
    practiceArea: "Personal Injury",
    location: "Houston, TX",
    firm: "Hargrove Injury Law",
    stat: "+512%",
    statLabel: "Organic leads in 9 months",
    summary:
      "A mid-size PI firm went from invisible in AI search to the most-cited injury firm in Houston across ChatGPT and Google AI Overviews.",
  },
  {
    slug: "family-law",
    practiceArea: "Family Law",
    location: "Toronto, ON",
    firm: "Bennett Family Law Group",
    stat: "+287%",
    statLabel: "Qualified consultations / month",
    summary:
      "By rebuilding their site and answer content around real client questions, this family firm tripled booked consultations in two quarters.",
  },
  {
    slug: "criminal-law",
    practiceArea: "Criminal Law",
    location: "Phoenix, AZ",
    firm: "Vega Criminal Defense",
    stat: "+341%",
    statLabel: "After-hours calls captured",
    summary:
      "An AI receptionist plus 24/7 intake stopped this defense practice from losing urgent, high-value calls to faster competitors.",
  },
  {
    slug: "estate-law",
    practiceArea: "Estate Law",
    location: "Naples, FL",
    firm: "Whitfield Estate &amp; Trust",
    stat: "+196%",
    statLabel: "High-intent organic traffic",
    summary:
      "Entity SEO and structured data made this estate practice the default answer for trust and probate questions across AI engines.",
  },
  {
    slug: "corporate-law",
    practiceArea: "Corporate Law",
    location: "New York, NY",
    firm: "Lindqvist Corporate Counsel",
    stat: "+228%",
    statLabel: "Inbound qualified deals",
    summary:
      "A boutique corporate firm built authority as a known entity, winning citations in Perplexity and Gemini for M&amp;A and formation queries.",
  },
];

export default function CaseStudiesPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Law Firm Case Studies",
          "Real results from law firms using LexScale.ai AI growth systems.",
          `${SITE_URL}/case-studies`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 text-center md:px-10">
          <Tag variant="gold">CASE STUDIES</Tag>
          <h1 className="mt-5 text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Real firms. Real growth.
          </h1>
          <p className="mx-auto mt-5 max-w-[680px] text-[17px] leading-relaxed text-white/70">
            Since 2013 we&apos;ve helped law firms across the US and Canada win
            clients in AI search. Here&apos;s what that looks like in practice —
            4,800+ leads, 3,200+ calls, and $12M+ in added revenue.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-6 md:grid-cols-2">
            {CASE_STUDIES.map((cs) => (
              <div
                key={cs.slug}
                className="flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all duration-200 hover:-translate-y-1 hover:shadow-[0_14px_40px_rgba(11,21,54,.14)]"
              >
                <div className="flex items-center justify-between">
                  <Tag variant="purple">{cs.practiceArea}</Tag>
                  <span className="flex items-center gap-1 text-[13px] text-slate-500">
                    <MapPin size={13} />
                    <span dangerouslySetInnerHTML={{ __html: cs.location }} />
                  </span>
                </div>

                <div className="mt-6 flex items-end gap-3">
                  <div className="text-[clamp(36px,5vw,48px)] font-extrabold leading-none text-grad-purple">
                    {cs.stat}
                  </div>
                  <div className="pb-1 text-[13px] font-semibold text-slate-500">
                    {cs.statLabel}
                  </div>
                </div>

                <h2
                  className="mt-5 text-[18px] font-extrabold tracking-tight text-navy"
                  dangerouslySetInnerHTML={{ __html: cs.firm }}
                />
                <p
                  className="mt-2 flex-1 text-[15px] leading-relaxed text-slate-600"
                  dangerouslySetInnerHTML={{ __html: cs.summary }}
                />

                <div className="mt-6">
                  <Button
                    href={`/case-studies/${cs.slug}`}
                    variant="ghost"
                    size="sm"
                  >
                    Read Case Study <ArrowRight size={15} />
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
