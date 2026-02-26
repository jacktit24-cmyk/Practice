import type { WheelPosition } from "@/lib/api/client";
import { currency, percent } from "@/lib/utils/format";

const dteBadge = (dte: number) => {
  if (dte <= 7) return "bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-300";
  if (dte <= 30) return "bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-300";
  return "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-300";
};

export function WheelGrid({ rows }: { rows: WheelPosition[] }) {
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900/60">
      <table className="w-full text-left text-sm">
        <thead className="bg-slate-100 text-slate-600 dark:bg-slate-900 dark:text-slate-400">
          <tr>
            {"Ticker,Phase,Strike,Exp,DTE,Premium,Capital,APY,Unreal P/L,Status".split(",").map((col) => (
              <th key={col} className="px-3 py-2 font-medium">{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.id} className="border-t border-slate-200 dark:border-slate-800">
              <td className="px-3 py-2">{row.ticker}</td>
              <td className="px-3 py-2">{row.phase}</td>
              <td className="px-3 py-2">{currency(row.strike)}</td>
              <td className="px-3 py-2">{row.expiration}</td>
              <td className="px-3 py-2">
                <span className={`rounded-full px-2 py-1 text-xs ${dteBadge(row.dte)}`}>{row.dte}</span>
              </td>
              <td className="px-3 py-2">{currency(row.premium_collected * 100 * row.contracts)}</td>
              <td className="px-3 py-2">{currency(row.capital_reserved)}</td>
              <td className="px-3 py-2">{row.apy !== null ? percent(row.apy) : "—"}</td>
              <td className="px-3 py-2">{currency(row.unrealized_pl)}</td>
              <td className="px-3 py-2">{row.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
