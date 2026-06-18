import { notFound } from "next/navigation";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { articleSchema, SITE_URL } from "@/lib/schema";
import { CATEGORIES, humanizeCategory } from "../../data";
import { getArticleContent } from "./content";
import ArticleClient from "./ArticleClient";

function findArticle(category: string, slug: string) {
  const cat = CATEGORIES[category];
  if (!cat) return null;
  const article = cat.articles.find((a) => a.slug === slug);
  if (!article) return null;
  return { cat, article };
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ category: string; slug: string }>;
}) {
  const { category, slug } = await params;
  const found = findArticle(category, slug);
  const content = getArticleContent(
    slug,
    found?.article.title ?? humanizeCategory(category),
    humanizeCategory(category)
  );
  return generatePageMetadata({
    title: content.title,
    slug: `insights/${category}/${slug}`,
    description: content.description,
    type: "article",
    publishedAt: found?.article.date ?? "2026-01-15",
  });
}

export default async function ArticlePage({
  params,
}: {
  params: Promise<{ category: string; slug: string }>;
}) {
  const { category, slug } = await params;
  const found = findArticle(category, slug);

  if (!found) {
    notFound();
  }

  const categoryName = found.cat.name;
  const content = getArticleContent(slug, found.article.title, categoryName);
  const url = `${SITE_URL}/insights/${category}/${slug}`;

  const related = found.cat.articles
    .filter((a) => a.slug !== slug)
    .map((a) => ({
      title: a.title,
      href: `/insights/${category}/${a.slug}`,
    }));

  return (
    <>
      <SchemaScript
        schema={articleSchema(
          content.title,
          content.description,
          url,
          found.article.date,
          "LexScale Editorial"
        )}
      />
      <ArticleClient
        title={content.title}
        category={categoryName}
        categoryHref={`/insights/${category}`}
        description={content.description}
        readTime={content.readTime}
        date={found.article.date}
        stats={content.stats}
        blocks={content.blocks}
        faqs={content.faqs}
        related={related}
      />
    </>
  );
}
