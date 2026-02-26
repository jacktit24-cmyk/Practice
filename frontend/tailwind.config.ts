import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class",
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./lib/**/*.{ts,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        gain: "#16a34a",
        loss: "#dc2626",
        surface: "#0f172a"
      }
    }
  },
  plugins: []
};

export default config;
