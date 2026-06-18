import Link from "next/link";
import {
  AnchorHTMLAttributes,
  ButtonHTMLAttributes,
  ReactNode,
} from "react";

type Variant = "primary" | "gold" | "outline" | "ghost";
type Size = "sm" | "md" | "lg";

const variantClasses: Record<Variant, string> = {
  primary:
    "text-white bg-gradient-to-br from-pu to-pu2 shadow-[0_4px_20px_rgba(106,92,255,.35)] hover:shadow-[0_10px_32px_rgba(106,92,255,.5)] hover:-translate-y-0.5",
  gold:
    "text-navy bg-gradient-to-br from-gold3 to-gold2 shadow-[0_4px_20px_rgba(212,175,55,.3)] hover:shadow-[0_10px_32px_rgba(212,175,55,.45)] hover:-translate-y-0.5",
  outline:
    "bg-transparent text-navy border-[1.5px] border-navy/20 hover:border-pu hover:text-pu hover:-translate-y-0.5",
  ghost: "bg-transparent text-pu hover:bg-pu/8",
};

const sizeClasses: Record<Size, string> = {
  sm: "px-4 py-2 text-[13px]",
  md: "px-6 py-3 text-[14px]",
  lg: "px-7 py-3.5 text-[15px]",
};

interface BaseProps {
  variant?: Variant;
  size?: Size;
  children: ReactNode;
  className?: string;
}

type ButtonAsButton = BaseProps &
  Omit<ButtonHTMLAttributes<HTMLButtonElement>, keyof BaseProps> & {
    href?: undefined;
  };

type ButtonAsLink = BaseProps &
  Omit<AnchorHTMLAttributes<HTMLAnchorElement>, keyof BaseProps> & {
    href: string;
  };

type ButtonProps = ButtonAsButton | ButtonAsLink;

export default function Button(props: ButtonProps) {
  const {
    variant = "primary",
    size = "md",
    children,
    className = "",
    ...rest
  } = props;

  const classes = `inline-flex items-center justify-center gap-2 rounded-full font-bold cursor-pointer transition-all duration-200 ${variantClasses[variant]} ${sizeClasses[size]} ${className}`;

  if ("href" in props && props.href) {
    const { href, ...anchorRest } =
      rest as AnchorHTMLAttributes<HTMLAnchorElement>;
    return (
      <Link href={props.href} className={classes} {...anchorRest}>
        {children}
      </Link>
    );
  }

  return (
    <button
      className={classes}
      {...(rest as ButtonHTMLAttributes<HTMLButtonElement>)}
    >
      {children}
    </button>
  );
}
