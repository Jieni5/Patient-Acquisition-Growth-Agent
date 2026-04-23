# Prototype Plan — Launch-Readiness Tracker

## What We're Building and Why

**Chosen prototype:** Launch-Readiness Tracker

A locally runnable internal tool that helps a delivery team track launch readiness for the Patient Acquisition & Growth Agent. Credible and functional, not production-ready.

**Chosen over alternatives because:**
- Tightest scope with the clearest output
- Data model maps directly to the delivery plan already written
- Every screen answers a question a real delivery team would ask before a steering call

---

## Scope — What's In, What's Out

**In:**
- Summary bar: overall readiness %, blocked item count, days to pilot go-live
- Milestone & workstream table: status, owner, blocked flag highlighted in red
- Go/no-go checklist: criteria grouped by category with completion state

**Out (deliberately cut for time):**
- Risk dashboard (covered in `dependency_risk_review.md`)
- Sidebar metadata and page config polish
- Separate components folder — everything lives in `app.py`
- Charts or visualizations beyond basic metrics

---

## Tech Stack

| Layer | Choice | Reason |
|---|---|---|
| Language | Python 3.11+ | Fast, readable, no boilerplate |
| UI | Streamlit | One command to run, no HTML/CSS/JS, clean enough for an internal tool |
| Data | `data.json` | Human-editable, no database, pre-populated with real engagement data |
| Dependencies | `streamlit` only | One pip install, no build step |

**To run:**
```bash
pip install streamlit
streamlit run app.py
```

---

## File Structure

```
/prototype/
├── app.py              # Entire app — single file
├── data.json           # All delivery data: workstreams, milestones, readiness criteria
└── requirements.txt    # streamlit
```

---

## Data Model — `data.json`

Three top-level keys:

```json
{
  "engagement": {
    "name": "Patient Acquisition & Growth Agent",
    "client": "Hospital Client",
    "pilot_date": "2026-06-17",
    "current_week": 3
  },
  "milestones": [
    {
      "id": "M1",
      "name": "Project Kickoff",
      "week": 1,
      "owner": "Delivery Lead",
      "workstream": "WS1 — Requirements & Workflow Discovery",
      "status": "Complete",
      "blocked": false,
      "blocker_reason": ""
    }
  ],
  "readiness_criteria": [
    {
      "category": "Integration",
      "criterion": "Scheduling system and calendar platform confirmed",
      "owner": "Integration Engineer",
      "status": "Complete"
    }
  ]
}
```

Status values: `"Complete"` / `"In Progress"` / `"Not Started"` / `"Blocked"`

---

## Step-by-Step Build Plan

---

### Step 1 — Create files and populate `data.json`
**~15 min**

- Create `/prototype` folder with `app.py`, `data.json`, `requirements.txt`
- Populate `data.json` with all 8 milestones and 6 workstreams from the delivery plan, and ~12 go/no-go readiness criteria from M7
- Use realistic mixed statuses (some Complete, some In Progress, one or two Blocked) so the UI has something meaningful to render

---

### Step 2 — Summary bar
**~10 min**

Top of `app.py`:
- Load `data.json`
- Calculate: readiness % (Complete criteria / total criteria), blocked milestone count, days to `pilot_date`
- Render with `st.metric` in three columns

---

### Step 3 — Milestone & workstream table
**~15 min**

- Build a Pandas DataFrame from `milestones`
- Highlight rows where `blocked: true` in red using `st.dataframe` with Pandas Styler
- Show columns: Milestone, Week, Workstream, Owner, Status, Blocker Reason
- Add a `st.selectbox` filter for status so blocked items can be isolated in one click

---

### Step 4 — Go/no-go readiness checklist
**~15 min**

- Group `readiness_criteria` by category
- For each category, show a sub-header with category completion %
- Render each criterion as a row: status icon (✅ / 🔄 / ⬜ / 🔴) + criterion text + owner
- Overall completion % already shown in summary bar

---

### Step 5 — Smoke test and README
**~5 min**

- Run the app, confirm all three views render correctly with mixed data states
- Write 5-line `README.md`: what it is, how to install, how to run, how to update data

---

## Total Build Time: ~60 minutes
