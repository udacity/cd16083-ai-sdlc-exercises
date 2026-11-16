# Scenario brief: online appointment booking at Cedar Clinic

## The clinic

Cedar Clinic is a family medical practice with three locations in one city and twelve providers
(doctors and nurse practitioners). It sees about 400 patients a week. Today patients book by phone,
8 am to 6 pm, Monday to Friday.

Every appointment is recorded in the clinic's **practice-management system**, the software the
front desk has used for nine years for schedules, patient records, and billing. It stays the record
of every appointment: anything the new booking system books, moves, or cancels must be written
there, and no appointment may exist only somewhere else. Other software can read and write
appointments through its interface.

Reminder text messages already go out from the practice-management system the day before each
appointment, through a messaging service the clinic pays for.

## What is wanted

Patients should be able to book, move, and cancel their own appointments from a phone or computer at
any hour, without calling.

## Three user groups

- **Patients** want to see open slots, book, move, and cancel at any hour. They identify themselves
  with the name, date of birth, and phone number the clinic has on file.
- **Front-desk staff** see the day across all three locations, move appointments when a provider
  runs late, and book by phone for patients who do not use the web. When a provider says so, they
  override a rule for one slot.
- **Administrators** (the practice manager and two location leads) set the rules and need to see
  who changed what.

## The rules

1. A cancellation less than 24 hours before the appointment is a **late cancellation**. It is still
   allowed. The system marks it late so the front desk can follow up.
2. No provider has two appointments in the same slot, unless front-desk staff deliberately override
   the rule for that slot.
3. An administrator sets each provider's bookable hours per location. Patients book inside those
   hours only.
4. A reason for visit is collected at booking, as free text, and is visible only to clinic staff.

## Out of scope

Payments, insurance checks, video visits, and any change to the practice-management system itself.
