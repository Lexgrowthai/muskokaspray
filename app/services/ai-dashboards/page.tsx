import {
  LayoutDashboard,
  BarChart3,
  Bell,
  PlugZap,
  RefreshCcw,
  Eye,
  Gauge,
  PieChart,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";

const NAME = "AI Dashboards & Analytics for Law Firms";
const DESCRIPTION =
  "See your firm's AI visibility, leads, and ROI in one live dashboard. LexScale builds custom analytics that unify AI citations, search rankings, calls, and revenue for law firms.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/ai-dashboards",
});

const steps = [
  {
    title: "Goals & Metrics Workshop",
    body: "We start with the numbers that actually run your firm — qualified leads, signed cases, cost per acquisition, AI visibility — and define the KPIs your dashboard will track.",
  },
  {
    title: "Data Source Integration",
    body: "We connect the sources: AI citation monitors, Google Search Console and Analytics, your call tracking, CRM, and ad platforms, unifying them into one clean data layer.",
  },
  {
    title: "Dashboard Design & Build",
    body: "We design a clear, role-aware dashboard — a partner-level overview plus operational detail for your marketing team — built to answer your real questions at a glance.",
  },
  {
    title: "Alerts & Automation",
    body: "We configure automated alerts for what matters: a drop in AI citations, a spike in missed calls, or a campaign outperforming, so your team acts on signals instead of digging for them.",
  },
  {
    title: "Review & Refine",
    body: "We meet to interpret the data, tie marketing activity to revenue, and refine the dashboard as your firm's goals and channels evolve over time.",
  },
];

const benefits = [
  {
    icon: Eye,
    title: "One Source of Truth",
    body: "Stop stitching together five tools and conflicting reports. Every metric — from AI citations to signed cases — lives in one place your whole team trusts.",
  },
  {
    icon: PieChart,
    title: "Prove Marketing ROI",
    body: "Connect spend to revenue. See which channels and AI engines actually drive cases, so budget goes where it returns the most.",
  },
  {
    icon: Gauge,
    title: "Decisions in Real Time",
    body: "Live data and alerts mean you spot problems and opportunities as they happen, not in a report that lands three weeks too late.",
  },
];

const faqs = [
  {
    question: "What does an AI dashboard actually show me?",
    answer:
      "A unified live view of your firm's growth: AI visibility (citations across ChatGPT, Gemini, and Perplexity), search rankings and traffic, calls and form leads, signed cases, cost per acquisition, and revenue — tied together so you can see the full funnel in one place.",
  },
  {
    question: "Which tools and platforms can you connect?",
    answer:
      "We integrate AI citation tracking, Google Search Console, Google Analytics 4, call tracking systems, common legal CRMs and intake tools, and ad platforms like Google and Meta Ads. If you use it and it has data, we can usually pull it in.",
  },
  {
    question: "Do I need technical skills to use the dashboard?",
    answer:
      "No. We design dashboards for busy attorneys and marketing staff — clean visuals, plain-language labels, and a high-level overview by default, with the option to drill into detail. We also train your team on how to read it.",
  },
  {
    question: "Can the dashboard track my AI search visibility specifically?",
    answer:
      "Yes. That's a core feature. We surface your citation share across the major AI engines, trend it over time, and connect it to downstream leads so you can see how AI visibility translates into actual cases.",
  },
  {
    question: "Is the dashboard custom or a template?",
    answer:
      "Custom. We build around your firm's specific goals, channels, and data sources rather than forcing a generic template, then refine it as your needs change. You own the dashboard and the underlying data.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/ai-dashboards"
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Services", url: `${SITE_URL}/services` },
          { name: NAME, url: `${SITE_URL}/services/ai-dashboards` },
        ])}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="purple">
            <LayoutDashboard size={13} /> AI Dashboards & Analytics
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            See Every Number That Grows Your Firm — in One Place
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            AI visibility, rankings, calls, leads, and revenue — unified in a
            live dashboard built for law firms. Stop guessing what&apos;s
            working and start running your marketing on real, connected data.
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
              href="/tools/roi-calculator"
              variant="outline"
              size="lg"
              className="border-white/25 text-white hover:border-white hover:text-white"
            >
              Try the ROI Calculator
            </Button>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">What We Do</Tag>
          <h2 className="mt-4 max-w-[760px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We turn scattered data into clear decisions
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            Most firms have plenty of data and almost no clarity — it lives in
            Google Analytics, a call-tracking app, a CRM, and an AI monitor that
            never talk to each other. Our AI dashboard service unifies all of it
            into a single live view designed for how law firms actually make
            decisions. You see AI citations, search performance, lead flow, and
            revenue together, with automated alerts when something moves. The
            result is a marketing operation you can steer with confidence
            instead of hunches.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step dashboard build
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
          <Tag variant="purple">Why It Matters</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            You can&apos;t grow what you can&apos;t see
          </h2>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
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
              <PlugZap size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Multi-source integration
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <BarChart3 size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Live KPI visualization
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <Bell size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Automated alerts
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Build & Manage
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              A custom analytics dashboard for your firm
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              Dashboard builds start at $3,500 with managed hosting and ongoing
              refinement from $500/month. Includes integration, custom design,
              alerts, and quarterly strategy reviews with your team.
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
                href="/services/ai-citation-tracking"
                variant="outline"
                size="lg"
                className="border-white/30 text-white hover:border-white hover:text-white"
              >
                See Citation Tracking
              </Button>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <FAQ faqs={faqs} title="AI Dashboards & Analytics FAQs" />
        </div>
      </section>
    </>
  );
}
