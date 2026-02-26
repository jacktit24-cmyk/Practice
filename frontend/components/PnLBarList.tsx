import type { PositionAnalytics } from "@/lib/types/domain";
import { currency, signedClass } from "@/lib/utils/format";

export function PnLBarList({ positions, title }: { positions: PositionAnalytics[]; title: string }) {
  const maxAbs = Math.max(...positions.map((position) => Math.abs(position.unrealizedPl)), 1);

  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">
      <h3 className="mb-3 text-sm font-medium text-slate-700 dark:text-slate-300">{title}</h3>
      <div className="space-y-3">
        {positions.map((position) => {
          const width = (Math.abs(position.unrealizedPl) / maxAbs) * 100;
          return (
            <div key={position.id}>
              <div className="mb-1 flex items-center justify-between text-xs text-slate-600 dark:text-slate-300">
                <span>{position.symbol}</span>
                <span className={signedClass(position.unrealizedPl)}>{currency(position.unrealizedPl)}</span>
              </div>
              <div className="h-2 rounded-full bg-slate-200 dark:bg-slate-800">
                <div
                  className={`h-2 rounded-full ${position.unrealizedPl >= 0 ? "bg-gain" : "bg-loss"}`}
                  style={{ width: `${width}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
