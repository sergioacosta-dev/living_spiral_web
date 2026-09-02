# Living Spiral Web

Web version of the Living Spiral Dreamspell calendar — Mayan Tzolkin-based daily kin lookup, meditations, and practices. Static frontend + Python serverless API on Vercel. Live at https://livingspiralweb.vercel.app. Status: **on hold** (deployed and working, no active development).

## Stack

- Static frontend: `index.html` + `app.js` + `style.css` (no framework)
- Python serverless functions in `api/` (Vercel's Python runtime, one file per endpoint)
- `living_spiral/` — pure calendar logic (Tzolkin calculation), importable by both the API handlers and any local scripts
- Deployed on Vercel; routes explicitly mapped in `vercel.json` (needed so `/api/*` doesn't get caught by the static-file catch-all)

## Endpoints

| Route | Handler |
|-------|---------|
| `/api/today` | `api/today.py` — today's kin |
| `/api/kin` | `api/kin.py` — kin lookup by date |
| `/api/practices` | `api/practices.py` |
| `/api/meditations` | `api/meditations.py` |

## Local Development

```bash
python dev_server.py   # serves static files + /api/* locally, no Vercel CLI needed
```

Uses absolute `sys.path` imports (not relative) specifically for Vercel serverless compatibility — each function runs in its own isolated environment.

## Deploy

```bash
vercel --prod
```

## Status

On hold as of 2026-07-13. Deployed and stable; no open bugs, no active backlog.
