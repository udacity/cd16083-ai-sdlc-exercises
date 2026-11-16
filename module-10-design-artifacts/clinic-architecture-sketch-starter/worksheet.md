# Lab 2 worksheet: generate and evaluate early-phase artifacts
Your name:

Fill this in as the lab guide directs. Keep `scenario-brief.md` open beside this worksheet; you will go back to it for every part. The two artifacts you evaluate, both checklists, and the policy lines you need are printed here where you use them. Do not open anything in `solutions/` until the lab guide says to.

## Part B. The supplied sketch against the design checklist

The vendor architect's sketch, as pasted into the proposal (the same text is in `architecture-sketch-supplied.md`). An **architecture sketch** is a rough description of a system's main parts and how they connect, made early to test ideas. A **service** here is one program with one job, running on its own. The vendor's abbreviations: **PMS** and **EHR** both mean the clinic's existing records system; **PHI** is protected health information, the US legal term for health details about a person. A **modular monolith**, named in the last line, is one program with internal sections instead of many separate services.

**Block diagram**

```
        ┌────────────┐   ┌────────────┐   ┌──────────────┐
        │ Patient Web│   │ Mobile App │   │ Staff Portal │
        └─────┬──────┘   └─────┬──────┘   └──────┬───────┘
              └────────────────┼─────────────────┘
                        ┌──────▼───────┐
                        │ API Gateway  │  (TLS, rate limit, WAF)
                        └──────┬───────┘
                        ┌──────▼───────┐
                        │ Auth Service │  (OIDC, MFA, RBAC)
                        └──────┬───────┘
     ┌───────────┬─────────────┼─────────────┬────────────┐
┌────▼────┐ ┌────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐ ┌────▼─────┐
│ Booking │ │ Provider │ │ Patient   │ │ Location/ │ │ Notifi-  │
│ Service │ │ Schedule │ │ Profile   │ │ Resource  │ │ cations  │
│         │ │ Service  │ │ Service   │ │ Service   │ │ (SMS/    │
│         │ │          │ │           │ │           │ │ email)   │
└────┬────┘ └────┬─────┘ └─────┬─────┘ └─────┬─────┘ └────▲─────┘
     └───────────┴──────┬──────┴─────────────┘            │
                 ┌──────▼──────┐   events   ┌─────────────┴┐
                 │ PostgreSQL  ├───────────►│ Message Queue│
                 └──────┬──────┘            └──────────────┘
                 ┌──────▼──────┐   ┌─────────────────┐
                 │ Redis cache │   │ EHR/PMS Adapter │
                 └─────────────┘   └─────────────────┘
```

**Key components**

- **Clients:** a responsive web app, a mobile app, and a staff portal for booking, rescheduling, and walk-ins.
- **API Gateway and Auth:** TLS and rate limiting at the gateway; OIDC with MFA for staff and role-based access scoped per location.
- **Booking Service:** searches availability and holds, confirms, reschedules, and cancels appointments. Stores each appointment, with the patient's reason for visit, in the PostgreSQL database. Prevents double-booking with a short-lived slot hold (Redis) plus a database constraint.
- **Provider Schedule Service:** working hours, time off, appointment types and durations, buffer times.
- **Location/Resource Service:** the three locations, rooms, and equipment.
- **Patient Profile Service:** demographics, insurance, and preferences. Keeps PHI isolated and encrypted.
- **Notifications:** consumes events from the queue and sends confirmations, reminders, and waitlist offers by SMS and email.
- **EHR/PMS Adapter:** syncs appointments with the clinic's records system (HL7/FHIR) through an anti-corruption layer.

**Data and infrastructure.** A single PostgreSQL database with a primary and a replica; Redis for availability caching and slot holds; a queue for events such as `AppointmentBooked` and `AppointmentCancelled`.

**Cross-cutting concerns.** Compliance: HIPAA, encryption at rest and in transit, audit logs. Reliability: stateless services in containers across multiple availability zones, with autoscaling. Extras: waitlist auto-fill, no-show tracking, optional telehealth links.

A modular monolith is a reasonable starting point for a three-site clinic. The service boundaries above can be split out later if needed.

Same method as Part A: pass or fail, the part of the sketch or the gap, a few words why. Item 2 is done for you as the example.

| # | Question, and what a "no" looks like | Pass or fail | Part of the sketch, or the gap | Why, in a few words |
|---|---|---|---|---|
| 1 | Is the brief's system of record still the record, with the write to it and its failure described? A no: appointments stored in a new place; the existing system "synced" or absent; nothing on a failed write. | | | |
| 2 | Are the brief's existing systems reused rather than duplicated? A no: a new part that does what an existing system already does. | fail | Notifications | Sends reminders by SMS and email; the practice-management system already sends them by text. |
| 3 | Is the reason for visit named, with where it is stored and who may read it? A no: the reason stored somewhere with no statement of who can see it. Encryption and logins say how data is protected, not who may read this field. | | | |
| 4 | Does the number of parts fit the problem? A no: more than about six parts (every box in the diagram is a part) for a clinic this size, or the sketch itself saying a simpler shape would do. | | | |

Which failure would need the most rebuilding to put right after the system is built? Item number (1, 3, or 4): ____

## Part E. Your sketch

Paste the sketch the assistant returned, including its "Assumptions to confirm" list, between the two lines:

---------- sketch start ----------

---------- sketch end ----------

Score your sketch on two of the design-checklist questions from Part B, items 1 and 3, two of the three the direction's constraints were written from. Each is answered by finding something, and each row says when it passes.

| # | Question | How to check, and when it passes | Pass or fail | What you found |
|---|---|---|---|---|
| 1 | Is the practice-management system still the record, with the write and its failure described? | Find the part that writes to it. Find the sentence that says what happens when the write fails. Pass when both are there. | | part ____ ; failed write: described / not described |
| 3 | Is the reason for visit named, with where it is stored and who may read it? | Find "reason for visit". Is there a place and a "who"? Pass when both are stated. | | stored in ____ ; read by ____ |

## Part H. Challenge 2: an alternative sketch and a decision record

The assistant's alternative sketch and its list of assumptions:

```
(paste here)
```

| Field | Your entry |
|---|---|
| Decision | (which sketch, in one line) |
| Alternative considered | (the other, in one line) |
| Why it lost | (two or three lines) |
| Assumptions both share that the clinic must confirm | (list) |
| Who decides | (a role at the clinic) |

| Failure mode in the supplied stories or sketch | What it would cost in delivery | The quality gate that would catch it |
|---|---|---|
| | | |
| | | |
| | | |
