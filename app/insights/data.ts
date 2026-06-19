export interface ArticleEntry {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
}

export interface CategoryData {
  name: string;
  description: string;
  articles: ArticleEntry[];
}

export const CATEGORIES: Record<string, CategoryData> = {
  chatgpt: {
    name: "ChatGPT",
    description:
      "Millions of people now ask ChatGPT for legal help before they ever contact a lawyer. Learn how to position your firm to be the answer.",
    articles: [
      {
        slug: "chatgpt-for-law-firms",
        title: "ChatGPT for Law Firms: Why Being Found on ChatGPT Matters",
        excerpt:
          "Search is changing. Consumers ask complete questions inside ChatGPT instead of typing keywords into Google. Here is what that means for your firm.",
        date: "2026-01-15",
      },
      {
        slug: "how-law-firms-can-rank-in-chatgpt",
        title: "How Law Firms Can Rank in ChatGPT",
        excerpt:
          "Learn the specific strategies law firms use to appear in ChatGPT recommendations — from entity building to content authority and structured data.",
        date: "2026-06-18",
      },
      {
        slug: "chatgpt-seo-for-lawyers",
        title: "ChatGPT SEO for Lawyers: A Complete Guide",
        excerpt:
          "ChatGPT SEO is different from Google SEO. This guide explains exactly what lawyers need to do to build visibility inside AI-generated legal answers.",
        date: "2026-06-18",
      },
      {
        slug: "why-chatgpt-matters-for-law-firms",
        title: "Why ChatGPT Matters for Law Firms",
        excerpt:
          "ChatGPT is reshaping how potential clients find legal help. Learn why law firms that ignore AI search are losing leads to competitors who show up in the answers.",
        date: "2026-06-18",
      },
      {
        slug: "how-chatgpt-finds-and-recommends-law-firms",
        title: "How ChatGPT Finds and Recommends Law Firms",
        excerpt:
          "Inside the mechanics of how ChatGPT identifies, evaluates, and recommends law firms — and what this means for how your firm builds its AI presence.",
        date: "2026-06-18",
      },
      {
        slug: "chatgpt-citations-explained",
        title: "ChatGPT Citations Explained for Law Firms",
        excerpt:
          "What does it mean when ChatGPT cites a law firm? Learn how AI citations work, why they matter, and how to earn them consistently across AI platforms.",
        date: "2026-06-18",
      },
      {
        slug: "chatgpt-vs-google-search-for-lawyers",
        title: "ChatGPT vs Google Search for Lawyers: Key Differences",
        excerpt:
          "How does ChatGPT compare to Google when it comes to how potential legal clients find lawyers? This guide breaks down the key differences.",
        date: "2026-06-18",
      },
      {
        slug: "how-ai-search-is-changing-legal-marketing",
        title: "How AI Search Is Changing Legal Marketing",
        excerpt:
          "AI search is fundamentally changing how law firms attract clients. The marketing strategies that win in an AI-first world look very different from yesterday's playbook.",
        date: "2026-06-18",
      },
      {
        slug: "best-practices-optimizing-law-firm-websites-for-chatgpt",
        title: "Best Practices for Optimizing Law Firm Websites for ChatGPT",
        excerpt:
          "A step-by-step guide to optimizing your law firm website so ChatGPT recognizes your firm as authoritative — covering schema, content structure, and technical implementation.",
        date: "2026-06-18",
      },
      {
        slug: "common-mistakes-law-firms-make-with-ai-search",
        title: "Common Mistakes Law Firms Make with AI Search",
        excerpt:
          "Most law firms are making the same preventable mistakes with AI search. Learn what they are and how to fix them before your competitors do.",
        date: "2026-06-18",
      },
      {
        slug: "future-of-chatgpt-and-legal-marketing",
        title: "The Future of ChatGPT and Legal Marketing",
        excerpt:
          "Where is AI search heading and what will it mean for law firms over the next five years? A clear-eyed look at the trends reshaping legal client acquisition.",
        date: "2026-06-18",
      },
    ],
  },
  gemini: {
    name: "Gemini",
    description:
      "Google is weaving Gemini into Search, Maps, Android, and Workspace. Understand how to appear inside Google's AI-generated answers.",
    articles: [
      {
        slug: "google-gemini-for-law-firms",
        title:
          "Google Gemini for Law Firms: Why Visibility on Google's AI Platform Matters",
        excerpt:
          "Google is integrating AI into every aspect of search. Here is how to position your firm to be part of Google's AI-generated answers.",
        date: "2026-01-20",
      },
      {
        slug: "gemini-ai-overviews-for-legal-queries",
        title: "Gemini, AI Overviews, and Legal Queries Explained",
        excerpt:
          "Where Gemini lives, how it sources answers, and what law firms must do to be cited across Google's ecosystem.",
        date: "2026-02-11",
      },
    ],
  },
  perplexity: {
    name: "Perplexity",
    description:
      "Perplexity is the answer engine for research-minded users — and it cites its sources. Learn how to become one of them.",
    articles: [
      {
        slug: "perplexity-for-law-firms",
        title: "Perplexity for Law Firms: Becoming a Cited Source",
        excerpt:
          "Perplexity shows its sources on every answer. We explain how law firms earn those citations and the traffic that follows.",
        date: "2026-01-28",
      },
      {
        slug: "source-authority-in-answer-engines",
        title: "Source Authority in Answer Engines",
        excerpt:
          "Why answer engines reward depth, accuracy, and entity consistency — and how to build the signals that get your firm referenced.",
        date: "2026-02-15",
      },
    ],
  },
  "ai-overviews": {
    name: "AI Overviews",
    description:
      "Google's AI Overviews now sit above the blue links on billions of searches. Here is how to influence what they say about your practice areas.",
    articles: [
      {
        slug: "winning-google-ai-overviews",
        title: "How Law Firms Win Google AI Overviews",
        excerpt:
          "AI Overviews summarize answers directly on the results page. The sources cited get visibility even when users do not click.",
        date: "2026-01-31",
      },
      {
        slug: "ai-overviews-and-local-legal-search",
        title: "AI Overviews and Local Legal Search",
        excerpt:
          "How location, reviews, and structured data shape whether your firm appears in the AI summary for local legal queries.",
        date: "2026-02-18",
      },
    ],
  },
  "entity-seo": {
    name: "Entity SEO",
    description:
      "AI engines reason about entities, not just keywords. Build your firm as a recognized entity so models understand who you are and what you do.",
    articles: [
      {
        slug: "entity-seo-for-law-firms",
        title: "Entity SEO for Law Firms: Beyond Keywords",
        excerpt:
          "Entities — people, places, and organizations — are how AI maps the world. Establish your firm as a known entity to earn AI trust.",
        date: "2026-01-25",
      },
      {
        slug: "building-firm-entity-signals",
        title: "Building Strong Firm Entity Signals",
        excerpt:
          "Consistent NAP data, sameAs links, and authoritative mentions tell AI engines that your firm is real, relevant, and trustworthy.",
        date: "2026-02-09",
      },
    ],
  },
  "structured-data": {
    name: "Structured Data",
    description:
      "Schema markup is the language AI engines trust. Learn which structured data types help law firms get understood and cited.",
    articles: [
      {
        slug: "schema-markup-for-law-firms",
        title: "Schema Markup for Law Firms That AI Engines Trust",
        excerpt:
          "From LegalService to FAQPage and Attorney schema, the right structured data makes your content machine-readable and citation-ready.",
        date: "2026-01-22",
      },
      {
        slug: "structured-data-mistakes-to-avoid",
        title: "Structured Data Mistakes Law Firms Should Avoid",
        excerpt:
          "Invalid markup, mismatched data, and missing entities quietly cost firms AI visibility. Here is how to audit and fix them.",
        date: "2026-02-13",
      },
    ],
  },
  "semantic-search": {
    name: "Semantic Search",
    description:
      "Modern engines rank by meaning, not exact-match keywords. Understand semantic search and write content AI actually comprehends.",
    articles: [
      {
        slug: "semantic-search-for-legal-content",
        title: "Semantic Search for Legal Content",
        excerpt:
          "Topic clusters, intent, and context now drive rankings. Learn how to structure legal content for meaning-based retrieval.",
        date: "2026-01-27",
      },
      {
        slug: "intent-and-context-in-ai-search",
        title: "Intent and Context in AI Search",
        excerpt:
          "AI weighs the full context of a query. We explain how to answer the question behind the question for legal searchers.",
        date: "2026-02-17",
      },
    ],
  },
  geo: {
    name: "GEO",
    description:
      "Generative Engine Optimization is SEO for AI answers. Learn the discipline of getting your firm surfaced by generative engines.",
    articles: [
      {
        slug: "what-is-generative-engine-optimization",
        title: "What Is Generative Engine Optimization (GEO)?",
        excerpt:
          "GEO is the practice of optimizing for AI-generated answers. We define the discipline and how it differs from classic SEO.",
        date: "2026-01-19",
      },
      {
        slug: "geo-playbook-for-law-firms",
        title: "A GEO Playbook for Law Firms",
        excerpt:
          "A step-by-step framework for earning citations, building authority, and measuring visibility across generative engines.",
        date: "2026-02-06",
      },
    ],
  },
  "knowledge-graphs": {
    name: "Knowledge Graphs",
    description:
      "Knowledge graphs are how AI maps your firm and its relationships. Learn to shape the graph entry that engines rely on.",
    articles: [
      {
        slug: "knowledge-graphs-and-law-firms",
        title: "How Knowledge Graphs Map Your Law Firm",
        excerpt:
          "AI engines lean on knowledge graphs to verify facts. We show how to influence yours through entities and authoritative sources.",
        date: "2026-02-01",
      },
      {
        slug: "earning-a-knowledge-panel",
        title: "Earning a Knowledge Panel for Your Firm",
        excerpt:
          "A knowledge panel signals authority to both users and AI. Here is how law firms build the entity foundations to earn one.",
        date: "2026-02-20",
      },
    ],
  },
  "voice-search": {
    name: "Voice Search",
    description:
      "Spoken queries are conversational, local, and immediate. Optimize your firm for the assistants people talk to every day.",
    articles: [
      {
        slug: "voice-search-for-law-firms",
        title: "Voice Search Optimization for Law Firms",
        excerpt:
          "Voice queries are longer and more conversational. Learn how to capture spoken legal questions across assistants and devices.",
        date: "2026-01-30",
      },
      {
        slug: "conversational-queries-and-intake",
        title: "Conversational Queries and Client Intake",
        excerpt:
          "How natural-language questions reshape the path to hiring a lawyer — and how to meet prospects at that moment.",
        date: "2026-02-19",
      },
    ],
  },
  "future-of-search": {
    name: "Future of Search",
    description:
      "Search is becoming an AI-first interface. Explore where legal marketing is heading and how to stay ahead of the shift.",
    articles: [
      {
        slug: "future-of-legal-marketing",
        title: "The Future of Legal Marketing Is AI Search",
        excerpt:
          "AI recommendations will increasingly name specific firms. The firms with authority today will dominate referrals tomorrow.",
        date: "2026-01-17",
      },
      {
        slug: "preparing-your-firm-for-ai-first-search",
        title: "Preparing Your Firm for AI-First Search",
        excerpt:
          "A forward-looking roadmap for the transition from blue links to AI answers — and the investments that compound.",
        date: "2026-02-08",
      },
    ],
  },
};

export const CATEGORY_SLUGS = Object.keys(CATEGORIES);

export function humanizeCategory(slug: string): string {
  return CATEGORIES[slug]?.name ?? slug.replace(/-/g, " ");
}
