# Transcript, Challenge 2 and Module 2 Demo: Direct, One Step Further: an alternative sketch and what each assumes

- Tool: GitHub Copilot Chat at github.com/copilot, Ask mode, default context ("All repositories")
- Model: Claude Sonnet 5.5
- Date: 2026-10-12
- Conversation: continued from `directed-sketch-first-run.md`; this is the second turn. The assistant had the direction and its own first sketch in front of it.
- Your output will vary. Backup for the Demo: Direct, One Step Further slide and the model run for Challenge 2.

## Prompt, exactly as sent

```
Give me one alternative architecture that meets the same constraints, then list what each of the two sketches assumes about the clinic that the context does not say.
```

## Response, unedited

# Alternative Architecture: One Combined Web App

This version drops the separate patient and staff front ends. One web app serves everyone, with role-based screens. It also keeps the booking rules and the audit log inside the same part.

## Block diagram

```
        [Web app: patient, front-desk, and admin screens]
        (new; one front end, one sign-in per role)
                          |
                          v
        +------------------------------------+
        |  Booking service (new)             |
        |  rules, provider hours, and the    |
        |  audit log in one database         |
        +------------------------------------+
                          |
                          v
        +------------------------------------+
        | Practice-management system         |
        | (existing; record of appointments) |
        +------------------------------------+
                          |
                          v
        [Messaging service] (existing)
```

That is four parts: two new and two existing. The audit log and the rules store are part of the booking service's database, not separate parts.

## Parts

**Web app (new).** One application with three sets of screens. Patients identify themselves with name, date of birth, and phone number, and then book, move, and cancel. Front-desk staff see the day across all three locations, move appointments, book by phone, and override the double-booking rule for one slot. Administrators set provider hours and read the audit log. The server decides what each role can see, not the screen.

**Booking service (new).** It enforces the rules:

- Patients book only inside the set hours.
- No provider is double-booked, unless staff override that slot.
- A cancellation under 24 hours is allowed and marked late.

Its database holds provider hours and an append-only audit log. It does not hold appointments. Each book, move, or cancel is written to the practice-management system first. Only on success is the audit entry made and the user told it worked. If the write fails, nothing changes, the user is told "not booked" or "not changed", and the failure is logged. Patients are told to try again or phone. Staff see the error and book by phone.

**Practice-management system (existing).** It stays the record of every appointment.

**Reminder messages (existing).** The practice-management system sends a text message the day before each appointment through the clinic's messaging service. The new system sends none.

## What the system must be like

- **Availability:** Booking is reachable 24 hours a day, 7 days a week. If the practice-management system is down, booking pauses and the phone line is the fallback. Staff screens must work 8 am to 6 pm, Monday to Friday.
- **Load:** About 400 patients a week and twelve providers. One modest deployment is enough.
- **Reason for visit:** Only front-desk staff and administrators may read it. The server refuses it to patients and anonymous users. Because everyone shares one app, this check must be tested on every screen and every data call.
- **Accountability:** Every change is attributed to a person.

## Trade-off against the first sketch

Fewer parts means less to run for a three-location clinic. The cost is that a fault in the shared app can expose staff-only data to patients. The first sketch separates the patient app from the staff app, which lowers that risk.

---

# What each sketch assumes about the clinic that the context does not say

## Shared by both sketches

1. The practice-management system's interface is fast enough for live booking and can reject or help detect two bookings for the same slot made at the same moment.
2. That interface has a place for the reason for visit and a late mark. If it does not, the booking service must keep them. That would break the "no appointment only elsewhere" rule for those fields and would need a decision.
3. Slot length comes from the practice-management system's existing scheduling.
4. Patient identity can be checked by matching the three details against the practice-management system's records, and failed attempts can be limited.
5. Staff and administrators have individual accounts with roles. The clinic has no such accounts system described today.
6. The clinic accepts a pause in online booking when the practice-management system is down, with the phone line as fallback.
7. How long the audit log is kept is not decided.
8. Someone at the clinic or a contractor can run and patch a web service. The context mentions no IT staff.

## Only in the first sketch

- The clinic accepts four new parts to run, in exchange for separating patient-facing and staff-facing software.

## Only in the alternative

- The clinic accepts a single shared app, with the extra testing burden on staff-only data, in exchange for fewer parts.
- One deployment can serve all three groups without staff screens being reachable from the public internet in a way that worries the clinic. The context does not say where staff are, for example inside the clinics only or also at home.
