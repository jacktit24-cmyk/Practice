import { getDueBadgeClass } from "../domain/status";

export function DueBadge({ daysLeft }: { daysLeft: number }) {
  const label = daysLeft < 0 ? "OVERDUE" : daysLeft === 0 ? "Due Today" : `${daysLeft}d left`;
  return <span className={`badge ${getDueBadgeClass(daysLeft)}`}>{label}</span>;
}

export function BoolBadge({ value, label }: { value: boolean | null; label: string }) {
  const cls = value === true ? "bool-yes" : value === false ? "bool-no" : "bool-na";
  const txt = value === true ? "Yes" : value === false ? "No" : "—";
  return <span className={`status-pill ${cls}`}>{label}: {txt}</span>;
}
