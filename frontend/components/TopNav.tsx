"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import { ThemeToggle } from "@/components/ThemeToggle";

const tabs = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/sensitivity", label: "Sensitivity" },
  { href: "/projection", label: "Projection" },
  { href: "/wheel", label: "Wheel Strategy" }
];

export function TopNav() {
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-10 border-b border-slate-200/80 bg-white/90 backdrop-blur dark:border-slate-800/80 dark:bg-slate-950/90">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <Link href="/dashboard" className="text-lg font-semibold tracking-tight text-slate-900 dark:text-white">
          OptionsLab
        </Link>
        <div className="flex items-center gap-3">
          <nav className="flex gap-2 rounded-xl bg-slate-100 p-1 dark:bg-slate-900">
            {tabs.map((tab) => {
              const active = pathname.startsWith(tab.href);
              return (
                <Link
                  key={tab.href}
                  href={tab.href}
                  className={`rounded-lg px-4 py-2 text-sm transition ${
                    active
                      ? "bg-indigo-500/20 text-indigo-700 dark:bg-indigo-500/30 dark:text-indigo-100"
                      : "text-slate-700 hover:bg-slate-200 dark:text-slate-300 dark:hover:bg-slate-800"
                  }`}
                >
                  {tab.label}
                </Link>
              );
            })}
          </nav>
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
