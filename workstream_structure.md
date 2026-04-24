# Patient Acquisition & Growth Agent — Workstream Structure

---

## Overview

This document defines the six major workstreams required to deliver the Patient Acquisition & Growth Agent. Each workstream has a clear objective, named owner, dependencies on other workstreams, and specific outputs that gate downstream work.

---

## Workstreams

---

### WS1 — Requirements & Workflow Discovery

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

### WS2 — Integrations & Scheduling Systems

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

### WS3 — Conversation Design & Knowledge Setup

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

### WS4 — Compliance & Privacy Review

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

### WS5 — QA & Pilot Readiness

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

### WS6 — Rollout & Performance Monitoring

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

## Dependency Map

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
