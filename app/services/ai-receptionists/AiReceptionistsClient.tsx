"use client";

import { useState } from "react";
import {
  PhoneCall,
  ClipboardCheck,
  CalendarDays,
  FileText,
  Zap,
  Globe,
} from "lucide-react";
import StickyCTA from "@/components/sections/StickyCTA";
import LeadFormModal from "@/components/sections/LeadFormModal";
import FAQ from "@/components/sections/FAQ";
import {
  Section,
  P,
  BulletList,
  InfoCard,
  FeatCard,
  DarkBox,
  DataTable,
  MistakeList,
  ProcessSteps,
  ServiceHero,
  TrustBar,
  FinalCta,
} from "@/components/sections/ServicePageKit";

const FAQS = [
  {
    question: "What is an AI receptionist for law firms?",
    answer:
      "An AI receptionist is a voice-based system that answers your firm's incoming calls 24 hours a day, 7 days a week. It greets callers, qualifies them as potential clients, collects basic case information, books consultations, and routes urgent matters to the appropriate attorney — without requiring a human staff member to be available.",
  },
  {
    question: "Will callers know they're speaking to an AI?",
    answer:
      "The system speaks naturally and professionally, and most callers will experience it as a capable phone service. We recommend being straightforward if a caller directly asks — the AI is designed to handle this gracefully and offer to connect with a human if the caller prefers. Most callers care far more about getting their question answered than about whether they spoke to a human.",
  },
  {
    question: "Can an AI receptionist replace a human receptionist?",
    answer:
      "It handles the majority of routine call volume — new client inquiries, appointment scheduling, basic case screening, and after-hours calls. For complex existing client matters or sensitive conversations, the system routes calls to the appropriate attorney or staff member. Most firms use it to extend their coverage, not replace human staff entirely.",
  },
  {
    question: "How does the AI receptionist qualify leads?",
    answer:
      "The system asks callers a set of qualifying questions specific to your practice areas — type of matter, jurisdiction, timeline, and basic facts. Based on your firm's criteria, it categorises the caller as a strong lead, a referral out, or a follow-up, and routes or logs accordingly.",
  },
  {
    question: "What happens when someone calls with an emergency?",
    answer:
      "The AI is configured to recognise urgency indicators — an arrest, an imminent court date, a situation requiring immediate counsel. When these triggers are detected, the call is escalated immediately to your designated on-call attorney via call transfer and simultaneous text alert. No emergency gets routed to a scheduling queue.",
  },
  {
    question: "Which practice management software does it integrate with?",
    answer:
      "We integrate with Clio, MyCase, Smokeball, Lawmatics, Google Calendar, Salesforce, HubSpot, and several others. If you use a system not on this list, we'll assess integration feasibility during onboarding. Most common legal practice management platforms are supported.",
  },
  {
    question: "Can I customise the greeting and the questions it asks?",
    answer:
      "Yes, completely. The greeting uses your firm's name and reflects your firm's tone. The qualifying questions are built specifically for your practice areas and your criteria for a qualified client. Nothing is generic out of the box — it's configured for your firm specifically.",
  },
  {
    question: "Does it work for multi-location firms?",
    answer:
      "Yes. We can configure separate intake flows for different office numbers, different practice groups, or different geographic locations — all managed within a single system. Routing logic can direct calls to the appropriate office or attorney based on the caller's matter type and location.",
  },
  {
    question: "How long does setup take?",
    answer:
      "Most firms are live within two to three weeks. The timeline includes practice area mapping, call flow design, integration setup, and testing. We don't go live until the system has been thoroughly tested and you're satisfied with how it handles your firm's common call scenarios.",
  },
  {
    question: "Is this compliant with lawyer advertising rules?",
    answer:
      "The AI receptionist is a call answering and intake tool, not an advertising medium. It doesn't make claims about legal services or provide legal advice — it collects information and facilitates scheduling. We recommend reviewing the call flow with your state bar's ethics guidance if you have specific compliance questions.",
  },
  {
    question: "What does it cost?",
    answer:
      "Pricing depends on call volume, the number of practice areas configured, and the integrations required. We structure it as a monthly service rather than a large upfront cost. The right way to evaluate it is to compare the cost against the value of one additional retained client per month.",
  },
];

const LIVE_CALLS = [
  {
    bg: "bg-emerald-500/15",
    name: "Maria T. — Personal Injury",
    sub: "Qualified · Booked for Tuesday 2pm",
    tag: "Booked",
    tagCls: "bg-emerald-500/15 text-emerald-600",
  },
  {
    bg: "bg-pu/15",
    name: "James R. — Family Law",
    sub: "After-hours · Intake form sent",
    tag: "Intake Sent",
    tagCls: "bg-pu/15 text-pu",
  },
  {
    bg: "bg-amber-500/12",
    name: "David K. — Criminal Defense",
    sub: "Urgent — Routed to on-call attorney",
    tag: "Escalated",
    tagCls: "bg-amber-500/15 text-amber-600",
  },
  {
    bg: "bg-emerald-500/15",
    name: "Aisha P. — Estate Planning",
    sub: "Qualified · Referred to partner",
    tag: "Referred",
    tagCls: "bg-emerald-500/15 text-emerald-600",
  },
  {
    bg: "bg-emerald-500/15",
    name: "Carlos M. — Immigration",
    sub: "Bilingual (ES) · Booked consultation",
    tag: "Booked",
    tagCls: "bg-emerald-500/15 text-emerald-600",
  },
];

export default function AiReceptionistsClient() {
  const [modalOpen, setModalOpen] = useState(false);
  const open = () => setModalOpen(true);

  return (
    <>
      <ServiceHero
        tag="Service · AI Receptionist"
        title="AI Receptionist For"
        highlight="Law Firms"
        sub="Your firm gets calls at 9 p.m. on a Friday and 7 a.m. on a Sunday. Most of those callers don't leave voicemails — they call the next firm. Our AI receptionist answers every call, qualifies every lead, and books every consultation, around the clock."
        pills={[
          "24/7 Call Answering",
          "Lead Qualification",
          "Consultation Booking",
          "Bilingual Available",
          "CRM Integration",
        ]}
        primaryCta="See A Live Demo"
        onPrimary={open}
      />

      {/* LIVE ACTIVITY VISUAL */}
      <section>
        <div className="mx-auto grid max-w-[1100px] items-center gap-10 px-6 py-16 md:px-10 lg:grid-cols-2">
          <div>
            <span className="mb-3.5 inline-block rounded-full border border-pu/15 bg-pu/8 px-3 py-1 text-[10px] font-bold uppercase tracking-wider text-pu">
              Live Activity
            </span>
            <h2 className="mb-3 text-[clamp(22px,2.8vw,34px)] font-extrabold leading-[1.15] tracking-tight text-navy">
              Every Call{" "}
              <span className="text-pu">Answered. Every Lead Captured.</span>
            </h2>
            <P>
              This is what your firm&apos;s call activity looks like with an AI
              receptionist running. Calls that used to go to voicemail — or
              worse, to a competitor — are now being answered, qualified, and
              booked into your calendar automatically.
            </P>
            <div className="mt-6 grid grid-cols-3 gap-3">
              {[
                { v: "94%", l: "Calls Answered", d: "↑ vs 61% avg" },
                { v: "3.2x", l: "More Consultations", d: "vs voicemail" },
                { v: "67%", l: "After-Hours Calls", d: "Captured" },
              ].map((s) => (
                <div
                  key={s.l}
                  className="rounded-2xl border border-pu/10 bg-white p-4 text-center"
                >
                  <div className="text-[24px] font-extrabold text-pu">
                    {s.v}
                  </div>
                  <div className="mt-1 text-[11px] font-semibold text-navy">
                    {s.l}
                  </div>
                  <div className="mt-0.5 text-[10px] text-slate-400">{s.d}</div>
                </div>
              ))}
            </div>
          </div>
          <div className="rounded-3xl border border-pu/12 bg-white p-5 shadow-[0_16px_48px_rgba(11,21,54,.1)]">
            <div className="mb-4 inline-flex items-center gap-2 rounded-full bg-emerald-500/10 px-3 py-1.5">
              <span className="h-2 w-2 animate-pulse rounded-full bg-emerald-500" />
              <span className="text-[11px] font-bold uppercase tracking-wide text-emerald-600">
                Live Calls Today
              </span>
            </div>
            <div className="flex flex-col gap-2.5">
              {LIVE_CALLS.map((c) => (
                <div
                  key={c.name}
                  className="flex items-center gap-3 rounded-xl border border-pu/8 bg-[#fafaff] p-3"
                >
                  <span
                    className={`flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-xl ${c.bg}`}
                  >
                    <PhoneCall size={15} className="text-navy/70" />
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="truncate text-[12.5px] font-bold text-navy">
                      {c.name}
                    </div>
                    <div className="truncate text-[11px] text-slate-500">
                      {c.sub}
                    </div>
                  </div>
                  <span
                    className={`flex-shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold ${c.tagCls}`}
                  >
                    {c.tag}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <TrustBar
        items={[
          "Answers in under 2 rings",
          "Available 24/7/365",
          "Integrates with Clio, MyCase & more",
          "English & Spanish support",
          "HIPAA-aware handling protocols",
        ]}
      />

      <Section
        tag="The Problem"
        title={
          <>
            Why Law Firms Miss So Many{" "}
            <span className="text-pu">Potential Clients</span>
          </>
        }
        className="border-t-0"
      >
        <P>
          The legal industry has a specific call problem that most other service
          businesses don&apos;t face. Legal matters tend to be urgent. A car
          accident victim isn&apos;t going to wait three days to schedule a
          consultation — they&apos;re calling multiple firms and retaining the
          first one that makes them feel heard.
        </P>
        <BulletList
          items={[
            "The majority of potential clients contact multiple law firms before deciding",
            "Firms that respond within the first few minutes win a significantly higher share",
            "A substantial portion of all legal inquiries happen outside business hours",
            "Most callers who reach voicemail don't leave a message and don't call back",
          ]}
        />
        <P>
          Staffing a human receptionist around the clock is not practical for
          most firms. The cost alone — salaries, benefits, training, turnover —
          makes 24/7 human coverage economically unviable for all but the
          largest practices. An AI receptionist gives small and mid-size firms
          capabilities that previously only large firms could afford.
        </P>
      </Section>

      <Section
        tag="How It Works"
        title={
          <>
            What Our AI Receptionist{" "}
            <span className="text-pu">Actually Does</span>
          </>
        }
      >
        <P>
          This category has a wide range of quality. Some AI receptionist tools
          are little more than glorified voicemail. What we build for law firms
          is a genuine intake system.
        </P>
        <div className="my-7 grid gap-4 sm:grid-cols-2">
          <InfoCard
            icon={<PhoneCall size={18} />}
            title="Answers Every Incoming Call"
          >
            Every call is answered within two rings, any time of day or night.
            The caller hears a professional greeting specific to your firm — not
            a generic recording or menu system.
          </InfoCard>
          <InfoCard
            icon={<ClipboardCheck size={18} />}
            title="Qualifies Leads With Smart Questions"
          >
            The AI asks qualifying questions specific to your practice areas —
            type of matter, jurisdiction, what happened, timeline — and routes
            each caller based on your firm&apos;s criteria.
          </InfoCard>
          <InfoCard
            icon={<CalendarDays size={18} />}
            title="Books Consultations Directly"
          >
            For qualified leads, the AI checks your calendar availability in real
            time and books the consultation directly, with confirmation sent to
            both the caller and your team.
          </InfoCard>
          <InfoCard
            icon={<FileText size={18} />}
            title="Sends Intake Forms Automatically"
          >
            After qualifying a caller, the system sends a customised intake form
            to their phone or email before the consultation — so your attorney
            has context before the first meeting.
          </InfoCard>
          <InfoCard icon={<Zap size={18} />} title="Escalates Urgent Matters">
            When a caller indicates an urgent situation — arrested client, active
            emergency, critical deadline — the system flags the call and routes
            it to the appropriate attorney immediately.
          </InfoCard>
          <InfoCard
            icon={<Globe size={18} />}
            title="Speaks Your Clients' Language"
          >
            Bilingual support in English and Spanish is available. The system
            detects language preference early in the conversation and adapts
            accordingly.
          </InfoCard>
        </div>
      </Section>

      <Section
        tag="Intake Comparison"
        title={
          <>
            Traditional Intake vs{" "}
            <span className="text-pu">AI-Powered Intake</span>
          </>
        }
      >
        <DataTable
          headers={["Scenario", "Traditional Intake", "AI Receptionist"]}
          rows={[
            [
              <strong key="a">Call at 8:30 p.m.</strong>,
              "Voicemail or missed call",
              "Answered, qualified, booked",
            ],
            [
              <strong key="b">Call on Saturday</strong>,
              "No one available",
              "Full intake completed",
            ],
            [
              <strong key="c">High call volume period</strong>,
              "Hold queues, dropped calls",
              "Every call handled simultaneously",
            ],
            [
              <strong key="d">Spanish-speaking caller</strong>,
              "Language barrier delay",
              "Handled in Spanish immediately",
            ],
            [
              <strong key="e">Urgent criminal call at 2 a.m.</strong>,
              "Unanswered or missed",
              "Escalated to on-call attorney",
            ],
            [
              <strong key="f">Consultation scheduling</strong>,
              "Requires back-and-forth calls",
              "Booked in real time on the call",
            ],
          ]}
        />
      </Section>

      <Section
        tag="Integration"
        title={
          <>
            Fits Into Your Existing <span className="text-pu">Workflow</span>
          </>
        }
      >
        <P>
          We integrate directly with the practice management software most law
          firms already use. Call records, qualified leads, and booked
          consultations flow directly into your existing system — not into a
          separate dashboard you have to remember to check.
        </P>
        <div className="my-7 grid gap-3.5 sm:grid-cols-2 lg:grid-cols-3">
          <FeatCard emoji="📋" title="Clio Integration">
            New matters created automatically from qualified calls. No double
            entry.
          </FeatCard>
          <FeatCard emoji="⚖️" title="MyCase">
            Client records and consultation bookings sync directly into MyCase.
          </FeatCard>
          <FeatCard emoji="📁" title="Smokeball">
            Lead data pushed to Smokeball for immediate follow-up workflow.
          </FeatCard>
          <FeatCard emoji="📅" title="Google Calendar">
            Real-time availability checking and booking against your calendar.
          </FeatCard>
          <FeatCard emoji="📊" title="Salesforce & HubSpot">
            Lead qualification data pushed to your CRM for pipeline tracking.
          </FeatCard>
          <FeatCard emoji="💬" title="SMS & Email Alerts">
            Instant notification to attorneys when a hot lead is booked or
            escalated.
          </FeatCard>
        </div>
      </Section>

      <Section
        tag="Practice Areas"
        title={
          <>
            Built For Every <span className="text-pu">Practice Area</span>
          </>
        }
      >
        <P>
          The qualifying questions your AI receptionist asks depend on the type
          of law you practice. We configure the intake flow specifically for
          your practice areas — the AI doesn&apos;t ask a personal injury
          question to a probate caller.
        </P>
        <DarkBox
          title="Practice Area Specific Intake Flows"
          items={[
            <>
              <strong className="text-white">Personal Injury</strong> — Date of
              incident, type of accident, injuries, parties involved, insurance
              status, statute of limitations check
            </>,
            <>
              <strong className="text-white">Family Law</strong> — Type of
              matter, children involved, whether proceedings have started,
              urgency level
            </>,
            <>
              <strong className="text-white">Criminal Defense</strong> — Charges
              or investigation type, jurisdiction, court date, urgency — with
              automatic escalation for imminent hearings
            </>,
            <>
              <strong className="text-white">Business Law</strong> — Business
              type, matter type, timeline, counterparty information
            </>,
            <>
              <strong className="text-white">Immigration</strong> — Matter type,
              current status, deadlines, bilingual intake for Spanish-speaking
              clients
            </>,
            <>
              <strong className="text-white">Wills &amp; Estates</strong> —
              Nature of inquiry, existing documents, urgency based on health
              situation
            </>,
          ]}
        />
      </Section>

      <Section
        tag="What We See"
        title={
          <>
            Common Intake Mistakes{" "}
            <span className="text-pu">Law Firms Make</span>
          </>
        }
      >
        <MistakeList
          items={[
            {
              title: "Relying On Voicemail As A Backup",
              body: "Most callers who reach voicemail don't leave a message and don't call back. Voicemail is not a safety net — it's a lead-loss mechanism disguised as one.",
            },
            {
              title: "No After-Hours Coverage",
              body: "Legal matters are not nine-to-five events. Car accidents, arrests, and family crises happen at all hours. Firms without after-hours coverage lose a disproportionate share of urgent, high-value matters.",
            },
            {
              title: "Intake Forms Completed At The Consultation",
              body: "Having attorneys collect basic intake information during a paid consultation is an inefficient use of everyone's time, and it results in incomplete information if the client doesn't retain.",
            },
            {
              title: "No Qualification Before Booking",
              body: "Booking consultations for matters completely outside your practice areas wastes attorney time. A proper intake system screens for fit before a consultation is ever scheduled.",
            },
            {
              title: "Slow Follow-Up On Web Leads",
              body: "Contact form submissions that sit in an inbox for hours or days lose most of their potential. Speed of response is a measurable factor in consultation conversion.",
            },
          ]}
        />
      </Section>

      <Section
        tag="Our Process"
        title={
          <>
            How We Set Up Your <span className="text-pu">AI Receptionist</span>
          </>
        }
      >
        <ProcessSteps
          steps={[
            {
              title: "Practice Area Mapping",
              body: "We document your practice areas, the matters you take, the geography you serve, and your criteria for a qualified lead versus a referral out. This becomes the foundation of your intake logic.",
            },
            {
              title: "Call Flow Design",
              body: "We design the conversation flow — how the AI greets callers, what questions it asks in what order, how it handles common objections, and how it routes based on matter type and urgency.",
            },
            {
              title: "Integration Setup",
              body: "We connect the system to your practice management software, calendar, and CRM. We configure SMS and email alerts so your team is notified immediately when a qualified lead is captured.",
            },
            {
              title: "Testing and Refinement",
              body: "We run through dozens of call scenarios — different practice areas, urgency levels, difficult callers — before going live, refining until the interaction feels natural and professionally appropriate.",
            },
            {
              title: "Monitoring and Optimisation",
              body: "After launch, we review call recordings and qualification data regularly, adjusting the intake logic — improving accuracy, refining question sequencing, and expanding coverage as your practice evolves.",
            },
          ]}
        />
      </Section>

      <FAQ faqs={FAQS} title="Frequently Asked Questions" />

      <FinalCta
        title="Stop Losing Clients to"
        highlight="Voicemail"
        body="Every unanswered call is a potential client who just called the next firm on the list. Book a strategy call and we'll show you exactly how many calls your firm is missing and what capturing them would be worth."
        primaryCta="See A Live Demo"
        onPrimary={open}
        note="No obligation. No hard sell. Just a real conversation about your firm's intake."
      />

      <StickyCTA
        message="How Many Calls Is Your Firm Missing?"
        ctaText="Get My Missed Call Report"
        onCtaClick={open}
      />
      <LeadFormModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        offer="Free Missed Call Analysis"
        title="How Many Calls Is Your Firm Missing Every Week?"
        description="Tell us about your firm and we'll show you exactly how many potential clients are calling after hours, hitting voicemail, and going to a competitor — and what capturing them would be worth to your practice."
      />
    </>
  );
}
