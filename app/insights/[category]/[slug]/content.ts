export interface ContentBlock {
  type: "h2" | "p" | "ul" | "callout";
  text?: string;
  items?: string[];
  heading?: string;
}

export interface ArticleStat {
  value: string;
  label: string;
}

export interface ArticleContent {
  title: string;
  description: string;
  readTime: string;
  stats: ArticleStat[];
  blocks: ContentBlock[];
  faqs: { question: string; answer: string }[];
}

const CHATGPT: ArticleContent = {
  title: "ChatGPT for Law Firms: Why Being Found on ChatGPT Matters",
  description:
    "Millions of people now ask AI platforms for legal help before they ever contact a lawyer. Here is what that shift means for your firm — and what to do about it.",
  readTime: "12 min read",
  stats: [
    { value: "1B+", label: "weekly ChatGPT messages" },
    { value: "60%", label: "of searches now zero-click" },
    { value: "1st", label: "cited firms win the referral" },
  ],
  blocks: [
    {
      type: "h2",
      heading: "The Future of Legal Marketing Is Already Changing",
      text: "The Future of Legal Marketing Is Already Changing",
    },
    {
      type: "p",
      text: "For over twenty years, Google has been the dominant way people searched for lawyers. Potential clients typed keywords, browsed listings, and called the firms that appeared at the top. Those investments in SEO, websites, and Google rankings were important — and they remain important today.",
    },
    {
      type: "p",
      text: "However, something significant is happening. Consumers are beginning to search differently. Instead of typing a few keywords into Google, people are increasingly asking complete questions inside artificial intelligence platforms such as ChatGPT.",
    },
    {
      type: "callout",
      text: "This shift may prove to be one of the biggest changes in legal marketing since the rise of Google itself. Forward-thinking law firms are paying attention — because visibility inside ChatGPT may become just as valuable as traditional search rankings.",
    },
    {
      type: "p",
      text: 'Instead of searching "family lawyer Toronto," people now ask "What do I need to do to protect my assets in a divorce in Ontario?" Instead of "criminal lawyer Boston," they ask "What should I do if I have been charged with assault?" These are fundamentally different interactions — and they require a fundamentally different approach to visibility.',
    },
    {
      type: "h2",
      heading: "What Is ChatGPT — and Why Do Legal Clients Use It?",
      text: "What Is ChatGPT — and Why Do Legal Clients Use It?",
    },
    {
      type: "p",
      text: "ChatGPT is an artificial intelligence platform developed by OpenAI that allows users to ask questions in natural language and receive conversational, detailed answers. Legal problems are emotional. People are often stressed, overwhelmed, and uncertain. Before they hire a lawyer, they want answers — they want to understand their rights, their options, their risks, and their next steps.",
    },
    {
      type: "p",
      text: "Historically, they turned to Google. Today, more consumers are turning to ChatGPT because it delivers immediate answers in plain language, without the need to click through ten different websites.",
    },
    {
      type: "ul",
      heading: "Real questions people ask ChatGPT about legal matters",
      items: [
        "What happens during a divorce?",
        "Should I hire a lawyer for probate?",
        "What should I do after being charged?",
        "Can I sue a contractor for bad work?",
        "How long does small claims court take?",
        "Do I need a lawyer to incorporate?",
      ],
    },
    {
      type: "p",
      text: "These are real questions. They represent real people, and they represent real opportunities for law firms that have positioned themselves to be the answer.",
    },
    {
      type: "h2",
      heading: "Search Is Becoming Conversational",
      text: "Search Is Becoming Conversational",
    },
    {
      type: "p",
      text: "The shift from keyword-based search to conversational AI is not just a trend — it is a structural change in how people gather information before making decisions. Yesterday, queries were short and fragmented with no context. Today, people provide full questions with full context and expect a full answer. Tomorrow, AI platforms will increasingly recommend specific firms by name, and the firms with strong authority signals will be cited first.",
    },
    {
      type: "h2",
      heading: "How to Position Your Firm to Be the Answer",
      text: "How to Position Your Firm to Be the Answer",
    },
    {
      type: "ul",
      heading: "What AI engines reward",
      items: [
        "Clear, authoritative content that directly answers real client questions.",
        "Strong entity signals so AI understands who your firm is and what you do.",
        "Structured data and schema markup that make your content machine-readable.",
        "Consistent citations and mentions across trusted legal directories and publications.",
        "Depth and accuracy — thin, generic pages do not earn AI trust.",
      ],
    },
    {
      type: "p",
      text: "Just like Page 1 of Google once dominated referrals, the firms that AI consistently cites will capture the next generation of legal clients. The work to earn those citations compounds — the earlier a firm starts, the larger its advantage.",
    },
  ],
  faqs: [
    {
      question: "Can my law firm really show up inside ChatGPT answers?",
      answer:
        "Yes. AI platforms draw on authoritative, well-structured content and strong entity signals when forming answers. Firms that publish clear, accurate content and build trust signals can be referenced when users ask relevant legal questions.",
    },
    {
      question: "Is ChatGPT visibility replacing traditional SEO?",
      answer:
        "No — it complements it. The same authority, content quality, and structured data that help you rank in Google also help AI engines understand and cite your firm. AI visibility is an additional layer, not a replacement.",
    },
    {
      question: "How long does it take to build AI search visibility?",
      answer:
        "It is a compounding effort rather than an overnight switch. Firms that invest early in authoritative content, entity SEO, and structured data build an advantage that grows as AI search adoption accelerates.",
    },
  ],
};

const GEMINI: ArticleContent = {
  title:
    "Google Gemini for Law Firms: Why Visibility on Google's AI Platform Matters",
  description:
    "Google is integrating AI into every aspect of search. Here is what that means for law firms — and how to position your firm to be part of Google's AI-generated answers.",
  readTime: "13 min read",
  stats: [
    { value: "8.5B", label: "Google searches per day" },
    { value: "100%", label: "of search is going AI-first" },
    { value: "3", label: "sources typically cited per answer" },
  ],
  blocks: [
    {
      type: "h2",
      heading: "The Future of Search Is Becoming More Intelligent",
      text: "The Future of Search Is Becoming More Intelligent",
    },
    {
      type: "p",
      text: "For decades, Google has been the dominant force in search. When consumers needed legal help, they typed a few keywords, scanned the results, and called the firms that appeared at the top. Law firms invested heavily in traditional SEO because Google was where prospective clients began their journey. Those investments remain important today.",
    },
    {
      type: "p",
      text: "But today, search is evolving again. Google is integrating artificial intelligence into virtually every aspect of its search ecosystem. At the center of that transformation is Google Gemini — and for law firms, understanding what Gemini means is no longer optional.",
    },
    {
      type: "callout",
      text: "Google processes billions of searches every day. As Gemini becomes more deeply integrated, the firms that appear within AI-generated answers will have a visibility advantage that no amount of traditional advertising can replicate.",
    },
    {
      type: "h2",
      heading: "What Is Google Gemini — and Where Does It Live?",
      text: "What Is Google Gemini — and Where Does It Live?",
    },
    {
      type: "p",
      text: "Google Gemini is Google's advanced artificial intelligence platform. Unlike standalone AI tools, Gemini has a unique strategic advantage: it is deeply embedded across Google's entire product ecosystem.",
    },
    {
      type: "ul",
      heading: "Where Gemini appears",
      items: [
        "Google Search and AI Overviews — summaries above the blue links.",
        "Google Maps — local AI answers for nearby legal help.",
        "Google Assistant — voice queries on Android and beyond.",
        "Gmail and Workspace — AI writing and research.",
        "Chrome — in-browser AI assistance.",
        "Gemini Chat — Google's conversational AI interface.",
      ],
    },
    {
      type: "p",
      text: "This deep integration is what separates Gemini from every other AI platform. ChatGPT is a standalone tool. Perplexity is a standalone tool. Gemini is woven into the search engine that billions of people use every single day.",
    },
    {
      type: "h2",
      heading: "Google Is Not Abandoning Search — It Is Transforming It",
      text: "Google Is Not Abandoning Search — It Is Transforming It",
    },
    {
      type: "p",
      text: "A common misunderstanding is that AI platforms are replacing Google. That is not what is happening. Google is transforming search from the inside — layering AI intelligence on top of the world's most trusted search engine. Traditional blue links are giving way to AI-generated answers, and AI Overviews now appear at the top of billions of search results.",
    },
    {
      type: "p",
      text: "Consumers are becoming accustomed to receiving information immediately, without clicking through multiple websites. The sources cited within an AI Overview get visibility even when users do not click — which makes being cited the new front page.",
    },
    {
      type: "h2",
      heading: "How Law Firms Earn Visibility in Gemini",
      text: "How Law Firms Earn Visibility in Gemini",
    },
    {
      type: "ul",
      heading: "Priorities for Gemini visibility",
      items: [
        "Build deep topical authority across your practice areas.",
        "Implement structured data so Google can parse and trust your content.",
        "Strengthen entity signals through consistent profiles and citations.",
        "Answer real conversational questions clients actually ask.",
        "Keep local signals — reviews, NAP, and Maps presence — accurate.",
      ],
    },
    {
      type: "p",
      text: "Gemini will increasingly become the primary interface for finding information. The firms that have built deep authority will be the firms that AI recommends — consistently, across every device and platform Google touches.",
    },
  ],
  faqs: [
    {
      question: "What is the difference between Gemini and AI Overviews?",
      answer:
        "Gemini is Google's underlying AI model. AI Overviews are one of its most visible outputs — the AI-generated summaries that now appear at the top of many search results, drawing on cited sources.",
    },
    {
      question: "Does ranking in Google still matter for Gemini visibility?",
      answer:
        "Yes. Traditional ranking signals, authority, and structured data all feed into how Gemini selects and cites sources. Strong organic SEO and AI visibility reinforce each other.",
    },
    {
      question: "How can a local law firm appear in AI Overviews?",
      answer:
        "Accurate local signals — Google Business Profile, reviews, consistent NAP data, and location-specific content — combined with authoritative answers to local legal questions improve the odds of being cited in local AI Overviews.",
    },
  ],
};

function genericContent(title: string, category: string): ArticleContent {
  return {
    title,
    description:
      "A practical guide for law firms on winning visibility in the era of AI-driven search.",
    readTime: "9 min read",
    stats: [
      { value: "60%", label: "of searches end without a click" },
      { value: "3x", label: "faster growth for AI-visible firms" },
      { value: "1st", label: "cited sources win the referral" },
    ],
    blocks: [
      {
        type: "h2",
        heading: "Why AI Search Visibility Matters for Law Firms",
        text: "Why AI Search Visibility Matters for Law Firms",
      },
      {
        type: "p",
        text: `Search behavior is shifting from typing keywords to asking complete questions inside AI engines. For law firms, that means ${category.toLowerCase()} is no longer a technical footnote — it is a core part of how prospective clients discover and choose counsel.`,
      },
      {
        type: "p",
        text: "AI engines summarize answers and cite a small handful of trusted sources. The firms that earn those citations capture attention before a prospect ever visits a website, while everyone else becomes invisible in the answer.",
      },
      {
        type: "callout",
        text: "Visibility inside AI answers is becoming as valuable as a first-page Google ranking once was. The firms that invest early build an advantage that compounds over time.",
      },
      {
        type: "h2",
        heading: "What AI Engines Reward",
        text: "What AI Engines Reward",
      },
      {
        type: "ul",
        heading: "Signals that earn citations",
        items: [
          "Clear, authoritative content that answers real client questions directly.",
          "Strong entity signals so engines understand who your firm is.",
          "Structured data and schema markup that make content machine-readable.",
          "Consistent citations across trusted legal directories and publications.",
          "Depth and accuracy — thin, generic pages do not earn AI trust.",
        ],
      },
      {
        type: "h2",
        heading: "How to Get Started",
        text: "How to Get Started",
      },
      {
        type: "p",
        text: "Begin with an audit of how AI engines currently describe and cite your firm. From there, prioritize authoritative content, entity SEO, and structured data across your highest-value practice areas. The work compounds — the earlier you start, the larger your advantage as AI search adoption accelerates.",
      },
    ],
    faqs: [
      {
        question: "Is AI search visibility replacing traditional SEO?",
        answer:
          "No — it complements it. The same authority, content quality, and structured data that help you rank in Google also help AI engines understand and cite your firm.",
      },
      {
        question: "How long does it take to build AI visibility?",
        answer:
          "It is a compounding effort rather than an overnight switch. Firms that invest early in authoritative content and structured data build an advantage that grows over time.",
      },
      {
        question: "Where should a law firm start?",
        answer:
          "Start with an audit of how AI engines describe your firm today, then prioritize content depth, entity signals, and schema markup across your most valuable practice areas.",
      },
    ],
  };
}

// Pull the 10 new ChatGPT articles from the dedicated data file
import { CHATGPT_ARTICLES } from "../../../chatgpt/data";

const CHATGPT_CONTENT_MAP: Record<string, ArticleContent> = Object.fromEntries(
  CHATGPT_ARTICLES.map((a) => [
    a.slug,
    {
      title: a.title,
      description: a.description,
      readTime: a.readTime,
      stats: a.stats,
      blocks: a.blocks,
      faqs: a.faqs,
    } satisfies ArticleContent,
  ])
);

export function getArticleContent(
  slug: string,
  fallbackTitle: string,
  categoryName: string
): ArticleContent {
  if (slug === "chatgpt-for-law-firms") return CHATGPT;
  if (slug === "google-gemini-for-law-firms") return GEMINI;
  if (CHATGPT_CONTENT_MAP[slug]) return CHATGPT_CONTENT_MAP[slug];
  return genericContent(fallbackTitle, categoryName);
}
