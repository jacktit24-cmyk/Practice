# Appraisal Workflow Manager

A premium, minimalist workflow manager for commercial appraisal teams.

## Features

- CSV job import with resilient column matching, normalization, and de-duplication (`Job Number` primary key, last-row-wins conflict handling).
- Board and list views with search, filters, and sorting.
- Dashboard KPI tiles + due timeline buckets.
- Rule-based status engine:
  - Completed
  - Overdue
  - Due Soon (0–5 business days)
  - Front-End Pending (7+ day jobs with front-end incomplete)
  - Awaiting Info
  - In Progress
  - New
- Escalation badges by business-days-left (including overdue and subtle pulse at 1 day left).
- Daily check-in prompt center for follow-up, information, and front-end completion prompts.
- Job detail drawer for yes/no confirmations and required front-end explanation notes.
- Local persistence of jobs, settings, and UI preferences.

## Tech Stack

- React + TypeScript + Vite
- Zustand state store
- React Router
- localStorage persistence wrapper

## Run

```bash
npm install
npm run dev
```

Build for production:

```bash
npm run build
npm run preview
```

## CSV Format

Required headers (case-insensitive, tolerant to spaces/underscores/dashes):

- Property Name
- Client Name
- Job Number
- Report Writer
- Fee
- Due Date
- Date Entered (optional; defaults to import timestamp)

Example:

```csv
Property Name,Client Name,Job Number,Report Writer,Fee,Due Date,Date Entered
Riverfront Office,Acme Capital,JOB-1021,A. Smith,"$4,500",2026-03-14,2026-03-01
Midtown Retail,Beacon REIT,JOB-1022,J. Lee,3800,03/18/2026,
```

## Business-day assumptions

- Weekends excluded.
- Holidays not excluded in MVP.
- `businessDaysLeft` is computed from **today (exclusive)** to **due date (inclusive)**.
- Due today = `0`.

## Notes for expansion

- `src/services/storage.ts` is interface-oriented for swapping to IndexedDB/backend.
- Domain logic lives in `src/domain/*` and selectors in `src/state/selectors.ts`.
