"use client";

import { useEffect, useMemo, useState } from "react";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

import { fetchSensitivity, type SensitivityRequest } from "@/lib/api/client";
import { currency, percent } from "@/lib/utils/format";

const defaultRequest: SensitivityRequest = {
  ticker: "AAPL",
  option_type: "CALL",
  strike: 200,
  expiration_days: 45,
  implied_volatility: 0.35,
  current_stock_price: 195,
  stock_price_scenarios: [170, 180, 190, 200, 210, 220],
  volatility_scenarios: [0.2, 0.3, 0.4],
  time_horizon_days: [15, 30, 45],
  risk_free_rate: 0.05
};

export default function SensitivityPage() {
  const [request, setRequest] = useState<SensitivityRequest>(defaultRequest);
  const [selectedIv, setSelectedIv] = useState(0.3);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [basePrice, setBasePrice] = useState<number>(0);
  const [rows, setRows] = useState<Array<{ spot: number; projected: number; pctChange: number }>>([]);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      setLoading(true);
      setError(null);
      try {
        const payload = {
          ...request,
          volatility_scenarios: [selectedIv]
        };
        const response = await fetchSensitivity(payload);

        if (cancelled) return;

        setBasePrice(response.base_price);

        const slice = response.scenarios
          .sort((a, b) => a.spot - b.spot)
          .map((scenario) => ({
            spot: scenario.spot,
            projected: scenario.price,
            pctChange: scenario.pct_change_vs_base
          }));

        const deduped = Object.values(
          slice.reduce<Record<number, { spot: number; projected: number; pctChange: number }>>((acc, row) => {
            acc[row.spot] = row;
            return acc;
          }, {})
        );

        setRows(deduped);
      } catch (apiError) {
        if (!cancelled) {
          setError(apiError instanceof Error ? apiError.message : "Unknown API error");
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    void load();

    return () => {
      cancelled = true;
    };
  }, [request, selectedIv]);

  const breakEven = useMemo(() => {
    if (!rows.length) return 0;
    const positive = rows.find((row) => row.projected > basePrice);
    return positive?.spot ?? rows[rows.length - 1].spot;
  }, [rows, basePrice]);

  return (
    <section className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-white">Option Sensitivity Engine</h1>
        <p className="mt-1 text-sm text-slate-400">Live backend integration for scenario pricing and Greeks-driven repricing.</p>
      </div>

      <div className="grid gap-4 rounded-2xl border border-slate-800 bg-slate-900/60 p-4 md:grid-cols-5">
        <label className="text-sm text-slate-300">
          Ticker
          <input
            value={request.ticker}
            onChange={(event) => setRequest((prev) => ({ ...prev, ticker: event.target.value.toUpperCase() }))}
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-950 px-2 py-1"
          />
        </label>
        <label className="text-sm text-slate-300">
          Type
          <select
            value={request.option_type}
            onChange={(event) => setRequest((prev) => ({ ...prev, option_type: event.target.value as "CALL" | "PUT" }))}
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-950 px-2 py-1"
          >
            <option value="CALL">CALL</option>
            <option value="PUT">PUT</option>
          </select>
        </label>
        <label className="text-sm text-slate-300">
          Strike
          <input
            type="number"
            value={request.strike}
            onChange={(event) => setRequest((prev) => ({ ...prev, strike: Number(event.target.value) }))}
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-950 px-2 py-1"
          />
        </label>
        <label className="text-sm text-slate-300">
          Spot
          <input
            type="number"
            value={request.current_stock_price}
            onChange={(event) => setRequest((prev) => ({ ...prev, current_stock_price: Number(event.target.value) }))}
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-950 px-2 py-1"
          />
        </label>
        <label className="text-sm text-slate-300">
          DTE
          <input
            type="number"
            value={request.expiration_days}
            onChange={(event) => setRequest((prev) => ({ ...prev, expiration_days: Number(event.target.value) }))}
            className="mt-1 w-full rounded-md border border-slate-700 bg-slate-950 px-2 py-1"
          />
        </label>
      </div>

      <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-sm text-slate-300">IV Shift:</span>
          {[0.2, 0.3, 0.4].map((iv) => (
            <button
              key={iv}
              type="button"
              onClick={() => setSelectedIv(iv)}
              className={`rounded-lg px-3 py-1 text-sm transition ${
                selectedIv === iv ? "bg-indigo-500/30 text-indigo-100" : "bg-slate-800 text-slate-300"
              }`}
            >
              {(iv * 100).toFixed(0)}%
            </button>
          ))}
          <span className="ml-auto text-sm text-slate-300">Base: {currency(basePrice)}</span>
        </div>
      </div>

      {error ? <p className="rounded-lg border border-loss/40 bg-loss/10 p-3 text-sm text-loss">{error}</p> : null}
      {loading ? <p className="text-sm text-slate-400">Loading scenarios…</p> : null}

      <div className="grid gap-4 lg:grid-cols-2">
        <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
          <h3 className="mb-3 text-sm font-medium text-slate-300">Sensitivity Surface (stock slice)</h3>
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={rows}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                <XAxis dataKey="spot" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip formatter={(value: number) => currency(value)} />
                <Legend />
                <Line type="monotone" dataKey="projected" stroke="#22c55e" strokeWidth={2} dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
          <h3 className="mb-3 text-sm font-medium text-slate-300">Heatmap Grid</h3>
          <div className="grid grid-cols-3 gap-2 text-center text-xs md:grid-cols-6">
            {rows.map((row) => {
              const intensity = Math.min(1, Math.abs(row.pctChange) / 40);
              const positive = row.pctChange >= 0;
              return (
                <div
                  key={row.spot}
                  className="rounded-lg border border-slate-800 p-3"
                  style={{
                    backgroundColor: positive
                      ? `rgba(34,197,94,${0.15 + intensity * 0.45})`
                      : `rgba(239,68,68,${0.15 + intensity * 0.45})`
                  }}
                >
                  <p className="text-slate-100">${row.spot}</p>
                  <p className="mt-1 text-slate-200">{currency(row.projected)}</p>
                  <p className={`mt-1 ${positive ? "text-gain" : "text-loss"}`}>{percent(row.pctChange)}</p>
                </div>
              );
            })}
          </div>
          <p className="mt-3 text-xs text-slate-400">Break-even visual line: Spot ≈ ${breakEven.toFixed(2)}</p>
        </div>
      </div>
    </section>
  );
}
