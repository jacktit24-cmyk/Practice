import type { ReactNode } from "react";
import { PromptCenter } from "../components/PromptCenter";

export function TopBar({ title, actions }: { title: string; actions?: ReactNode }) {
  return (
    <header className="topbar">
      <div>
        <h2>{title}</h2>
      </div>
      <div className="row-gap">
        {actions}
        <PromptCenter />
      </div>
    </header>
  );
}
