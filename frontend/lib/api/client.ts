/**
 * Centralized frontend API client wrapper.
 */
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export interface SensitivityRequest {
  ticker: string;
  option_type: "CALL" | "PUT";
  strike: number;
  expiration_days: number;
  implied_volatility: number;
  current_stock_price: number;
  stock_price_scenarios: number[];
  volatility_scenarios: number[];
  time_horizon_days: number[];
  risk_free_rate: number;
}

export interface SensitivityScenario {
  spot: number;
  volatility: number;
  time_to_expiry_years: number;
  price: number;
  delta: number;
  gamma: number;
  theta: number;
  vega: number;
  pct_change_vs_base: number;
}

export interface SensitivityResponse {
  base_price: number;
  scenarios: SensitivityScenario[];
}

export async function fetchSensitivity(request: SensitivityRequest): Promise<SensitivityResponse> {
  const response = await fetch(`${API_BASE_URL}/api/pricing/sensitivity`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
    cache: "no-store"
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(`Sensitivity API error (${response.status}): ${message}`);
  }

  return (await response.json()) as SensitivityResponse;
}
