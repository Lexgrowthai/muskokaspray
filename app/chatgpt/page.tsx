import Link from "next/link";
import { ArrowRight, Clock, Sparkles } from "lucide-react";
import SchemaScript from "@/components/schema/SchemaScript";
import Button from "@/components/ui/Button";
import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";
import { CHATGPT_ARTICLES } from "./data";

export const metadata = generatePageMetadata({
  title: "ChatGPT for Law Firms: The Complete Guide",
  slug: "chatgpt",
  description:
    "Everything law firms need to know about ranking in ChatGPT, understanding AI citations, and winning new clients through AI-powered search.",
});

function formatDate(date: string): string {
  return new Date(date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export default function ChatGPTHubPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "ChatGPT for Law Firms: The Complete Guide",
          "Everything law firms need to know about ranking in ChatGPT, understanding AI citations, and winning new clients through AI-powered search.",
          `${SITE_URL}/chatgpt`
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "ChatGPT for Law Firms", url: `${SITE_URL}/chatgpt` },
        ])}
      />

      {/* Hero */}
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <span className="mb-5 inline-flex items-center gap-2 rounded-full border border-pu/30 bg-pu/10 px-4 py-1.5 text-[12px] font-bold uppercase tracking-wide text-pu3">
            <Sparkles size={14} /> ChatGPT for Law Firms
          </span>
          <h1 className="mx-auto max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            ChatGPT for Law Firms:{" "}
            <span className="text-grad-gold">The Complete Guide</span>
          </h1>
          <p className="mx-auto mt-6 max-w-[640px] text-[17px] leading-relaxed text-slate-300">
            Everything your firm needs to know about ranking in ChatGPT,
            understanding AI citations, and winning new clients through
            AI-powered search — before your competitors figure it out.
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
            <Button variant="primary" size="lg" href="/services/chatgpt-optimization">
              See Our ChatGPT Optimization Service
              <ArrowRight size={18} className="ml-2" />
            </Button>
            <Button variant="outline" size="lg" href="/tools/ai-visibility-checker">
              Check Your AI Visibility Free
            </Button>
          </div>
        </div>
      </section>

      {/* Articles grid */}
      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mb-12 text-center">
            <h2 className="text-[clamp(24px,3vw,36px)] font-extrabold tracking-tight text-navy">
              {CHATGPT_ARTICLES.length} in-depth guides for law firms
            </h2>
            <p className="mx-auto mt-3 max-w-[560px] text-[16px] text-slate-600">
              Strategy, tactics, and technical playbooks written for practicing
              lawyers and legal marketers — not generic AI filler.
            </p>
          </div>

          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-2">
            {CHATGPT_ARTICLES.map((article) => (
              <Link
                key={article.slug}
                href={`/chatgpt/${article.slug}`}
                className="group flex flex-col rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] transition-all hover:-translate-y-1 hover:border-pu/40"
              >
                <div className="mb-4 flex items-center gap-3">
                  <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-pu/10 text-pu">
                    <Sparkles size={18} />
                  </div>
                  <div className="flex items-center gap-2 text-[12px] text-slate-400">
                    <Clock size={12} />
                    <span>{article.readTime}</span>
                    <span className="mx-1">·</span>
                    <span>{formatDate(article.publishedAt)}</span>
                  </div>
                </div>
                <h2 className="mb-2 text-[18px] font-extrabold leading-snug tracking-tight text-navy transition-colors group-hover:text-pu">
                  {article.title}
                </h2>
                <p className="flex-1 text-[14px] leading-relaxed text-slate-600">
                  {article.description}
                </p>
                <span className="mt-5 inline-flex items-center gap-1.5 text-[13px] font-bold text-pu">
                  Read guide
                  <ArrowRight
                    size={15}
                    className="transition-transform group-hover:translate-x-1"
                  />
                </span>
                <div className="mt-5 h-1 w-full rounded-full bg-gradient-to-r from-pu to-pu2 opacity-70" />
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* CTA section */}
      <section className="bg-slate-50/60">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="rounded-3xl border border-pu/10 bg-gradient-to-br from-navy to-navy/90 p-10 text-center text-white shadow-[0_12px_40px_rgba(11,21,54,.2)]">
            <span className="mb-4 inline-flex items-center gap-2 rounded-full border border-pu/30 bg-pu/10 px-4 py-1.5 text-[12px] font-bold uppercase tracking-wide text-pu3">
              <Sparkles size={13} /> Free Tool
            </span>
            <h2 className="mx-auto max-w-[600px] text-[clamp(24px,3vw,36px)] font-extrabold leading-tight tracking-tight">
              See Where Your Firm Stands in ChatGPT Right Now
            </h2>
            <p className="mx-auto mt-4 max-w-[480px] text-[16px] leading-relaxed text-slate-300">
              Run a free AI visibility check and find out whether ChatGPT is
              recommending your firm — or your competitors — when potential
              clients ask for a lawyer.
            </p>
            <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
              <Button variant="gold" size="lg" href="/tools/ai-visibility-checker">
                Check My AI Visibility Free
                <ArrowRight size={18} className="ml-2" />
              </Button>
              <Link
                href="/services/chatgpt-optimization"
                className="inline-flex items-center gap-2 rounded-full border border-white/20 px-6 py-3 text-[15px] font-bold text-white transition-all hover:border-white/40 hover:bg-white/5"
              >
                View ChatGPT Optimization Service
                <ArrowRight size={16} />
              </Link>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
