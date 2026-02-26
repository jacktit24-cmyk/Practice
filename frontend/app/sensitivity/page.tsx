"use client";

import { useMemo, useState } from "react";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

import { currency, percent } from "@/lib/utils/format";

const basePrice = 8.42;
const stockGrid = [170, 180, 190, 200, 210, 220];
const ivGrid = [0.2, 0.3, 0.4];

export default function SensitivityPage() {
  const [selectedIv, setSelectedIv] = useState(0.3);

  const rows = useMemo(
    () =>
      stockGrid.map((spot) => {
        const sensitivity = (spot - 195) * 0.18;
        const ivImpact = (selectedIv - 0.3) * 14;
        const projected = Math.max(0.1, basePrice + sensitivity + ivImpact);
        return {
          spot,
          projected,
          pctChange: ((projected - basePrice) / basePrice) * 100
        };
      }),
    [selectedIv]
  );

  return (
    <section className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-white">Option Sensitivity Engine</h1>
        <p className="mt-1 text-sm text-slate-400">Project option price across stock/volatility scenarios and visualize risk profile.</p>
      </div>

      <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-sm text-slate-300">IV Shift:</span>
          {ivGrid.map((iv) => (
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
        </div>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
          <h3 className="mb-3 text-sm font-medium text-slate-300">Sensitivity Surface (2D slice)</h3>
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
          <div className="grid grid-cols-6 gap-2 text-center text-xs">
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
          <p className="mt-3 text-xs text-slate-400">Break-even reference line: Stock price ≈ $203.40</p>
        </div>
      </div>
    </section>
  );
}
