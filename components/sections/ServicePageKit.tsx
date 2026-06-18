import { ReactNode } from "react";
import { CheckCircle2, XCircle } from "lucide-react";
import Button from "@/components/ui/Button";

export function Section({
  tag,
  title,
  children,
  className = "",
}: {
  tag: string;
  title: ReactNode;
  children: ReactNode;
  className?: string;
}) {
  return (
    <section className={`border-t border-pu/8 ${className}`}>
      <div className="mx-auto max-w-[860px] px-6 py-16 md:px-10">
        <span className="mb-3.5 inline-block rounded-full border border-pu/15 bg-pu/8 px-3 py-1 text-[10px] font-bold uppercase tracking-wider text-pu">
          {tag}
        </span>
        <h2 className="mb-5 text-[clamp(22px,2.8vw,34px)] font-extrabold leading-[1.15] tracking-tight text-navy">
          {title}
        </h2>
        {children}
      </div>
    </section>
  );
}

export function P({ children }: { children: ReactNode }) {
  return (
    <p className="mb-4 text-[15.5px] leading-[1.85] text-slate-700 last:mb-0">
      {children}
    </p>
  );
}

export function H3({ children }: { children: ReactNode }) {
  return (
    <h3 className="mb-2.5 mt-8 text-[18px] font-bold tracking-tight text-navy">
      {children}
    </h3>
  );
}

export function Pull({ children }: { children: ReactNode }) {
  return (
    <div className="my-6 rounded-r-xl border-l-[3px] border-pu bg-pu/5 px-6 py-4 text-[15px] italic leading-[1.8] text-slate-700">
      {children}
    </div>
  );
}

export function BulletList({ items }: { items: ReactNode[] }) {
  return (
    <ul className="my-5 flex flex-col gap-2.5">
      {items.map((item, i) => (
        <li
          key={i}
          className="flex items-start gap-2.5 text-[15px] leading-[1.7] text-slate-700"
        >
          <span className="mt-[9px] h-1.5 w-1.5 flex-shrink-0 rounded-full bg-pu" />
          <span>{item}</span>
        </li>
      ))}
    </ul>
  );
}

export function InfoCard({
  icon,
  title,
  children,
}: {
  icon: ReactNode;
  title: string;
  children: ReactNode;
}) {
  return (
    <div className="rounded-2xl border border-pu/10 bg-white p-6 transition-all hover:-translate-y-1 hover:border-pu/30 hover:shadow-[0_16px_44px_rgba(106,92,255,.1)]">
      <span className="mb-3.5 flex h-10 w-10 items-center justify-center rounded-xl bg-pu/10 text-pu">
        {icon}
      </span>
      <h4 className="mb-1.5 text-[14px] font-bold text-navy">{title}</h4>
      <p className="text-[13px] leading-[1.65] text-slate-500">{children}</p>
    </div>
  );
}

export function FeatCard({
  emoji,
  title,
  children,
}: {
  emoji: string;
  title: string;
  children: ReactNode;
}) {
  return (
    <div className="rounded-2xl border border-pu/10 bg-white p-5 text-center transition-all hover:-translate-y-1 hover:border-pu/30 hover:shadow-[0_12px_32px_rgba(106,92,255,.09)]">
      <div className="mb-2.5 text-[28px]">{emoji}</div>
      <div className="mb-1.5 text-[13px] font-bold text-navy">{title}</div>
      <div className="text-[12px] leading-[1.55] text-slate-500">
        {children}
      </div>
    </div>
  );
}

export function DarkBox({
  title,
  items,
}: {
  title: string;
  items: ReactNode[];
}) {
  return (
    <div className="my-8 rounded-2xl bg-gradient-to-br from-navy to-[#162050] p-8 md:p-10">
      <h3 className="mb-3.5 text-[20px] font-extrabold text-white">{title}</h3>
      <ul className="flex flex-col gap-2.5">
        {items.map((item, i) => (
          <li
            key={i}
            className="flex items-start gap-2.5 text-[13.5px] leading-[1.65] text-white/65"
          >
            <span className="mt-2 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-pu3" />
            <span>{item}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function DataTable({
  headers,
  rows,
}: {
  headers: string[];
  rows: ReactNode[][];
}) {
  return (
    <div className="my-6 overflow-x-auto rounded-2xl border border-pu/12">
      <table className="w-full border-collapse">
        <thead>
          <tr>
            {headers.map((h, i) => (
              <th
                key={i}
                className="bg-gradient-to-br from-navy to-[#162050] px-4 py-3.5 text-left text-[12px] font-bold tracking-wide text-white/85"
              >
                {h}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, ri) => (
            <tr key={ri} className="hover:bg-pu/[.03]">
              {row.map((cell, ci) => (
                <td
                  key={ci}
                  className="border-t border-pu/8 px-4 py-3.5 text-[13.5px] text-slate-700 [&_strong]:font-semibold [&_strong]:text-navy"
                >
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export function MistakeList({
  items,
}: {
  items: { title: string; body: string }[];
}) {
  return (
    <div className="my-5 flex flex-col gap-3">
      {items.map((m, i) => (
        <div
          key={i}
          className="flex items-start gap-3.5 rounded-2xl border border-red-500/12 bg-white p-5"
        >
          <span className="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-lg bg-red-500/10 text-red-500">
            <XCircle size={16} />
          </span>
          <div>
            <h4 className="mb-1 text-[13.5px] font-bold text-navy">
              {m.title}
            </h4>
            <p className="text-[13px] leading-[1.6] text-slate-500">{m.body}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export function ProcessSteps({
  steps,
}: {
  steps: { title: string; body: string }[];
}) {
  return (
    <div className="relative my-7 flex flex-col">
      <div className="absolute bottom-6 left-6 top-6 hidden w-0.5 bg-gradient-to-b from-pu to-transparent md:block" />
      {steps.map((s, i) => (
        <div key={i} className="relative flex items-start gap-5 py-5">
          <span className="relative z-10 flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-pu to-pu2 text-[16px] font-black text-white shadow-[0_4px_16px_rgba(106,92,255,.35)]">
            {i + 1}
          </span>
          <div className="pt-2">
            <h4 className="mb-1.5 text-[15px] font-bold text-navy">{s.title}</h4>
            <p className="text-[13.5px] leading-[1.7] text-slate-500">
              {s.body}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
}

export function ServiceHero({
  tag,
  title,
  highlight,
  sub,
  pills,
  primaryCta,
  onPrimary,
}: {
  tag: string;
  title: string;
  highlight: string;
  sub: string;
  pills: string[];
  primaryCta: string;
  onPrimary: () => void;
}) {
  return (
    <section className="hero-gradient relative overflow-hidden">
      <div className="grid-bg absolute inset-0 opacity-40" />
      <div className="relative z-10 mx-auto max-w-[860px] px-6 py-20 text-center md:px-10">
        <span className="mb-5 inline-flex items-center gap-2 rounded-full border border-pu/25 bg-pu/12 px-4 py-1.5 text-[11px] font-bold uppercase tracking-wider text-pu3">
          {tag}
        </span>
        <h1 className="text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
          {title} <span className="text-grad-purple">{highlight}</span>
        </h1>
        <p className="mx-auto mt-5 max-w-[620px] text-[17px] leading-[1.75] text-white/55">
          {sub}
        </p>
        <div className="mt-8 flex flex-wrap justify-center gap-2">
          {pills.map((p) => (
            <span
              key={p}
              className="rounded-full border border-pu/25 bg-pu/12 px-3.5 py-1.5 text-[12px] font-semibold text-pu3"
            >
              {p}
            </span>
          ))}
        </div>
        <div className="mt-9 flex flex-wrap justify-center gap-3">
          <Button variant="primary" size="lg" onClick={onPrimary}>
            {primaryCta}
          </Button>
          <Button
            href="/tools/ai-visibility-checker"
            variant="outline"
            size="lg"
            className="border-white/20 text-white hover:border-pu/45 hover:text-white"
          >
            Book A Strategy Call
          </Button>
        </div>
      </div>
    </section>
  );
}

export function TrustBar({ items }: { items: string[] }) {
  return (
    <div className="border-y border-pu/8 bg-[#f8f7ff]">
      <div className="mx-auto flex max-w-[900px] flex-wrap items-center justify-center gap-x-8 gap-y-3 px-6 py-5 md:px-10">
        {items.map((item) => (
          <div
            key={item}
            className="flex items-center gap-2 text-[12px] font-semibold text-slate-600"
          >
            <span className="flex h-[22px] w-[22px] items-center justify-center rounded-full bg-pu/10 text-pu">
              <CheckCircle2 size={12} />
            </span>
            {item}
          </div>
        ))}
      </div>
    </div>
  );
}

export function IntroBox({ children }: { children: ReactNode }) {
  return (
    <section>
      <div className="mx-auto max-w-[860px] px-6 pt-16 md:px-10">
        <div className="rounded-3xl border border-pu/13 bg-gradient-to-br from-pu/6 to-pu/[.02] p-8 md:p-10">
          {children}
        </div>
      </div>
    </section>
  );
}

export function FinalCta({
  title,
  highlight,
  body,
  primaryCta,
  onPrimary,
  note,
}: {
  title: string;
  highlight: string;
  body: string;
  primaryCta: string;
  onPrimary: () => void;
  note: string;
}) {
  return (
    <section className="hero-gradient relative overflow-hidden">
      <div className="grid-bg absolute inset-0 opacity-40" />
      <div className="relative z-10 mx-auto max-w-[640px] px-6 py-20 text-center md:px-10">
        <span className="mb-5 inline-flex items-center rounded-full border border-pu/25 bg-pu/12 px-4 py-1.5 text-[11px] font-bold uppercase tracking-wider text-pu3">
          Get Started
        </span>
        <h2 className="text-[clamp(26px,3.2vw,42px)] font-extrabold leading-[1.1] tracking-tight text-white">
          {title} <span className="text-grad-purple">{highlight}</span>
        </h2>
        <p className="mx-auto mt-4 max-w-[480px] text-[16px] leading-[1.75] text-white/50">
          {body}
        </p>
        <div className="mt-8 flex flex-wrap justify-center gap-3">
          <Button variant="primary" size="lg" onClick={onPrimary}>
            {primaryCta}
          </Button>
          <Button
            href="/tools/ai-visibility-checker"
            variant="outline"
            size="lg"
            className="border-white/20 text-white hover:border-pu/45 hover:text-white"
          >
            Book A Strategy Call
          </Button>
        </div>
        <p className="mt-8 text-[12px] text-white/25">{note}</p>
      </div>
    </section>
  );
}
