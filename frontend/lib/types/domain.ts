/**
 * Shared frontend domain models for OptionsLab modules.
 */
export type OptionType = "CALL" | "PUT";

export interface PortfolioPosition {
  id: string;
  symbol: string;
  optionType: OptionType;
  strike: number;
  expiration: string;
  quantity: number;
  costBasis: number;
  marketValue: number;
  underlyingPrice: number;
}

export interface PositionAnalytics extends PortfolioPosition {
  unrealizedPl: number;
  unrealizedPlPct: number;
  intrinsicValue: number;
  extrinsicValue: number;
  breakEven: number;
  daysToExpiration: number;
  deltaEstimate: number;
}

export interface ProjectionScenario {
  name: string;
  stockShiftPct: number;
  volatilityShiftPct: number;
  daysForward: number;
}
