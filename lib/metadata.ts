import type { Metadata } from "next";

export const SITE_URL = "https://lexscale.ai";
export const SITE_NAME = "LexScale.ai";
export const DEFAULT_DESCRIPTION =
  "LexScale.ai builds AI growth systems for law firms — AI search optimization, AI SEO, websites, chatbots, and receptionists that win clients across ChatGPT, Gemini, Perplexity, and Google AI.";

interface GeneratePageMetadataArgs {
  title: string;
  description: string;
  slug: string;
  type?: "website" | "article";
  publishedAt?: string;
}

export function generatePageMetadata({
  title,
  description,
  slug,
  type = "website",
  publishedAt,
}: GeneratePageMetadataArgs): Metadata {
  const normalizedSlug = slug.replace(/^\/+/, "");
  const url = normalizedSlug ? `${SITE_URL}/${normalizedSlug}` : SITE_URL;
  const fullTitle = `${title} | ${SITE_NAME}`;

  return {
    title,
    description,
    alternates: {
      canonical: url,
    },
    openGraph: {
      type,
      title: fullTitle,
      description,
      url,
      siteName: SITE_NAME,
      ...(publishedAt ? { publishedTime: publishedAt } : {}),
    },
    twitter: {
      card: "summary_large_image",
      title: fullTitle,
      description,
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        "max-image-preview": "large",
        "max-snippet": -1,
        "max-video-preview": -1,
      },
    },
  };
}
