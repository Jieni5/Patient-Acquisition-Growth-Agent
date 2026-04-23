# Technical Readiness Note — Scheduling & Calendar Integration

**Workstream:** WS2 — Integrations & Scheduling Systems  
**Prepared for:** Delivery Lead, Integration Engineer, Client IT  
**Purpose:** Define what must be true before build begins on the scheduling and calendar integration layer

---

## Why This Workstream First

Scheduling is the engagement's critical path. Every other workstream — conversation design, QA, pilot scope — assumes the agent can read provider availability and write confirmed appointments in real time. If this integration cannot be established reliably before Week 4, the prototype demo slips and every downstream milestone moves with it. This note defines exactly what "ready to build" means for this layer so the team can assess readiness early and resolve blockers before they compound.

---

## Technical Inputs Required

These artifacts must exist before build begins:

| Input | Description | Who Provides |
|---|---|---|
| System of record confirmation | Which system is the authoritative source for provider availability and appointment booking (EHR, practice management system, or standalone calendar) | Client Operations + IT |
| API documentation | Official API docs or integration guide for the scheduling system (REST, HL7 FHIR, proprietary SDK) | EHR/calendar vendor |
| Sandbox / test environment | A non-production environment with representative provider schedules and appointment types that can be safely written to during development | Client IT |
| API credentials | Client ID, secret, OAuth tokens, or API keys for sandbox access | Client IT |
| Appointment type definitions | Full list of bookable appointment types, durations, and any constraints (e.g., new patient vs. follow-up, insurance required, referral needed) | Client Operations |
| Provider availability rules | Which providers are bookable via the agent, their hours, and any blackout windows | Client Operations + Clinical Lead |
| Firewall / network access | Confirmation that the agent's hosting environment can reach the scheduling system's API endpoints | Client IT |

---

## Systems and Teams That Must Be Involved

**Client-side:**
- **Client IT / EHR Administrator** — owns API access, sandbox provisioning, firewall rules, and credential issuance
- **Practice Operations Manager** — owns the scheduling rules, appointment type definitions, and provider availability configurations
- **Clinical Lead or Provider Representative** — must validate that the agent's booking logic respects clinical constraints (e.g., no double-booking, no booking outside provider's scope)
- **Privacy Officer** — must review what patient and provider data fields the integration reads and writes before build begins (feeds WS4)

**Vendor-side:**
- **EHR or Practice Management Vendor** (e.g., Epic, Athenahealth, Kareo, Jane App) — may need to issue API access, enable specific API modules, or provide a sandbox environment; vendor SLA for this must be confirmed in Week 1
- **Calendar Platform Vendor** (if applicable, e.g., Google Workspace, Microsoft 365) — if provider calendars are managed separately from the EHR, a second integration path must be scoped

**Delivery-side:**
- **Integration Engineer** — owns the connection design, error handling, and sandbox testing
- **Compliance Lead** — reviews data flow before build (what PHI fields cross which system boundary)

---

## Questions That Must Be Answered Before Build Begins

These are open questions that, if left unanswered, will cause rework mid-build:

1. **What is the scheduling system?**  
   EHR with built-in scheduling (e.g., Epic, Athenahealth), standalone practice management tool (e.g., Kareo, Jane), or a separate calendar platform (Google, Outlook)? Each has a different integration path.

2. **Does the system have a supported API for external booking?**  
   Some EHRs expose read-only APIs but do not allow external write access for appointment creation. If write access is unavailable, what is the fallback?

3. **What authentication model does the API use?**  
   OAuth 2.0, API key, SMART on FHIR, or session-based? This determines how credentials are managed and rotated.

4. **Can the API return real-time availability?**  
   Or does it require a polling model with potential staleness? Real-time is required for a good patient experience; polling introduces race conditions where a slot appears available but is already taken.

5. **What appointment data fields are required to create a booking?**  
   Minimum fields needed (patient ID, provider ID, slot time, appointment type) vs. fields the system enforces as mandatory (insurance ID, referring provider, chief complaint).

6. **How are appointment conflicts handled at the API level?**  
   Does the system return a conflict error if a slot is taken between availability check and booking write? How should the agent handle this gracefully?

7. **Are there rate limits or throttling on the API?**  
   Relevant if the agent is handling multiple concurrent outreach conversations.

8. **What patient identifier is used?**  
   Does the scheduling system expect a system-specific patient ID that must be looked up from the CRM first, or can it match on name and date of birth?

9. **Who owns the sandbox environment and how quickly can it be provisioned?**  
   If vendor provisioning is required, this could take 1–3 weeks. Must be initiated in Week 1.

10. **Has legal reviewed the data sharing between the agent platform and the EHR?**  
    Specifically: does passing PHI to the AI agent require an updated or new BAA with the AI platform vendor?

---

## What Could Go Wrong Technically

| Risk | Details | Probability |
|---|---|---|
| No external write access to the EHR | Some EHR vendors lock appointment creation to their own UI or certified partners only. Discovery may reveal the agent can read availability but cannot write bookings. | Medium |
| Sandbox not available until mid-engagement | Vendor provisioning delays or IT queue depth push sandbox access past Week 3, compressing QA time. | Medium |
| Real-time availability not supported | The API returns cached or batch-updated availability, meaning the agent books slots that are already taken — resulting in double-bookings surfaced only at the clinic. | Low–Medium |
| Patient ID resolution failure | The CRM lead record does not carry a matching EHR patient ID, requiring a lookup-by-demographics step that adds latency and error surface. | Medium |
| Auth token expiry mid-conversation | If OAuth tokens expire during an active booking flow and refresh logic is not implemented, the booking write fails silently. | Low |
| Appointment type field mismatch | The appointment types configured in the EHR do not match the names used in the conversation design, causing booking failures for certain appointment categories. | Medium |
| Firewall blocks API calls from agent host | Client network policy may not permit outbound API calls from an external hosted service to the internal EHR endpoint without a VPN or allowlist configuration. | Medium |

---

## What "Ready to Build" Means

Build on the scheduling integration should not begin until **all of the following are true:**

- [ ] Scheduling system and calendar platform confirmed and documented
- [ ] API documentation reviewed by Integration Engineer; write access for appointment creation confirmed
- [ ] Sandbox environment provisioned and accessible from the development environment
- [ ] API credentials issued and a successful test call (read availability) demonstrated
- [ ] Appointment type definitions and provider availability rules received from client operations
- [ ] Patient identifier resolution path defined (how the agent maps a lead record to an EHR patient ID)
- [ ] Conflict and error handling behavior documented (what the agent does if a slot is unavailable at write time)
- [ ] Compliance Lead has reviewed the integration data flow and confirmed no blocking PHI concerns
- [ ] Firewall / network access confirmed for the agent's hosting environment

If any item above is unchecked at the Technical Design Checkpoint (M3, Week 3), the item becomes a tracked blocker with an owner and a resolution deadline. Items unchecked by end of Week 4 trigger a pilot scope adjustment discussion with the Delivery Lead and client sponsor.

---

## Recommended First Action

During Week 1, the Integration Engineer should request the following from client IT in a single written communication, with a response deadline of end of Week 2:

1. Name and version of the scheduling/EHR system in use
2. Whether an external API is available for appointment reads and writes
3. Contact at the EHR vendor for API access and sandbox provisioning
4. Estimated time to provision sandbox access
5. Network / firewall requirements for external API access
