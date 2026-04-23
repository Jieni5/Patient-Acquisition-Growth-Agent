# Patient Acquisition & Growth Agent — Dependency & Risk Review

---

## Overview

This document identifies the most critical dependencies and risks for the Patient Acquisition & Growth Agent engagement. Each risk is assessed for why it matters to delivery, how it will be monitored throughout the engagement, and how the team will mitigate it before it becomes a blocker.

Risks are organized from highest delivery impact to lowest.

---

## Risk Register

---

### R1 — CRM / Calendar Integration Complexity

**Why it matters**  
The agent's core value — booking appointments directly into provider calendars — depends entirely on reliable, real-time read/write access to the scheduling system and CRM. If the EHR or practice management system uses a proprietary API, lacks HL7/FHIR support, or requires a vendor-specific connector, integration can consume weeks of unplanned effort. A failure here blocks the prototype demo (M5) and delays every milestone downstream.

**How we monitor it**  
- Integration Engineer completes an API capability assessment in Week 1 alongside discovery
- Technical Design Checkpoint (M3) includes a hard gate: sandbox environment provisioned and at least one successful test API call demonstrated
- Integration risk flag raised immediately if vendor support is required and response SLA exceeds 5 business days

**How we mitigate it**  
- Identify and contact EHR/calendar vendor during Week 1, before discovery closes
- Prioritize systems with existing HL7/FHIR or open REST APIs (e.g., Epic MyChart, Athenahealth, Google Calendar, Microsoft Bookings)
- If direct API access is unavailable, scope a fallback: human-in-the-loop scheduling confirmation as an interim mechanism for the pilot
- Define a clear escalation path: if sandbox access is not confirmed by end of Week 2, Delivery Lead escalates to client IT and sponsor immediately

---

### R2 — Compliance Issues Around PHI and Patient Data

**Why it matters**  
The agent touches Protected Health Information (PHI) at every step: reading patient records to personalize outreach, transmitting scheduling data, and logging conversation history. A HIPAA violation — even during testing — can expose the client to regulatory liability and destroy trust. TCPA violations (contacting patients without proper consent) carry per-message fines. Compliance issues discovered late derail the launch-readiness review and may require architectural rework.

**How we monitor it**  
- Compliance Review (M4) opens at Week 3 and runs in parallel with the build — not after it
- Compliance Lead reviews the integration data flow diagram and all conversation scripts before QA begins
- A compliance sign-off memo is a hard prerequisite for the M7 Launch-Readiness Review
- Any use of real patient data in QA or testing requires prior written approval from the client Privacy Officer

**How we mitigate it**  
- Use only synthetic or anonymized test data in QA (Week 6) unless explicit written approval is granted
- Confirm BAA status with the AI platform vendor in Week 1; initiate amendment immediately if needed
- Build opt-in/opt-out into every outreach channel from day one — not as an afterthought
- Restrict PHI fields passed to the agent to the minimum necessary (e.g., first name, appointment type, provider preference — not full medical history)
- Document data retention and deletion policy before pilot launch

---

### R3 — Unclear Routing and Scheduling Rules

**Why it matters**  
Appointment scheduling is rarely simple: different providers have different availability windows, some appointment types require prior authorization, certain patients must be routed to specific locations or providers, and same-day slots may be reserved. If these rules are not fully captured during discovery, the agent will either fail to book correctly, double-book, or route patients to the wrong provider — eroding clinical staff trust immediately and likely killing adoption.

**How we monitor it**  
- Discovery sessions (WS1) include a dedicated scheduling rules workshop with the front-desk team and at least one provider
- A scheduling rules matrix is produced as a WS1 output and signed off before WS3 conversation design begins
- QA test plan (M6) includes explicit test cases for routing edge cases: unavailable provider, appointment type mismatch, insurance constraint

**How we mitigate it**  
- Do not begin conversation design until the scheduling rules matrix is approved — partial rules lead to partial flows that must be rebuilt
- Where rules are ambiguous, document the assumption explicitly and get written client confirmation
- Build a clear fallback for unresolvable routing: agent informs the patient it cannot complete booking and transfers to a human scheduler
- Pilot with a single provider or appointment type to limit routing complexity in Week 8; expand scope only after rules are validated in production

---

### R4 — Poor Lead Data Quality

**Why it matters**  
The agent's dormant patient re-engagement capability depends on having accurate, reachable contact records: valid phone numbers, current email addresses, and up-to-date consent flags. If the lead or patient database is stale, duplicated, or missing opt-in records, outreach will fail to reach patients, generate opt-out spikes, or — in the worst case — contact patients who have explicitly asked not to be contacted, creating a TCPA liability.

**How we monitor it**  
- Data quality assessment is scoped as a WS1 output: Integration Engineer and Business Analyst run a sample analysis of the CRM/patient database in Week 1–2
- Key metrics reviewed: percentage of records with valid contact info, age of last contact attempt, presence of consent flags
- Lead data quality score reported at Technical Design Checkpoint (M3)

**How we mitigate it**  
- Run a data cleanse pass before pilot: de-duplicate records, suppress contacts older than a defined threshold (e.g., 18 months with no contact), validate opt-in status
- Define a minimum data quality threshold for pilot eligibility (e.g., records must have a valid email or phone and a documented opt-in)
- Do not attempt to contact patients with missing consent records — flag them for manual review by client staff
- Build suppression list logic into the agent from day one: do not re-contact patients who have opted out or been seen recently

---

### R5 — Escalation and Fallback Gaps in Patient Conversations

**Why it matters**  
Patients will ask questions the agent cannot answer, express frustration, describe urgent symptoms, or request to speak with a person. If the agent lacks clear escalation paths — or worse, loops patients in a dead-end conversation — it creates a poor patient experience, increases complaint risk, and in clinical edge cases (e.g., a patient describing an emergency) could pose a safety risk. Escalation failures are also a fast path to clinical staff distrust.

**How we monitor it**  
- Escalation triggers and fallback logic are defined in WS3 as a required output, reviewed by client operations before staging deployment
- QA test plan (M6) includes specific escalation test cases: patient requests human, agent hits unknown input three times, patient mentions urgent or emergency language
- Post-pilot: escalation rate tracked weekly; a spike indicates unhandled conversation paths

**How we mitigate it**  
- Define and document all escalation triggers before conversation design begins: urgent symptom keywords, explicit human request, repeated failed understanding, end-of-business-hours routing
- Every conversation path must have a defined exit: either a successful booking, a human handoff, or a graceful close with a callback option
- Agent never presents itself as a clinician and always offers a human alternative within two failed attempts to resolve a query
- Establish a monitored handoff channel (e.g., SMS to on-call front-desk staff) so escalated conversations are not dropped

---

### R6 — Low Response Quality from the Agent

**Why it matters**  
If the agent gives incorrect, vague, or off-brand responses — wrong insurance information, incorrect hours, misquoted provider names — patients lose confidence, call the front desk to verify, or abandon the booking entirely. Repeated quality failures undermine the business case for the agent and make clinical staff reluctant to trust it with real patients.

**How we monitor it**  
- Knowledge base accuracy reviewed by client operations team as part of WS3 sign-off
- Internal QA in Week 6 includes a response quality review: a set of representative patient questions evaluated against expected answers
- Post-pilot: track escalation-to-human rate as a proxy for response quality failures; review conversation logs weekly for the first four weeks

**How we mitigate it**  
- Build the knowledge base from authoritative client sources only: official website, current fee schedules, verified provider bios — not from memory or inference
- Client operations team reviews and approves every FAQ response and scheduling script before staging deployment
- Scope the knowledge base conservatively for the pilot: cover the top 20 most common patient questions rather than attempting comprehensive coverage on day one
- Build a "I'm not sure — let me connect you with our team" response for any out-of-scope question rather than allowing the agent to guess

---

### R7 — Unanswered Operational Edge Cases

**Why it matters**  
Real patient interactions surface scenarios that no one anticipated in discovery: a patient wants to book for a family member, a provider is on unexpected leave, a patient has a complex insurance situation, or a slot is cancelled while the patient is mid-conversation. If the team has not defined handling for these cases, the agent will either fail silently, give a wrong answer, or produce an inconsistent experience that requires manual cleanup.

**How we monitor it**  
- Discovery sessions include an explicit edge case workshop: "what are the ten things that go wrong most often with scheduling?"
- Edge cases are logged in the requirements document and each is assigned a handling decision: agent handles, agent escalates, or out of scope for pilot
- QA test plan includes a dedicated edge case suite

**How we mitigate it**  
- Time-box edge case handling for the pilot: the agent does not need to handle every scenario on day one, but every unhandled scenario must have a documented graceful fallback
- Establish a weekly edge case review in the first four weeks of pilot: client operations logs new scenarios encountered, team prioritizes which to address in the next iteration
- Pilot scope restriction is itself a mitigation: limiting to one appointment type and a small provider pool reduces edge case surface area dramatically

---

### R8 — Stakeholder Misalignment

**Why it matters**  
Hospital engagements typically involve multiple stakeholders with different priorities: operations wants efficiency, clinical staff want control, IT wants security, and marketing wants conversion metrics. If these groups have conflicting expectations about what the agent will and will not do — and those conflicts are not surfaced and resolved during discovery — they will re-emerge during UAT or launch readiness and stall sign-off.

**How we monitor it**  
- Kickoff meeting (M1) explicitly surfaces stakeholder priorities and areas of potential tension
- Requirements document sign-off requires sign-off from operations, IT, and clinical leadership — not just one sponsor
- Weekly steering updates include a standing agenda item: open issues and decisions needed

**How we mitigate it**  
- RACI established at kickoff: one named decision-maker per workstream on the client side
- Scope disagreements escalated to the executive sponsor within 48 hours rather than resolved informally between workstream owners
- Pilot framing helps: positioning Week 8 as a "learning exercise with defined success criteria" rather than a full production launch reduces the stakes of individual stakeholder objections and creates space for iteration

---

## Dependency Map

```
Client IT access & API credentials ──────────────────► R1 (Integration Complexity)
Client data quality & consent records ───────────────► R4 (Lead Data Quality)
Scheduling rules matrix (WS1 output) ────────────────► R3 (Routing Rules)
                                                      ► R7 (Edge Cases)
Compliance sign-off (WS4) ───────────────────────────► R2 (PHI / Compliance)
Knowledge base approval (WS3) ───────────────────────► R6 (Response Quality)
Escalation logic design (WS3) ───────────────────────► R5 (Escalation Gaps)
Stakeholder RACI (M1) ───────────────────────────────► R8 (Misalignment)
```

---

## Risk Summary Table

| # | Risk | Impact | Likelihood | Primary Mitigation |
|---|---|---|---|---|
| R1 | CRM/calendar integration complexity | High | Medium | API assessment Week 1; fallback scope defined |
| R2 | Compliance / PHI exposure | High | Medium | Compliance track opens Week 3; BAA confirmed early |
| R3 | Unclear scheduling/routing rules | High | High | Rules matrix signed off before conversation design |
| R4 | Poor lead data quality | Medium | High | Data quality assessment before pilot; suppression logic |
| R5 | Escalation/fallback gaps | High | Medium | Escalation logic required WS3 output; QA test suite |
| R6 | Low agent response quality | Medium | Medium | Knowledge base from authoritative sources; ops sign-off |
| R7 | Unanswered operational edge cases | Medium | High | Edge case workshop in discovery; graceful fallbacks |
| R8 | Stakeholder misalignment | Medium | Medium | RACI at kickoff; exec sponsor escalation path |
