# Direction scaffold: an architecture sketch for Cedar Clinic

The Context describes the clinic, as `scenario-brief.md` does. The example part, the evaluation criteria, and two
constraints are written for you. You finish three constraints, then select everything below the
line, paste it into a new chat with your AI assistant, and send it.

Under *Constraints*, finish the three sentences. Each one turns a question from the design checklist
(the four printed in Part B of the worksheet) into a rule for the assistant:

1. "The practice-management system ..." Design-checklist item 1 asks: is the brief's system of record
   still the record, with the write to it and its failure described? Finish the sentence so the
   sketch must say how the new system writes to it and what happens when the write fails.
2. "The reason for visit ..." Design-checklist item 3 asks: is the reason for visit named, with where
   it is stored and who may read it? Finish the sentence so the sketch must say both.
3. "No more than ..." Design-checklist item 4 asks: does the number of parts fit the problem? Give
   the most parts allowed, counting the systems that already exist. Six is a good number for this
   clinic.

---------- Everything below this line is what you paste ----------

## What to produce

Using the context, constraints, example, and evaluation criteria below, write an architecture sketch for online appointment booking at Cedar Clinic.

## Context

Cedar Clinic is a family medical practice with three locations in one city and twelve providers. It sees about 400 patients a week. Today patients book by phone, 8 am to 6 pm, Monday to Friday.

Every appointment is recorded in the clinic's practice-management system, which stays the record of every appointment: anything the new booking system books, moves, or cancels must be written there, and no appointment may exist only somewhere else. It has an interface other software can use to read and write appointments. Reminder text messages already go out from it the day before each appointment, through a messaging service the clinic pays for.

Three user groups. Patients want to see open slots, book, move, and cancel at any hour; they identify themselves with the name, date of birth, and phone number the clinic has on file. Front-desk staff see the day across all three locations, move appointments when a provider runs late, book by phone for patients who do not use the web, and override a rule for one slot when a provider says so. Administrators (the practice manager and two location leads) set the rules and need to see who changed what.

Rules: (1) A cancellation less than 24 hours before the appointment is a late cancellation. It is still allowed; the system marks it late so the front desk can follow up. (2) No provider has two appointments in the same slot, unless front-desk staff deliberately override the rule for that slot. (3) An administrator sets each provider's bookable hours per location; patients book inside those hours only. (4) A reason for visit is collected at booking, as free text, and is visible only to clinic staff.

Out of scope: payments, insurance checks, video visits, and any change to the practice-management system itself.

## Constraints

- About 400 words plus a block diagram in text. Name every part of the system in the diagram, and for each part say whether it is new or already exists.
- Do not add systems, standards, or features the context does not mention. List anything you had to assume under a heading "Assumptions to confirm".
- The practice-management system
- The reason for visit
- No more than

## Example

One part described in the shape I want:

**Reminder messages (existing).** The practice-management system sends a text message the day before each appointment through the clinic's messaging service. The new system does not send reminders; an appointment it writes to the practice-management system gets a reminder like any other.

## Evaluation criteria

I will check the sketch against these before using it:
1. Is the practice-management system the record of appointments, with the write to it and its failure described?
2. Does the sketch reuse the existing reminder messages rather than adding its own?
3. Is the reason for visit named, with where it is stored and who may read it?
4. Does the number of parts fit a three-location clinic?
