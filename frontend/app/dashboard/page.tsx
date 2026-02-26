"use client";

import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";

import { MarketPulse } from "@/components/MarketPulse";
import { PnLBarList } from "@/components/PnLBarList";
import { PositionsTable } from "@/components/PositionsTable";
import { SummaryCard } from "@/components/SummaryCard";
import { samplePositions } from "@/lib/mock/positions";
import { toAnalytics } from "@/lib/utils/analytics";
import { currency } from "@/lib/utils/format";

const colors = ["#6366f1", "#22c55e", "#0ea5e9", "#f59e0b", "#eab308", "#ec4899"];

export default function DashboardPage() {
  const analytics = toAnalytics(samplePositions);
  const totalValue = analytics.reduce((sum, row) => sum + row.marketValue, 0);
  const totalPnL = analytics.reduce((sum, row) => sum + row.unrealizedPl, 0);
  const totalPnLPct = (totalPnL / analytics.reduce((sum, row) => sum + row.costBasis, 0)) * 100;

  const winners = [...analytics].sort((a, b) => b.unrealizedPl - a.unrealizedPl).slice(0, 5);
  const losers = [...analytics].sort((a, b) => a.unrealizedPl - b.unrealizedPl).slice(0, 5);

  const exposureMap = analytics.reduce<Record<string, number>>((acc, row) => {
    acc[row.symbol] = (acc[row.symbol] ?? 0) + row.marketValue;
    return acc;
  }, {});
  const pieData = Object.entries(exposureMap).map(([name, value]) => ({ name, value }));

  return (
    <section className="space-y-6">
      <div className="grid gap-4 lg:grid-cols-4">
        <div className="lg:col-span-3">
          <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">LEAPS Portfolio Dashboard</h1>
          <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
            Long-call portfolio overview with exposure and momentum tracking.
          </p>
        </div>
        <MarketPulse />
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <SummaryCard title="Total Portfolio Value" value={totalValue} />
        <SummaryCard title="Total Unrealized P/L" value={totalPnL} percentValue={totalPnLPct} />
        <SummaryCard title="Top Winner" value={winners[0]?.unrealizedPl ?? 0} />
        <SummaryCard title="Top Loser" value={losers[0]?.unrealizedPl ?? 0} />
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <div className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60 lg:col-span-1">
          <h3 className="mb-4 text-sm font-medium text-slate-600 dark:text-slate-300">Underlying Exposure</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={pieData} dataKey="value" nameKey="name" innerRadius={50} outerRadius={90}>
                  {pieData.map((entry, index) => (
                    <Cell key={entry.name} fill={colors[index % colors.length]} />
                  ))}
                </Pie>
                <Tooltip formatter={(value: number) => currency(value)} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="grid gap-4 lg:col-span-2 md:grid-cols-2">
          <PnLBarList positions={winners} title="Top 5 Winners" />
          <PnLBarList positions={losers} title="Top 5 Losers" />
        </div>
      </div>

      <PositionsTable positions={analytics} />
    </section>
  );
}
