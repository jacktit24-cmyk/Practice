"use client";

import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

import { samplePositions } from "@/lib/mock/positions";
import { toAnalytics } from "@/lib/utils/analytics";
import { currency, percent, signedClass } from "@/lib/utils/format";

const scenarios = [
  { name: "Base", stockShift: 0, volShift: 0, days: 0, multiplier: 1 },
  { name: "Bull +10%", stockShift: 10, volShift: -5, days: 30, multiplier: 1.16 },
  { name: "Stress -12%", stockShift: -12, volShift: 9, days: 30, multiplier: 0.78 }
];

export default function ProjectionPage() {
  const analytics = toAnalytics(samplePositions);
  const baseValue = analytics.reduce((sum, row) => sum + row.marketValue, 0);

  const scenarioValues = scenarios.map((scenario) => ({
    ...scenario,
    projectedValue: baseValue * scenario.multiplier,
    netPl: baseValue * scenario.multiplier - baseValue,
    returnPct: (scenario.multiplier - 1) * 100
  }));

  const weightedDelta =
    analytics.reduce((sum, row) => sum + row.deltaEstimate * row.marketValue, 0) /
    analytics.reduce((sum, row) => sum + row.marketValue, 0);

  return (
    <section className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-white">Portfolio Projection Simulator</h1>
        <p className="mt-1 text-sm text-slate-400">Compare portfolio outcomes under configurable forward scenarios.</p>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        <article className="rounded-2xl border border-slate-800 bg-slate-900/60 p-5">
          <p className="text-sm text-slate-400">Before Value</p>
          <p className="mt-2 text-2xl font-semibold text-white">{currency(baseValue)}</p>
        </article>
        <article className="rounded-2xl border border-slate-800 bg-slate-900/60 p-5">
          <p className="text-sm text-slate-400">After (Bull)</p>
          <p className="mt-2 text-2xl font-semibold text-gain">{currency(scenarioValues[1].projectedValue)}</p>
        </article>
        <article className="rounded-2xl border border-slate-800 bg-slate-900/60 p-5">
          <p className="text-sm text-slate-400">Weighted Delta</p>
          <p className={`mt-2 text-2xl font-semibold ${signedClass(weightedDelta)}`}>{weightedDelta.toFixed(3)}</p>
        </article>
      </div>

      <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
        <h3 className="mb-3 text-sm font-medium text-slate-300">Scenario Comparison</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={scenarioValues}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
              <XAxis dataKey="name" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" />
              <Tooltip formatter={(value: number) => currency(value)} />
              <Legend />
              <Bar dataKey="projectedValue" fill="#6366f1" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="rounded-2xl border border-slate-800 bg-slate-900/60 p-4">
        <h3 className="mb-3 text-sm font-medium text-slate-300">Before vs After Summary</h3>
        <div className="grid gap-3 md:grid-cols-3">
          {scenarioValues.map((scenario) => (
            <div key={scenario.name} className="rounded-xl border border-slate-800 bg-slate-950/70 p-3">
              <p className="text-sm text-slate-300">{scenario.name}</p>
              <p className="mt-1 text-sm text-slate-400">
                Shift: {scenario.stockShift}% stock / {scenario.volShift}% IV / {scenario.days}d
              </p>
              <p className="mt-2 text-slate-100">{currency(scenario.projectedValue)}</p>
              <p className={`text-sm ${signedClass(scenario.netPl)}`}>
                {currency(scenario.netPl)} ({percent(scenario.returnPct)})
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
