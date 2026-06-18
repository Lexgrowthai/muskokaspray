import { notFound } from "next/navigation";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { articleSchema, breadcrumbSchema, SITE_URL } from "@/lib/schema";
import { CHATGPT_ARTICLES, CHATGPT_SLUGS } from "../data";
import ArticleClient from "../../insights/[category]/[slug]/ArticleClient";

export function generateStaticParams() {
  return CHATGPT_SLUGS.map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = CHATGPT_ARTICLES.find((a) => a.slug === slug);
  if (!article) return {};
  return generatePageMetadata({
    title: article.title,
    slug: `chatgpt/${slug}`,
    description: article.description,
    type: "article",
    publishedAt: article.publishedAt,
  });
}

export default async function ChatGPTArticlePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = CHATGPT_ARTICLES.find((a) => a.slug === slug);
  if (!article) notFound();

  const url = `${SITE_URL}/chatgpt/${slug}`;
  const related = article.related
    .map((s) => CHATGPT_ARTICLES.find((a) => a.slug === s))
    .filter(Boolean)
    .map((a) => ({ title: a!.title, href: `/chatgpt/${a!.slug}` }));

  return (
    <>
      <SchemaScript
        schema={articleSchema(
          article.title,
          article.description,
          url,
          article.publishedAt,
          "LexScale Editorial"
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "ChatGPT for Law Firms", url: `${SITE_URL}/chatgpt` },
          { name: article.title, url },
        ])}
      />
      <ArticleClient
        title={article.title}
        category="ChatGPT for Law Firms"
        categoryHref="/chatgpt"
        description={article.description}
        readTime={article.readTime}
        date={article.publishedAt}
        stats={article.stats}
        blocks={article.blocks}
        faqs={article.faqs}
        related={related}
      />
    </>
  );
}
