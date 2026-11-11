# Financial Harness: Frontend

React + TypeScript + Vite. Styling with Tailwind CSS v4.

## Run it

```bash
cd frontend
npm install
cp .env.example .env     # then set VITE_API_BASE_URL (value from Danial)
npm run dev              # development server
npm run build            # type-check + production build
npm run lint
```

## Folder structure

| Folder | Purpose |
| --- | --- |
| `src/config` | Settings from `.env` |
| `src/services` | API calls only (no UI). `apiClient.ts` has no endpoints yet |
| `src/types` | Shared TypeScript types (`DataMeta` is a proposal, see below) |
| `src/layouts` | App shell and responsive sidebar |
| `src/components/ui` | Reusable UI: Card, state views, DataSourceFooter, Logo |
| `src/pages` | One screen per route |
| `src/routes` | Navigation list (also tells each page which API it waits for) |

## Rules this project follows

- No fake AI answers, prices or indicators. Empty sections say which API they wait for.
- No endpoints are invented. Services are added only after Danial confirms the contract.
- Every financial result will use `DataSourceFooter` (source, timestamp, reporting period, assumptions, delayed or simulated labels).
- Frontend does not calculate AI or financial results.

## Status (Stage 2)

Done: theme, responsive layout and sidebar, routing for all 11 modules, landing page, dashboard shell, AI assistant shell, shared state components, API client skeleton.

Waiting on backend/AI contracts: every data-driven section (see the "dependency" text in `src/routes/navigation.ts`).

## Open questions for the team

- Danial: endpoint, method, request/response, auth and error format for each API.
- Hamid: sample JSON for chat, strategy, simulation and Python results.
- Both: agree on the `DataMeta` shape in `src/types/common.ts` (source, timestamp, reporting period, assumptions, freshness, simulation flag).
