import Link from "next/link";
import Button from "@/components/ui/Button";

export default function NotFound() {
  return (
    <section className="hero-gradient relative flex min-h-[70vh] items-center justify-center overflow-hidden px-6 py-24">
      <div className="grid-bg absolute inset-0 opacity-40" />
      <div className="relative z-10 text-center">
        <p className="text-grad-purple text-[120px] font-black leading-none">
          404
        </p>
        <h1 className="mt-2 text-[28px] font-extrabold text-white">
          Page Not Found
        </h1>
        <p className="mx-auto mt-3 max-w-md text-[15px] text-slate-400">
          The page you&apos;re looking for doesn&apos;t exist or has moved.
          Let&apos;s get you back on track.
        </p>
        <div className="mt-8 flex justify-center gap-3">
          <Button href="/" variant="primary" size="lg">
            Back to Home
          </Button>
          <Link
            href="/services"
            className="inline-flex items-center rounded-full border border-white/20 px-7 py-3.5 text-[15px] font-semibold text-white transition-colors hover:border-pu hover:text-pu3"
          >
            View Services
          </Link>
        </div>
      </div>
    </section>
  );
}
