import { currency, percent, signedClass } from "@/lib/utils/format";

interface SummaryCardProps {
  title: string;
  value: number;
  percentValue?: number;
}

export function SummaryCard({ title, value, percentValue }: SummaryCardProps) {
  return (
    <article className="rounded-2xl border border-slate-800 bg-gradient-to-br from-slate-900 to-slate-950 p-5 shadow-lg shadow-black/20 transition hover:-translate-y-0.5">
      <p className="text-sm text-slate-400">{title}</p>
      <p className={`mt-2 text-2xl font-semibold ${signedClass(value)}`}>{currency(value)}</p>
      {typeof percentValue === "number" ? <p className={`mt-1 text-sm ${signedClass(percentValue)}`}>{percent(percentValue)}</p> : null}
    </article>
  );
}
