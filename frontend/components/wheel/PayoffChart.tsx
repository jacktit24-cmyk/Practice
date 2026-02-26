"use client";

import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

import type { WheelPosition } from "@/lib/api/client";

export function PayoffChart({ positions }: { positions: WheelPosition[] }) {
  const points = [-20, -10, 0, 10, 20].map((shift) => {
    const value = positions.reduce((sum, row) => sum + row.unrealized_pl + shift * row.contracts * 5, 0);
    return { shift, value };
  });

  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">
      <h3 className="mb-3 text-sm font-semibold text-slate-800 dark:text-slate-200">Wheel Payoff (Scenario Slice)</h3>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={points}>
            <CartesianGrid strokeDasharray="3 3" stroke="#94a3b8" />
            <XAxis dataKey="shift" />
            <YAxis />
            <Tooltip />
            <Area dataKey="value" stroke="#22c55e" fill="#86efac" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}
