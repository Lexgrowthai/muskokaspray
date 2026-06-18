"use client";

import { useState, useEffect, useMemo } from "react";
import { PhoneMissed, TrendingDown, CalendarX } from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";

// Conservative share of inbound calls that convert into signed cases.
const CALL_TO_CASE_RATE = 0.25;

function useCountUp(target: number, duration = 1200) {
  const [value, setValue] = useState(0);

  useEffect(() => {
    let raf = 0;
    let start: number | null = null;
    const from = 0;
    function step(ts: number) {
      if (start === null) start = ts;
      const progress = Math.min((ts - start) / duration, 1);
      // easeOutCubic
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(from + (target - from) * eased);
      if (progress < 1) raf = requestAnimationFrame(step);
    }
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [target, duration]);

  return value;
}

export default function MissedCallClient() {
  const [callsPerWeek, setCallsPerWeek] = useState(40);
  const [answerRate, setAnswerRate] = useState(70);
  const [caseValue, setCaseValue] = useState(5000);

  const { annualRevenueLost, monthlyLeadsMissed, missedPerWeek } =
    useMemo(() => {
      const missedFraction = (100 - answerRate) / 100;
      const missedWeek = callsPerWeek * missedFraction;
      const missedYear = missedWeek * 52;
      const lostCasesYear = missedYear * CALL_TO_CASE_RATE;
      const revenueYear = lostCasesYear * caseValue;
      const leadsMonth = (missedWeek * 52) / 12;
      return {
        annualRevenueLost: Math.round(revenueYear),
        monthlyLeadsMissed: Math.round(leadsMonth),
        missedPerWeek: Math.round(missedWeek),
      };
    }, [callsPerWeek, answerRate, caseValue]);

  const animatedRevenue = useCountUp(annualRevenueLost);
  const animatedLeads = useCountUp(monthlyLeadsMissed);

  const currency = (n: number) =>
    n.toLocaleString("en-US", {
      style: "currency",
      currency: "USD",
      maximumFractionDigits: 0,
    });

  return (
    <>
      <section className="hero-gradient relative overflow-hidden">
        <div className="grid-bg absolute inset-0 opacity-40" />
        <div className="relative z-10 mx-auto max-w-[1100px] px-6 py-20 md:px-10">
          <div className="mx-auto max-w-[720px] text-center">
            <Tag variant="gold">MISSED CALL CALCULATOR</Tag>
            <h1 className="mt-5 text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
              How much is every missed call costing you?
            </h1>
            <p className="mx-auto mt-5 max-w-[600px] text-[17px] leading-relaxed text-white/70">
              The average law firm misses 1 in 3 calls. Each one could be a
              signed case walking to a competitor. Move the sliders to see your
              number.
            </p>
          </div>
        </div>
      </section>

      <section>
        <div className="mx-auto max-w-[980px] px-6 py-20 md:px-10">
          <div className="grid gap-7 lg:grid-cols-[1fr_1fr]">
            {/* Inputs */}
            <div className="rounded-2xl border border-pu/10 bg-white p-7 shadow-[0_6px_28px_rgba(11,21,54,.08)] md:p-9">
              <h2 className="text-[20px] font-extrabold tracking-tight text-navy">
                Your numbers
              </h2>

              <div className="mt-7 space-y-8">
                <div>
                  <div className="flex items-baseline justify-between">
                    <label
                      htmlFor="calls"
                      className="text-[14px] font-semibold text-navy"
                    >
                      Inbound calls per week
                    </label>
                    <span className="text-[18px] font-extrabold text-pu">
                      {callsPerWeek}
                    </span>
                  </div>
                  <input
                    id="calls"
                    type="range"
                    min={5}
                    max={200}
                    step={5}
                    value={callsPerWeek}
                    onChange={(e) => setCallsPerWeek(Number(e.target.value))}
                    className="mt-3 w-full accent-pu"
                  />
                </div>

                <div>
                  <div className="flex items-baseline justify-between">
                    <label
                      htmlFor="answer"
                      className="text-[14px] font-semibold text-navy"
                    >
                      Call answer rate
                    </label>
                    <span className="text-[18px] font-extrabold text-pu">
                      {answerRate}%
                    </span>
                  </div>
                  <input
                    id="answer"
                    type="range"
                    min={20}
                    max={100}
                    step={1}
                    value={answerRate}
                    onChange={(e) => setAnswerRate(Number(e.target.value))}
                    className="mt-3 w-full accent-pu"
                  />
                </div>

                <div>
                  <div className="flex items-baseline justify-between">
                    <label
                      htmlFor="value"
                      className="text-[14px] font-semibold text-navy"
                    >
                      Average case value
                    </label>
                    <span className="text-[18px] font-extrabold text-pu">
                      {currency(caseValue)}
                    </span>
                  </div>
                  <input
                    id="value"
                    type="range"
                    min={500}
                    max={50000}
                    step={500}
                    value={caseValue}
                    onChange={(e) => setCaseValue(Number(e.target.value))}
                    className="mt-3 w-full accent-pu"
                  />
                  <input
                    type="number"
                    min={0}
                    value={caseValue}
                    onChange={(e) =>
                      setCaseValue(Math.max(0, Number(e.target.value)))
                    }
                    className="mt-3 w-full rounded-xl border border-pu/15 px-4 py-2.5 text-[14px] text-navy focus:border-pu focus:outline-none"
                    aria-label="Average case value in dollars"
                  />
                </div>
              </div>

              <p className="mt-7 text-[12px] leading-relaxed text-slate-400">
                Assumes roughly 1 in 4 answered calls becomes a signed case — a
                conservative intake conversion rate for most practice areas.
              </p>
            </div>

            {/* Results */}
            <div className="flex flex-col gap-5">
              <div className="rounded-2xl bg-navy p-8 text-center shadow-[0_6px_28px_rgba(11,21,54,.18)]">
                <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-white/10 text-gold2">
                  <TrendingDown size={22} />
                </div>
                <div className="mt-4 text-[13px] font-semibold uppercase tracking-wider text-white/60">
                  Estimated annual revenue lost
                </div>
                <div className="mt-2 text-[clamp(34px,5vw,52px)] font-extrabold leading-none text-grad-gold">
                  {currency(Math.round(animatedRevenue))}
                </div>
                <div className="mt-3 text-[14px] text-white/70">
                  ~{missedPerWeek} missed calls every week
                </div>
              </div>

              <div className="rounded-2xl border border-pu/10 bg-white p-8 text-center shadow-[0_6px_28px_rgba(11,21,54,.08)]">
                <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-pu/8 text-pu">
                  <CalendarX size={22} />
                </div>
                <div className="mt-4 text-[13px] font-semibold uppercase tracking-wider text-slate-500">
                  Potential leads missed per month
                </div>
                <div className="mt-2 text-[clamp(34px,5vw,52px)] font-extrabold leading-none text-grad-purple">
                  {Math.round(animatedLeads)}
                </div>
              </div>

              <div className="rounded-2xl bg-gradient-to-br from-pu to-pu2 p-7 text-center text-white shadow-[0_6px_28px_rgba(106,92,255,.3)]">
                <div className="flex items-center justify-center gap-2 text-[16px] font-bold">
                  <PhoneMissed size={18} /> Stop losing these calls
                </div>
                <p className="mx-auto mt-2 max-w-[360px] text-[14px] leading-relaxed text-white/85">
                  Our AI receptionists answer every call, 24/7, and book intake
                  automatically. See how fast it pays for itself.
                </p>
                <div className="mt-5 flex justify-center">
                  <Button href="/services/ai-receptionists" variant="gold" size="md">
                    Get a Free Strategy Call
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
