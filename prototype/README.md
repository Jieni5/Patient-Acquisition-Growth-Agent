# Launch-Readiness Tracker

A locally runnable internal delivery tool for tracking pilot launch readiness for the
**Patient Acquisition & Growth Agent** engagement.

---

## What It Does

The app has three sections:

**1. Summary Bar**
Three headline metrics calculated automatically from the data:
- Overall readiness % (based on go/no-go criteria completion)
- Number of blocked milestones
- Days remaining to pilot go-live

**2. Milestones & Workstream Status**
An editable table showing all 8 delivery milestones with owner, workstream, week,
status, and blocker reason. Use the filter dropdown to isolate milestones by status.
- `Status ✏️` column: click any cell to change the status via dropdown
- `Blocker` column: free-text editable — type a blocker reason when status is Blocked

**3. Go / No-Go Readiness Checklist**
17 launch criteria grouped by category (Integration, Compliance, Conversation Design,
QA, Operations). Each criterion shows a status icon and an inline dropdown to update
its state. Category-level completion percentages update as criteria are marked complete.

Clicking **Save all changes** writes all edits back to `data.json` and refreshes the
page automatically — summary bar metrics update immediately.

---

## Files

```
prototype/
├── app.py           — Streamlit app (single file, ~177 lines)
├── data.json        — All delivery data: engagement info, milestones, readiness criteria
├── requirements.txt — streamlit, pandas
└── README.md
```

---

## Install and Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the app**
```bash
streamlit run app.py
```

Opens at `http://localhost:8501` in your browser.

---

## Updating Delivery Data

All data lives in `data.json`. You can update it two ways:

**In the app** — change milestone statuses and blocker text directly in the table,
update checklist criterion statuses via the dropdowns, then click Save. The page
refreshes and all metrics recalculate.

**Directly in data.json** — open the file in any editor. Useful for bulk updates or
changing fields that are read-only in the UI (milestone names, owners, workstream
assignments). Refresh the browser after saving.

### Valid status values
Applies to both milestones and readiness criteria:
```
"Complete" | "In Progress" | "Not Started" | "Blocked"
```

### Changing engagement details
Edit the `"engagement"` block at the top of `data.json` to update the client name,
pilot target date, or current week number:
```json
{
  "engagement": {
    "name": "Patient Acquisition & Growth Agent",
    "client": "Hospital Client",
    "pilot_date": "2026-06-17",
    "current_week": 3
  }
}
```
