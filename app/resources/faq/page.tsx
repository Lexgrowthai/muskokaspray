import { generatePageMetadata } from "@/lib/metadata";
import { webPageSchema, SITE_URL } from "@/lib/schema";
import SchemaScript from "@/components/schema/SchemaScript";
import FAQ from "@/components/sections/FAQ";
import Button from "@/components/ui/Button";

export const metadata = generatePageMetadata({
  title: "Frequently Asked Questions",
  description:
    "Answers to the most common questions law firms ask about AI search, LexScale's services, getting started, and pricing.",
  slug: "resources/faq",
});

const aiSearch = [
  {
    question: "What is AI search and why does it matter for law firms?",
    answer:
      "AI search refers to how tools like ChatGPT, Google AI Overviews, Gemini, and Perplexity answer questions directly instead of just returning a list of blue links. When a potential client asks one of these tools to recommend a personal injury or family lawyer, the answer is generated from sources the AI trusts. If your firm isn't part of that trusted set, you're invisible at the exact moment someone is choosing who to call. It matters because client behavior is shifting fast — more research now starts and often ends inside an AI assistant.",
  },
  {
    question: "How is being cited by ChatGPT different from ranking on Google?",
    answer:
      "Traditional Google ranking is about earning a position on a results page; the user still clicks through and decides. AI citation is about being named inside the answer itself — the AI does the recommending. That means the bar is higher: the model has to recognize your firm as a credible entity, understand what you do, and find consistent, authoritative information about you across the web. You can rank #1 on Google and still never be mentioned by ChatGPT if your entity and content signals aren't aligned for AI consumption.",
  },
  {
    question: "Will AI search replace Google for finding lawyers?",
    answer:
      "Not entirely, and not overnight — but it's already capturing a meaningful share of high-intent legal research. Google itself now leads with AI Overviews above traditional results for many legal queries. The smart approach isn't to abandon Google; it's to optimize for both classic search and AI answer engines at the same time, since the underlying signals (authority, structured data, entity clarity) heavily overlap.",
  },
  {
    question: "What signals do AI models use to decide which firms to recommend?",
    answer:
      "Large language models lean on a blend of signals: how clearly your firm is defined as an entity (in knowledge graphs, on authoritative directories, and via schema markup), the depth and consistency of content about your practice areas, third-party validation like reviews and citations, and demonstrable experience and expertise (E-E-A-T). Consistency across every place you appear online is critical — conflicting names, addresses, or descriptions confuse the model and weaken your citation odds.",
  },
  {
    question: "Can a small or solo law firm compete in AI search?",
    answer:
      "Yes — and often more easily than in saturated Google rankings. AI answers are frequently localized and topic-specific, so a solo immigration attorney with deep, well-structured content and strong entity signals can be cited ahead of a large general-practice firm that hasn't optimized for AI. Focus and topical authority beat sheer size. Small firms that move early have a real first-mover advantage before competitors catch on.",
  },
];

const services = [
  {
    question: "What does LexScale.ai actually do?",
    answer:
      "We build AI growth systems for law firms. That spans AI search optimization (getting you cited by ChatGPT, Gemini, Perplexity, and Google AI), AI SEO, conversion-focused AI websites, entity SEO and structured data, plus AI chatbots and AI receptionists that capture and qualify leads around the clock. The goal is a single connected system that wins visibility and turns it into booked consultations.",
  },
  {
    question: "Which AI platforms do you optimize for?",
    answer:
      "We optimize for the platforms your clients actually use: ChatGPT, Google Gemini and AI Overviews, Perplexity, and Microsoft Copilot. Each engine weighs signals slightly differently, so we tailor entity, content, and structured-data work to each while building the shared authority foundation that helps across all of them.",
  },
  {
    question: "Do you only work with law firms?",
    answer:
      "Yes. Since 2013 we've focused exclusively on law firms across the United States and Canada. That specialization means we understand legal client journeys, bar advertising rules, practice-area nuances, and the specific ways AI engines evaluate legal authority — knowledge a generalist agency simply doesn't have.",
  },
  {
    question: "How is AI search optimization different from the SEO I already pay for?",
    answer:
      "Traditional SEO optimizes web pages to rank in a list of links. AI search optimization (sometimes called AISO or GEO) optimizes how AI models understand and cite your firm inside generated answers. It adds layers most SEO providers don't touch: entity definition, knowledge-graph presence, machine-readable structured data, and content engineered to be quoted by language models. We do both, because they reinforce each other.",
  },
  {
    question: "Can you work alongside our existing marketing team or agency?",
    answer:
      "Absolutely. We frequently complement an in-house marketer or an existing SEO/PPC agency by owning the AI-search layer they aren't equipped for. We share our roadmap, coordinate on content, and make sure our entity and structured-data work strengthens — rather than conflicts with — what's already in place.",
  },
];

const gettingStarted = [
  {
    question: "How do we get started with LexScale?",
    answer:
      "It starts with a free AI visibility check and strategy call. We analyze how your firm currently appears across major AI engines, identify the gaps holding back your citations, and map out a prioritized plan. There's no obligation — you walk away with a clear picture of where you stand even if you don't engage us.",
  },
  {
    question: "How long before we see results in AI search?",
    answer:
      "Most firms see early movement — improved entity recognition and first citations — within 60 to 90 days, with momentum compounding from there. Speed depends on your starting authority, how competitive your practice area and market are, and how much foundational work (schema, content, entity cleanup) is needed. AI search rewards consistency, so the firms that commit see the largest gains over 6 to 12 months.",
  },
  {
    question: "What do you need from our firm to begin?",
    answer:
      "Very little of your time. We need access to your website and analytics, your business listings and profiles, and a short kickoff conversation about your practice areas, target clients, and goals. From there our team handles the heavy lifting — audits, technical implementation, content, and reporting — and checks in on a regular cadence.",
  },
  {
    question: "Do we need to rebuild our website to work with you?",
    answer:
      "Usually not. We can implement entity SEO, structured data, and AI-search content on most existing platforms. If your site is technically limiting your visibility or conversions, we'll tell you honestly and can build a fast, conversion-focused AI website — but that's a recommendation, never a requirement to start.",
  },
  {
    question: "How do you measure and report on progress?",
    answer:
      "We track AI citations across ChatGPT, Gemini, Perplexity, and Google AI Overviews, alongside traditional rankings, organic traffic, leads, and booked calls. You get clear, plain-English reporting tied to outcomes that matter — not vanity metrics — so you always know what the investment is producing.",
  },
];

const pricing = [
  {
    question: "How much does AI search optimization cost?",
    answer:
      "Pricing depends on your firm's size, the number of practice areas and locations, and how competitive your market is. Engagements are scoped to your goals rather than sold as one-size-fits-all packages. The fastest way to get an accurate number is the free strategy call, where we assess your situation and quote a plan built around your priorities.",
  },
  {
    question: "Do you offer month-to-month or require long-term contracts?",
    answer:
      "AI search is a compounding, ongoing discipline, so most clients work with us on a continuous basis to keep building and defending their visibility. That said, we structure engagements to be fair and outcome-driven, and we'll walk you through the terms transparently on your strategy call so there are no surprises.",
  },
  {
    question: "Is there a setup or onboarding fee?",
    answer:
      "Some engagements include an initial foundation phase — auditing your entity, cleaning up listings, implementing schema, and building core content — which may be scoped separately from ongoing work. We'll lay out exactly what's included and what it costs before you commit. Nothing is hidden.",
  },
  {
    question: "What kind of ROI can a law firm expect?",
    answer:
      "Our clients have collectively generated 4,800+ leads, 3,200+ calls, an average 432% traffic increase, and $12M+ in added revenue. Individual results vary by practice area and market, but because AI citations reach clients at the highest-intent moment — when they're choosing who to call — the return on visibility is typically strong and durable.",
  },
  {
    question: "What if AI search doesn't drive results for our firm?",
    answer:
      "We set realistic expectations up front and tie our work to measurable outcomes, so you're never guessing. If something isn't performing, we diagnose why and adjust the strategy — that's the advantage of an ongoing, data-driven relationship rather than a fire-and-forget project. Our incentive is your sustained growth.",
  },
];

export default function FAQPage() {
  return (
    <>
      <SchemaScript
        schema={webPageSchema(
          "Frequently Asked Questions | LexScale.ai",
          "Answers about AI search, our services, getting started, and pricing for law firms.",
          `${SITE_URL}/resources/faq`
        )}
      />

      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-24 text-center md:px-10">
          <p className="mb-4 text-sm font-bold uppercase tracking-[0.2em] text-pu3">
            Resources
          </p>
          <h1 className="mx-auto max-w-[760px] text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
            Frequently asked questions
          </h1>
          <p className="mx-auto mt-6 max-w-[600px] text-[17px] leading-relaxed text-white/70">
            Everything law firms want to know about AI search and how we help
            you win it — answered clearly and honestly.
          </p>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="flex flex-col gap-16">
            <FAQ faqs={aiSearch} title="AI Search" />
            <FAQ faqs={services} title="Our Services" />
            <FAQ faqs={gettingStarted} title="Getting Started" />
            <FAQ faqs={pricing} title="Pricing" />
          </div>

          <div className="mx-auto mt-16 max-w-[760px] rounded-2xl bg-navy p-10 text-center shadow-[0_6px_28px_rgba(11,21,54,.16)]">
            <h2 className="text-[clamp(22px,2.4vw,30px)] font-extrabold tracking-tight text-white">
              Still have questions?
            </h2>
            <p className="mx-auto mt-4 max-w-[520px] text-[16px] leading-relaxed text-white/70">
              Book a free strategy call and we'll answer them in the context of
              your firm — plus show you exactly where you stand in AI search.
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
