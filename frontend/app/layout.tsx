import "./globals.css";
import type { Metadata } from "next";

import { TopNav } from "@/components/TopNav";

export const metadata: Metadata = {
  title: "OptionsLab",
  description: "Advanced Options Dashboard & Sensitivity Engine"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body>
        <TopNav />
        <main className="mx-auto max-w-7xl px-6 py-8">{children}</main>
      </body>
    </html>
  );
}
