"use client";

import { useEffect, useState } from "react";
import { Sparkles, X } from "lucide-react";

interface StickyCTAProps {
  message: string;
  ctaText?: string;
  onCtaClick?: () => void;
}

export default function StickyCTA({
  message,
  ctaText = "Get Started",
  onCtaClick,
}: StickyCTAProps) {
  const [visible, setVisible] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 400);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  if (dismissed) return null;

  return (
    <div
      className={`fixed bottom-0 left-0 right-0 z-[90] transition-transform duration-300 ${
        visible ? "translate-y-0" : "translate-y-full"
      }`}
    >
      <div className="mx-auto flex max-w-[1100px] items-center justify-between gap-4 border-t border-pu/20 bg-white/95 px-5 py-3.5 shadow-[0_-8px_32px_rgba(11,21,54,.12)] backdrop-blur-xl md:px-8">
        <div className="flex items-center gap-3">
          <span className="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-xl bg-pu/10 text-pu">
            <Sparkles size={18} />
          </span>
          <span className="text-[13px] font-bold text-navy md:text-[15px]">
            {message}
          </span>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={onCtaClick}
            className="rounded-full bg-gradient-to-br from-pu to-pu2 px-5 py-2.5 text-[13px] font-bold text-white shadow-[0_4px_20px_rgba(106,92,255,.35)] transition-all hover:-translate-y-0.5"
          >
            {ctaText}
          </button>
          <button
            aria-label="Dismiss"
            onClick={() => setDismissed(true)}
            className="flex h-8 w-8 items-center justify-center rounded-full text-slate-400 hover:bg-slate-100"
          >
            <X size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}
