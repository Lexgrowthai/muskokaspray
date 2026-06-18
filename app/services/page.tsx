import Link from "next/link";
import {
  ArrowRight,
  Globe,
  Search,
  Sparkles,
  MessageSquare,
  Stars,
  Compass,
  Network,
  Code2,
  Bot,
  PhoneCall,
  LayoutDashboard,
  Quote,
  type LucideIcon,
} from "lucide-react";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import { SERVICES_ITEMS } from "@/lib/navigation";

export const metadata = generatePageMetadata({
  title: "Our AI Systems",
  slug: "services",
  description:
    "Explore LexScale.ai's full suite of AI growth systems for law firms — AI websites, AI SEO, AI search optimization, chatbots, receptionists, dashboards, and citation tracking built to win clients across Google, ChatGPT, Gemini, and Perplexity.",
});

const ICONS: Record<string, LucideIcon> = {
  Globe,
  Search,
  Sparkles,
  MessageSquare,
  Stars,
  Compass,
  Network,
  Code2,
  Bot,
  PhoneCall,
  LayoutDashboard,
  Quote,
};

export default function ServicesPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Our AI Systems",
          "The full suite of AI growth systems LexScale.ai builds for law firms — across AI search, websites, automation, and analytics.",
          `${SITE_URL}/services`
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Services", url: `${SITE_URL}/services` },
        ])}
      />

      {/* HERO */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <span className="mb-5 inline-flex items-center gap-2 rounded-full border border-pu/25 bg-pu/12 px-4 py-1.5 text-[11px] font-bold uppercase tracking-wider text-pu3">
            <Sparkles size={13} /> The Full Suite
          </span>
          <h1 className="mx-auto max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Our AI Systems
          </h1>
          <p className="mx-auto mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/55">
            Twelve integrated AI growth systems built exclusively for law firms.
            Every one is designed to win you clients across Google, ChatGPT,
            Gemini, Perplexity, and the moments that matter — the call, the
            chat, the search.
          </p>
          <div className="mt-9 flex flex-wrap justify-center gap-3">
            <Button
              href="/tools/ai-visibility-checker"
              variant="primary"
              size="lg"
            >
              Get a Free Strategy Call
            </Button>
            <Button href="/case-studies" variant="outline" size="lg">
              See the Results
            </Button>
          </div>
        </div>
      </section>

      {/* SERVICES GRID */}
      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {SERVICES_ITEMS.map((item) => {
              const Icon = ICONS[item.iconName ?? "Sparkles"] ?? Sparkles;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 hover:border-pu/30 hover:shadow-[0_16px_44px_rgba(106,92,255,.14)]"
                >
                  <span className="mb-5 flex h-12 w-12 items-center justify-center rounded-xl bg-pu/10 text-pu transition-colors group-hover:bg-pu group-hover:text-white">
                    <Icon size={22} />
                  </span>
                  <h2 className="text-[17px] font-extrabold tracking-tight text-navy">
                    {item.label}
                  </h2>
                  <p className="mt-2 flex-1 text-[14px] leading-relaxed text-slate-500">
                    {item.description}
                  </p>
                  <span className="mt-5 inline-flex items-center gap-1.5 text-[13px] font-bold text-pu">
                    Learn More
                    <ArrowRight
                      size={15}
                      className="transition-transform group-hover:translate-x-1"
                    />
                  </span>
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* CLOSING CTA */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 text-center md:px-10">
          <h2 className="mx-auto max-w-[640px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-white">
            Not Sure Where to Start?
          </h2>
          <p className="mx-auto mt-4 max-w-[520px] text-[16px] leading-relaxed text-white/50">
            Most firms begin with a free visibility check. We&apos;ll show you
            exactly where you stand across Google and the AI engines — and which
            systems will move the needle fastest.
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
      </section>
    </>
  );
}
