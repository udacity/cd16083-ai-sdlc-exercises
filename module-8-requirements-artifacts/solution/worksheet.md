# Lab 2 worksheet: generate and evaluate early-phase artifacts
Your name:

Fill this in as the lab guide directs. Keep `scenario-brief.md` open beside this worksheet; you will go back to it for every part. The two artifacts you evaluate, both checklists, and the policy lines you need are printed here where you use them. Do not open anything in `solutions/` until the lab guide says to.

## Part A. The supplied stories against the requirements checklist

The practice manager's stories, as the vendor received them (the same text is in `user-stories-supplied.md`). A **user story** is one sentence of what a user needs and why, in the form "As a …, I want …, so that …". **Acceptance criteria** are the checkable conditions a story must meet to count as done.

**Story 1.** As a patient, I want to create an account with my email address, so that I can book appointments online.

- Email address is verified before the account is activated.
- Duplicate accounts are rejected.

**Story 2.** As a patient, I want to search for open slots by provider, location, and date, so that I can find a time that suits me.

- Only slots that are open right now are shown.
- The three filters can be combined.

**Story 3.** As a patient, I want to select a slot and confirm my booking, so that my time is reserved.

**Story 4.** As a patient, I want to cancel an appointment at any time, so that the slot can be released for others.

- A cancelled slot is returned to availability.
- The patient receives a cancellation confirmation by email.

**Story 5.** As a patient, I want to describe my reason for the visit when I book, so that the provider can prepare.

- The reason is free text, up to 200 characters.
- The reason is shown on the patient's confirmation screen and in the confirmation email.

**Story 6.** As the clinic, we need patient data encrypted with AES-256 in line with HIPAA, so that it is legally protected.

- Data is encrypted in transit and at rest.

**Story 7.** As an administrator, I want to set a cancellation window, so that the clinic's policy is enforced automatically.

- The window is 24 hours.
- A cancellation inside the window is refused by the system.

**Story 8.** As an administrator, I want to set each provider's bookable hours at each location, so that patients can book only inside them.

- Hours are set separately per provider per location.
- After a change, patients see only slots inside the new hours.

Three of the six questions are worked for you (items 2, 3, and 5). Score the other three by finding something, as each row says; each row says when it passes. Write **pass** or **fail** and what you found.

| # | Question, and what a "no" looks like | How to check, and when it passes | Pass or fail | What you found |
|---|---|---|---|---|
| 1 | Does every user group in the brief have at least one story? A no: a user group named in the brief does not have a story. | Count the stories for patients, for front-desk staff, and for administrators (the three groups the brief names). Pass when all three counts are 1 or more. | fail | patients 5 front desk 0 administrators 2 |
| 2 | Does every story have acceptance criteria someone could check? A no: a story has no criteria, or criteria that cannot be tested ("works well"). | Worked for you. | fail | Story 3 has no criteria, so there is no way to say when it is done. |
| 3 | Do the stories agree with each other? A no: two stories contradict each other. | Worked for you. | fail | Story 4 lets a patient cancel at any time; story 7 refuses a cancellation inside 24 hours. Both cannot be built. |
| 4 | Does every story agree with the rules in the brief? A no: a story, or one of its criteria, contradicts a rule in the brief. | Find the story that handles a cancellation less than 24 hours before the appointment, and the story whose criteria say who may see the reason for visit. Pass when the late cancellation is allowed and marked late (rule 1 in `scenario-brief.md`) and the reason for visit is visible to clinic staff only (rule 4). | fail | story 7 and story 5 |
| 5 | Does everything in the stories trace to the brief? A no: a story adds a feature, system, rule, or standard the brief does not ask for. | Worked for you. | fail | Story 6 names AES-256 and HIPAA; the brief says nothing about either. |
| 6 | Is every rule and every existing system in the brief covered by at least one story? A no: a rule or system in the brief is not mentioned in any story. | Find the practice-management system and the reminder text messages by name in the stories or their criteria. A mention inside one criterion counts, and so does a wrong one (a wrong rule is item 4's problem). Pass when both have a story number. | fail | practice-management system: story none reminder texts: story none |

The prompt that produced the supplied stories, exactly as sent: "Write user stories for an online appointment booking system for a medical clinic." How many words is it? 13 Does it name Cedar Clinic, its user groups, or its rules? no

## Part C. Before you paste: what may go in the prompt

The clinic's data-handling policy says, in part: **Never in a prompt:** a patient's name, date of birth, phone number, email address, or address; a reason for visit, diagnosis, medication, or any other health detail about a person; anything copied from a patient record, an appointment record, a message to or from a patient, or a bill, even with the name removed. **Allowed:** how the clinic works (locations, providers, hours, rules); role names; the kind of data a system holds, described in general; synthetic patients, made up and labeled as such. (The full page is `data-handling-policy.md`.)

Four things someone might add to the Context section of `scaffold-stories.md`. Judge each by the policy lines above, not by the scaffold's own constraints. Mark it **allowed** or **not allowed** and copy the few words of the policy that decide it, as row 1 does. Row 1 is done for you.

| Row | Item | Allowed or not | The few words of the policy that decide it |
|---|---|---|---|
| 1 | The clinic's three locations, twelve providers, and hours | allowed | How the clinic works. |
| 2 | A real patient's name and date of birth, to make the example story realistic | not allowed | a patient's name, date of birth |
| 3 | A made-up patient, labeled as made up: "Patient A (invented), born in 1980, booked a slot and cancelled it 20 hours before" | allowed | synthetic patients, made up and labeled as such |
| 4 | A real reason for visit copied from last week's bookings, to show the format | not allowed | a reason for visit … or any other health detail about a person; anything copied from … an appointment record |

## Part D. Your stories

Paste the stories the assistant returned, including its "Assumptions to confirm" list, between the two lines:

---------- stories start ----------

# Cedar Clinic: Online Appointment Booking, Release 1 User Stories

**Story 1: See open slots.** As a patient, I want to see open slots by provider and location at any hour, so that I can choose a time without calling during clinic hours.
Acceptance criteria:

1. Open slots can be viewed at any hour, every day of the week.
2. Only slots inside the provider's bookable hours for that location are shown (Rule 3).
3. A slot that already has an appointment for that provider is not shown as open, because patients cannot override Rule 2.

**Story 2: Book an appointment.** As a patient, I want to book an open slot and give a reason for my visit, so that my appointment is confirmed without a phone call.
Acceptance criteria:

1. Before booking, I identify myself with the name, date of birth, and phone number the clinic has on file. A booking is refused if they do not match.
2. I enter a reason for visit as free text when booking (Rule 4).
3. The appointment is written to the practice-management system before I see a confirmation.
4. If the write fails, I see that the booking did not go through and the slot stays open.

**Story 3: Move an appointment.** As a patient, I want to move my appointment to another open slot, so that I can change plans without calling.
Acceptance criteria:

1. I can move only an appointment that matches my identifying details, and only to a slot shown as open (Rules 2 and 3).
2. The change is written to the practice-management system before I see a confirmation.
3. If the write fails, I see that the move did not go through and my original appointment is unchanged.

**Story 4: Cancel an appointment.** As a patient, I want to cancel my appointment at any hour, so that the clinic can offer the slot to someone else.
Acceptance criteria:

1. I can cancel at any time, including less than 24 hours before the appointment (Rule 1).
2. The cancellation is written to the practice-management system before I see a confirmation. If the write fails, I see that it did not go through and the appointment remains.
3. If the cancellation is less than 24 hours before the appointment, it is recorded as late in the practice-management system and shown as late to front-desk staff.

**Story 5: Reason for visit stays private.** As a patient, I want my reason for visit seen only by clinic staff, so that my health details stay private.
Acceptance criteria:

1. The reason is not shown to patients on any patient-facing screen or message, including the booking confirmation and the day-before reminder text message.
2. Front-desk staff and administrators can see the reason.

**Story 6: Front desk sees and moves the day.** As front-desk staff, I want to see the day's appointments across all three locations and move them when a provider runs late, so that patients and providers stay coordinated.
Acceptance criteria:

1. One view shows all appointments for a chosen day at all three locations.
2. A move is written to the practice-management system, and the view shows the new time only after the write succeeds.
3. Late cancellations are visibly marked so staff can follow up (Rule 1).

**Story 7: Front desk books by phone and overrides.** As front-desk staff, I want to book for patients who call, and to override the double-booking rule for one slot when a provider says so, so that patients without web access are served and provider decisions are honored.
Acceptance criteria:

1. Staff can book an appointment for a caller, with a reason for visit, and it is written to the practice-management system before staff see a confirmation.
2. By default, a slot that already has an appointment for that provider cannot be booked (Rule 2).
3. Staff can deliberately override Rule 2 for one named slot only. Other slots are unaffected, and the override is recorded with the staff member who made it.

**Story 8: Administrators set rules and review changes.** As an administrator, I want to set each provider's bookable hours per location and see who changed what, so that the booking rules are accurate and accountable.
Acceptance criteria:

1. I can set and change bookable hours for each provider at each location (Rule 3). New hours apply to slots shown to patients from then on.
2. I can see a record of changes to appointments (booked, moved, cancelled, override) and to bookable hours, each showing who made the change and when.
3. Staff cannot change bookable hours unless they are administrators.

## Assumptions to confirm

1. Whether a patient's move counts as a cancellation for Rule 1 when the original appointment is less than 24 hours away.
2. Whether the existing day-before reminder text messages cover appointments made online without further work, and whether the practice-management system's interface can store the late mark, the reason for visit, and the override. If it cannot, how those are recorded without any appointment existing only elsewhere.
3. What a patient sees when their details do not match the clinic's file, and how many attempts are allowed.
4. Whether staff moving an appointment can place it outside bookable hours or on an occupied slot.
5. Whether the change history in Story 8 can be kept in the new booking system or must also be written to the practice-management system.
6. Slot length, and how far ahead patients may book.
7. Who counts as "front-desk staff" for the purpose of Story 8's restriction, and how staff sign in.

---------- stories end ----------

Score your stories on three of the six requirements-checklist questions from Part A. Each is answered by finding something, not by reading everything, and each row says when it passes.

| # | Question | How to check, and when it passes | Pass or fail | What you found |
|---|---|---|---|---|
| 1 | Does every user group have at least one story? | Count the stories for patients, for front-desk staff, and for administrators. Pass when all three counts are 1 or more. | pass | patients 5 front desk 2 administrators 1 |
| 4 | Does every story agree with the rules in the brief? | Find the story that handles a cancellation less than 24 hours before the appointment, and the story whose criteria say who may see the reason for visit (if no story says, that is a fail). Pass when the late cancellation is allowed and marked late (rule 1) and the reason for visit is visible to clinic staff only (rule 4). | pass | story 4 and story 5 |
| 6 | Is every rule and existing system covered? | Find the practice-management system and the reminder text messages by name in the stories or their criteria. A mention inside one criterion counts; a mention only in the "Assumptions to confirm" list does not. Pass when both have a story number. | pass | practice-management system: story 2 reminder texts: story 5 |

Count. Your Part A verdicts for these same three questions (rows 1, 4, and 6 of the Part A table) say the supplied stories failed 3 of the three. Yours pass 3 of the three.

## Part F. Written assessment

Who reviews: stories go to **the practice manager**, who owns the clinic's rules and data. Sketches go to **the vendor's architect**, who takes any question about the clinic to the practice manager.

Fill the table one row at a time, left to right, and finish the row before starting the next one. Each row names the one Part to look in. The first yes/no column comes from the verdicts you wrote there: does the artifact fail an item you scored? The second is answered by looking at what you pasted there: is there an "Assumptions to confirm" section with at least one item? The supplied artifacts have none, so their second column is filled in. The fifth column names what decided the row: the number of any item that failed in that Part (one is enough), or, if no item failed, the number of the first assumption in the pasted list. One number, read from the Part you are already looking at. The verdict follows: **reliable as written** only if both answers are no; otherwise **needs human review**. A directed output that lands in "needs human review" has not failed; its assumptions are the list of questions for the clinic.

| Artifact | Where to look | Fails an item you scored? (yes/no) | Has an "Assumptions to confirm" section? (yes/no) | The item or assumption that decided it (one number) | Verdict |
|---|---|---|---|---|---|
| The supplied stories | Part A | yes | no | item 3 | needs human review |
| The supplied sketch | Part B | | no | item ____ | |
| Your stories | Part D | no | yes | assumption 1 | needs human review |
| Your sketch | Part E | | | item ____ or assumption ____ | |
