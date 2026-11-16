# Direction scaffold: user stories for Cedar Clinic

A direction has four parts: context, constraints, examples, evaluation criteria. The context, one
example story, two constraints, and the first evaluation criterion are written for you. You finish
the other two constraints and add two criteria. Then you select everything below the line, paste it
into your AI assistant, and send it.

1. Before anything else, do Part C of the worksheet. It decides what may go in the Context. Nothing
   in the Context below breaks the clinic's data-handling policy.
2. Under *Constraints*, finish the two sentences. Both come from the requirements checklist printed
   in Part A of the worksheet. The first ends with what item 1 asks for: "Does every user group in
   the brief have at least one story?" The second ends with what item 2 asks for: "Does every story
   have acceptance criteria someone could check?" Write each in your own words.
3. Under *Evaluation criteria*, add two questions to the one given, in the same shape: each answered
   yes or no by reading the stories with the context beside them. Take two items you marked "fail"
   in Part A of the worksheet, other than 1 and 2, and write them as questions in your own words.
   The four to choose from: 3 Do the stories agree with each other? 4 Does every story agree with
   the rules in the brief? 5 Does everything in the stories trace to the brief? 6 Is every rule and
   every existing system in the brief covered by at least one story?

---------- Everything below this line is what you paste ----------

## What to produce

Using the context, constraints, example, and evaluation criteria below, write the user stories for the first release of online appointment booking at Cedar Clinic.

## Context

Cedar Clinic is a family medical practice with three locations in one city and twelve providers. It sees about 400 patients a week. Today patients book by phone, 8 am to 6 pm, Monday to Friday.

Every appointment is recorded in the clinic's practice-management system, which stays the record of every appointment: anything the new booking system books, moves, or cancels must be written there, and no appointment may exist only somewhere else. It has an interface other software can use to read and write appointments. Reminder text messages already go out from it the day before each appointment, through a messaging service the clinic pays for.

Three user groups. Patients want to see open slots, book, move, and cancel at any hour; they identify themselves with the name, date of birth, and phone number the clinic has on file. Front-desk staff see the day across all three locations, move appointments when a provider runs late, book by phone for patients who do not use the web, and override a rule for one slot when a provider says so. Administrators (the practice manager and two location leads) set the rules and need to see who changed what.

Rules: (1) A cancellation less than 24 hours before the appointment is a late cancellation. It is still allowed; the system marks it late so the front desk can follow up. (2) No provider has two appointments in the same slot, unless front-desk staff deliberately override the rule for that slot. (3) An administrator sets each provider's bookable hours per location; patients book inside those hours only. (4) A reason for visit is collected at booking, as free text, and is visible only to clinic staff.

Out of scope: payments, insurance checks, video visits, and any change to the practice-management system itself.

## Constraints

- If a story needs something the context does not say, write it under a heading "Assumptions to confirm" instead of inside the story. Do not add features, systems, rules, or standards the context does not mention.
- Use no patient names or other personal details, real or invented.
- No more than six stories, and
- Every story has two to four acceptance criteria that

## Example

One story in the shape I want:

**Story: Book inside bookable hours.** As a patient, I want to see only the slots inside a provider's bookable hours at a location, so that I cannot book a time the clinic will not honor.
Acceptance criteria:
1. A slot outside the provider's bookable hours for that location is not shown.
2. A booked slot is written to the practice-management system before the patient sees a confirmation.
3. If the write fails, the patient sees that the booking did not go through and the slot stays open.

## Evaluation criteria

I will check the stories against these before using them:
1. Does every user group in the context have at least one story?
2.
3.
