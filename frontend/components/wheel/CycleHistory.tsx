import { currency } from "@/lib/utils/format";

export function CycleHistory({
  rows
}: {
  rows: Array<{ ticker: string; expiration: string; capital_release: number }>;
}) {
  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">
      <h3 className="text-sm font-semibold text-slate-800 dark:text-slate-200">Capital Release Schedule</h3>
      <div className="mt-3 space-y-2 text-sm">
        {rows.slice(0, 8).map((row) => (
          <div key={`${row.ticker}-${row.expiration}`} className="flex items-center justify-between rounded-lg bg-slate-50 px-3 py-2 dark:bg-slate-800/70">
            <span className="text-slate-700 dark:text-slate-200">
              {row.ticker} — {row.expiration}
            </span>
            <span className="font-medium text-slate-900 dark:text-white">{currency(row.capital_release)}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
