import { HTMLAttributes, ReactNode } from "react";

type CardVariant = "default" | "dark" | "gold";

const variants: Record<CardVariant, string> = {
  default:
    "bg-white border border-pu/10 shadow-[0_6px_28px_rgba(11,21,54,.08)]",
  dark: "bg-gradient-to-br from-navy to-[#162050] border border-pu/25 text-white",
  gold: "bg-gradient-to-br from-[#1a0808] to-[#2a1505] border border-gold/25 text-white",
};

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  variant?: CardVariant;
  hover?: boolean;
}

export default function Card({
  children,
  variant = "default",
  hover = true,
  className = "",
  ...rest
}: CardProps) {
  return (
    <div
      className={`rounded-2xl p-6 transition-all duration-300 ${
        variants[variant]
      } ${
        hover
          ? "hover:-translate-y-1 hover:shadow-[0_20px_56px_rgba(106,92,255,.13)]"
          : ""
      } ${className}`}
      {...rest}
    >
      {children}
    </div>
  );
}
