# Patient Acquisition & Growth Agent — Delivery Plan: Workstream Structure

## Engagement Overview

**Solution:** AI-powered Patient Acquisition & Growth Agent  
**Core Capabilities:** 
- Personalized inbound/dormant lead outreach
- Patient Q&A
- Direct appointment scheduling into provider calendars  

**Client Goals:** Fill open slots via waitlist activation, engage leads within seconds, automate scheduling conversations

---

## Workstream Structure

---

### 1. Requirements & Workflow Discovery

**Objective**  
Capture the end-to-end patient journey, define lead sources and dormancy criteria, map current scheduling workflows, and establish success metrics before any build begins.

**Owner / Function**  
Delivery Lead + Business Analyst (with active client participation from operations and front-desk teams)

**Major Dependencies**  
- Client availability for discovery sessions (operations, front desk, clinical leadership)
- Access to current CRM/EHR data to understand lead and patient record structure
- Agreement on what constitutes a "dormant" patient and target patient segments

**Primary Outputs**  
- Signed-off requirements document covering lead sources, outreach triggers, and scheduling rules
- Current-state workflow map (how leads are handled today)
- Future-state workflow map (how the agent will change those flows)
- Agreed KPIs: slot fill rate, response time, booking conversion rate, opt-out rate
- Risk and assumption log

---

### 2. Integrations & Scheduling Systems

**Objective**  
Establish reliable, secure connections between the AI agent and the client's EHR/practice management system, provider calendars, and CRM or lead database so that the agent can read availability and write confirmed appointments in real time.

**Owner / Function**  
Integration Engineer / Technical Lead

**Major Dependencies**  
- WS1 output: confirmed systems of record (EHR, calendar platform, CRM)
- Client IT access: API credentials, sandbox/test environment, firewall approvals
- EHR/calendar vendor support for API or HL7/FHIR endpoints
- Compliance sign-off on data flows (feeds into WS4)

**Primary Outputs**  
- Integration architecture diagram (data flow, systems touched, auth model)
- Working API connections to: provider calendar(s), EHR or scheduling system, lead/patient database
- Sandbox environment with test data for QA
- Integration test results and error-handling documentation

---

### 3. Conversation Design & Knowledge Setup

**Objective**  
Design the agent's end-to-end conversation flows for inbound inquiries, dormant patient re-engagement, and appointment booking. Build and validate the knowledge base the agent uses to answer patient questions accurately.

**Owner / Function**  
Conversation Designer / AI Product Lead

**Major Dependencies**  
- WS1 output: patient journey map, key questions patients ask, scheduling rules and constraints
- WS2 output: confirmed integration capabilities (what the agent can actually read/write at runtime)
- Client sign-off on tone, brand voice, and escalation paths (when to hand off to a human)
- Compliance guidance on what the agent may and may not say (feeds from WS4)

**Primary Outputs**  
- Conversation flow diagrams for all primary paths: inbound lead, dormant outreach, scheduling, FAQ, escalation
- Approved script/prompt library with response templates
- Knowledge base covering services, providers, insurance accepted, location/hours, common FAQs
- Fallback and human-handoff logic documentation
- Agent configuration deployed to staging environment

---

### 4. Compliance & Privacy Review

**Objective**  
Ensure the agent's data handling, patient communications, and scheduling actions comply with HIPAA, applicable state privacy laws, and the client's internal policies. Identify and mitigate risk before any patient-facing go-live.

**Owner / Function**  
Compliance Lead / Legal Counsel (client-side Privacy Officer as key stakeholder)

**Major Dependencies**  
- WS2 output: data flow and integration architecture (to assess what PHI moves where)
- WS3 output: conversation scripts and knowledge base (to review for prohibited claims or disclosures)
- Client's existing BAA (Business Associate Agreement) status with vendors
- Regulatory landscape: HIPAA, TCPA (for outreach via SMS/email), state telehealth rules if applicable

**Primary Outputs**  
- HIPAA data flow assessment and gap analysis
- Approved data retention and deletion policy for agent interactions
- TCPA-compliant opt-in/opt-out mechanism confirmed in conversation flows
- Signed or updated BAA with AI platform vendor
- Compliance sign-off memo required before WS5 QA with real patient data

---

### 5. QA & Pilot Readiness

**Objective**  
Validate that the full system — integrations, conversation flows, scheduling writes, and escalation paths — works correctly and safely under realistic conditions before exposing it to live patients.

**Owner / Function**  
QA Lead + Delivery Lead (with client front-desk team participating in UAT)

**Major Dependencies**  
- WS2 output: stable integration environment with test data
- WS3 output: agent deployed to staging with all flows configured
- WS4 output: compliance sign-off (required before testing with any real or representative PHI)
- Defined test scenarios and acceptance criteria from WS1

**Primary Outputs**  
- QA test plan covering: happy path booking, edge cases, fallback triggers, integration failure handling
- Bug log and resolution tracker
- User Acceptance Testing (UAT) results with client sign-off
- Pilot scope definition: which patient segment, which providers, which channels, duration
- Go/no-go checklist completed and approved by Delivery Lead and client sponsor

---

### 6. Rollout & Performance Monitoring

**Objective**  
Execute a controlled pilot launch, monitor agent performance against agreed KPIs, gather user feedback, and establish the operating rhythm for ongoing optimization and potential full rollout.

**Owner / Function**  
Delivery Lead + Client Operations Lead (ongoing support by AI Product Lead and Integration Engineer)

**Major Dependencies**  
- WS5 output: go/no-go approval, UAT sign-off
- Live system access: production calendar, EHR, CRM credentials
- Client staff trained on escalation handling and how to review agent activity
- Monitoring and alerting infrastructure in place

**Primary Outputs**  
- Pilot launch executed for defined patient/provider segment
- Live monitoring dashboard tracking: slot fill rate, lead response time, booking conversion, escalation rate, opt-out rate
- Weekly performance report cadence established
- Issue triage and hotfix process documented
- Pilot retrospective with go/full-rollout recommendation
- Handoff documentation and runbook for client operations team

---

## Workstream Dependency Summary

```
WS1 (Discovery)
  └─► WS2 (Integrations)
  └─► WS3 (Conversation Design)
        └─► WS4 (Compliance) ◄── WS2
              └─► WS5 (QA & Pilot Readiness) ◄── WS2, WS3
                    └─► WS6 (Rollout & Monitoring)
```

WS1 is the critical prerequisite. WS2 and WS3 can progress in parallel once WS1 is complete. WS4 runs concurrently with WS2 and WS3 but must formally close before WS5 touches any real patient data. WS5 gates WS6.

---

## Key Roles Summary

| Role | Workstreams |
|---|---|
| Delivery Lead | WS1, WS5, WS6 |
| Business Analyst | WS1 |
| Integration Engineer | WS2 |
| Conversation Designer / AI Product Lead | WS3, WS6 |
| Compliance Lead / Legal | WS4 |
| QA Lead | WS5 |
| Client Operations Lead | WS1, WS5, WS6 |
| Client IT / Privacy Officer | WS2, WS4 |

---

---

## Milestones & Timeline — Weeks 1–8

### Timeline at a Glance

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

### Milestone Detail

---

#### M1 — Project Kickoff `Week 1`

**Goal**  
Align all stakeholders on scope, roles, ways of working, and success criteria before any discovery work begins.

**What happens**  
- Kickoff meeting with client sponsors, operations, IT, and delivery team
- Confirm engagement scope, out-of-scope items, and prototype boundaries
- Establish communication cadence: weekly steering update, async issue log, shared workspace
- Distribute and agree on the workstream structure and this milestone plan

**Exit Criteria**  
- Kickoff deck presented and questions resolved
- RACI confirmed, primary client contacts named per workstream
- Shared project tracker accessible to all parties

---

#### M2 — Discovery & Requirements Alignment `Weeks 1–2`

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

#### M3 — Technical Design Checkpoint `Week 3`

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

#### M4 — Compliance Review Open `Weeks 3–4`

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

#### M5 — Prototype / Integration Demo `Weeks 4–5`

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

#### M6 — QA & Internal Review `Week 6`

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

#### M7 — Launch-Readiness Review `Week 7`

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

#### M8 — Pilot Go-Live `Week 8`

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

### Milestone Summary — Visual Timeline

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

**Critical path:** M1 → M2 → M3 → M5 → M6 → M7 → M8  
**Parallel track:** M4 (Compliance) runs concurrently from Week 3 and must close by M7.
