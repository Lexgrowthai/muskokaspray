"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import * as Icons from "lucide-react";
import { ChevronDown, Menu, X } from "lucide-react";
import { NAV_ITEMS, NavDropdownItem } from "@/lib/navigation";

function DropIcon({ name }: { name?: string }) {
  if (!name) return null;
  const Ico = (Icons as unknown as Record<string, React.ComponentType<{ size?: number; className?: string }>>)[name];
  if (!Ico) return null;
  return <Ico size={16} className="text-pu" />;
}

function DropdownItem({ item }: { item: NavDropdownItem }) {
  return (
    <Link
      href={item.href}
      className="flex items-start gap-3 rounded-[10px] p-2.5 transition-colors hover:bg-pu/[0.07]"
    >
      <span className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg bg-pu/10">
        <DropIcon name={item.iconName} />
      </span>
      <span>
        <span className="block text-[12.5px] font-semibold text-navy">
          {item.label}
        </span>
        <span className="mt-0.5 block text-[11px] text-slate-400">
          {item.description}
        </span>
      </span>
    </Link>
  );
}

export default function Nav() {
  const pathname = usePathname();
  const [mobileOpen, setMobileOpen] = useState(false);

  const isActive = (href?: string) =>
    href && (href === "/" ? pathname === "/" : pathname.startsWith(href));

  return (
    <nav className="sticky top-0 z-[100] flex items-center justify-between border-b border-pu/[0.09] bg-white/[0.93] px-5 py-4 backdrop-blur-xl md:px-10">
      <Link href="/" className="text-[19px] font-extrabold tracking-[-0.4px] text-navy">
        Lex<span className="text-pu">Scale</span>.ai
      </Link>

      <ul className="hidden items-center gap-6 lg:flex">
        {NAV_ITEMS.map((item) => (
          <li key={item.label} className="group relative">
            {item.dropdown ? (
              <>
                <span className="flex cursor-pointer items-center gap-1 text-[13px] font-medium text-slate-600 transition-colors group-hover:text-pu">
                  {item.label}
                  <ChevronDown
                    size={14}
                    className="opacity-50 transition-transform group-hover:rotate-180"
                  />
                </span>
                <div
                  className={`invisible absolute left-1/2 top-full -translate-x-1/2 rounded-2xl border border-pu/[0.12] bg-white p-2 opacity-0 shadow-[0_16px_48px_rgba(11,21,54,.12)] transition-all duration-200 group-hover:visible group-hover:opacity-100 ${
                    item.columns === 2
                      ? "grid w-[560px] grid-cols-2 gap-1"
                      : "w-[300px]"
                  }`}
                >
                  {item.dropdown.map((d) => (
                    <DropdownItem key={d.label + d.href} item={d} />
                  ))}
                </div>
              </>
            ) : (
              <Link
                href={item.href!}
                className={`text-[13px] font-medium transition-colors hover:text-pu ${
                  isActive(item.href) ? "text-pu" : "text-slate-600"
                }`}
              >
                {item.label}
              </Link>
            )}
          </li>
        ))}
      </ul>

      <div className="hidden lg:block">
        <Link
          href="/tools/ai-visibility-checker"
          className="rounded-full bg-pu px-5 py-2.5 text-[13px] font-semibold text-white transition-all hover:-translate-y-0.5 hover:bg-[#5848e8]"
        >
          Get a Free Strategy Call
        </Link>
      </div>

      <button
        aria-label="Toggle menu"
        className="lg:hidden"
        onClick={() => setMobileOpen((o) => !o)}
      >
        {mobileOpen ? <X size={24} /> : <Menu size={24} />}
      </button>

      {mobileOpen && (
        <div className="fixed inset-0 top-[61px] z-[99] overflow-y-auto bg-white px-6 py-6 lg:hidden">
          <ul className="flex flex-col gap-1">
            {NAV_ITEMS.map((item) => (
              <li key={item.label} className="border-b border-pu/[0.07] py-2">
                {item.dropdown ? (
                  <details>
                    <summary className="flex cursor-pointer list-none items-center justify-between py-2 text-[15px] font-semibold text-navy">
                      {item.label}
                      <ChevronDown size={16} />
                    </summary>
                    <div className="flex flex-col gap-1 py-2 pl-2">
                      {item.dropdown.map((d) => (
                        <Link
                          key={d.label + d.href}
                          href={d.href}
                          onClick={() => setMobileOpen(false)}
                          className="py-1.5 text-[13px] text-slate-600"
                        >
                          {d.label}
                        </Link>
                      ))}
                    </div>
                  </details>
                ) : (
                  <Link
                    href={item.href!}
                    onClick={() => setMobileOpen(false)}
                    className="block py-2 text-[15px] font-semibold text-navy"
                  >
                    {item.label}
                  </Link>
                )}
              </li>
            ))}
          </ul>
          <Link
            href="/tools/ai-visibility-checker"
            onClick={() => setMobileOpen(false)}
            className="mt-6 block rounded-full bg-pu px-5 py-3 text-center text-[14px] font-semibold text-white"
          >
            Get a Free Strategy Call
          </Link>
        </div>
      )}
    </nav>
  );
}
