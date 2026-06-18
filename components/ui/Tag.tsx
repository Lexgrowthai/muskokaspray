import { ReactNode } from "react";

type TagVariant = "purple" | "gold" | "blue" | "green";

const variants: Record<TagVariant, string> = {
  purple: "bg-pu/8 border-pu/20 text-pu",
  gold: "bg-gold/8 border-gold/25 text-gold3",
  blue: "bg-blue-500/8 border-blue-500/20 text-blue-600",
  green: "bg-emerald-500/8 border-emerald-500/20 text-emerald-600",
};

interface TagProps {
  children: ReactNode;
  variant?: TagVariant;
  className?: string;
}

export default function Tag({
  children,
  variant = "purple",
  className = "",
}: TagProps) {
  return (
    <span
      className={`inline-flex items-center gap-2 rounded-full border px-3.5 py-1.5 text-[11px] font-bold uppercase tracking-[0.8px] ${variants[variant]} ${className}`}
    >
      {children}
    </span>
  );
}
