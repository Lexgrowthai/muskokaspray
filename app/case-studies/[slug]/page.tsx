import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { MapPin, CheckCircle2, Quote } from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";

interface ResultStat {
  value: string;
  label: string;
}

interface Testimonial {
  quote: string;
  author: string;
  role: string;
}

interface CaseStudy {
  slug: string;
  practiceArea: string;
  firm: string;
  location: string;
  metaTitle: string;
  metaDescription: string;
  intro: string;
  challenge: string;
  solution: string;
  solutionSteps: string[];
  results: ResultStat[];
  testimonial: Testimonial;
}

const CASE_STUDIES: Record<string, CaseStudy> = {
  "personal-injury": {
    slug: "personal-injury",
    practiceArea: "Personal Injury",
    firm: "Hargrove Injury Law",
    location: "Houston, TX",
    metaTitle: "Personal Injury Case Study — +512% Leads in AI Search",
    metaDescription:
      "How Hargrove Injury Law became the most-cited personal injury firm in Houston across ChatGPT, Gemini, and Google AI Overviews, growing organic leads 512% in nine months.",
    intro:
      "Hargrove Injury Law is an eight-attorney personal injury practice in Houston handling car accidents, truck collisions, and premises liability. For years the firm relied almost entirely on referrals and paid ads — but rising ad costs and a flood of national competitors squeezed their margins and made growth unpredictable.",
    challenge:
      "When prospective clients started asking ChatGPT and Google's AI Overviews \"who is the best injury lawyer in Houston?\", Hargrove was nowhere to be found. Their website was technically dated, had no structured data, and almost no content that AI engines could confidently cite. Meanwhile competitors with weaker case results were being recommended by name. The firm was paying $90+ per click for keywords it couldn't win organically, and its cost per signed case had nearly doubled in two years.",
    solution:
      "We rebuilt Hargrove's digital foundation as an AI-first authority engine — making the firm the clearest, most trustworthy, and most machine-readable answer for injury questions in the Houston market.",
    solutionSteps: [
      "Migrated the site to a fast, conversion-built platform with full LegalService and Attorney structured data so AI engines could parse the firm's expertise unambiguously.",
      "Published 40+ answer-shaped practice pages and FAQs mapped to the exact questions people ask AI engines about injury claims, settlements, and the Texas legal process.",
      "Built the firm's entity profile across authoritative sources, aligning their name, attorneys, case results, and reviews so AI models recognized Hargrove as a known, credible entity.",
      "Implemented AI citation tracking to monitor where ChatGPT, Gemini, and Perplexity surfaced the firm — then doubled down on the topics already winning.",
      "Added a 24/7 AI receptionist and intake chatbot so the surge of new inquiries converted instead of going to voicemail.",
    ],
    results: [
      { value: "+512%", label: "Organic leads in 9 months" },
      { value: "#1", label: "Most-cited injury firm in ChatGPT (Houston)" },
      { value: "-44%", label: "Cost per signed case" },
      { value: "3.1x", label: "Return on engagement in year one" },
    ],
    testimonial: {
      quote:
        "We used to fight for every click. Now AI tools recommend us by name before anyone even reaches our site. LexScale didn't just bring traffic — they made us the answer.",
      author: "Marcus Hargrove",
      role: "Managing Partner, Hargrove Injury Law",
    },
  },
  "family-law": {
    slug: "family-law",
    practiceArea: "Family Law",
    firm: "Bennett Family Law Group",
    location: "Toronto, ON",
    metaTitle: "Family Law Case Study — Consultations Tripled in Two Quarters",
    metaDescription:
      "How Bennett Family Law Group grew qualified consultations 287% by rebuilding their site and answer content around the real questions families ask AI engines.",
    intro:
      "Bennett Family Law Group is a five-lawyer practice in Toronto focused on divorce, custody, and high-net-worth separation. Their reputation was excellent locally, but their online presence didn't reflect it — and the emotionally charged, research-heavy nature of family law meant prospective clients spent weeks asking questions online before ever calling.",
    challenge:
      "Families facing separation increasingly turned to ChatGPT and Google AI for guidance on custody, support, and process before choosing a lawyer. Bennett's site offered thin, generic content that AI engines ignored, so the firm was invisible at the exact moment trust was being formed. Worse, the contact path was clunky and after-hours inquiries — common for stressed clients — went unanswered until the next business day.",
    solution:
      "We repositioned Bennett as the calm, authoritative voice answering the questions Ontario families actually ask — and made it effortless to turn that trust into a booked consultation.",
    solutionSteps: [
      "Rebuilt the site with clear, empathetic answer content covering Ontario divorce, custody, and support questions, structured so AI engines could quote it directly.",
      "Added FAQPage and LegalService structured data plus author attribution to establish the firm's lawyers as recognized subject-matter experts.",
      "Created practice-specific landing pages for divorce, custody, and high-net-worth separation, each with a frictionless consultation booking flow.",
      "Deployed an AI intake chatbot that answers common questions 24/7 and books consultations directly into the firm's calendar.",
      "Tracked AI citations to continuously expand the topics where the firm was being surfaced and recommended.",
    ],
    results: [
      { value: "+287%", label: "Qualified consultations / month" },
      { value: "+163%", label: "Organic search traffic" },
      { value: "41%", label: "Of consults booked after hours" },
      { value: "2 qtrs", label: "To triple booked consultations" },
    ],
    testimonial: {
      quote:
        "Clients now tell us they found their answers on our site — and that's why they trusted us before we even met. The after-hours bookings alone changed our practice.",
      author: "Claire Bennett",
      role: "Founding Partner, Bennett Family Law Group",
    },
  },
};

// Generic template for the remaining practice areas so every slug renders.
const GENERIC: Record<
  string,
  { practiceArea: string; firm: string; location: string; stat: string; statLabel: string }
> = {
  "criminal-law": {
    practiceArea: "Criminal Law",
    firm: "Vega Criminal Defense",
    location: "Phoenix, AZ",
    stat: "+341%",
    statLabel: "After-hours calls captured",
  },
  "estate-law": {
    practiceArea: "Estate Law",
    firm: "Whitfield Estate & Trust",
    location: "Naples, FL",
    stat: "+196%",
    statLabel: "High-intent organic traffic",
  },
  "corporate-law": {
    practiceArea: "Corporate Law",
    firm: "Lindqvist Corporate Counsel",
    location: "New York, NY",
    stat: "+228%",
    statLabel: "Inbound qualified deals",
  },
};

function buildGeneric(slug: string): CaseStudy | null {
  const g = GENERIC[slug];
  if (!g) return null;
  return {
    slug,
    practiceArea: g.practiceArea,
    firm: g.firm,
    location: g.location,
    metaTitle: `${g.practiceArea} Case Study — ${g.stat} Growth`,
    metaDescription: `How ${g.firm} grew with a LexScale.ai AI growth system — ${g.stat} ${g.statLabel.toLowerCase()}.`,
    intro: `${g.firm} is a respected ${g.practiceArea.toLowerCase()} practice in ${g.location}. Like many firms, they delivered outstanding results for clients but struggled to be found in an AI-driven search landscape where prospects increasingly ask ChatGPT, Gemini, and Perplexity for recommendations before ever picking up the phone.`,
    challenge: `Despite a strong local reputation, ${g.firm} was effectively invisible to the AI engines now shaping how clients choose counsel. Their website lacked the structured data and authoritative, answer-shaped content that AI models rely on to cite a source, so competitors were being recommended in their place — and valuable inquiries slipped away.`,
    solution: `We applied the LexScale.ai AI growth system to make ${g.firm} the clearest, most trustworthy, and most machine-readable answer for ${g.practiceArea.toLowerCase()} questions in their market.`,
    solutionSteps: [
      "Rebuilt the firm's site on a fast, conversion-focused platform with complete legal structured data.",
      `Published answer-shaped content mapped to the real questions clients ask AI engines about ${g.practiceArea.toLowerCase()}.`,
      "Strengthened the firm's entity profile across authoritative sources so AI models recognized it as credible.",
      "Added 24/7 AI intake so the increase in inquiries converted instead of being missed.",
      "Tracked AI citations and continuously expanded the winning topics.",
    ],
    results: [
      { value: g.stat, label: g.statLabel },
      { value: "+150%", label: "Organic search visibility" },
      { value: "24/7", label: "AI-powered client intake" },
      { value: "Top 3", label: "AI citation share in market" },
    ],
    testimonial: {
      quote: `LexScale made us the firm AI tools recommend by name. The difference in qualified inquiries has been transformative for our ${g.practiceArea.toLowerCase()} practice.`,
      author: `${g.firm.split(" ")[0]} Partner`,
      role: `Managing Partner, ${g.firm}`,
    },
  };
}

function getCaseStudy(slug: string): CaseStudy | null {
  return CASE_STUDIES[slug] ?? buildGeneric(slug);
}

export function generateStaticParams() {
  return [
    { slug: "personal-injury" },
    { slug: "family-law" },
    { slug: "criminal-law" },
    { slug: "estate-law" },
    { slug: "corporate-law" },
  ];
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const cs = getCaseStudy(slug);
  if (!cs) {
    return generatePageMetadata({
      title: "Case Study Not Found",
      description: "This case study could not be found.",
      slug: `case-studies/${slug}`,
    });
  }
  return generatePageMetadata({
    title: cs.metaTitle,
    description: cs.metaDescription,
    slug: `case-studies/${slug}`,
  });
}

export default async function CaseStudyPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const cs = getCaseStudy(slug);

  if (!cs) {
    notFound();
  }

  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          cs.metaTitle,
          cs.metaDescription,
          `${SITE_URL}/case-studies/${cs.slug}`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[820px] px-6 py-20 md:px-10">
          <div className="flex items-center gap-3">
            <Tag variant="gold">{cs.practiceArea}</Tag>
            <span className="flex items-center gap-1 text-[13px] text-white/70">
              <MapPin size={13} /> {cs.location}
            </span>
          </div>
          <h1 className="mt-5 text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            {cs.firm}
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/70">
            {cs.intro}
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[820px] px-6 py-20 md:px-10">
          {/* Challenge */}
          <div>
            <h2 className="text-[clamp(22px,2.6vw,30px)] font-extrabold tracking-tight text-navy">
              The Challenge
            </h2>
            <p className="mt-4 text-[16px] leading-relaxed text-slate-600">
              {cs.challenge}
            </p>
          </div>

          {/* Solution */}
          <div className="mt-14">
            <h2 className="text-[clamp(22px,2.6vw,30px)] font-extrabold tracking-tight text-navy">
              The Solution
            </h2>
            <p className="mt-4 text-[16px] leading-relaxed text-slate-600">
              {cs.solution}
            </p>
            <ul className="mt-6 space-y-4">
              {cs.solutionSteps.map((step, i) => (
                <li key={i} className="flex gap-3">
                  <CheckCircle2
                    size={20}
                    className="mt-0.5 shrink-0 text-pu"
                  />
                  <span className="text-[15px] leading-relaxed text-slate-700">
                    {step}
                  </span>
                </li>
              ))}
            </ul>
          </div>

          {/* Results */}
          <div className="mt-14">
            <h2 className="text-[clamp(22px,2.6vw,30px)] font-extrabold tracking-tight text-navy">
              The Results
            </h2>
            <div className="mt-6 grid grid-cols-2 gap-5 md:grid-cols-4">
              {cs.results.map((r, i) => (
                <div
                  key={i}
                  className="rounded-2xl border border-pu/10 bg-white p-6 text-center shadow-[0_6px_28px_rgba(11,21,54,.08)]"
                >
                  <div className="text-[clamp(26px,3vw,34px)] font-extrabold leading-none text-grad-purple">
                    {r.value}
                  </div>
                  <div className="mt-2 text-[12px] font-semibold leading-snug text-slate-500">
                    {r.label}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Testimonial */}
          <figure className="mt-14 rounded-2xl bg-navy p-8 md:p-10">
            <Quote size={28} className="text-gold2" />
            <blockquote className="mt-4 text-[clamp(18px,2.2vw,24px)] font-semibold leading-snug text-white">
              &ldquo;{cs.testimonial.quote}&rdquo;
            </blockquote>
            <figcaption className="mt-6 text-[14px] text-white/70">
              <span className="font-bold text-white">
                {cs.testimonial.author}
              </span>{" "}
              — {cs.testimonial.role}
            </figcaption>
          </figure>

          {/* CTA */}
          <div className="mt-14 text-center">
            <h2 className="text-[clamp(22px,2.6vw,30px)] font-extrabold tracking-tight text-navy">
              Want results like {cs.firm}?
            </h2>
            <p className="mx-auto mt-3 max-w-[520px] text-[16px] leading-relaxed text-slate-600">
              Book a free strategy call and we&apos;ll show you exactly how to
              win clients in AI search for your practice area and market.
            </p>
            <div className="mt-6 flex flex-wrap justify-center gap-3">
              <Button href="/tools/ai-visibility-checker" variant="primary" size="lg">
                Get a Free Strategy Call
              </Button>
              <Button href="/case-studies" variant="outline" size="lg">
                View All Case Studies
              </Button>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
