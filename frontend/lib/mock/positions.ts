import type { PortfolioPosition } from "@/lib/types/domain";

export const samplePositions: PortfolioPosition[] = [
  {
    id: "1",
    symbol: "AAPL",
    optionType: "CALL",
    strike: 200,
    expiration: "2026-06-19",
    quantity: 4,
    costBasis: 3400,
    marketValue: 4020,
    underlyingPrice: 214.3
  },
  {
    id: "2",
    symbol: "TSLA",
    optionType: "PUT",
    strike: 175,
    expiration: "2026-04-17",
    quantity: 3,
    costBasis: 2550,
    marketValue: 2230,
    underlyingPrice: 190.8
  },
  {
    id: "3",
    symbol: "MSFT",
    optionType: "CALL",
    strike: 460,
    expiration: "2026-09-18",
    quantity: 2,
    costBasis: 1980,
    marketValue: 2355,
    underlyingPrice: 472.1
  },
  {
    id: "4",
    symbol: "NVDA",
    optionType: "CALL",
    strike: 140,
    expiration: "2026-05-15",
    quantity: 6,
    costBasis: 3920,
    marketValue: 4630,
    underlyingPrice: 153.2
  },
  {
    id: "5",
    symbol: "SPY",
    optionType: "PUT",
    strike: 510,
    expiration: "2026-03-20",
    quantity: 2,
    costBasis: 1700,
    marketValue: 1395,
    underlyingPrice: 521.6
  },
  {
    id: "6",
    symbol: "AMZN",
    optionType: "CALL",
    strike: 230,
    expiration: "2026-07-17",
    quantity: 3,
    costBasis: 2140,
    marketValue: 2435,
    underlyingPrice: 238.7
  }
];
