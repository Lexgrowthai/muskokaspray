import Link from "next/link";
import {
  Building2,
  Users,
  Activity,
  Clock,
  Eye,
  ShieldCheck,
  PhoneCall,
  Globe,
  Search,
  FileText,
  Workflow,
  BarChart3,
  MessageSquare,
  ArrowRight,
  Heart,
  Compass,
  Zap,
} from "lucide-react";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";

export const metadata = generatePageMetadata({
  title: "About LexScale.ai — Built for Law Firms, Powered by AI",
  description:
    "LexScale.ai combines 10+ years of legal marketing experience with cutting-edge AI. Learn how we help law firms grow through intelligent automation and AI-powered search visibility.",
  slug: "about",
});

const TIMELINE = [
  {
    year: "2013 — Founded",
    title: "Traditional Legal Marketing",
    desc: "Started helping law firms with professional website development and search engine optimization — building online visibility from the ground up.",
    gold: false,
  },
  {
    year: "2015 – 2019",
    title: "Deepening Legal Expertise",
    desc: "Expanded into local search, Google Business optimization, and content marketing. Developed a deep understanding of how legal clients search, evaluate, and choose lawyers.",
    gold: false,
  },
  {
    year: "2020 – 2022",
    title: "Watching the Shift Begin",
    desc: "Recognized the early signals of AI's impact on search behavior and client engagement. Began building frameworks for the next generation of legal growth.",
    gold: false,
  },
  {
    year: "2023 — Transformation",
    title: "LexScale.ai Is Born",
    desc: "Combined a decade of legal marketing experience with modern AI to create the most comprehensive growth ecosystem built exclusively for law firms.",
    gold: true,
  },
  {
    year: "Today",
    title: "AI-Powered Growth at Scale",
    desc: "Delivering AI receptionists, intelligent websites, search visibility systems, and automation tools that help law firms compete in an increasingly digital world.",
    gold: true,
  },
];

const EVO_OLD = [
  "WordPress Websites",
  "Search Engine Optimization",
  "Local Search Optimization",
  "Content Marketing",
  "Google Business Profile",
];

const EVO_NEW = [
  "AI Receptionists",
  "AI Website Systems",
  "AI Search Visibility",
  "AI Chat Assistants",
  "Workflow Automation",
  "Lead Tracking & Analytics",
];

const DIFFERENCE = [
  {
    icon: Building2,
    title: "Law Firms Only",
    desc: "Every strategy, website, and system we build is designed around how legal clients search, evaluate, and engage with lawyers. We don't serve every industry — we master one.",
  },
  {
    icon: Users,
    title: "Hands-On Approach",
    desc: "Because we remain selective about the firms we work with, we maintain a hands-on approach that prioritizes quality, responsiveness, and long-term relationships.",
  },
  {
    icon: Activity,
    title: "Results-Driven",
    desc: "We measure success by what matters to you: more qualified leads, more consultations booked, stronger visibility, and better client experiences.",
  },
  {
    icon: Clock,
    title: "Fast Response Times",
    desc: "Direct access to your team. No ticketing systems, no junior account managers. When you need something, you reach someone who can act immediately.",
  },
  {
    icon: Eye,
    title: "Full Transparency",
    desc: "Clear reporting, honest communication, and no hidden fees. You always know what we're doing, why we're doing it, and what results it's producing.",
  },
  {
    icon: ShieldCheck,
    title: "Long-Term Partnerships",
    desc: "We build relationships, not transactions. Our clients stay with us because we continue to deliver value as their practice grows and the landscape evolves.",
  },
];

const SYSTEMS = [
  {
    icon: PhoneCall,
    title: "AI Receptionist & Voice Systems",
    items: [
      "24/7 AI Call Answering",
      "Voice AI Assistants",
      "Missed Call Text-Back Automation",
      "Consultation Booking Systems",
      "Call Recording & Summaries",
      "SMS Follow-Up Automation",
    ],
  },
  {
    icon: Globe,
    title: "AI Website Systems",
    items: [
      "High-Converting Law Firm Websites",
      "AI Chat Assistants",
      "Mobile-First Design",
      "Conversion Tracking",
      "Dynamic Content Systems",
      "Speed Optimization",
    ],
  },
  {
    icon: Search,
    title: "AI Search Visibility Systems",
    items: [
      "AI SEO Optimization",
      "Structured Data & Schema Markup",
      "Entity Development",
      "Local & Voice Search Optimization",
      "AI Search Optimization (AISO)",
      "Authority Building & Content Architecture",
    ],
  },
  {
    icon: FileText,
    title: "AI Content Systems",
    items: [
      "Long-Form Authority Content",
      "FAQ Generation",
      "Blog Content Systems",
      "Knowledge Base Development",
      "Internal Linking Systems",
      "Practice Area Content Clusters",
    ],
  },
  {
    icon: Workflow,
    title: "AI Automation Systems",
    items: [
      "Email & SMS Automation",
      "Workflow Automation",
      "CRM Integrations",
      "Appointment Scheduling",
      "Lead Capture Systems",
    ],
  },
  {
    icon: BarChart3,
    title: "Analytics & Intelligence",
    items: [
      "Call Tracking & Lead Attribution",
      "Dashboard Reporting",
      "ROI Monitoring",
      "Conversion Tracking",
      "Performance Analytics",
      "Pipeline Tracking",
    ],
  },
  {
    icon: MessageSquare,
    title: "AI Client Experience Systems",
    items: [
      "Live Chat Systems",
      "AI Intake Assistants",
      "Instant Response Systems",
      "FAQ Assistants",
      "Consultation Booking Systems",
    ],
  },
];

const TECH = [
  {
    label: "Artificial Intelligence",
    chips: ["OpenAI", "Claude (Anthropic)", "Google Gemini", "Perplexity", "Grok", "ElevenLabs"],
  },
  {
    label: "Voice AI & Communication",
    chips: ["Twilio", "Voice AI Systems", "SMS Automation", "AI Receptionists"],
  },
  {
    label: "Website & Development",
    chips: ["Vercel", "GitHub", "Supabase", "Cloudflare", "Astro", "Next.js"],
  },
  {
    label: "Automation & Integrations",
    chips: ["Make.com", "Zapier", "Calendly", "CRM Platforms"],
  },
  {
    label: "Analytics & Search",
    chips: [
      "Google Analytics",
      "Google Search Console",
      "Google Business Profile",
      "AI Visibility Tracking",
      "Call Tracking Systems",
    ],
  },
  {
    label: "Payment Systems",
    chips: ["Stripe", "PayPal", "Square"],
  },
];

const PHILOSOPHY = [
  {
    icon: Heart,
    title: "Behind Every Strategy",
    desc: "Behind every website, automation, and AI system is a commitment to helping lawyers serve more people and build stronger practices.",
  },
  {
    icon: Compass,
    title: "Looking Beyond Google",
    desc: "Potential clients increasingly discover firms through AI platforms, conversational search, and voice assistants. We prepare firms for where search is heading — not just where it's been.",
  },
  {
    icon: Zap,
    title: "Built for What's Next",
    desc: "Law firms that embrace these changes will thrive. Our role is to be the partner that helps you get there first.",
  },
];

const SEARCH_SHIFT = [
  { platform: "AI Platforms", sub: "ChatGPT · Perplexity · Gemini", pct: 72, trend: "↑ 72%", featured: true },
  { platform: "Google Search", sub: "Traditional results", pct: 85, trend: "85%", featured: false },
  { platform: "Voice Search", sub: "Siri · Alexa · Google", pct: 41, trend: "↑ 41%", featured: false },
  { platform: "Social Discovery", sub: "LinkedIn · Reviews", pct: 28, trend: "28%", featured: false },
];

export default function AboutPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "About LexScale.ai",
          "LexScale.ai combines 10+ years of legal marketing experience with cutting-edge AI to help law firms grow through intelligent automation and AI-powered visibility.",
          `${SITE_URL}/about`
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "About", url: `${SITE_URL}/about` },
        ])}
      />

      {/* HERO */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto grid max-w-[1100px] items-center gap-12 px-6 py-24 md:grid-cols-2 md:px-10 md:py-28">
          <div>
            <Tag variant="gold" className="mb-6">
              About LexScale.ai
            </Tag>
            <h1 className="text-[clamp(32px,4vw,56px)] font-black leading-[1.05] tracking-tight text-white">
              Built for Law Firms.
              <br />
              <span className="text-grad-gold">Powered by AI.</span>
            </h1>
            <p className="mt-5 max-w-[480px] text-[16px] leading-relaxed text-white/60">
              LexScale.ai was created with one goal in mind: helping law firms
              grow through modern technology, intelligent automation, and
              AI-powered search visibility.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button variant="gold" size="lg" href="/tools/ai-visibility-checker">
                Schedule a Strategy Call
              </Button>
              <Button
                href="/services"
                variant="outline"
                size="lg"
                className="border-white/30 text-white hover:border-pu hover:text-pu3"
              >
                Explore Our AI Systems
              </Button>
            </div>
            <div className="mt-8 flex flex-wrap gap-x-6 gap-y-2">
              {["Law Firm Exclusive", "Serving Firms Since 2013", "AI-First Methodology"].map(
                (t) => (
                  <span
                    key={t}
                    className="text-[12.5px] font-semibold text-white/50"
                  >
                    {t}
                  </span>
                )
              )}
            </div>
          </div>

          {/* Founding card */}
          <div className="flex flex-col gap-5">
            <div className="relative overflow-hidden rounded-3xl border border-gold/20 bg-white/[0.04] p-9">
              <span className="absolute inset-x-0 top-0 h-0.5 bg-gradient-to-r from-transparent via-gold2 to-transparent" />
              <div className="mb-1 text-[13px] font-bold uppercase tracking-wide text-white/50">
                Founded
              </div>
              <div className="text-[64px] font-black leading-none tracking-tighter text-gold2">
                2013
              </div>
              <p className="mt-3 text-[14px] leading-relaxed text-white/55">
                Long before AI transformed the legal industry, we were helping
                law firms grow online — building sustainable visibility and real
                client relationships.
              </p>
            </div>
            <div className="grid grid-cols-2 gap-3.5">
              {[
                { v: "10+", l: "Years Serving Law Firms", gold: true },
                { v: "100%", l: "Legal Industry Focus", gold: false },
                { v: "7", l: "AI System Categories", gold: true },
                { v: "US & CA", l: "Markets Served", gold: false },
              ].map((m) => (
                <div
                  key={m.l}
                  className="rounded-2xl border border-white/10 bg-white/[0.04] p-5"
                >
                  <div
                    className={`text-[28px] font-black tracking-tight ${
                      m.gold ? "text-gold2" : "text-white"
                    }`}
                  >
                    {m.v}
                  </div>
                  <div className="mt-1 text-[11px] font-semibold uppercase tracking-wide text-white/40">
                    {m.l}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* MISSION STRIP */}
      <section className="bg-gradient-to-r from-gold3 via-gold2 to-[#e8c020]">
        <div className="mx-auto flex max-w-[1100px] flex-wrap items-center justify-between gap-8 px-6 py-10 md:px-10">
          <div>
            <p className="max-w-[600px] text-[clamp(18px,2.2vw,26px)] font-extrabold leading-snug tracking-tight text-navy">
              Our mission is simple: help forward-thinking law firms grow,
              improve the client experience, and position themselves for the
              future.
            </p>
            <p className="mt-2 text-[14px] font-medium text-navy/60">
              Strategy · Automation · AI Visibility · Long-Term Partnerships
            </p>
          </div>
          <ShieldCheck size={52} className="text-navy/40" strokeWidth={1.5} />
        </div>
      </section>

      {/* STORY / TIMELINE + EVOLUTION */}
      <section className="bg-gradient-to-b from-white to-[#f8f7ff]">
        <div className="mx-auto grid max-w-[1100px] items-start gap-16 px-6 py-20 md:grid-cols-2 md:px-10">
          <div>
            <Tag variant="purple" className="mb-4">
              Our Journey
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
              Serving Law Firms <span className="text-pu">Since 2013</span>
            </h2>
            <p className="mt-3 text-[16px] leading-relaxed text-slate-500">
              Long before AI transformed legal marketing, we were in the
              trenches helping law firms build sustainable online visibility.
            </p>
            <div className="relative mt-10 pl-9">
              <span className="absolute bottom-2 left-[10px] top-2 w-0.5 bg-gradient-to-b from-pu to-pu/10" />
              {TIMELINE.map((t) => (
                <div key={t.year} className="relative mb-12 last:mb-0">
                  <span
                    className={`absolute -left-[31px] top-1 h-5 w-5 rounded-full border-[3px] border-white ${
                      t.gold
                        ? "bg-gradient-to-br from-gold3 to-gold2 shadow-[0_0_0_3px_rgba(212,175,55,.25)]"
                        : "bg-gradient-to-br from-pu to-pu2 shadow-[0_0_0_3px_rgba(106,92,255,.2)]"
                    }`}
                  />
                  <div
                    className={`mb-1.5 text-[11px] font-extrabold uppercase tracking-wider ${
                      t.gold ? "text-gold3" : "text-pu"
                    }`}
                  >
                    {t.year}
                  </div>
                  <h3 className="mb-2 text-[18px] font-extrabold tracking-tight text-navy">
                    {t.title}
                  </h3>
                  <p className="text-[14px] leading-relaxed text-slate-500">
                    {t.desc}
                  </p>
                </div>
              ))}
            </div>
          </div>

          <div className="md:sticky md:top-24">
            <Tag variant="gold" className="mb-4">
              Then vs Now
            </Tag>
            <h3 className="mb-7 text-[22px] font-extrabold leading-snug tracking-tight text-navy">
              From Websites to AI-Powered Ecosystems
            </h3>
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="rounded-2xl border border-pu/10 bg-white p-6">
                <div className="mb-4 border-b border-pu/10 pb-3 text-[12px] font-extrabold uppercase tracking-wide text-pu">
                  Traditional Foundation
                </div>
                <ul className="space-y-2.5">
                  {EVO_OLD.map((e) => (
                    <li key={e} className="flex items-center gap-2.5">
                      <span className="h-2 w-2 flex-shrink-0 rounded-full bg-pu" />
                      <span className="text-[13px] font-semibold text-slate-600">
                        {e}
                      </span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="rounded-2xl border border-pu/25 bg-gradient-to-br from-navy to-[#162050] p-6">
                <div className="mb-4 border-b border-gold/15 pb-3 text-[12px] font-extrabold uppercase tracking-wide text-gold2">
                  AI-Powered Systems
                </div>
                <ul className="space-y-2.5">
                  {EVO_NEW.map((e) => (
                    <li key={e} className="flex items-center gap-2.5">
                      <span className="h-2 w-2 flex-shrink-0 rounded-full bg-gold2" />
                      <span className="text-[13px] font-semibold text-white/80">
                        {e}
                      </span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* DIFFERENCE */}
      <section className="bg-navy">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto max-w-[640px] text-center">
            <Tag variant="gold" className="mb-4">
              Why We&apos;re Different
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-white">
              A Different Kind of{" "}
              <span className="text-grad-gold">Growth Partner</span>
            </h2>
            <p className="mt-3 text-[16px] leading-relaxed text-white/65">
              Unlike traditional agencies that work with every industry
              imaginable, LexScale.ai focuses exclusively on law firms.
            </p>
          </div>
          <div className="mt-12 grid gap-5 md:grid-cols-3">
            {DIFFERENCE.map((d) => {
              const Icon = d.icon;
              return (
                <div
                  key={d.title}
                  className="rounded-2xl border border-white/8 bg-white/[0.04] p-7 transition-all duration-300 hover:-translate-y-1 hover:border-pu/25 hover:bg-pu/8"
                >
                  <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl border border-gold/20 bg-gold/10 text-gold2">
                    <Icon size={22} />
                  </span>
                  <h3 className="mb-2.5 text-[16px] font-bold text-white">
                    {d.title}
                  </h3>
                  <p className="text-[13.5px] leading-relaxed text-white/50">
                    {d.desc}
                  </p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* SYSTEMS */}
      <section className="bg-gradient-to-b from-[#f8f7ff] to-white">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto max-w-[640px] text-center">
            <Tag variant="purple" className="mb-4">
              What We Build
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
              AI Systems We <span className="text-pu">Deploy</span>
            </h2>
            <p className="mt-3 text-[16px] leading-relaxed text-slate-500">
              Seven categories of AI technology working together to grow your
              practice.
            </p>
          </div>
          <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {SYSTEMS.map((s) => {
              const Icon = s.icon;
              return (
                <div
                  key={s.title}
                  className="group relative overflow-hidden rounded-2xl border border-pu/10 bg-white p-7 transition-all duration-300 hover:-translate-y-1.5 hover:border-pu/25 hover:shadow-[0_18px_48px_rgba(106,92,255,.1)]"
                >
                  <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-pu/8 text-pu transition-colors group-hover:bg-gradient-to-br group-hover:from-pu group-hover:to-pu2 group-hover:text-white">
                    <Icon size={22} />
                  </span>
                  <h3 className="mb-3 text-[15px] font-extrabold text-navy">
                    {s.title}
                  </h3>
                  <ul className="space-y-1.5">
                    {s.items.map((item) => (
                      <li
                        key={item}
                        className="flex items-start gap-2 text-[12.5px] leading-snug text-slate-500"
                      >
                        <span className="mt-1.5 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-pu" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* TECH STACK */}
      <section className="bg-[#06090f]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto mb-12 max-w-[640px] text-center">
            <Tag variant="gold" className="mb-4">
              Technology Stack
            </Tag>
            <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-white">
              Powered by Leading AI &{" "}
              <span className="text-grad-gold">Technology Platforms</span>
            </h2>
            <p className="mt-3 text-[16px] leading-relaxed text-white/65">
              We integrate the world&apos;s most advanced AI and development
              platforms to build systems that are reliable, scalable, and
              future-proof.
            </p>
          </div>
          <div className="space-y-10">
            {TECH.map((cat) => (
              <div key={cat.label}>
                <div className="mb-4 flex items-center gap-3 text-[11px] font-bold uppercase tracking-[1.2px] text-gold2/50">
                  {cat.label}
                  <span className="h-px flex-1 bg-white/6" />
                </div>
                <div className="flex flex-wrap gap-2.5">
                  {cat.chips.map((chip) => (
                    <span
                      key={chip}
                      className="inline-flex items-center gap-2 rounded-full border border-white/8 bg-white/[0.04] px-4 py-2.5 text-[13px] font-semibold text-white/70 transition-colors hover:border-pu/30 hover:bg-pu/12 hover:text-white"
                    >
                      <span className="h-1.5 w-1.5 rounded-full bg-pu3" />
                      {chip}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* PHILOSOPHY */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto grid max-w-[1100px] items-center gap-12 px-6 py-20 md:grid-cols-2 md:px-10">
          <div>
            <Tag variant="gold" className="mb-5">
              Our Philosophy
            </Tag>
            <h2 className="mb-8 text-[clamp(26px,3.2vw,42px)] font-extrabold leading-tight tracking-tight text-white">
              Technology Should Never{" "}
              <span className="text-grad-gold">Replace Relationships.</span>
            </h2>
            <blockquote className="mb-9 border-l-[3px] border-gold2 pl-7 text-[clamp(18px,2.2vw,26px)] font-bold italic leading-snug tracking-tight text-white">
              &ldquo;AI should enhance responsiveness, improve efficiency, and
              create better experiences for prospective clients — not replace
              the human connection that makes great law firms great.&rdquo;
            </blockquote>
            <div className="space-y-5">
              {PHILOSOPHY.map((p) => {
                const Icon = p.icon;
                return (
                  <div key={p.title} className="flex items-start gap-3.5">
                    <span className="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-xl border border-gold/20 bg-gold/10 text-gold2">
                      <Icon size={16} />
                    </span>
                    <div>
                      <div className="mb-1 text-[14px] font-bold text-white">
                        {p.title}
                      </div>
                      <p className="text-[13px] leading-relaxed text-white/50">
                        {p.desc}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Search shift panel */}
          <div className="relative overflow-hidden rounded-3xl border border-white/8 bg-white/[0.03] p-9">
            <span className="absolute inset-x-0 top-0 h-0.5 bg-gradient-to-r from-transparent via-gold2 to-transparent" />
            <div className="mb-5 text-[13px] font-bold uppercase tracking-wide text-white/40">
              Where Clients Find Lawyers — 2025
            </div>
            <div className="space-y-3">
              {SEARCH_SHIFT.map((row) => (
                <div
                  key={row.platform}
                  className={`flex items-center gap-4 rounded-2xl border p-4 ${
                    row.featured
                      ? "border-gold/20 bg-gold/[0.07]"
                      : "border-white/6 bg-white/[0.04]"
                  }`}
                >
                  <div className="w-[110px] flex-shrink-0">
                    <div
                      className={`text-[13px] font-bold ${
                        row.featured ? "text-gold2" : "text-white"
                      }`}
                    >
                      {row.platform}
                    </div>
                    <div className="mt-0.5 text-[11px] text-white/35">
                      {row.sub}
                    </div>
                  </div>
                  <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-white/8">
                    <div
                      className={`h-full rounded-full ${
                        row.featured
                          ? "bg-gradient-to-r from-gold3 to-gold2"
                          : "bg-gradient-to-r from-pu to-pu3"
                      }`}
                      style={{ width: `${row.pct}%` }}
                    />
                  </div>
                  <div className="w-12 flex-shrink-0 text-right text-[11px] font-bold text-white/55">
                    {row.trend}
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-7 border-t border-white/7 pt-6">
              <div className="mb-3.5 text-[12px] font-bold uppercase tracking-wide text-white/35">
                AI Platforms Answering Legal Queries
              </div>
              <div className="flex flex-wrap gap-2">
                {["ChatGPT", "Perplexity", "Google AI", "Bing AI"].map((p) => (
                  <span
                    key={p}
                    className="rounded-full border border-white/8 bg-white/5 px-3.5 py-1.5 text-[12px] font-semibold text-white/60"
                  >
                    {p}
                  </span>
                ))}
                <span className="rounded-full border border-gold/20 bg-gold/8 px-3.5 py-1.5 text-[12px] font-semibold text-gold2">
                  Is Your Firm Visible?
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FINAL CTA */}
      <section className="hero-gradient relative overflow-hidden border-t border-white/5">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[760px] px-6 py-24 text-center md:px-10">
          <span className="mb-7 inline-flex items-center gap-2 rounded-full border border-gold/25 bg-gold/10 px-4 py-2 text-[11px] font-bold uppercase tracking-wide text-gold2">
            <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-gold2" />
            Now Accepting New Law Firm Clients
          </span>
          <h2 className="text-[clamp(28px,3.5vw,48px)] font-black leading-[1.1] tracking-tight text-white">
            Built for Law Firms.
            <br />
            <span className="text-grad-gold">Powered by AI.</span>
          </h2>
          <p className="mx-auto mt-4 max-w-[480px] text-[16px] leading-relaxed text-white/50">
            Ready to grow your practice with intelligent systems built for the
            way clients search, engage, and hire lawyers today?
          </p>
          <div className="mt-9 flex flex-wrap justify-center gap-3">
            <Button variant="gold" size="lg" href="/tools/ai-visibility-checker">
              Schedule a Strategy Call
            </Button>
            <Link
              href="/services"
              className="inline-flex items-center justify-center gap-2 rounded-full border-[1.5px] border-white/25 px-7 py-3.5 text-[15px] font-bold text-white transition-all hover:-translate-y-0.5 hover:border-white/60"
            >
              Explore Our AI Systems <ArrowRight size={16} />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
