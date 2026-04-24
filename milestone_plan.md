# Patient Acquisition & Growth Agent — Milestone Plan

---

## Overview

This document defines the eight delivery milestones across the 8-week engagement. Each milestone has a clear goal, describes what happens during that period, and specifies exit criteria that must be met before the next milestone begins.

**Critical path:** M1 → M2 → M3 → M5 → M6 → M7 → M8  
**Parallel track:** M4 (Compliance) runs concurrently from Week 3 and must close by M7.

---

## Timeline at a Glance

| Week | Milestone | Workstream(s) |
|---|---|---|
| 1 | **M1** — Project Kickoff | WS1 |
| 1–2 | **M2** — Discovery & Requirements Alignment | WS1 |
| 3 | **M3** — Technical Design Checkpoint | WS2, WS3 |
| 3–4 | **M4** — Compliance Review Open | WS4 |
| 4–5 | **M5** — Prototype / Integration Demo | WS2, WS3 |
| 6 | **M6** — QA & Internal Review | WS5 |
| 7 | **M7** — Launch-Readiness Review | WS4, WS5 |
| 8 | **M8** — Pilot Go-Live | WS6 |

---

## Milestones

---

### M1 — Project Kickoff `Week 1`

**Goal**  
Align all stakeholders on scope, roles, ways of working, and success criteria before any discovery work begins.

**What happens**  
- Kickoff meeting with client sponsors, operations, IT, and delivery team
- Confirm engagement scope, out-of-scope items, and prototype boundaries
- Establish communication cadence: weekly steering update, async issue log, shared workspace
- Distribute and agree on the workstream structure and milestone plan

**Exit Criteria**  
- Kickoff deck presented and questions resolved
- RACI confirmed, primary client contacts named per workstream
- Shared project tracker accessible to all parties

---

### M2 — Discovery & Requirements Alignment `Weeks 1–2`

**Goal**  
Complete all discovery sessions and produce a signed-off requirements document that the technical and design workstreams can build against.

**What happens**  
- Structured interviews with front-desk staff, operations leads, and a provider representative
- Map current lead intake and scheduling process (current-state workflow)
- Define: lead sources, dormancy thresholds, outreach channels (SMS, email, voice), scheduling constraints, escalation triggers
- Draft and review future-state workflow map
- Agree on KPIs and pilot success thresholds

**Exit Criteria**  
- Requirements document signed off by client sponsor and Delivery Lead
- Future-state workflow map approved
- KPIs and pilot success thresholds documented and agreed

---

### M3 — Technical Design Checkpoint `Week 3`

**Goal**  
Confirm the integration architecture and conversation design approach are viable before build begins, catching any system access or API blockers early.

**What happens**  
- Integration Engineer presents: systems to connect (EHR, calendar, CRM), API availability, auth model, data flow diagram
- Conversation Designer presents: primary conversation flows, channel strategy, fallback/escalation design
- Client IT reviews and confirms sandbox access and API credentials
- Open items logged; blockers escalated immediately

**Exit Criteria**  
- Integration architecture diagram reviewed and approved (client IT + Delivery Lead)
- Conversation flow structure approved (client operations + Delivery Lead)
- Sandbox environment provisioned or timeline confirmed
- No unresolved blockers that would delay WS2/WS3 build

---

### M4 — Compliance Review Open `Weeks 3–4`

**Goal**  
Initiate formal compliance and privacy review in parallel with the build phase so that sign-off can be achieved before QA rather than after.

**What happens**  
- Share integration architecture diagram and conversation scripts with Compliance Lead and client Privacy Officer
- Complete HIPAA data flow assessment
- Confirm BAA status with AI platform vendor; initiate update if needed
- Review TCPA opt-in/opt-out mechanism in conversation flows
- Draft data retention and deletion policy

**Exit Criteria**  
- HIPAA data flow assessment complete with no critical unresolved gaps
- BAA confirmed or amendment in progress with hard deadline before M7
- TCPA mechanism approved in conversation design
- Compliance sign-off memo drafted (to be finalized at M7)

---

### M5 — Prototype / Integration Demo `Weeks 4–5`

**Goal**  
Demonstrate a working end-to-end prototype in a sandbox environment: agent receives an inbound or dormant lead trigger, conducts a scheduling conversation, and writes a confirmed appointment to the provider calendar.

**What happens**  
- Integration Engineer demonstrates live API connections: calendar read/write, lead record retrieval
- Conversation Designer demonstrates agent flows: inbound inquiry, dormant outreach, booking confirmation, escalation handoff
- Client operations and front-desk team observe and provide structured feedback
- Gaps and refinements logged in issue tracker

**Exit Criteria**  
- Successful end-to-end demo: lead → conversation → confirmed booking in sandbox calendar
- Feedback log reviewed; critical gaps assigned with owners and target dates
- Prototype accepted by Delivery Lead as QA-ready (or rework sprint defined)

---

### M6 — QA & Internal Review `Week 6`

**Goal**  
Execute structured QA across all conversation paths, integration scenarios, and edge cases. Complete internal review before client UAT.

**What happens**  
- QA Lead runs test plan: happy path, edge cases (no availability, patient declines, system timeout), fallback triggers, escalation routing
- Integration failure handling tested (calendar API down, EHR timeout)
- Bug log reviewed; P1/P2 issues resolved before UAT begins
- Client front-desk team conducts UAT: walks through key flows in sandbox as a simulated patient

**Exit Criteria**  
- All P1 bugs resolved; P2 bugs have documented workarounds or agreed resolution timeline
- UAT completed with client sign-off
- Go/no-go checklist populated (to be formally reviewed at M7)

---

### M7 — Launch-Readiness Review `Week 7`

**Goal**  
Conduct a formal go/no-go review with all workstream leads and client sponsor. Confirm every readiness criterion is met before pilot launch is authorized.

**What happens**  
- Delivery Lead chairs launch-readiness meeting
- Each workstream lead presents status against exit criteria
- Compliance Lead presents and finalizes sign-off memo
- Go/no-go checklist reviewed line by line
- Pilot scope confirmed: patient segment, providers, channels, duration, volume cap
- Client operations team confirms staff readiness for escalation handling
- Production credentials and monitoring infrastructure verified

**Exit Criteria**  
- Go/no-go decision formally recorded with client sponsor signature
- Compliance sign-off memo finalized and on file
- All production access confirmed and tested
- Monitoring dashboard live and verified
- Rollback plan documented

---

### M8 — Pilot Go-Live `Week 8`

**Goal**  
Launch the agent to a controlled pilot population, monitor live performance, and establish the weekly reporting cadence.

**What happens**  
- Agent activated for pilot patient segment and provider(s)
- Real-time monitoring in place: slot fill rate, response time, booking conversion, escalation rate, opt-out rate
- Delivery Lead and client operations lead on standby for first 48 hours
- Week 1 pilot performance report issued at end of Week 8
- Issue triage process active; hotfix path confirmed

**Exit Criteria**  
- Agent live and handling real patient interactions
- No P1 production issues in first 48 hours (or hotfix deployed and resolved)
- Week 1 performance data captured and reported
- Retrospective scheduled for end of pilot period

---

## Visual Timeline

```
Week 1   │ M1 Kickoff ──────────────────────────────────────────────────
Week 1-2 │          M2 Discovery & Requirements Alignment ──────────────
Week 3   │                    M3 Technical Design Checkpoint ────────────
Week 3-4 │                    M4 Compliance Review Open ────────────────►(closes M7)
Week 4-5 │                              M5 Prototype / Integration Demo ─
Week 6   │                                        M6 QA & Internal Review
Week 7   │                                                  M7 Launch-Readiness Review
Week 8   │                                                            M8 Pilot Go-Live
```
