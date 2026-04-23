import json
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Launch-Readiness Tracker", layout="wide")

with open("data.json") as f:
    data = json.load(f)

engagement = data["engagement"]
milestones = data["milestones"]
criteria = data["readiness_criteria"]

# --- Calculations ---
total_criteria = len(criteria)
complete_criteria = sum(1 for c in criteria if c["status"] == "Complete")
readiness_pct = int((complete_criteria / total_criteria) * 100) if total_criteria else 0

blocked_milestones = sum(1 for m in milestones if m["blocked"])

pilot_date = date.fromisoformat(engagement["pilot_date"])
days_to_golive = (pilot_date - date.today()).days

# --- Header ---
st.title("Launch-Readiness Tracker")
st.caption(f"{engagement['name']}  ·  Client: {engagement['client']}  ·  Week {engagement['current_week']} of 8")

st.divider()

# --- Summary Bar ---
col1, col2, col3 = st.columns(3)

col1.metric(
    label="Overall Readiness",
    value=f"{readiness_pct}%",
    delta=f"{complete_criteria} of {total_criteria} criteria met",
    delta_color="normal"
)

col2.metric(
    label="Blocked Milestones",
    value=blocked_milestones,
    delta="Needs attention" if blocked_milestones > 0 else "None blocked",
    delta_color="inverse" if blocked_milestones > 0 else "normal"
)

col3.metric(
    label="Days to Pilot Go-Live",
    value=days_to_golive,
    delta=f"Target: {pilot_date.strftime('%b %d, %Y')}",
    delta_color="off"
)

st.divider()

# --- Milestone & Workstream Table ---
st.subheader("Milestones & Workstream Status")

status_filter = st.selectbox(
    "Filter by status",
    options=["All", "Blocked", "In Progress", "Not Started", "Complete"],
    index=0
)

STATUS_ICON = {
    "Complete":    "✅ Complete",
    "In Progress": "🔄 In Progress",
    "Not Started": "⬜ Not Started",
    "Blocked":     "🔴 Blocked",
}

rows = []
for m in milestones:
    display_status = "Blocked" if m["blocked"] else m["status"]
    rows.append({
        "ID":         m["id"],
        "Milestone":  m["name"],
        "Week":       m["week"],
        "Workstream": m["workstream"],
        "Owner":      m["owner"],
        "Status":     STATUS_ICON.get(display_status, display_status),
        "Blocker":    m["blocker_reason"] if m["blocked"] else "",
        "_blocked":   m["blocked"],
    })

df = pd.DataFrame(rows)

if status_filter != "All":
    if status_filter == "Blocked":
        df = df[df["_blocked"]]
    else:
        df = df[df["Status"] == STATUS_ICON.get(status_filter, status_filter)]

display_df = df.drop(columns=["_blocked"])

def highlight_blocked(row):
    if row["Blocker"] != "":
        return ["background-color: #4a1010; color: white"] * len(row)
    return [""] * len(row)

st.dataframe(
    display_df.style.apply(highlight_blocked, axis=1),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# --- Go/No-Go Readiness Checklist ---
st.subheader("Go / No-Go Readiness Checklist")

CRITERIA_ICON = {
    "Complete":    "✅",
    "In Progress": "🔄",
    "Not Started": "⬜",
    "Blocked":     "🔴",
}

# Group criteria by category
from collections import defaultdict
by_category = defaultdict(list)
for c in criteria:
    by_category[c["category"]].append(c)

for category, items in by_category.items():
    cat_total = len(items)
    cat_complete = sum(1 for c in items if c["status"] == "Complete")
    cat_pct = int((cat_complete / cat_total) * 100)

    st.markdown(f"**{category}** &nbsp;&nbsp; `{cat_complete}/{cat_total} complete ({cat_pct}%)`")

    for c in items:
        icon = CRITERIA_ICON.get(c["status"], "⬜")
        st.markdown(
            f"{icon} &nbsp; {c['criterion']} &nbsp; <span style='color:gray;font-size:0.85em'>— {c['owner']}</span>",
            unsafe_allow_html=True,
        )

    st.write("")
