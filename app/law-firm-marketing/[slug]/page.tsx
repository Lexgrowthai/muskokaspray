import { notFound } from "next/navigation";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { articleSchema, breadcrumbSchema, faqSchema, SITE_URL } from "@/lib/schema";
import { SILO_META, ARTICLES, ARTICLE_SLUGS } from "../data";
import ArticleClient from "@/app/insights/[category]/[slug]/ArticleClient";

export function generateStaticParams() {
  return ARTICLE_SLUGS.map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = ARTICLES.find((a) => a.slug === slug);
  if (!article) return {};
  return generatePageMetadata({
    title: article.title,
    slug: `${SILO_META.slug}/${slug}`,
    description: article.description,
    type: "article",
    publishedAt: article.date,
  });
}

export default async function SiloArticlePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = ARTICLES.find((a) => a.slug === slug);
  if (!article) notFound();

  const url = `${SITE_URL}/${SILO_META.slug}/${slug}`;
  const related = article.related
    .map((s) => ARTICLES.find((a) => a.slug === s))
    .filter(Boolean)
    .map((a) => ({ title: a!.title, href: `/${SILO_META.slug}/${a!.slug}` }));

  return (
    <>
      <SchemaScript
        schema={articleSchema(
          article.title,
          article.description,
          url,
          article.date,
          "LexScale Editorial"
        )}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: SILO_META.name, url: `${SITE_URL}/${SILO_META.slug}` },
          { name: article.title, url },
        ])}
      />
      <SchemaScript schema={faqSchema(article.faqs)} />
      <ArticleClient
        title={article.title}
        category={SILO_META.name}
        categoryHref={`/${SILO_META.slug}`}
        description={article.description}
        readTime={article.readTime}
        date={article.date}
        stats={article.stats}
        blocks={article.blocks}
        faqs={article.faqs}
        related={related}
      />
    </>
  );
}
