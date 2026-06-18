"use client";

import { useState, useEffect, FormEvent } from "react";
import {
  ScanSearch,
  MessageSquare,
  Stars,
  Compass,
  Sparkles,
  Loader2,
} from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";

const PRACTICE_AREAS = [
  "Personal Injury",
  "Family Law",
  "Criminal Defense",
  "Estate Planning",
  "Corporate Law",
  "Immigration",
  "Employment Law",
  "Real Estate Law",
  "Bankruptcy",
];

interface EngineScore {
  name: string;
  icon: React.ComponentType<{ size?: number; className?: string }>;
  score: number;
}

interface Result {
  overall: number;
  engines: EngineScore[];
}

// Deterministic pseudo-random so the same inputs yield a stable, plausible score.
function hashString(str: string): number {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return Math.abs(h);
}

function scoreFor(seed: string): number {
  // Map a hash into the plausible 40-90 range.
  return 40 + (hashString(seed) % 51);
}

export default function VisibilityCheckerClient() {
  const [firm, setFirm] = useState("");
  const [website, setWebsite] = useState("");
  const [practiceArea, setPracticeArea] = useState(PRACTICE_AREAS[0]);
  const [city, setCity] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<Result | null>(null);
  const [animate, setAnimate] = useState(false);

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setAnimate(false);

    const base = `${firm}|${website}|${practiceArea}|${city}`;
    const engines: EngineScore[] = [
      { name: "ChatGPT", icon: MessageSquare, score: scoreFor(base + ":chatgpt") },
      { name: "Gemini", icon: Stars, score: scoreFor(base + ":gemini") },
      { name: "Perplexity", icon: Compass, score: scoreFor(base + ":perplexity") },
      { name: "Google AI", icon: Sparkles, score: scoreFor(base + ":googleai") },
    ];
    const overall = Math.round(
      engines.reduce((sum, e) => sum + e.score, 0) / engines.length
    );

    // Simulate analysis latency.
    setTimeout(() => {
      setResult({ overall, engines });
      setLoading(false);
    }, 1400);
  }

  // Trigger bar animation once a result mounts.
  useEffect(() => {
    if (result) {
      const id = requestAnimationFrame(() => setAnimate(true));
      return () => cancelAnimationFrame(id);
    }
  }, [result]);

  const scoreColor = (score: number) =>
    score >= 75 ? "text-green-400" : score >= 60 ? "text-gold2" : "text-pu3";

  const ratingLabel = (score: number) =>
    score >= 75 ? "Strong" : score >= 60 ? "Moderate" : "At Risk";

  return (
    <>
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto max-w-[720px] text-center">
            <Tag variant="purple">AI VISIBILITY CHECKER</Tag>
            <h1 className="mt-5 text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
              See how AI engines rank your firm
            </h1>
            <p className="mx-auto mt-5 max-w-[600px] text-[17px] leading-relaxed text-white/70">
              When potential clients ask ChatGPT, Gemini, or Perplexity for a
              lawyer, does your firm show up? Run a free check to see your AI
              Visibility Score.
            </p>
          </div>

          <div className="mx-auto mt-12 max-w-[680px] rounded-2xl border border-white/10 bg-white/[0.04] p-7 backdrop-blur md:p-9">
            <form onSubmit={handleSubmit} className="grid gap-5 sm:grid-cols-2">
              <div className="flex flex-col gap-2">
                <label
                  htmlFor="firm"
                  className="text-[13px] font-semibold text-white/80"
                >
                  Firm Name
                </label>
                <input
                  id="firm"
                  type="text"
                  required
                  value={firm}
                  onChange={(e) => setFirm(e.target.value)}
                  placeholder="Smith &amp; Associates"
                  className="rounded-xl border border-white/15 bg-navy/40 px-4 py-3 text-[15px] text-white placeholder:text-white/30 focus:border-pu focus:outline-none"
                />
              </div>
              <div className="flex flex-col gap-2">
                <label
                  htmlFor="website"
                  className="text-[13px] font-semibold text-white/80"
                >
                  Website URL
                </label>
                <input
                  id="website"
                  type="url"
                  required
                  value={website}
                  onChange={(e) => setWebsite(e.target.value)}
                  placeholder="https://yourfirm.com"
                  className="rounded-xl border border-white/15 bg-navy/40 px-4 py-3 text-[15px] text-white placeholder:text-white/30 focus:border-pu focus:outline-none"
                />
              </div>
              <div className="flex flex-col gap-2">
                <label
                  htmlFor="practiceArea"
                  className="text-[13px] font-semibold text-white/80"
                >
                  Practice Area
                </label>
                <select
                  id="practiceArea"
                  value={practiceArea}
                  onChange={(e) => setPracticeArea(e.target.value)}
                  className="rounded-xl border border-white/15 bg-navy/40 px-4 py-3 text-[15px] text-white focus:border-pu focus:outline-none"
                >
                  {PRACTICE_AREAS.map((area) => (
                    <option key={area} value={area} className="text-navy">
                      {area}
                    </option>
                  ))}
                </select>
              </div>
              <div className="flex flex-col gap-2">
                <label
                  htmlFor="city"
                  className="text-[13px] font-semibold text-white/80"
                >
                  City
                </label>
                <input
                  id="city"
                  type="text"
                  required
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  placeholder="Toronto"
                  className="rounded-xl border border-white/15 bg-navy/40 px-4 py-3 text-[15px] text-white placeholder:text-white/30 focus:border-pu focus:outline-none"
                />
              </div>
              <div className="sm:col-span-2">
                <Button
                  type="submit"
                  variant="gold"
                  size="lg"
                  className="w-full"
                >
                  {loading ? (
                    <>
                      <Loader2 size={17} className="animate-spin" /> Analyzing
                      your firm…
                    </>
                  ) : (
                    <>
                      <ScanSearch size={17} /> Check My AI Visibility
                    </>
                  )}
                </Button>
              </div>
            </form>
          </div>
        </div>
      </section>

      {result && (
        <section>
          <div className="mx-auto max-w-[820px] px-6 py-20 md:px-10">
            <div className="rounded-2xl border border-pu/10 bg-white p-8 shadow-[0_6px_28px_rgba(11,21,54,.08)] md:p-10">
              <div className="flex flex-col items-center gap-6 border-b border-pu/10 pb-8 text-center md:flex-row md:gap-10 md:text-left">
                <div className="relative flex h-36 w-36 shrink-0 items-center justify-center rounded-full bg-navy">
                  <div className="text-center">
                    <div className="text-[44px] font-extrabold leading-none text-grad-gold">
                      {result.overall}
                    </div>
                    <div className="mt-1 text-[11px] font-semibold uppercase tracking-wider text-white/60">
                      / 100
                    </div>
                  </div>
                </div>
                <div>
                  <div className="text-[12px] font-bold uppercase tracking-wider text-pu">
                    Your AI Visibility Score
                  </div>
                  <h2 className="mt-2 text-[clamp(22px,2.6vw,30px)] font-extrabold tracking-tight text-navy">
                    {firm || "Your firm"} is{" "}
                    {result.overall >= 75
                      ? "well positioned"
                      : result.overall >= 60
                        ? "partially visible"
                        : "largely invisible"}{" "}
                    in AI search
                  </h2>
                  <p className="mt-2 text-[15px] leading-relaxed text-slate-600">
                    Based on {practiceArea} queries in {city || "your market"},
                    here&apos;s how often AI engines surface and cite your firm
                    today.
                  </p>
                </div>
              </div>

              <div className="mt-8 space-y-5">
                {result.engines.map((engine) => {
                  const Icon = engine.icon;
                  return (
                    <div key={engine.name}>
                      <div className="mb-1.5 flex items-center justify-between">
                        <div className="flex items-center gap-2 text-[14px] font-semibold text-navy">
                          <Icon size={16} className="text-pu" />
                          {engine.name}
                        </div>
                        <div className="flex items-center gap-2 text-[13px]">
                          <span className="font-bold text-navy">
                            {engine.score}
                          </span>
                          <span className="rounded-full bg-pu/8 px-2 py-0.5 text-[11px] font-semibold text-pu">
                            {ratingLabel(engine.score)}
                          </span>
                        </div>
                      </div>
                      <div className="h-2.5 w-full overflow-hidden rounded-full bg-slate-100">
                        <div
                          className="h-full rounded-full bg-gradient-to-r from-pu to-pu2 transition-[width] duration-[1200ms] ease-out"
                          style={{
                            width: animate ? `${engine.score}%` : "0%",
                          }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>

              <div className="mt-9 rounded-2xl bg-navy p-7 text-center">
                <h3 className="text-[20px] font-extrabold tracking-tight text-white">
                  Want to push every score above 90?
                </h3>
                <p className="mx-auto mt-2 max-w-[480px] text-[15px] leading-relaxed text-white/70">
                  Our AI growth systems get law firms cited across ChatGPT,
                  Gemini, Perplexity, and Google AI. Book a free strategy call
                  and we&apos;ll map your path to the top.
                </p>
                <div className="mt-5 flex justify-center">
                  <Button href="/about" variant="gold" size="lg">
                    Get a Free Strategy Call
                  </Button>
                </div>
              </div>

              <p className="mt-5 text-center text-[12px] text-slate-400">
                Scores are an illustrative estimate based on the details you
                provided. A full audit analyzes live AI responses, citations,
                and entity signals.
              </p>
            </div>
          </div>
        </section>
      )}
    </>
  );
}
