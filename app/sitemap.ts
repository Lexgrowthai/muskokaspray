import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/metadata";
import {
  SERVICES_ITEMS,
  INSIGHTS_ITEMS,
  TOOLS_ITEMS,
} from "@/lib/navigation";
import { CHATGPT_SLUGS } from "./chatgpt/data";
import { ARTICLE_SLUGS as GEMINI_SLUGS, SILO_META as GEMINI_META } from "./gemini/data";
import { ARTICLE_SLUGS as PERPLEXITY_SLUGS, SILO_META as PERPLEXITY_META } from "./perplexity/data";
import { ARTICLE_SLUGS as AI_WEBSITES_SLUGS, SILO_META as AI_WEBSITES_META } from "./ai-websites/data";
import { ARTICLE_SLUGS as AI_SEO_SLUGS, SILO_META as AI_SEO_META } from "./ai-seo/data";
import { ARTICLE_SLUGS as SCHEMA_SLUGS, SILO_META as SCHEMA_META } from "./schema/data";
import { ARTICLE_SLUGS as AI_RECEPTIONISTS_SLUGS, SILO_META as AI_RECEPTIONISTS_META } from "./ai-receptionists/data";
import { ARTICLE_SLUGS as AI_CHATBOTS_SLUGS, SILO_META as AI_CHATBOTS_META } from "./ai-chatbots/data";
import { ARTICLE_SLUGS as LAW_FIRM_MARKETING_SLUGS, SILO_META as LAW_FIRM_MARKETING_META } from "./law-firm-marketing/data";
import { ARTICLE_SLUGS as FUTURE_OF_SEARCH_SLUGS, SILO_META as FUTURE_OF_SEARCH_META } from "./future-of-search/data";

const GLOSSARY_TERMS = [
  "entity-seo",
  "knowledge-graph",
  "ai-overviews",
  "geo",
  "schema-markup",
  "semantic-search",
  "structured-data",
  "aiso",
  "e-e-a-t",
  "topical-authority",
];

const CASE_STUDIES = [
  "personal-injury",
  "family-law",
  "criminal-law",
  "estate-law",
  "corporate-law",
];

const INSIGHT_ARTICLES: Record<string, string[]> = {
  chatgpt: ["chatgpt-for-law-firms"],
  gemini: ["google-gemini-for-law-firms"],
};

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();

  const staticRoutes = [
    "",
    "about",
    "services",
    "insights",
    "tools",
    "case-studies",
    "resources",
    "resources/faq",
    "resources/glossary",
    "resources/guides",
    "resources/comparisons",
  ].map((path) => ({
    url: path ? `${SITE_URL}/${path}` : SITE_URL,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: path === "" ? 1 : 0.8,
  }));

  const serviceRoutes = SERVICES_ITEMS.map((s) => ({
    url: `${SITE_URL}${s.href}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: 0.9,
  }));

  const insightCategoryRoutes = INSIGHTS_ITEMS.map((i) => ({
    url: `${SITE_URL}${i.href}`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.7,
  }));

  const insightArticleRoutes = Object.entries(INSIGHT_ARTICLES).flatMap(
    ([category, slugs]) =>
      slugs.map((slug) => ({
        url: `${SITE_URL}/insights/${category}/${slug}`,
        lastModified: now,
        changeFrequency: "monthly" as const,
        priority: 0.6,
      }))
  );

  const chatgptArticleRoutes = CHATGPT_SLUGS.map((slug) => ({
    url: `${SITE_URL}/insights/chatgpt/${slug}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  const toolRoutes = Array.from(
    new Set(TOOLS_ITEMS.map((t) => t.href))
  ).map((href) => ({
    url: `${SITE_URL}${href}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: 0.6,
  }));

  const glossaryRoutes = GLOSSARY_TERMS.map((term) => ({
    url: `${SITE_URL}/resources/glossary/${term}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: 0.5,
  }));

  const caseStudyRoutes = CASE_STUDIES.map((slug) => ({
    url: `${SITE_URL}/case-studies/${slug}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: 0.6,
  }));

  const silos = [
    { meta: GEMINI_META, slugs: GEMINI_SLUGS },
    { meta: PERPLEXITY_META, slugs: PERPLEXITY_SLUGS },
    { meta: AI_WEBSITES_META, slugs: AI_WEBSITES_SLUGS },
    { meta: AI_SEO_META, slugs: AI_SEO_SLUGS },
    { meta: SCHEMA_META, slugs: SCHEMA_SLUGS },
    { meta: AI_RECEPTIONISTS_META, slugs: AI_RECEPTIONISTS_SLUGS },
    { meta: AI_CHATBOTS_META, slugs: AI_CHATBOTS_SLUGS },
    { meta: LAW_FIRM_MARKETING_META, slugs: LAW_FIRM_MARKETING_SLUGS },
    { meta: FUTURE_OF_SEARCH_META, slugs: FUTURE_OF_SEARCH_SLUGS },
  ];

  const siloHubRoutes = silos.map(({ meta }) => ({
    url: `${SITE_URL}/${meta.slug}`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const siloArticleRoutes = silos.flatMap(({ meta, slugs }) =>
    slugs.map((slug) => ({
      url: `${SITE_URL}/${meta.slug}/${slug}`,
      lastModified: now,
      changeFrequency: "monthly" as const,
      priority: 0.7,
    }))
  );

  return [
    ...staticRoutes,
    ...serviceRoutes,
    ...insightCategoryRoutes,
    ...insightArticleRoutes,
    ...chatgptArticleRoutes,
    ...siloHubRoutes,
    ...siloArticleRoutes,
    ...toolRoutes,
    ...glossaryRoutes,
    ...caseStudyRoutes,
  ];
}
