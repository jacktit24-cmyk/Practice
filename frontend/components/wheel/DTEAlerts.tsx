import type { WheelPosition } from "@/lib/api/client";

export function DTEAlerts({ alerts }: { alerts: WheelPosition[] }) {
  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">
      <h3 className="text-sm font-semibold text-slate-800 dark:text-slate-200">DTE Alerts (≤ 7 days)</h3>
      <ul className="mt-3 space-y-2 text-sm">
        {alerts.length ? (
          alerts.map((alert) => (
            <li key={alert.id} className="rounded-lg bg-red-50 px-3 py-2 text-red-700 dark:bg-red-900/20 dark:text-red-300">
              {alert.ticker} {alert.phase} expires in {alert.dte} days — action needed.
            </li>
          ))
        ) : (
          <li className="text-slate-500 dark:text-slate-400">No urgent expirations.</li>
        )}
      </ul>
    </section>
  );
}
