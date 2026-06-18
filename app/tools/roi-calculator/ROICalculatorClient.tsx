"use client";

import { useState, useEffect, useMemo } from "react";
import { TrendingUp, Users, DollarSign } from "lucide-react";
import Button from "@/components/ui/Button";
import Tag from "@/components/ui/Tag";

function useCountUp(target: number, duration = 1200) {
  const [value, setValue] = useState(0);

  useEffect(() => {
    let raf = 0;
    let start: number | null = null;
    function step(ts: number) {
      if (start === null) start = ts;
      const progress = Math.min((ts - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(target * eased);
      if (progress < 1) raf = requestAnimationFrame(step);
    }
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [target, duration]);

  return value;
}

export default function ROICalculatorClient() {
  const [monthlyLeads, setMonthlyLeads] = useState(30);
  const [targetIncrease, setTargetIncrease] = useState(40);
  const [caseValue, setCaseValue] = useState(6000);
  const [closeRate, setCloseRate] = useState(30);

  const { additionalLeadsMonth, additionalCasesYear, additionalRevenueYear } =
    useMemo(() => {
      const extraLeadsMonth = monthlyLeads * (targetIncrease / 100);
      const extraLeadsYear = extraLeadsMonth * 12;
      const extraCasesYear = extraLeadsYear * (closeRate / 100);
      const extraRevenueYear = extraCasesYear * caseValue;
      return {
        additionalLeadsMonth: extraLeadsMonth,
        additionalCasesYear: extraCasesYear,
        additionalRevenueYear: Math.round(extraRevenueYear),
      };
    }, [monthlyLeads, targetIncrease, caseValue, closeRate]);

  const animatedRevenue = useCountUp(additionalRevenueYear);

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
            <Tag variant="purple">ROI CALCULATOR</Tag>
            <h1 className="mt-5 text-[clamp(30px,3.8vw,50px)] font-extrabold leading-[1.1] tracking-tight text-white">
              Project your growth ROI
            </h1>
            <p className="mx-auto mt-5 max-w-[600px] text-[17px] leading-relaxed text-white/70">
              See the additional revenue your firm could add each year by
              growing your monthly leads with an AI growth system.
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
                      htmlFor="leads"
                      className="text-[14px] font-semibold text-navy"
                    >
                      Current monthly leads
                    </label>
                    <span className="text-[18px] font-extrabold text-pu">
                      {monthlyLeads}
                    </span>
                  </div>
                  <input
                    id="leads"
                    type="range"
                    min={5}
                    max={300}
                    step={5}
                    value={monthlyLeads}
                    onChange={(e) => setMonthlyLeads(Number(e.target.value))}
                    className="mt-3 w-full accent-pu"
                  />
                </div>

                <div>
                  <div className="flex items-baseline justify-between">
                    <label
                      htmlFor="increase"
                      className="text-[14px] font-semibold text-navy"
                    >
                      Target lead increase
                    </label>
                    <span className="text-[18px] font-extrabold text-pu">
                      {targetIncrease}%
                    </span>
                  </div>
                  <input
                    id="increase"
                    type="range"
                    min={10}
                    max={300}
                    step={5}
                    value={targetIncrease}
                    onChange={(e) => setTargetIncrease(Number(e.target.value))}
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

                <div>
                  <div className="flex items-baseline justify-between">
                    <label
                      htmlFor="close"
                      className="text-[14px] font-semibold text-navy"
                    >
                      Lead-to-client close rate
                    </label>
                    <span className="text-[18px] font-extrabold text-pu">
                      {closeRate}%
                    </span>
                  </div>
                  <input
                    id="close"
                    type="range"
                    min={5}
                    max={100}
                    step={1}
                    value={closeRate}
                    onChange={(e) => setCloseRate(Number(e.target.value))}
                    className="mt-3 w-full accent-pu"
                  />
                </div>
              </div>
            </div>

            {/* Results */}
            <div className="flex flex-col gap-5">
              <div className="rounded-2xl bg-navy p-8 text-center shadow-[0_6px_28px_rgba(11,21,54,.18)]">
                <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-white/10 text-gold2">
                  <TrendingUp size={22} />
                </div>
                <div className="mt-4 text-[13px] font-semibold uppercase tracking-wider text-white/60">
                  Projected additional revenue / year
                </div>
                <div className="mt-2 text-[clamp(34px,5vw,52px)] font-extrabold leading-none text-grad-gold">
                  {currency(Math.round(animatedRevenue))}
                </div>
              </div>

              <div className="grid grid-cols-2 gap-5">
                <div className="rounded-2xl border border-pu/10 bg-white p-6 text-center shadow-[0_6px_28px_rgba(11,21,54,.08)]">
                  <div className="mx-auto flex h-10 w-10 items-center justify-center rounded-xl bg-pu/8 text-pu">
                    <Users size={18} />
                  </div>
                  <div className="mt-3 text-[11px] font-semibold uppercase tracking-wider text-slate-500">
                    Extra leads / month
                  </div>
                  <div className="mt-1 text-[28px] font-extrabold leading-none text-grad-purple">
                    {Math.round(additionalLeadsMonth)}
                  </div>
                </div>
                <div className="rounded-2xl border border-pu/10 bg-white p-6 text-center shadow-[0_6px_28px_rgba(11,21,54,.08)]">
                  <div className="mx-auto flex h-10 w-10 items-center justify-center rounded-xl bg-pu/8 text-pu">
                    <DollarSign size={18} />
                  </div>
                  <div className="mt-3 text-[11px] font-semibold uppercase tracking-wider text-slate-500">
                    Extra cases / year
                  </div>
                  <div className="mt-1 text-[28px] font-extrabold leading-none text-grad-purple">
                    {Math.round(additionalCasesYear)}
                  </div>
                </div>
              </div>

              <div className="rounded-2xl bg-gradient-to-br from-pu to-pu2 p-7 text-center text-white shadow-[0_6px_28px_rgba(106,92,255,.3)]">
                <div className="text-[16px] font-bold">
                  Ready to hit these numbers?
                </div>
                <p className="mx-auto mt-2 max-w-[360px] text-[14px] leading-relaxed text-white/85">
                  We&apos;ve added $12M+ in revenue for law firms. Book a free
                  strategy call and we&apos;ll build your growth roadmap.
                </p>
                <div className="mt-5 flex justify-center">
                  <Button href="/about" variant="gold" size="md">
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
