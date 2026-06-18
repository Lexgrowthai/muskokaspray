import {
  Quote,
  Radar,
  ListChecks,
  TrendingUp,
  RefreshCcw,
  AlertTriangle,
  Trophy,
  Search,
} from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, SITE_URL } from "@/lib/schema";

const NAME = "AI Citation Tracking for Law Firms";
const DESCRIPTION =
  "Know exactly when and where AI engines cite your firm. LexScale monitors ChatGPT, Gemini, and Perplexity for your mentions, citation share, and competitor presence — reported every cycle.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/ai-citation-tracking",
});

const steps = [
  {
    title: "Build Your Prompt Set",
    body: "We assemble the questions your prospects actually ask AI — by practice area, location, and intent — into a tracked prompt library that represents real demand for your firm.",
  },
  {
    title: "Multi-Engine Monitoring",
    body: "We run that prompt set across ChatGPT, Gemini, Perplexity, and AI Overviews on a fixed schedule, capturing whether your firm is mentioned, cited, linked, or absent.",
  },
  {
    title: "Citation Share Scoring",
    body: "We score your presence into a citation share metric and benchmark it against named competitors, so you know not just if you appear, but how you stack up.",
  },
  {
    title: "Accuracy & Sentiment Checks",
    body: "We verify that what the models say about your firm is correct and on-brand, flagging outdated facts, wrong details, or unfavorable framing that needs correcting.",
  },
  {
    title: "Report & Recommend",
    body: "Each cycle you get a clear report — trends, wins, gaps, and competitor moves — with prioritized recommendations to grow your citation share.",
  },
];

const benefits = [
  {
    icon: Radar,
    title: "Visibility You Can't Otherwise See",
    body: "AI answers leave no analytics trail. Citation tracking is the only way to know whether the models are recommending your firm or sending clients to a competitor.",
  },
  {
    icon: Trophy,
    title: "Benchmark Against Rivals",
    body: "Know exactly which competing firms own the AI answers in your market — and by how much — so your strategy targets the gaps that matter.",
  },
  {
    icon: AlertTriangle,
    title: "Catch Misinformation Fast",
    body: "Models sometimes state wrong facts about firms. Continuous monitoring flags inaccuracies early so you can correct the underlying sources before they spread.",
  },
];

const faqs = [
  {
    question: "What is AI citation tracking?",
    answer:
      "It's the ongoing measurement of when, where, and how AI engines mention or cite your firm. We run a defined set of prospect questions across the major models on a schedule and record your appearances, links, and citation share over time.",
  },
  {
    question: "Which AI engines do you track?",
    answer:
      "ChatGPT (including Search), Google Gemini and AI Overviews, and Perplexity by default. We can add other emerging answer engines as they gain traction in your market.",
  },
  {
    question: "How is citation share calculated?",
    answer:
      "For each tracked prompt we record whether your firm is mentioned, cited, or linked, then aggregate across the prompt set into a share metric. We benchmark it against the competitors you care about so you see relative position, not just raw counts.",
  },
  {
    question: "What do I do with the tracking data?",
    answer:
      "The reports show exactly where you're winning, where you're missing, and which competitors are ahead. That directs optimization work — which pages to strengthen, which sources to reinforce, and which facts to correct — so effort goes where it moves the needle.",
  },
  {
    question: "Can citation tracking run alongside an optimization program?",
    answer:
      "Yes, and it's most powerful that way. Tracking is the measurement layer for AI search optimization — it proves what's working and tells us where to focus next. Many firms start with tracking to establish a baseline before scaling optimization.",
  },
];

export default function Page() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(
          NAME,
          DESCRIPTION,
          SITE_URL + "/services/ai-citation-tracking"
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-white md:px-10">
          <Tag variant="gold">
            <Quote size={13} /> AI Citation Tracking
          </Tag>
          <h1 className="mt-5 max-w-[820px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight">
            Know Exactly When AI Recommends Your Firm
          </h1>
          <p className="mt-5 max-w-[640px] text-[17px] leading-relaxed text-white/75">
            AI answers don&apos;t show up in your analytics — but they decide
            who prospects call. We monitor ChatGPT, Gemini, and Perplexity for
            your firm&apos;s mentions, citation share, and competitor presence,
            reported every cycle.
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
              href="/services/ai-search-optimization"
              variant="outline"
              size="lg"
              className="border-white/25 text-white hover:border-white hover:text-white"
            >
              Explore AI Search Optimization
            </Button>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="gold">What We Do</Tag>
          <h2 className="mt-4 max-w-[760px] text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            We make your AI visibility measurable
          </h2>
          <p className="mt-5 max-w-[720px] text-[16px] leading-relaxed text-slate-600">
            When a prospect asks ChatGPT for a lawyer, no dashboard records what
            happened — yet that answer may decide who gets the call. AI citation
            tracking closes that blind spot. We build a prompt set that mirrors
            real demand in your market, run it across every major AI engine on a
            schedule, and turn the results into a clear picture: your citation
            share, your competitors&apos; position, the accuracy of what
            models say, and where to focus next. It&apos;s the measurement
            foundation every serious AI strategy needs.
          </p>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <Tag variant="purple">How It Works</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            Our five-step tracking process
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
          <Tag variant="gold">Why It Matters</Tag>
          <h2 className="mt-4 text-[clamp(26px,3.2vw,42px)] font-extrabold tracking-tight text-navy">
            What gets measured gets won
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
              <Search size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Multi-engine monitoring
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <ListChecks size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Citation share scoring
              </span>
            </div>
            <div className="flex items-center gap-3 rounded-2xl border border-pu/10 bg-white p-5">
              <TrendingUp size={20} className="text-pu" />
              <span className="text-[14px] font-semibold text-navy">
                Competitor benchmarking
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-navy/[0.02]">
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-pu to-pu2 p-10 text-white md:p-14">
            <div className="flex items-center gap-2 text-[12px] font-bold uppercase tracking-[1px] text-white/70">
              <RefreshCcw size={15} /> Ongoing Monitoring
            </div>
            <h2 className="mt-3 max-w-[640px] text-[clamp(24px,2.8vw,36px)] font-extrabold leading-tight">
              AI citation tracking for law firms
            </h2>
            <p className="mt-4 max-w-[600px] text-[16px] leading-relaxed text-white/80">
              Tracking starts at $800/month and includes a custom prompt set,
              multi-engine monitoring, citation share scoring, competitor
              benchmarking, and a clear report each cycle. A perfect baseline
              before scaling optimization.
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
                href="/services/ai-dashboards"
                variant="outline"
                size="lg"
                className="border-white/30 text-white hover:border-white hover:text-white"
              >
                See AI Dashboards
              </Button>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <FAQ faqs={faqs} title="AI Citation Tracking FAQs" />
        </div>
      </section>
    </>
  );
}
