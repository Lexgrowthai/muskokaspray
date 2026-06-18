import { MessageSquare, Zap, Clock, TrendingUp, Shield, Users, Bot, PhoneCall } from "lucide-react";
import Tag from "@/components/ui/Tag";
import Button from "@/components/ui/Button";
import FAQ from "@/components/sections/FAQ";
import SchemaScript from "@/components/schema/SchemaScript";
import { generatePageMetadata } from "@/lib/metadata";
import { serviceSchema, breadcrumbSchema, faqSchema, SITE_URL } from "@/lib/schema";

const NAME = "AI Chatbots for Law Firms";
const DESCRIPTION =
  "Turn website visitors into booked consultations 24/7. LexScale deploys intelligent AI chat assistants trained on your practice areas to qualify leads, answer questions, and schedule appointments automatically.";

export const metadata = generatePageMetadata({
  title: NAME,
  description: DESCRIPTION,
  slug: "services/ai-chatbots",
});

const steps = [
  {
    title: "Practice Area Training",
    desc: "We train your AI chatbot on your specific practice areas, common client questions, intake criteria, and firm policies — so it responds with accuracy and authority.",
  },
  {
    title: "Conversation Flow Design",
    desc: "We build structured conversation flows that guide visitors from their first question to a booked consultation, capturing all the information your intake team needs.",
  },
  {
    title: "Website Integration",
    desc: "Your AI chatbot is deployed seamlessly on your website — branded to match your firm, launching at the right moment to maximize engagement without being intrusive.",
  },
  {
    title: "CRM & Calendar Connection",
    desc: "We connect your chatbot to your scheduling system and CRM so leads are captured, qualified, and booked automatically — no manual follow-up required.",
  },
  {
    title: "Monitoring & Optimization",
    desc: "We review conversation logs, identify drop-off points, and continuously refine responses to improve conversion rates and lead quality over time.",
  },
];

const benefits = [
  {
    icon: Clock,
    title: "24/7 Lead Capture",
    desc: "Most legal inquiries happen outside business hours. Your AI chatbot never sleeps — capturing and qualifying leads at 2am just as effectively as 2pm.",
  },
  {
    icon: Zap,
    title: "Instant Response",
    desc: "Respond to every visitor in under 8 seconds. Speed is a competitive advantage — the firm that responds first wins the client most of the time.",
  },
  {
    icon: TrendingUp,
    title: "Higher Conversion Rates",
    desc: "Websites with AI chat convert significantly more visitors into leads than contact forms alone. Conversation creates commitment.",
  },
  {
    icon: Shield,
    title: "Pre-Qualified Leads",
    desc: "Your chatbot filters out off-topic inquiries and collects key intake information — so your team only spends time on genuinely qualified prospects.",
  },
];

const faqs = [
  {
    question: "Will the AI chatbot give legal advice?",
    answer:
      "No — your AI chatbot is configured to provide information about your firm and practice areas, guide visitors toward booking a consultation, and answer common procedural questions. It does not provide legal advice, and all responses include appropriate disclaimers.",
  },
  {
    question: "How long does setup take?",
    answer:
      "Most law firm chatbot deployments are live within 7–14 days. This includes training on your practice areas, conversation flow design, website integration, and testing.",
  },
  {
    question: "Can the chatbot book appointments directly?",
    answer:
      "Yes. We integrate with Calendly, Clio, and other scheduling platforms so your chatbot can show available times and book consultations directly in the conversation.",
  },
  {
    question: "What happens to the leads the chatbot captures?",
    answer:
      "All leads are sent to your CRM, email, or dashboard in real time. You receive an immediate notification with the contact details and conversation summary for every qualified lead.",
  },
  {
    question: "Will it work on mobile?",
    answer:
      "Absolutely. Your AI chatbot is fully responsive and optimized for mobile users — who represent the majority of legal website visitors.",
  },
];

export default function AiChatbotsPage() {
  return (
    <>
      <SchemaScript
        schema={serviceSchema(NAME, DESCRIPTION, `${SITE_URL}/services/ai-chatbots`)}
      />
      <SchemaScript
        schema={breadcrumbSchema([
          { name: "Home", url: SITE_URL },
          { name: "Services", url: `${SITE_URL}/services` },
          { name: NAME, url: `${SITE_URL}/services/ai-chatbots` },
        ])}
      />
      <SchemaScript schema={faqSchema(faqs)} />

      {/* Hero */}
      <section className="hero-gradient py-24 px-6 text-center relative overflow-hidden">
        <div className="grid-bg absolute inset-0" />
        <div className="relative z-10 max-width mx-auto max-w-3xl">
          <Tag variant="purple" className="mb-5">
            AI Chatbots for Law Firms
          </Tag>
          <h1 className="text-4xl md:text-6xl font-black text-white leading-tight tracking-tight mb-5">
            Convert More Visitors Into{" "}
            <span className="text-grad-purple">Booked Consultations</span>
          </h1>
          <p className="text-lg text-white/60 leading-relaxed mb-8 max-w-2xl mx-auto">
            {DESCRIPTION}
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <Button href="/tools/ai-visibility-checker" variant="primary" size="lg">
              Get a Free Demo
            </Button>
            <Button href="/services" variant="outline" size="lg">
              All Services
            </Button>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-14 px-6 bg-navy border-b border-white/5">
        <div className="max-w-4xl mx-auto grid grid-cols-3 gap-8 text-center">
          {[
            { val: "3.8x", label: "More Leads vs Contact Form" },
            { val: "<8s", label: "Average Response Time" },
            { val: "71%", label: "After-Hours Engagement" },
          ].map((s) => (
            <div key={s.label}>
              <div className="text-4xl font-black text-grad-purple mb-1">{s.val}</div>
              <div className="text-sm text-white/40 uppercase tracking-wide font-semibold">{s.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* What We Do */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-14">
            <Tag variant="purple" className="mb-4">What We Build</Tag>
            <h2 className="text-3xl md:text-4xl font-black text-navy tracking-tight mb-4">
              Intelligent Chatbots Built for <span className="text-purple">Law Firms</span>
            </h2>
            <p className="text-lg text-slate-500 max-w-2xl mx-auto">
              Not a generic widget. A purpose-built AI assistant trained on legal intake, your practice areas, and your firm&apos;s specific needs.
            </p>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            {benefits.map((b) => (
              <div key={b.title} className="card p-7 flex gap-5">
                <div className="w-12 h-12 rounded-xl bg-purple/10 flex items-center justify-center flex-shrink-0">
                  <b.icon className="w-6 h-6 text-purple" />
                </div>
                <div>
                  <h3 className="text-base font-bold text-navy mb-2">{b.title}</h3>
                  <p className="text-sm text-slate-500 leading-relaxed">{b.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 px-6 bg-slate-50">
        <div className="max-w-3xl mx-auto">
          <div className="text-center mb-14">
            <Tag variant="purple" className="mb-4">The Process</Tag>
            <h2 className="text-3xl font-black text-navy tracking-tight">
              How It Works
            </h2>
          </div>
          <div className="flex flex-col gap-8">
            {steps.map((step, i) => (
              <div key={step.title} className="flex gap-6 items-start">
                <div className="w-10 h-10 rounded-full bg-purple flex items-center justify-center text-white font-black text-sm flex-shrink-0 mt-1">
                  {i + 1}
                </div>
                <div>
                  <h3 className="text-base font-bold text-navy mb-1">{step.title}</h3>
                  <p className="text-sm text-slate-500 leading-relaxed">{step.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Practice Areas */}
      <section className="py-20 px-6 bg-navy">
        <div className="max-w-5xl mx-auto text-center">
          <Tag variant="gold" className="mb-4">Practice Areas</Tag>
          <h2 className="text-3xl font-black text-white tracking-tight mb-4">
            Trained for Every <span className="text-gold">Practice Area</span>
          </h2>
          <p className="text-white/60 mb-10 max-w-2xl mx-auto">
            We build practice-area-specific conversation flows so your chatbot asks the right intake questions for every type of legal matter.
          </p>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              "Family Law", "Personal Injury", "Criminal Defence", "Immigration",
              "Business Law", "Real Estate", "Estate Planning", "Employment Law",
            ].map((area) => (
              <div key={area} className="bg-white/5 border border-white/10 rounded-xl py-4 px-5 text-sm font-semibold text-white/80">
                {area}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-3xl mx-auto">
          <div className="text-center mb-12">
            <Tag variant="purple" className="mb-4">FAQ</Tag>
            <h2 className="text-3xl font-black text-navy tracking-tight">Common Questions</h2>
          </div>
          <FAQ faqs={faqs} />
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-6 hero-gradient">
        <div className="max-w-2xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-black text-white tracking-tight mb-4">
            Ready to Convert More Visitors?
          </h2>
          <p className="text-white/55 mb-8 text-lg">
            See how an AI chatbot can transform your firm&apos;s website into a 24/7 lead generation system.
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <Button href="/tools/ai-visibility-checker" variant="primary" size="lg">
              Get a Free Demo →
            </Button>
            <Button href="/case-studies" variant="outline" size="lg">
              See Client Results
            </Button>
          </div>
        </div>
      </section>
    </>
  );
}
