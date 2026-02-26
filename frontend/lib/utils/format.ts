export const currency = (value: number): string =>
  new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 2 }).format(value);

export const percent = (value: number): string => `${value.toFixed(2)}%`;

export const signedClass = (value: number): string =>
  value >= 0 ? "text-gain" : "text-loss";
