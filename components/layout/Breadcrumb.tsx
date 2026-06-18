"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ChevronRight } from "lucide-react";
import { breadcrumbSchema, SITE_URL } from "@/lib/schema";

const ACRONYMS = new Set([
  "ai",
  "seo",
  "geo",
  "faq",
  "roi",
  "aiso",
  "us",
]);

const SPECIAL: Record<string, string> = {
  chatgpt: "ChatGPT",
  "e-e-a-t": "E-E-A-T",
  "ai-overviews": "AI Overviews",
  "ai-seo": "AI SEO",
};

function humanize(segment: string): string {
  if (SPECIAL[segment]) return SPECIAL[segment];
  return segment
    .split("-")
    .map((word) =>
      ACRONYMS.has(word.toLowerCase())
        ? word.toUpperCase()
        : word.charAt(0).toUpperCase() + word.slice(1)
    )
    .join(" ");
}

export default function Breadcrumb() {
  const pathname = usePathname();
  const segments = pathname.split("/").filter(Boolean);

  if (segments.length === 0) return null;

  const items = [
    { name: "Home", url: `${SITE_URL}/` },
    ...segments.map((seg, i) => ({
      name: humanize(seg),
      url: `${SITE_URL}/${segments.slice(0, i + 1).join("/")}`,
    })),
  ];

  const crumbs = [
    { label: "Home", href: "/" },
    ...segments.map((seg, i) => ({
      label: humanize(seg),
      href: `/${segments.slice(0, i + 1).join("/")}`,
    })),
  ];

  return (
    <nav
      aria-label="Breadcrumb"
      className="mx-auto max-w-[1100px] px-6 py-4 md:px-10"
    >
      <ol className="flex flex-wrap items-center gap-1.5 text-[12px] text-slate-500">
        {crumbs.map((crumb, i) => {
          const last = i === crumbs.length - 1;
          return (
            <li key={crumb.href} className="flex items-center gap-1.5">
              {last ? (
                <span className="font-semibold text-navy">{crumb.label}</span>
              ) : (
                <Link
                  href={crumb.href}
                  className="transition-colors hover:text-pu"
                >
                  {crumb.label}
                </Link>
              )}
              {!last && (
                <ChevronRight size={13} className="text-slate-300" />
              )}
            </li>
          );
        })}
      </ol>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(breadcrumbSchema(items), null, 0),
        }}
      />
    </nav>
  );
}
