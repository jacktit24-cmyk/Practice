"use client";

import { useEffect, useState, type FormEvent } from "react";

import { createWheelPosition, fetchWheelDashboard, type WheelDashboard } from "@/lib/api/client";
import { CycleHistory } from "@/components/wheel/CycleHistory";
import { DTEAlerts } from "@/components/wheel/DTEAlerts";
import { IncomeSummary } from "@/components/wheel/IncomeSummary";
import { PayoffChart } from "@/components/wheel/PayoffChart";
import { WheelGrid } from "@/components/wheel/WheelGrid";

const initialForm = {
  ticker: "AAPL",
  phase: "CSP" as "CSP" | "CC",
  contracts: 1,
  strike: 170,
  expiration: "2026-03-20",
  premium_collected: 2.1,
  current_option_value: 1.4,
  opened_dte: 45,
  status: "Open",
  stock_cost_basis: 170,
  linked_cycle_id: null as string | null
};

export default function WheelPage() {
  const [dashboard, setDashboard] = useState<WheelDashboard | null>(null);
  const [form, setForm] = useState(initialForm);
  const [error, setError] = useState<string | null>(null);

  const load = async () => {
    try {
      const response = await fetchWheelDashboard();
      setDashboard(response);
      setError(null);
    } catch (requestError) {
      setError(requestError instanceof Error ? requestError.message : "Failed to load wheel dashboard");
    }
  };

  useEffect(() => {
    void load();
    const interval = setInterval(load, 300000);
    return () => clearInterval(interval);
  }, []);

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    await createWheelPosition(form);
    setForm(initialForm);
    await load();
  };

  if (!dashboard) {
    return <section className="rounded-xl border border-slate-200 bg-white p-5 dark:border-slate-800 dark:bg-slate-900/60">Loading wheel strategy dashboard…</section>;
  }

  return (
    <section className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">Wheel Strategy Command Center</h1>
        <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">Income-focused CSP/CC tracking, DTE risk, and capital release planning.</p>
      </div>

      {error ? <p className="rounded-lg border border-red-300 bg-red-50 p-3 text-sm text-red-700 dark:border-red-800 dark:bg-red-900/20 dark:text-red-300">{error}</p> : null}

      <IncomeSummary summary={dashboard.summary} />

      <form onSubmit={submit} className="grid gap-3 rounded-2xl border border-slate-200 bg-white p-4 md:grid-cols-4 dark:border-slate-800 dark:bg-slate-900/60">
        <input className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.ticker} onChange={(event) => setForm((prev) => ({ ...prev, ticker: event.target.value.toUpperCase() }))} placeholder="Ticker" />
        <select className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.phase} onChange={(event) => setForm((prev) => ({ ...prev, phase: event.target.value as "CSP" | "CC" }))}>
          <option value="CSP">CSP</option>
          <option value="CC">CC</option>
        </select>
        <input type="number" className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.strike} onChange={(event) => setForm((prev) => ({ ...prev, strike: Number(event.target.value) }))} placeholder="Strike" />
        <input type="date" className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.expiration} onChange={(event) => setForm((prev) => ({ ...prev, expiration: event.target.value }))} />
        <input type="number" step="0.01" className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.premium_collected} onChange={(event) => setForm((prev) => ({ ...prev, premium_collected: Number(event.target.value) }))} placeholder="Premium" />
        <input type="number" step="0.01" className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.current_option_value} onChange={(event) => setForm((prev) => ({ ...prev, current_option_value: Number(event.target.value) }))} placeholder="Current Value" />
        <input type="number" className="rounded border border-slate-300 bg-white px-2 py-1 dark:border-slate-700 dark:bg-slate-950" value={form.contracts} onChange={(event) => setForm((prev) => ({ ...prev, contracts: Number(event.target.value) }))} placeholder="Contracts" />
        <button type="submit" className="rounded bg-indigo-600 px-4 py-2 text-white">Add Position</button>
      </form>

      <WheelGrid rows={dashboard.positions} />

      <div className="grid gap-4 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <PayoffChart positions={dashboard.positions} />
        </div>
        <DTEAlerts alerts={dashboard.dte_alerts} />
      </div>

      <CycleHistory rows={dashboard.capital_release_schedule} />
    </section>
  );
}
