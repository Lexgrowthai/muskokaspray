"use client";

import { useState } from "react";
import { Plus, X } from "lucide-react";
import { faqSchema } from "@/lib/schema";

interface FAQItem {
  question: string;
  answer: string;
}

interface FAQProps {
  faqs: FAQItem[];
  title?: string;
}

export default function FAQ({ faqs, title }: FAQProps) {
  const [open, setOpen] = useState<number | null>(0);

  return (
    <div className="mx-auto max-w-[760px]">
      {title && (
        <h2 className="mb-8 text-center text-[28px] font-extrabold tracking-tight text-navy">
          {title}
        </h2>
      )}
      <div className="flex flex-col gap-3">
        {faqs.map((faq, i) => {
          const isOpen = open === i;
          return (
            <div
              key={i}
              className="overflow-hidden rounded-2xl border border-pu/10 bg-white"
            >
              <button
                onClick={() => setOpen(isOpen ? null : i)}
                className="flex w-full items-center justify-between gap-4 px-6 py-5 text-left"
              >
                <span className="text-[15px] font-semibold text-navy">
                  {faq.question}
                </span>
                <span className="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-full bg-pu/10 text-pu">
                  {isOpen ? <X size={15} /> : <Plus size={15} />}
                </span>
              </button>
              <div
                className="grid transition-all duration-300 ease-in-out"
                style={{
                  gridTemplateRows: isOpen ? "1fr" : "0fr",
                }}
              >
                <div className="overflow-hidden">
                  <p className="px-6 pb-5 text-[14px] leading-relaxed text-slate-600">
                    {faq.answer}
                  </p>
                </div>
              </div>
            </div>
          );
        })}
      </div>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(faqSchema(faqs), null, 0),
        }}
      />
    </div>
  );
}
