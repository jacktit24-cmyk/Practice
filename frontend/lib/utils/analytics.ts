import type { PortfolioPosition, PositionAnalytics } from "@/lib/types/domain";

const estimateDelta = (optionType: "CALL" | "PUT", moneyness: number, daysToExpiry: number): number => {
  const timeFactor = Math.max(0.25, Math.min(1, daysToExpiry / 365));
  const base = 0.5 + Math.tanh(moneyness) * 0.35;
  const scaled = Math.min(0.98, Math.max(0.05, base * timeFactor + 0.2));
  return optionType === "CALL" ? scaled : scaled - 1;
};

export const toAnalytics = (positions: PortfolioPosition[]): PositionAnalytics[] => {
  const now = new Date();

  return positions.map((position) => {
    const unrealizedPl = position.marketValue - position.costBasis;
    const unrealizedPlPct = (unrealizedPl / position.costBasis) * 100;
    const intrinsicValuePerContract =
      position.optionType === "CALL"
        ? Math.max(position.underlyingPrice - position.strike, 0)
        : Math.max(position.strike - position.underlyingPrice, 0);

    const intrinsicValue = intrinsicValuePerContract * position.quantity * 100;
    const extrinsicValue = Math.max(position.marketValue - intrinsicValue, 0);
    const premiumPerContract = position.marketValue / (position.quantity * 100);
    const breakEven =
      position.optionType === "CALL" ? position.strike + premiumPerContract : position.strike - premiumPerContract;

    const expiration = new Date(position.expiration);
    const daysToExpiration = Math.max(0, Math.ceil((expiration.getTime() - now.getTime()) / (1000 * 60 * 60 * 24)));

    const moneyness = (position.underlyingPrice - position.strike) / position.strike;
    const deltaEstimate = estimateDelta(position.optionType, moneyness, daysToExpiration);

    return {
      ...position,
      unrealizedPl,
      unrealizedPlPct,
      intrinsicValue,
      extrinsicValue,
      breakEven,
      daysToExpiration,
      deltaEstimate
    };
  });
};
