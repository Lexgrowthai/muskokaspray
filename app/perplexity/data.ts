import type { ContentBlock, ArticleStat } from "@/app/insights/[category]/[slug]/content";

export interface SiloArticle {
  slug: string;
  title: string;
  description: string;
  readTime: string;
  date: string;
  stats: ArticleStat[];
  blocks: ContentBlock[];
  faqs: { question: string; answer: string }[];
  related: string[];
}

export const SILO_META = {
  name: "Perplexity AI for Law Firms",
  description: "Perplexity is the answer engine for research-minded users \u2014 and it shows its sources on every answer. Learn how to become one of the cited sources.",
  slug: "perplexity",
};

export const ARTICLES: SiloArticle[] = [
  {
    slug: "perplexity-ai-for-law-firms",
    title: "Perplexity AI for Law Firms: Why It Matters and How to Get Cited",
    description: "Perplexity answers millions of legal questions every month and cites its sources visibly. Here is how law firms earn those citations and the authority that follows.",
    readTime: "11 min read",
    date: "2026-06-18",
    stats: [
      { value: "100M+", label: "monthly Perplexity users" },
      { value: "5\u20138", label: "sources shown per Perplexity answer" },
      { value: "3x", label: "higher trust when a source is visibly cited" },
    ],
    blocks: [
      { type: "h2", heading: "What Makes Perplexity Different from ChatGPT and Google", text: "What Makes Perplexity Different from ChatGPT and Google" },
      { type: "p", text: "Perplexity is often called an 'answer engine' rather than a search engine or chatbot. The distinction matters for law firms. Unlike Google, which returns a list of links for users to evaluate, Perplexity synthesizes an answer and cites the specific sources it drew from \u2014 displayed prominently alongside the answer. Unlike ChatGPT, which primarily uses training data, Perplexity retrieves live web content and attributes it directly." },
      { type: "p", text: "For a law firm, this means Perplexity citations are visible endorsements. When a prospective client asks 'what should I do after a car accident in Georgia' and Perplexity's answer prominently cites your firm's content, that exposure carries more trust weight than a blue link buried in a search results page." },
      { type: "callout", text: "Perplexity's users skew toward research-minded professionals and educated consumers \u2014 exactly the profile of someone who is seriously considering hiring a lawyer rather than casually browsing." },
      { type: "h2", heading: "How Perplexity Selects Its Sources", text: "How Perplexity Selects Its Sources" },
      { type: "ul", heading: "Source selection factors for Perplexity", items: ["Content freshness \u2014 Perplexity crawls and indexes recent content heavily.", "Direct relevance \u2014 pages that answer the exact question asked are strongly preferred.", "Domain authority \u2014 established legal websites with backlinks earn preference.", "Content clarity \u2014 well-structured, scannable content is easier for AI to parse and cite.", "Lack of fluff \u2014 concise, information-dense pages outperform padded content."] },
      { type: "h2", heading: "Strategies to Earn Perplexity Citations", text: "Strategies to Earn Perplexity Citations" },
      { type: "p", text: "The most effective approach combines fresh, specific content with strong technical signals. Publish regular updates to your practice area pages \u2014 even minor updates signal freshness. Create dedicated FAQ pages for the most common questions in your practice area. Use structured data so Perplexity's crawlers can efficiently parse your content. Earn backlinks from legal directories, local bar associations, and reputable media." },
    ],
    faqs: [
      { question: "Is Perplexity used enough to matter for law firm marketing?", answer: "Yes. With over 100 million monthly users and a fast-growing base of educated, research-oriented users, Perplexity represents a meaningful and underserved opportunity for law firms." },
      { question: "Does Perplexity use the same signals as Google?", answer: "Partially. Perplexity uses live web crawling and values many of the same signals as Google \u2014 domain authority, backlinks, content quality. But it places heavier weight on freshness and direct relevance than traditional SEO does." },
      { question: "Can a small firm with a new website earn Perplexity citations?", answer: "Yes, especially for hyper-specific local queries. A detailed, accurate page answering 'what are the grounds for divorce in Manitoba' from a local family law firm can outperform a large national site that only covers the topic superficially." },
    ],
    related: ["how-to-get-cited-on-perplexity", "perplexity-vs-chatgpt-for-legal-research"],
  },
  {
    slug: "how-to-get-cited-on-perplexity",
    title: "How to Get Your Law Firm Cited on Perplexity AI",
    description: "A practical playbook for earning visible citations on Perplexity \u2014 the answer engine that shows its sources to millions of research-minded users.",
    readTime: "10 min read",
    date: "2026-06-18",
    stats: [
      { value: "Fresh", label: "content crawled within 48 hours gets priority" },
      { value: "FAQPage", label: "schema pages cited 2.1x more often" },
      { value: "6\u201312", label: "months to build consistent citation presence" },
    ],
    blocks: [
      { type: "h2", heading: "The Content Blueprint for Perplexity Citations", text: "The Content Blueprint for Perplexity Citations" },
      { type: "p", text: "Perplexity rewards content that is specific, accurate, and immediately useful. Generic law firm content \u2014 'We are a dedicated team of experienced attorneys committed to your success' \u2014 is invisible to answer engines. What earns citations is content that directly answers the question a prospective client is asking right now." },
      { type: "ul", heading: "Content types that earn Perplexity citations", items: ["Specific legal Q&A pages: 'What happens at a first DUI hearing in Texas?'", "Process explanations: step-by-step guides through legal procedures in your jurisdiction.", "Statute and case law summaries written in plain language for consumers.", "Comparison pages: 'Mediation vs. litigation for divorce \u2014 which is right for you?'", "Updated resource pages that reflect recent law changes."] },
      { type: "h2", heading: "Technical Optimizations for Perplexity", text: "Technical Optimizations for Perplexity" },
      { type: "p", text: "Ensure your site is crawlable and fast. Perplexity prioritizes pages that load quickly, are mobile-friendly, and have no crawl blocks in robots.txt. Submit a sitemap to Google Search Console \u2014 Perplexity uses Google's index as one of its sources. Add FAQPage and Q&A schema to any page with question-and-answer content." },
      { type: "callout", text: "Update your key content pages regularly. Even minor updates signal freshness to Perplexity's crawler, improving your odds of being pulled into real-time answer generation." },
    ],
    faqs: [
      { question: "Do I need to submit my site directly to Perplexity?", answer: "There is no direct submission mechanism. Perplexity discovers content through its own crawls and through Google's index. Ensuring your site is indexed on Google is the most reliable path to Perplexity discovery." },
      { question: "How often should I update my practice area pages?", answer: "At minimum, review and update key pages quarterly. For areas where law changes frequently \u2014 tax law, immigration, employment law \u2014 monthly updates are worth the investment." },
      { question: "Does having lots of pages help?", answer: "Quality over quantity. Ten detailed, specific, well-structured pages will outperform 100 thin pages. Focus on answering the most important questions in your practice area comprehensively." },
    ],
    related: ["perplexity-ai-for-law-firms", "perplexity-vs-chatgpt-for-legal-research"],
  },
  {
    slug: "perplexity-vs-chatgpt-for-legal-research",
    title: "Perplexity vs ChatGPT for Legal Research: Key Differences for Law Firms",
    description: "How do Perplexity and ChatGPT differ when clients use them to research legal questions? What those differences mean for your firm's AI visibility strategy.",
    readTime: "9 min read",
    date: "2026-06-18",
    stats: [
      { value: "Live", label: "Perplexity uses real-time web data" },
      { value: "Training", label: "ChatGPT primarily uses training knowledge" },
      { value: "2x", label: "more source transparency on Perplexity vs ChatGPT" },
    ],
    blocks: [
      { type: "h2", heading: "The Core Difference: Live Web vs. Training Data", text: "The Core Difference: Live Web vs. Training Data" },
      { type: "p", text: "The most important distinction between Perplexity and ChatGPT for law firm visibility is how each platform sources its answers. Perplexity retrieves live web content in real time and cites those sources explicitly. ChatGPT primarily draws on knowledge learned during training \u2014 a fixed snapshot of the internet that does not update with new content you publish." },
      { type: "p", text: "This has profound implications for strategy. Improving your website content today can affect your Perplexity citations within days or weeks as its crawler picks up the changes. The same content improvements may not influence ChatGPT's answers for months \u2014 or may not affect them at all until OpenAI retrains the model. For firms that want fast, measurable results, Perplexity is often the more responsive platform." },
      { type: "h2", heading: "Citation Visibility: How Each Platform Shows Sources", text: "Citation Visibility: How Each Platform Shows Sources" },
      { type: "ul", heading: "How each platform attributes sources", items: ["Perplexity: numbered citations shown prominently alongside the answer, visible immediately.", "ChatGPT: does not consistently cite sources; may mention firm names without linking.", "Perplexity Pro: even richer citations with page previews and links.", "ChatGPT with Browsing: can cite web sources but does so less consistently than Perplexity."] },
      { type: "callout", text: "For law firms, visible citation on Perplexity acts as a trust signal. Prospective clients can see that your firm's content was judged authoritative enough to be the source of the answer they just read." },
    ],
    faqs: [
      { question: "Should law firms optimize for Perplexity or ChatGPT first?", answer: "Both matter, but they reward somewhat different investments. Perplexity responds faster to fresh, well-structured content. ChatGPT rewards long-term entity building and authority signals. A comprehensive AI visibility strategy covers both." },
      { question: "Can the same content work for both platforms?", answer: "Yes. High-quality, specific, well-structured content that answers real client questions performs well on both platforms. The technical signals differ slightly, but the content principles are the same." },
      { question: "Which platform do legal clients use more?", answer: "ChatGPT currently has more users overall. But Perplexity's user base skews heavily toward educated, research-oriented consumers \u2014 a profile that closely matches someone seriously considering hiring a lawyer." },
    ],
    related: ["perplexity-ai-for-law-firms", "how-to-get-cited-on-perplexity"],
  },
];

export const ARTICLE_SLUGS = ARTICLES.map((a) => a.slug);
