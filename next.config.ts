import type { NextConfig } from "next";
import createMDX from "@next/mdx";

const withMDX = createMDX({
  extension: /\.mdx?$/,
});

const nextConfig: NextConfig = {
  pageExtensions: ["ts", "tsx", "js", "jsx", "md", "mdx"],
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
    ];
  },
};

export default withMDX(nextConfig);
