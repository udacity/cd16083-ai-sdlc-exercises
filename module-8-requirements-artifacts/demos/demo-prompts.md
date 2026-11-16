# Module 8 demo prompts

Evaluate AI-Generated Requirements Artifacts

Every prompt used in this module's demo videos, in the order it was pasted into Claude Code in the Udacity workspace. Where a prompt refers to a file, the file sits in the demo's workspace folder.

# Demo 1

No live prompt. The demo reads prepared Atlas materials.

# Demo 2: Writing the rules before the AI writes the stories

Workspace folder: atlas-demo (1-rules.md, 2-team-brief.md, 3-first-stories.md, 4-requirements-checklist.md).

**Prompt A: open questions.**

> We are adding a feature to Atlas, an online tutoring marketplace where students anywhere book one-hour video sessions with tutors anywhere. The request is: "Let students book sessions with tutors." Before writing anything, what questions does this request leave open? List them, most important first. Reply with the list only. Do not read any files and do not ask me anything else.

**Prompt B: contradiction check.**

> Here is a set of user stories another prompt produced for this feature. Check the set for contradictions: any two stories, or any two acceptance criteria, that cannot both be true at once. For each one, quote the two lines and say why they conflict. Do not fix anything and do not rewrite the stories. Reply with the findings only.
> 
> **Story 1.** As a student, I want to browse tutors by subject, so that I can find someone who teaches what I need.
> - Tutors can be filtered by subject and by hourly rate.
> - Each tutor shows a rating and an hourly rate.
> 
> **Story 2.** As a student, I want to see a tutor's available times, so that I can pick a session that suits me.
> - Open one-hour slots are shown for the next 14 days.
> - Each slot shows its start time, for example "3:00 PM".
> 
> **Story 3.** As a student, I want to book a one-hour session, so that the time is reserved for me.
> - A booked slot is removed from the tutor's availability.
> - A confirmation is sent to the student's email address.
> 
> **Story 4.** As a student, I want to pay when I book, so that my session is confirmed.
> - Payment is taken through the payments provider.
> - The booking is confirmed only after the payment succeeds.
> 
> **Story 5.** As a student, I want to cancel a session, so that I am not charged for a session I can't attend.
> - Students can cancel a session at any time.
> - A cancelled session is refunded in full.
> 
> **Story 6.** As a tutor, I want to set my weekly availability, so that students can book me only when I'm free.
> - Availability is set in one-hour blocks.
> - Each block is entered as a start time, for example "3:00 PM".
> 
> **Story 7.** As a tutor, I want to be paid for every booked slot, so that my time is protected.
> - Tutors are paid weekly for every booked session.
> - Payouts go through the payments provider.
> 
> **Story 8.** As a student, I want a reminder before my session, so that I don't miss it.
> - A reminder is sent to the student's email address one hour before the session.
> - The reminder includes the link to the video session.

**Prompt C: generate with the rules.**

> Using the context, rules, example and evaluation criteria below, write the user stories with acceptance criteria for this feature. Reply with the stories only. Do not create or edit any files and do not ask me questions first. If something is not covered by the context or the rules, add it to a short "Assumptions to confirm" list at the end instead of guessing.
> 
> **Context**
> 
> Atlas is an online tutoring marketplace. Students anywhere book one-hour video sessions with tutors anywhere. The request is: "Let students book sessions with tutors."
> 
> Who uses it:
> - Students, who book and attend sessions. Tutors and students are often in different time zones.
> - Parents or guardians, who book for students under 18. Many younger students have no email address of their own.
> - Tutors, who set their availability and are paid for each session.
> 
> Existing systems: a payments provider that charges students and pays tutors weekly, and a video service that hosts the sessions.
> 
> **Rules**
> 
> 1. A session can be cancelled free of charge up to 24 hours before it starts. After that, the student is not refunded and the tutor is still paid.
> 2. Every session time is shown in each person's own local time.
> 3. Confirmations and reminders go to whoever booked. For a student under 18, that is the parent, by email or text message.
> 4. A session can be moved to another time with the same tutor up to 24 hours before it starts.
> 
> **Example**
> 
> **Story: Cancel a session.** As a student, I want to cancel a booked session, so that I am not charged for a session I cannot attend.
> - Cancelling 24 hours or more before the start refunds the student in full and frees the slot.
> - Cancelling less than 24 hours before the start gives no refund, and the tutor is paid for the session.
> - The cancellation notice goes to whoever booked, by their chosen method.
> 
> **Evaluation criteria**
> 
> 1. Does every story have acceptance criteria someone could check?
> 2. Do the stories agree with each other, and with the four rules?
> 3. Is every rule and every existing system covered by at least one story?
> 4. Is the set no longer than eight stories, with a story for each user group?

