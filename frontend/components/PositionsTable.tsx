"use client";

import { useMemo, useState } from "react";

import type { PositionAnalytics } from "@/lib/types/domain";
import { currency, percent, signedClass } from "@/lib/utils/format";

type SortableKey = keyof Pick<
  PositionAnalytics,
  "symbol" | "marketValue" | "unrealizedPl" | "unrealizedPlPct" | "daysToExpiration" | "deltaEstimate"
>;

export function PositionsTable({ positions }: { positions: PositionAnalytics[] }) {
  const [sortKey, setSortKey] = useState<SortableKey>("marketValue");
  const [descending, setDescending] = useState(true);

  const sorted = useMemo(() => {
    const clone = [...positions];
    clone.sort((a, b) => {
      const left = a[sortKey];
      const right = b[sortKey];
      if (typeof left === "string" && typeof right === "string") {
        return descending ? right.localeCompare(left) : left.localeCompare(right);
      }
      return descending ? Number(right) - Number(left) : Number(left) - Number(right);
    });
    return clone;
  }, [positions, sortKey, descending]);

  const onSort = (key: SortableKey) => {
    if (key === sortKey) {
      setDescending((prev) => !prev);
      return;
    }
    setSortKey(key);
    setDescending(true);
  };

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900/60">
      <table className="w-full text-left text-sm">
        <thead className="bg-slate-100 text-slate-600 dark:bg-slate-900 dark:text-slate-400">
          <tr>
            {[
              ["symbol", "Symbol"],
              ["marketValue", "Market Value"],
              ["unrealizedPl", "P/L"],
              ["unrealizedPlPct", "P/L %"],
              ["daysToExpiration", "DTE"],
              ["deltaEstimate", "Delta"]
            ].map(([key, label]) => (
              <th key={key} className="px-4 py-3 font-medium">
                <button
                  type="button"
                  onClick={() => onSort(key as SortableKey)}
                  className="inline-flex items-center gap-1 transition hover:text-slate-900 dark:hover:text-slate-200"
                >
                  {label}
                </button>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {sorted.map((position) => (
            <tr key={position.id} className="border-t border-slate-200 text-slate-700 dark:border-slate-800 dark:text-slate-200">
              <td className="px-4 py-3">{position.symbol}</td>
              <td className="px-4 py-3">{currency(position.marketValue)}</td>
              <td className={`px-4 py-3 ${signedClass(position.unrealizedPl)}`}>{currency(position.unrealizedPl)}</td>
              <td className={`px-4 py-3 ${signedClass(position.unrealizedPlPct)}`}>{percent(position.unrealizedPlPct)}</td>
              <td className="px-4 py-3">{position.daysToExpiration}</td>
              <td className={`px-4 py-3 ${signedClass(position.deltaEstimate)}`}>{position.deltaEstimate.toFixed(3)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
