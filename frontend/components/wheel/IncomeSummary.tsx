import { currency, percent } from "@/lib/utils/format";

export function IncomeSummary({
  summary
}: {
  summary: {
    total_premium_open: number;
    total_premium_mtd: number;
    total_premium_ytd: number;
    weighted_apy_csp: number;
    capital_deployed_csp: number;
    capital_at_risk_cc: number;
    next_expiration_alerts: number;
  };
}) {
  const cards = [
    ["Premium Open", currency(summary.total_premium_open)],
    ["Premium MTD", currency(summary.total_premium_mtd)],
    ["Premium YTD", currency(summary.total_premium_ytd)],
    ["Weighted CSP APY", percent(summary.weighted_apy_csp)],
    ["CSP Capital Deployed", currency(summary.capital_deployed_csp)],
    ["CC Capital at Risk", currency(summary.capital_at_risk_cc)],
    ["Expiring ≤ 7d", String(summary.next_expiration_alerts)]
  ];

  return (
    <div className="grid gap-3 md:grid-cols-3 lg:grid-cols-4">
      {cards.map(([label, value]) => (
        <article key={label} className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">
          <p className="text-xs text-slate-500 dark:text-slate-400">{label}</p>
          <p className="mt-2 text-lg font-semibold text-slate-900 dark:text-white">{value}</p>
        </article>
      ))}
    </div>
  );
}
