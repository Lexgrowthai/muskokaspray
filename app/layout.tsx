import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Script from "next/script";
import "./globals.css";
import Nav from "@/components/layout/Nav";
import Footer from "@/components/layout/Footer";
import SchemaScript from "@/components/schema/SchemaScript";
import { organizationSchema, websiteSchema } from "@/lib/schema";
import { SITE_URL, DEFAULT_DESCRIPTION } from "@/lib/metadata";

const inter = Inter({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800", "900"],
  variable: "--font-inter",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "AI Growth Systems for Law Firms | LexScale.ai",
    template: "%s | LexScale.ai",
  },
  description: DEFAULT_DESCRIPTION,
  robots: { index: true, follow: true },
  openGraph: {
    siteName: "LexScale.ai",
    images: [{ url: "/og-image.png", width: 1200, height: 630, alt: "LexScale.ai" }],
  },
  twitter: {
    card: "summary_large_image",
    site: "@lexscaleai",
    images: ["/og-image.png"],
  },
};

const GA_ID = "G-XXXXXXXXXX";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} h-full`}>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <SchemaScript schema={organizationSchema()} />
        <SchemaScript schema={websiteSchema()} />
      </head>
      <body className="flex min-h-full flex-col font-sans">
        <Script
          src={`https://www.googletagmanager.com/gtag/js?id=${GA_ID}`}
          strategy="afterInteractive"
        />
        <Script id="ga-init" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '${GA_ID}');
          `}
        </Script>
        <Nav />
        <main className="flex-1">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
