"use client";

import { useEffect, useState, FormEvent } from "react";
import { CheckCircle2, X } from "lucide-react";

interface LeadFormModalProps {
  isOpen: boolean;
  onClose: () => void;
  offer?: string;
  title?: string;
  description?: string;
}

const PRACTICE_AREAS = [
  "Personal Injury",
  "Family Law",
  "Criminal Defense",
  "Estate Planning",
  "Corporate Law",
  "Immigration",
  "Employment Law",
  "Other",
];

export default function LeadFormModal({
  isOpen,
  onClose,
  offer = "Free Strategy Call",
  title = "Get Your Free Strategy Call",
  description = "Tell us about your firm and we'll show you exactly where you stand in AI search.",
}: LeadFormModalProps) {
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    if (isOpen) {
      document.addEventListener("keydown", onKey);
      document.body.style.overflow = "hidden";
    }
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div
      className="fixed inset-0 z-[200] flex items-center justify-center bg-navy/60 p-4 backdrop-blur-sm"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-md rounded-3xl border border-pu/15 bg-white p-8 shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          aria-label="Close"
          onClick={onClose}
          className="absolute right-4 top-4 flex h-9 w-9 items-center justify-center rounded-full text-slate-400 hover:bg-slate-100"
        >
          <X size={20} />
        </button>

        {submitted ? (
          <div className="py-8 text-center">
            <span className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-emerald-500/10 text-emerald-500">
              <CheckCircle2 size={36} />
            </span>
            <h3 className="mb-2 text-[22px] font-extrabold text-navy">
              You&apos;re all set!
            </h3>
            <p className="text-[14px] text-slate-600">
              Thanks — our team will reach out within one business day with your{" "}
              {offer.toLowerCase()}.
            </p>
          </div>
        ) : (
          <>
            <span className="mb-3 inline-flex items-center rounded-full border border-pu/20 bg-pu/8 px-3 py-1 text-[11px] font-bold uppercase tracking-wide text-pu">
              {offer}
            </span>
            <h3 className="mb-1.5 text-[22px] font-extrabold tracking-tight text-navy">
              {title}
            </h3>
            <p className="mb-6 text-[13px] leading-relaxed text-slate-500">
              {description}
            </p>
            <form onSubmit={handleSubmit} className="flex flex-col gap-3">
              <input
                required
                name="name"
                placeholder="Your name"
                className="rounded-xl border border-pu/15 px-4 py-3 text-[14px] outline-none focus:border-pu"
              />
              <input
                required
                name="firm"
                placeholder="Firm name"
                className="rounded-xl border border-pu/15 px-4 py-3 text-[14px] outline-none focus:border-pu"
              />
              <input
                required
                name="phone"
                type="tel"
                placeholder="Phone"
                className="rounded-xl border border-pu/15 px-4 py-3 text-[14px] outline-none focus:border-pu"
              />
              <select
                required
                name="practiceArea"
                defaultValue=""
                className="rounded-xl border border-pu/15 px-4 py-3 text-[14px] text-slate-700 outline-none focus:border-pu"
              >
                <option value="" disabled>
                  Practice area
                </option>
                {PRACTICE_AREAS.map((p) => (
                  <option key={p} value={p}>
                    {p}
                  </option>
                ))}
              </select>
              <input
                name="website"
                type="url"
                placeholder="Website URL"
                className="rounded-xl border border-pu/15 px-4 py-3 text-[14px] outline-none focus:border-pu"
              />
              <button
                type="submit"
                className="mt-2 rounded-full bg-gradient-to-br from-pu to-pu2 px-6 py-3.5 text-[15px] font-bold text-white shadow-[0_4px_20px_rgba(106,92,255,.35)] transition-all hover:-translate-y-0.5"
              >
                Claim {offer}
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
}
