# Worksheet: generate and evaluate early-phase artifacts
Your name:

Keep `scenario-brief.md` open beside this worksheet; you will go back to it for every part. The artifacts you evaluate, the checklists, and the policy lines you need are printed here where you use them.

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
| 1 | Does every user group in the brief have at least one story? A no: a user group named in the brief does not have a story. | Count the stories for patients, for front-desk staff, and for administrators (the three groups the brief names). Pass when all three counts are 1 or more. | | patients ____ front desk ____ administrators ____ |
| 2 | Does every story have acceptance criteria someone could check? A no: a story has no criteria, or criteria that cannot be tested ("works well"). | Worked for you. | fail | Story 3 has no criteria, so there is no way to say when it is done. |
| 3 | Do the stories agree with each other? A no: two stories contradict each other. | Worked for you. | fail | Story 4 lets a patient cancel at any time; story 7 refuses a cancellation inside 24 hours. Both cannot be built. |
| 4 | Does every story agree with the rules in the brief? A no: a story, or one of its criteria, contradicts a rule in the brief. | Find the story that handles a cancellation less than 24 hours before the appointment, and the story whose criteria say who may see the reason for visit. Pass when the late cancellation is allowed and marked late (rule 1 in `scenario-brief.md`) and the reason for visit is visible to clinic staff only (rule 4). | | story ____ and story ____ |
| 5 | Does everything in the stories trace to the brief? A no: a story adds a feature, system, rule, or standard the brief does not ask for. | Worked for you. | fail | Story 6 names AES-256 and HIPAA; the brief says nothing about either. |
| 6 | Is every rule and every existing system in the brief covered by at least one story? A no: a rule or system in the brief is not mentioned in any story. | Find the practice-management system and the reminder text messages by name in the stories or their criteria. A mention inside one criterion counts, and so does a wrong one (a wrong rule is item 4's problem). Pass when both have a story number. | | practice-management system: story ____ reminder texts: story ____ (or "none") |

The prompt that produced the supplied stories, exactly as sent: "Write user stories for an online appointment booking system for a medical clinic." How many words is it? ____ Does it name Cedar Clinic, its user groups, or its rules? yes / no

## Part C. Before you paste: what may go in the prompt

The clinic's data-handling policy says, in part: **Never in a prompt:** a patient's name, date of birth, phone number, email address, or address; a reason for visit, diagnosis, medication, or any other health detail about a person; anything copied from a patient record, an appointment record, a message to or from a patient, or a bill, even with the name removed. **Allowed:** how the clinic works (locations, providers, hours, rules); role names; the kind of data a system holds, described in general; synthetic patients, made up and labeled as such. (The full page is `data-handling-policy.md`.)

Four things someone might add to the Context section of `scaffold-stories.md`. Judge each by the policy lines above, not by the scaffold's own constraints. Mark it **allowed** or **not allowed** and copy the few words of the policy that decide it, as row 1 does. Row 1 is done for you.

| Row | Item | Allowed or not | The few words of the policy that decide it |
|---|---|---|---|
| 1 | The clinic's three locations, twelve providers, and hours | allowed | How the clinic works. |
| 2 | A real patient's name and date of birth, to make the example story realistic | | |
| 3 | A made-up patient, labeled as made up: "Patient A (invented), born in 1980, booked a slot and cancelled it 20 hours before" | | |
| 4 | A real reason for visit copied from last week's bookings, to show the format | | |

## Part D. Your stories

Paste the stories the assistant returned, including its "Assumptions to confirm" list, between the two lines:

---------- stories start ----------

---------- stories end ----------

Score your stories on three of the six requirements-checklist questions from Part A. Each is answered by finding something, not by reading everything, and each row says when it passes.

| # | Question | How to check, and when it passes | Pass or fail | What you found |
|---|---|---|---|---|
| 1 | Does every user group have at least one story? | Count the stories for patients, for front-desk staff, and for administrators. Pass when all three counts are 1 or more. | | patients ____ front desk ____ administrators ____ |
| 4 | Does every story agree with the rules in the brief? | Find the story that handles a cancellation less than 24 hours before the appointment, and the story whose criteria say who may see the reason for visit (if no story says, that is a fail). Pass when the late cancellation is allowed and marked late (rule 1) and the reason for visit is visible to clinic staff only (rule 4). | | story ____ and story ____ |
| 6 | Is every rule and existing system covered? | Find the practice-management system and the reminder text messages by name in the stories or their criteria. A mention inside one criterion counts; a mention only in the "Assumptions to confirm" list does not. Pass when both have a story number. | | practice-management system: story ____ reminder texts: story ____ (or "none") |

Count. Your Part A verdicts for these same three questions (rows 1, 4, and 6 of the Part A table) say the supplied stories failed ____ of the three. Yours pass ____ of the three.

## Part F. Written assessment

Who reviews: stories go to **the practice manager**, who owns the clinic's rules and data.

Fill the table one row at a time, left to right, and finish the row before starting the next one. Each row names the one Part to look in. The first yes/no column comes from the verdicts you wrote there: does the artifact fail an item you scored? The second is answered by looking at what you pasted there: is there an "Assumptions to confirm" section with at least one item? The supplied stories have none, so their second column is filled in. The fifth column names what decided the row: the number of any item that failed in that Part (one is enough), or, if no item failed, the number of the first assumption in the pasted list. One number, read from the Part you are already looking at. The verdict follows: **reliable as written** only if both answers are no; otherwise **needs human review**. A directed output that lands in "needs human review" has not failed; its assumptions are the list of questions for the clinic.

| Artifact | Where to look | Fails an item you scored? (yes/no) | Has an "Assumptions to confirm" section? (yes/no) | The item or assumption that decided it (one number) | Verdict |
|---|---|---|---|---|---|
| The supplied stories | Part A | | no | item ____ | |
| Your stories | Part D | | | item ____ or assumption ____ | |
