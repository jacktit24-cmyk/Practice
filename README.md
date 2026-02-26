# OptionsLab – Advanced Options Dashboard & Sensitivity Engine

Production-focused options analytics platform with a modular Next.js frontend and FastAPI backend.

## Architecture

- `frontend/` — Next.js + TypeScript + Tailwind + Recharts + Zustand UI
- `backend/` — FastAPI application and quantitative/income strategy services
- `backend/pricing/` — isolated Black-Scholes pricing and Greeks engine
- `backend/app/services/wheel_service.py` — wheel strategy income/cycle analytics
- `backend/market_data/` — provider abstraction for future Polygon/Tradier/Yahoo connectors

## Build Phases

1. ✅ **Phase 1** — Scaffold full project structure
2. ✅ **Phase 2** — Backend pricing engine + sensitivity grid + unit tests
3. ✅ **Phase 3** — Frontend dashboard/sensitivity/projection module UI
4. ✅ **Phase 4 (in progress)** — Live API integration + Wheel Strategy command center

## New in this iteration

- Added **Wheel Strategy** module (Tab 4) with command grid, income summary, DTE alerts, payoff chart, and capital release schedule.
- Added backend wheel CRUD + dashboard endpoints with JSON persistence.
- Added **market pulse** endpoint and dashboard widget for:
  - CNN Fear & Greed
  - Market regime score
  - VIX price/change alert
- Added light-theme default and dark-theme toggle.

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
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000 npm run dev -- --hostname 0.0.0.0 --port 3000
```

## Testing

```bash
cd backend
PYTHONPATH=. pytest -q

cd ../frontend
npm run build
```

## API Endpoints

- `GET /api/health`
- `POST /api/pricing/sensitivity`
- `GET /api/market/signals`
- `GET /api/wheel/dashboard`
- `GET /api/wheel/positions`
- `POST /api/wheel/positions`
- `PATCH /api/wheel/positions/{position_id}`
- `DELETE /api/wheel/positions/{position_id}`
