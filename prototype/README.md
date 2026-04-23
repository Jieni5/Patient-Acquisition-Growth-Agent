# Launch-Readiness Tracker

Internal delivery tool for tracking pilot launch readiness for the **Patient Acquisition & Growth Agent** engagement.

## What it does

- **Summary bar** — overall readiness %, blocked milestone count, days to pilot go-live
- **Milestone table** — all 8 milestones with owner, workstream, status, and blocker reasons highlighted in red
- **Go/no-go checklist** — 17 launch criteria grouped by category (Integration, Compliance, Conversation Design, QA, Operations), each with completion state

## Install and run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Update delivery data

All data lives in `data.json` — no code changes needed.

- Change a milestone status: set `"status"` to `"Complete"`, `"In Progress"`, `"Not Started"`, or `"Blocked"`
- Flag a blocker: set `"blocked": true` and add a reason in `"blocker_reason"`
- Update a readiness criterion: change its `"status"` field — the summary bar readiness % updates automatically

Refresh the browser after saving `data.json` to see changes.
