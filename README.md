# OptionsLab – Advanced Options Dashboard & Sensitivity Engine

Production-focused options analytics platform with a modular Next.js frontend and FastAPI backend.

## Architecture

- `frontend/` — Next.js + TypeScript + Tailwind + Recharts + Zustand UI
- `backend/` — FastAPI application and quantitative services
- `backend/pricing/` — isolated Black-Scholes pricing and Greeks engine
- `backend/market_data/` — provider abstraction for future Polygon/Tradier/Yahoo connectors

## Build Phases

1. ✅ **Phase 1** — Scaffold full project structure
2. ✅ **Phase 2** — Backend pricing engine + sensitivity grid + unit tests
3. ⏳ **Phase 3** — Frontend dashboard module implementation
4. ⏳ **Phase 4** — Frontend/backend API integration

## Local Setup

### Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev -- --hostname 0.0.0.0 --port 3000
```

## Testing

Run backend pricing tests:

```bash
cd backend
PYTHONPATH=. pytest -q
```

## Current API Endpoints

- `GET /api/health`
- `POST /api/pricing/sensitivity`

### `POST /api/pricing/sensitivity` request body

```json
{
  "ticker": "AAPL",
  "option_type": "CALL",
  "strike": 200,
  "expiration_days": 45,
  "implied_volatility": 0.35,
  "current_stock_price": 195,
  "stock_price_scenarios": [180, 190, 200, 210],
  "volatility_scenarios": [0.25, 0.35, 0.45],
  "time_horizon_days": [15, 30, 45],
  "risk_free_rate": 0.05
}
```
