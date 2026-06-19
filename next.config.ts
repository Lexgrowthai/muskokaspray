import type { NextConfig } from "next";
import createMDX from "@next/mdx";

const withMDX = createMDX({
  extension: /\.mdx?$/,
});

const nextConfig: NextConfig = {
  pageExtensions: ["ts", "tsx", "js", "jsx", "md", "mdx"],
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "X-Frame-Options", value: "SAMEORIGIN" },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "X-DNS-Prefetch-Control", value: "on" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          {
            key: "Permissions-Policy",
            value: "camera=(), microphone=(), geolocation=()",
          },
        ],
      },
      {
        source: "/_next/static/(.*)",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
      {
        source: "/(.*\\.(?:png|jpg|jpeg|gif|webp|svg|ico|woff2|woff))",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=2592000, stale-while-revalidate=86400",
          },
        ],
      },
    ];
  },
  async redirects() {
    return [
      { source: "/index.html", destination: "/", permanent: true },
      { source: "/about.html", destination: "/about", permanent: true },
      {
        source: "/ai-seo-for-law-firms.html",
        destination: "/services/ai-seo",
        permanent: true,
      },
      {
        source: "/ai-website-design-for-law-firms.html",
        destination: "/services/ai-websites",
        permanent: true,
      },
      {
        source: "/ai-receptionist-for-law-firms.html",
        destination: "/services/ai-receptionists",
        permanent: true,
      },
      {
        source: "/ai-chatbot-for-law-firms.html",
        destination: "/services/ai-chatbots",
        permanent: true,
      },
      {
        source: "/chatgpt-for-law-firms.html",
        destination: "/insights/chatgpt/chatgpt-for-law-firms",
        permanent: true,
      },
      {
        source: "/google-gemini-for-law-firms.html",
        destination: "/insights/gemini/google-gemini-for-law-firms",
        permanent: true,
      },
      // Redirect the standalone /chatgpt/* section to /insights/chatgpt/*
      { source: "/chatgpt", destination: "/insights/chatgpt", permanent: true },
      {
        source: "/chatgpt/:slug",
        destination: "/insights/chatgpt/:slug",
        permanent: true,
      },
    ];
  },
};

export default withMDX(nextConfig);
