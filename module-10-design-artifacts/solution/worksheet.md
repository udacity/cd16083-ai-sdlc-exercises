# Worksheet: generate and evaluate early-phase artifacts
Your name:

Keep `scenario-brief.md` open beside this worksheet; you will go back to it for every part. The artifacts you evaluate, the checklists, and the policy lines you need are printed here where you use them.

## Part B. The supplied sketch against the design checklist

The vendor architect's sketch, as pasted into the proposal (the same text is in `architecture-sketch-supplied.md`). An **architecture sketch** is a rough description of a system's main parts and how they connect, made early to test ideas. A **service** here is one program with one job, running on its own. The vendor's abbreviations: **PMS** and **EHR** both mean the clinic's existing records system; **PHI** is protected health information, the US legal term for health details about a person. A **modular monolith**, named in the last line, is one program with internal sections instead of many separate services.

**Block diagram**

```
   ┌────────────┐   ┌────────────┐   ┌──────────────┐
   │ Patient Web│   │ Mobile App │   │ Staff Portal │
   └─────┬──────┘   └─────┬──────┘   └──────┬───────┘
         └────────────────┼─────────────────┘
                   ┌──────▼───────┐
                   │ API Gateway  │ (TLS, rate limit, WAF)
                   └──────┬───────┘
                   ┌──────▼───────┐
                   │ Auth Service │ (OIDC, MFA, RBAC)
                   └──────┬───────┘
     ┌───────────┬─────────────┼─────────────┬────────────┐
┌────▼────┐ ┌────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐ ┌────▼─────┐
│ Booking │ │ Provider │ │  Patient  │ │ Location/ │ │ Notifi-  │
│ Service │ │ Schedule │ │  Profile  │ │ Resource  │ │ cations  │
│         │ │ Service  │ │  Service  │ │ Service   │ │ (SMS/    │
│         │ │          │ │           │ │           │ │  email)  │
└────┬────┘ └────┬─────┘ └─────┬─────┘ └─────┬─────┘ └────▲─────┘
     └───────────┴──────┬──────┴─────────────┘            │
                 ┌──────▼──────┐   events   ┌─────────────┴┐
                 │ PostgreSQL  ├───────────►│ Message Queue│
                 └──────┬──────┘            └──────────────┘
                 ┌──────▼──────┐          ┌─────────────────┐
                 │ Redis cache │          │ EHR/PMS Adapter │
                 └─────────────┘          └─────────────────┘
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

Score each item the same way: pass or fail, the part of the sketch or the gap, and a few words why. Item 2 is done for you as the example.

| # | Question, and what a "no" looks like | Pass or fail | Part of the sketch, or the gap | Why, in a few words |
|---|---|---|---|---|
| 1 | Is the brief's system of record still the record, with the write to it and its failure described? A no: appointments stored in a new place; the existing system "synced" or absent; nothing on a failed write. | fail | Booking Service; EHR/PMS Adapter | Appointments are stored in the new PostgreSQL database and the practice-management system is only "synced"; nothing on a failed write. |
| 2 | Are the brief's existing systems reused rather than duplicated? A no: a new part that does what an existing system already does. | fail | Notifications | Sends reminders by SMS and email; the practice-management system already sends them by text. |
| 3 | Is the reason for visit named, with where it is stored and who may read it? A no: the reason stored somewhere with no statement of who can see it. Encryption and logins say how data is protected, not who may read this field. | fail | Booking Service; Patient Profile Service | Stored "with the appointment" in PostgreSQL; nothing says who may read it. "PHI isolated and encrypted" is a how, not a who. |
| 4 | Does the number of parts fit the problem? A no: more than about six parts (every box in the diagram is a part) for a clinic this size, or the sketch itself saying a simpler shape would do. | fail | The diagram; the last sentence | Fourteen boxes for 400 patients a week, and the sketch's own last line says a modular monolith "is a reasonable starting point". |

Which failure would need the most rebuilding to put right after the system is built? Item number (1, 3, or 4): 1

## Part E. Your sketch

Paste the sketch the assistant returned, including its "Assumptions to confirm" list, between the two lines:

---------- sketch start ----------

**Cedar Clinic online booking: architecture sketch**

```
Patients (browser)            Front-desk staff / Administrators
        |                                  |
        v                                  v
[1 Patient booking site]          [2 Staff console]
        (new)                            (new)
            \                            /
             v                          v
                [3 Booking service] (new)
                 |                 |
                 v                 v
     [4 Booking database]   [5 Practice-management system (PMS)]
           (new)                     (existing)
                                         |
                                         v
                              [6 Reminder messages]
                              (existing, sends via the
                               clinic's messaging service)
```

1. **Patient booking site (new).** Patients identify themselves with name, date of birth, and phone number, matched against the PMS records through the booking service. They see open slots, book, move, and cancel at any hour. Reason for visit is a free-text field. It is never shown back on any patient-facing page.

2. **Staff console (new).** Front-desk staff see the day across all three locations, move appointments, book by phone, and override the double-booking rule for one slot. Administrators set each provider's bookable hours per location and view the change history.

3. **Booking service (new).** It enforces the rules:

- Patients book only within the bookable hours.
- No provider has two appointments in one slot unless staff override that slot.
- A cancellation under 24 hours before the appointment is allowed and marked late.

Every book, move, and cancel is written to the PMS first. A change is confirmed to the user only after the PMS accepts it.

4. **Booking database (new).** It holds the following:

- Provider hours and rules.
- The audit log of who changed what, which administrators can read.
- Late-cancellation flags.
- Reason for visit, stored in a restricted table. Only the booking service's staff-facing functions can read it, and they serve only signed-in front-desk staff and administrators. Patients and the patient site have no read path to it.

It holds no appointment as the only copy.

5. **Practice-management system (existing).** It remains the record of every appointment and is not changed. The booking service uses its existing interface to read and write appointments.

6. **Reminder messages (existing).** The PMS sends a text the day before each appointment through the clinic's messaging service. The new system sends no reminders. An appointment written to the PMS gets a reminder like any other.

**When the PMS write fails.** The booking service does not confirm the change. It tells the patient the booking did not go through and to try again or phone the clinic. For staff it shows the error. Nothing is kept as a pending appointment, so no appointment exists only in the new system. The failure is logged in the audit log. A move or cancel that fails leaves the original appointment unchanged.

**Assumptions to confirm**

- The PMS interface can read existing appointments and write new ones, so slot availability can be derived from it.
- The PMS interface can tell the booking service whether a write succeeded.
- The PMS can mark an appointment as a late cancellation, or the booking database holds that flag.
- Staff and administrators sign in with accounts the clinic already manages or will create. Administrators have a distinct role from front-desk staff.
- Patient identity matching can be done by looking up name, date of birth, and phone in the PMS.
- Reason for visit does not need to be written to the PMS.

---------- sketch end ----------

Score your sketch on two of the design-checklist questions from Part B, items 1 and 3, two of the three the direction's constraints were written from. Each is answered by finding something, and each row says when it passes.

| # | Question | How to check, and when it passes | Pass or fail | What you found |
|---|---|---|---|---|
| 1 | Is the practice-management system still the record, with the write and its failure described? | Find the part that writes to it. Find the sentence that says what happens when the write fails. Pass when both are there. | pass | part 3 (Booking service) ; failed write: described |
| 3 | Is the reason for visit named, with where it is stored and who may read it? | Find "reason for visit". Is there a place and a "who"? Pass when both are stated. | pass | stored in a restricted table in the booking database (part 4) ; read by signed-in front-desk staff and administrators only |

Audit-log check: this sketch's audit log records "who changed what", with no stored values, so the reason for visit stays in its restricted table. The earlier recorded sketch that Part H builds on records "the old and new values" of every change, which puts the reason for visit into the audit log as well.

## Part H. An alternative sketch and a decision record

The assistant's alternative sketch and its list of assumptions:

```
Alternative Architecture: One Combined Web App

One web app serves everyone, with role-based screens (patient, front-desk, admin), one booking
service holding the rules, provider hours and the audit log in one database, plus the
practice-management system and the messaging service. Four parts: two new and two existing.

Trade-off against the first sketch: fewer parts means less to run for a three-location clinic.
The cost is that a fault in the shared app can expose staff-only data to patients. The first
sketch separates the patient app from the staff app, which lowers that risk.

Reason for visit: only front-desk staff and administrators may read it. Because everyone shares
one app, this check must be tested on every screen and every data call.

Shared by both sketches:
1. The practice-management system's interface is fast enough for live booking and can reject or
   help detect two bookings for the same slot made at the same moment.
2. That interface has a place for the reason for visit and a late mark.
3. Slot length comes from the practice-management system's existing scheduling.
4. Patient identity can be checked by matching the three details against its records.
5. Staff and administrators have individual accounts with roles.
6. The clinic accepts a pause in online booking when the practice-management system is down.
7. How long the audit log is kept is not decided.
8. Someone at the clinic or a contractor can run and patch a web service.
(Abridged.)
```

| Field | Your entry |
|---|---|
| Decision | The six-part sketch: separate patient and staff web apps, a booking service, an audit log, the practice-management system as the record, the existing reminder messages. |
| Alternative considered | The four-part sketch: one web app with role-based screens, the rules and audit log inside the booking service's database. |
| Why it lost | Rule 4 says the reason for visit is visible only to clinic staff. The alternative puts patient and staff screens in one app and says itself the check "must be tested on every screen and every data call". Separate apps make the rule part of the design, not of the testing. Two fewer parts does not pay for that at 400 patients a week; a clinic with no IT staff (assumption 8) might reasonably choose the other way. |
| Assumptions both share that the clinic must confirm | (1) The interface is fast enough for live booking and can reject two bookings for one slot. (2) It has a place for the reason for visit and a late mark. (3) Slot length comes from it. (4) Patients can be identified by name, date of birth, and phone number. (5) Staff and administrators have accounts with roles. (6) Online booking pauses when the practice-management system is down. (7) Audit log retention is not set. (8) Someone can run and patch a web service. |
| Who decides | The practice manager, with the vendor's architect; assumptions 1 and 2 need the practice-management system's vendor. |

| Failure mode in the supplied stories or sketch | What it would cost in delivery | The quality gate that would catch it |
|---|---|---|
| The sketch stores appointments in its own database and "syncs" with the practice-management system (design item 1). | The core built around the wrong record; found when the front desk sees a booking in one system and not the other. Rebuild of the booking service and its data model. | A design review against the brief before any code; later and dearer, an integration test that books through the new system and reads the appointment back from the practice-management system. |
| The sketch's Notifications part sends its own reminders (design item 2). | Patients get two reminders with different timings; found by the front desk from complaints. | A design review that lists every existing system and asks what the new one duplicates. |
| Story 5 shows the reason for visit on the patient's confirmation screen and email (requirements item 4; design item 3). | Health detail sent to a patient's inbox in violation of the clinic's own rule. Found in production, by a patient. | A code review that checks what each screen and message may show against the data rule; a responsible-use check before release. |
