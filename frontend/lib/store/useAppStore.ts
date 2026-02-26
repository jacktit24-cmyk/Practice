import { create } from "zustand";
import type { PortfolioPosition } from "@/lib/types/domain";

interface AppState {
  positions: PortfolioPosition[];
  setPositions: (positions: PortfolioPosition[]) => void;
}

export const useAppStore = create<AppState>((set) => ({
  positions: [],
  setPositions: (positions) => set({ positions })
}));
