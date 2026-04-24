import json
import streamlit as st
import pandas as pd
from datetime import date
from collections import defaultdict

st.set_page_config(page_title="Launch-Readiness Tracker", layout="wide")

DATA_FILE = "data.json"

def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

data = load_data()
engagement = data["engagement"]
milestones = data["milestones"]
criteria = data["readiness_criteria"]

STATUS_OPTIONS = ["Complete", "In Progress", "Not Started", "Blocked"]

STATUS_ICON = {
    "Complete":    "✅ Complete",
    "In Progress": "🔄 In Progress",
    "Not Started": "⬜ Not Started",
    "Blocked":     "🔴 Blocked",
}

CRITERIA_ICON = {
    "Complete":    "✅",
    "In Progress": "🔄",
    "Not Started": "⬜",
    "Blocked":     "🔴",
}

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
st.caption("Click any cell in the **Status ✏️** column to change it. Click **Save all changes** when done.")

status_filter = st.selectbox(
    "Filter by status",
    options=["All", "Blocked", "In Progress", "Not Started", "Complete"],
)

filtered = [m for m in milestones if status_filter == "All" or (
    ("Blocked" if m["blocked"] else m["status"]) == status_filter
)]

ms_df = pd.DataFrame([{
    "ID":         m["id"],
    "Milestone":  m["name"],
    "Week":       m["week"],
    "Workstream": m["workstream"],
    "Owner":      m["owner"],
    "Status":     "Blocked" if m["blocked"] else m["status"],
    "Blocker":    m["blocker_reason"] if m["blocked"] else "",
} for m in filtered])

edited_df = st.data_editor(
    ms_df,
    use_container_width=True,
    hide_index=True,
    disabled=["ID", "Milestone", "Week", "Workstream", "Owner"],
    column_config={
        "ID":         st.column_config.TextColumn("ID",         width="small"),
        "Week":       st.column_config.NumberColumn("Week",     width="small"),
        "Milestone":  st.column_config.TextColumn("Milestone",  width="medium"),
        "Workstream": st.column_config.TextColumn("Workstream", width="medium"),
        "Owner":      st.column_config.TextColumn("Owner",      width="small"),
        "Status":     st.column_config.SelectboxColumn(
            "Status ✏️",
            options=STATUS_OPTIONS,
            required=True,
            width="small",
        ),
        "Blocker":    st.column_config.TextColumn("Blocker",    width="large"),
    },
    key="milestone_editor",
)

# Write edits back to milestones list
id_to_milestone = {m["id"]: m for m in milestones}
for _, row in edited_df.iterrows():
    m = id_to_milestone.get(row["ID"])
    if m:
        m["status"]         = row["Status"]
        m["blocked"]        = row["Status"] == "Blocked"
        m["blocker_reason"] = row["Blocker"] if row["Status"] == "Blocked" else ""

st.divider()

# --- Go/No-Go Readiness Checklist ---
st.subheader("Go / No-Go Readiness Checklist")
st.caption("Update each criterion status. Click **Save all changes** when done.")

by_category = defaultdict(list)
for c in criteria:
    by_category[c["category"]].append(c)

for category, items in by_category.items():
    cat_total = len(items)
    cat_complete = sum(1 for c in items if c["status"] == "Complete")
    cat_pct = int((cat_complete / cat_total) * 100)

    st.markdown(f"**{category}** &nbsp;&nbsp; `{cat_complete}/{cat_total} complete ({cat_pct}%)`")

    for i, c in enumerate(items):
        col_icon, col_text, col_select = st.columns([1, 6, 3])
        col_icon.markdown(
            f"<div style='padding-top:8px'>{CRITERIA_ICON.get(c['status'], '⬜')}</div>",
            unsafe_allow_html=True
        )
        col_text.markdown(
            f"<div style='padding-top:8px'>{c['criterion']} "
            f"<span style='color:gray;font-size:0.85em'>— {c['owner']}</span></div>",
            unsafe_allow_html=True
        )
        new_status = col_select.selectbox(
            "Status",
            options=STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(c["status"]),
            key=f"rc_{category}_{i}",
            label_visibility="collapsed",
        )
        c["status"] = new_status

    st.write("")

st.divider()

# --- Save Button ---
if st.button("💾  Save all changes", type="primary", use_container_width=True):
    save_data(data)
    st.rerun()
