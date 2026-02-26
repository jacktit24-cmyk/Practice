"use client";

import { useEffect, useState } from "react";

import { fetchMarketSignals, type MarketSignals } from "@/lib/api/client";

export function MarketPulse() {
  const [signals, setSignals] = useState<MarketSignals | null>(null);

  useEffect(() => {
    let cancelled = false;
    const load = async () => {
      try {
        const response = await fetchMarketSignals();
        if (!cancelled) {
          setSignals(response);
        }
      } catch {
        if (!cancelled) {
          setSignals(null);
        }
      }
    };

    void load();
    const interval = setInterval(load, 300000);
    return () => {
      cancelled = true;
      clearInterval(interval);
    };
  }, []);

  if (!signals) {
    return <section className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">Loading market pulse…</section>;
  }

  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-4 dark:border-slate-800 dark:bg-slate-900/60">
      <h3 className="text-sm font-semibold text-slate-800 dark:text-slate-200">Market Pulse</h3>
      <div className="mt-3 space-y-2 text-sm text-slate-600 dark:text-slate-300">
        <p>
          CNN Fear &amp; Greed: <strong>{signals.fear_greed_score.toFixed(0)}</strong> ({signals.fear_greed_label})
        </p>
        <p>
          Regime Score: <strong>{signals.regime_score.toFixed(0)}</strong> ({signals.regime_label})
        </p>
        <p>
          VIX: <strong>{signals.vix_price.toFixed(2)}</strong> ({signals.vix_change_pct.toFixed(2)}%)
        </p>
        <p className="font-medium text-amber-600 dark:text-amber-300">{signals.vix_alert}</p>
      </div>
    </section>
  );
}
