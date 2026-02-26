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

export interface WheelPosition {
  id: string;
  ticker: string;
  phase: "CSP" | "CC";
  contracts: number;
  strike: number;
  expiration: string;
  dte: number;
  premium_collected: number;
  capital_reserved: number;
  apy: number | null;
  unrealized_pl: number;
  status: string;
  break_even: number;
  current_option_value: number;
  opened_dte: number;
  stock_cost_basis?: number;
  linked_cycle_id?: string;
}

export interface WheelDashboard {
  summary: {
    total_premium_open: number;
    total_premium_mtd: number;
    total_premium_ytd: number;
    weighted_apy_csp: number;
    capital_deployed_csp: number;
    capital_at_risk_cc: number;
    next_expiration_alerts: number;
  };
  positions: WheelPosition[];
  dte_alerts: WheelPosition[];
  capital_release_schedule: Array<{ ticker: string; expiration: string; capital_release: number }>;
}

export interface MarketSignals {
  fear_greed_score: number;
  fear_greed_label: string;
  vix_price: number;
  vix_change_pct: number;
  vix_alert: string;
  regime_score: number;
  regime_label: string;
}

async function parseResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const message = await response.text();
    throw new Error(`API error (${response.status}): ${message}`);
  }
  return (await response.json()) as T;
}

export async function fetchSensitivity(request: SensitivityRequest): Promise<SensitivityResponse> {
  const response = await fetch(`${API_BASE_URL}/api/pricing/sensitivity`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
    cache: "no-store"
  });
  return parseResponse<SensitivityResponse>(response);
}

export async function fetchWheelDashboard(): Promise<WheelDashboard> {
  const response = await fetch(`${API_BASE_URL}/api/wheel/dashboard`, { cache: "no-store" });
  return parseResponse<WheelDashboard>(response);
}

export interface WheelPositionCreatePayload {
  ticker: string;
  phase: "CSP" | "CC";
  contracts: number;
  strike: number;
  expiration: string;
  premium_collected: number;
  current_option_value: number;
  opened_dte: number;
  status: string;
  stock_cost_basis?: number;
  linked_cycle_id?: string | null;
}

export async function createWheelPosition(payload: WheelPositionCreatePayload): Promise<WheelPosition> {
  const response = await fetch(`${API_BASE_URL}/api/wheel/positions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  return parseResponse<WheelPosition>(response);
}

export async function fetchMarketSignals(): Promise<MarketSignals> {
  const response = await fetch(`${API_BASE_URL}/api/market/signals`, { cache: "no-store" });
  return parseResponse<MarketSignals>(response);
}
