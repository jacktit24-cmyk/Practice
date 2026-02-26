/**
 * Core frontend domain models used by dashboard, sensitivity, and projection modules.
 * These will be expanded as backend contracts are implemented.
 */
export type OptionType = "CALL" | "PUT";

export interface PortfolioPosition {
  symbol: string;
  optionType: OptionType;
  strike: number;
  expiration: string;
  quantity: number;
  costBasis: number;
  marketValue: number;
  underlyingPrice: number;
}
