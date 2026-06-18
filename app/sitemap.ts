import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/metadata";
import {
  SERVICES_ITEMS,
  INSIGHTS_ITEMS,
  TOOLS_ITEMS,
} from "@/lib/navigation";

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

  return [
    ...staticRoutes,
    ...serviceRoutes,
    ...insightCategoryRoutes,
    ...insightArticleRoutes,
    ...toolRoutes,
    ...glossaryRoutes,
    ...caseStudyRoutes,
  ];
}
