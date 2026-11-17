# Worksheet: map an AI-assisted workflow to the guiding principles
Your name:

Keep `workflow-narrative.md` open beside this file; you will go back to it for every row. Do not open `team-prompts.md` until Part E asks for it.

## Part A. Principles map

Two rules. You are judging the team's handling of each step, not the person who acted. The step where a check was skipped gets the mark, not the step where the consequence showed up.

**First, the facts.** Pick from the lists. Workflow step 1 is done as the model, and steps 2 and 3 are worked in the first demo video. You do steps 6 and 7.

What was the output checked against? Pick one: **the email** · **the customer** · **the ticket comment** · **an AI output** (say which: the story's criteria, the code, the tests, or the description) · **nothing**

What was available to the team at this step and not used? Pick one or two: **the email** · **the ticket's criteria** · **the ticket comment** · **the change itself** · **the pull request** · **a fresher hour** · **nothing**

| Step | Checked against | Available and not used |
|---|---|---|
| 1. Priya turns the email into a user story | nothing | the email |
| 2. Priya asks what the request leaves open | the customer | the ticket's criteria |
| 3. Marcus asks for the code | an AI output (the story's criteria) | the ticket comment |
| 6. Dana reviews | an AI output (the description and the tests) | the change itself; a fresher hour |
| 7. Sam asks for a release checklist | nothing | the pull request; the ticket's criteria |

**Then, the marks.** **S**: the team satisfied the principle at this step. **V**: the team violated it. **–**: the question does not apply at this step. Each mark follows from the row's facts. Read the columns left to right and take the first that fits:

| Question | Mark V when | Mark S when | Mark – when |
|---|---|---|---|
| Where can you move up a level? | The team asked for a finished thing (a story, code, a description, a checklist) without saying what it must contain, or reworked the assistant's output by hand instead of restating what it must contain | The team asked for something it then judged itself: questions to choose from, or output checked against criteria it supplied | Nobody asked the assistant for anything at this step |
| Where might this over-rely on AI? | "Checked against" is an AI output or nothing | "Checked against" is the email, the customer, or the ticket comment | No AI output is produced or passed on at this step |
| How can we ensure quality? | A gate was due (code to run, a change to review, a release to check) and it checked only against an AI output, or was skipped | The gate checked against the email, the customer's answer, or a rule written from them; or a requirement was checked with the customer before anything was built | No gate was due: nothing was built, reviewed, or released at this step |
| Is it sustainable? | "Available and not used" includes a fresher hour | The narrative says the hour or the load was a factor and the team dealt with it (waited, or split the work); or the team waited for an answer instead of keeping the assistant's pace | The narrative mentions no hour or load pressure at this step |

| Step | Move up a level? | Over-rely on AI? | Ensure quality? | Sustainable? |
|---|---|---|---|---|
| 1. Priya turns the email into a user story | V | V | – | – |
| 2. Priya asks what the request leaves open | V | S | S | S |
| 3. Marcus asks for the code | S | V | V | – |
| 6. Dana reviews | – | V | V | V |
| 7. Sam asks for a release checklist | V | V | V | – |

Step 1, why: Priya asked for a story and criteria without saying what they must contain (V). The story went into the backlog with no check against the email (V). No quality gate was due yet, and time played no part (–, –).

## Part C. Direct the assistant with the scaffold

Open `scaffold.md`, finish the constraints and the evaluation criteria, and run it in your AI assistant. Paste the checklist it returned here.

```
- [ ] Pull request with the migration, nightly job step and email template is reviewed and merged into main. Owner: platform engineer. Verified by the merged PR and a passing CI run on main.
- [ ] Database migration adding `reminded_for` run in production by hand and verified against the subscriptions table. Owner: platform engineer. Verified by checking that the column exists and that existing rows are intact.
- [ ] Migration run and checked on a staging copy of the database before production (confirm: a staging environment exists). Owner: platform engineer. Verified by the migration output and a row count before and after.
- [ ] Deploy from main happens only after the migration is confirmed, so the new job step never runs without the column. Owner: platform engineer. Verified by the deploy log timestamp coming after the migration timestamp.
- [ ] Reminder is sent three days before the renewal date. Owner: QA engineer. Verified by running the nightly job against a test subscription renewing in three days and confirming one email arrives. Subscriptions renewing in two or four days must get none.
- [ ] `reminded_for` is set after sending, so a second nightly run does not send a duplicate. Owner: QA engineer. Verified by running the job twice and confirming one email and the stored `reminded_for` value.
- [ ] Reminder email content is correct and the cancel link works. Owner: QA engineer. Verified by opening the received email and clicking the link to confirm it reaches cancellation for the right subscription.
- [ ] Email passes through the third-party sending service and is delivered, not spam-foldered (confirm: the service's sandbox or test mode is available). Owner: QA engineer. Verified by delivery status in the service's dashboard and inbox placement in a test mailbox.
- [ ] The nightly renewal charge still runs on its due date and is unaffected by the new step. Owner: QA engineer. Verified by a test renewal being charged once, with a job log showing no errors.
- [ ] A failure in the reminder step (such as an email service outage) does not stop the nightly charges (confirm). Owner: QA engineer. Verified by forcing a send failure in staging and confirming charges still complete.
- [ ] After the first production nightly run, the job log and email service dashboard are checked for errors and send counts that match the number of subscriptions renewing in three days. Owner: platform engineer. Verified by comparing the counts to a database query.
- [ ] Customer-facing communication is decided: whether to announce the new reminder, and support knows what the email looks like (confirm: Alder Box wants an announcement). Owner: product owner. Verified by written confirmation of the decision and, if announcing, the sent message.
```

## Part D. Written evaluation

Three oversight decisions the team made, in the order they happened, and what went wrong on Monday morning because of each one. One line each.

| Step | The decision | What went wrong on Monday because of it |
|---|---|---|
| 2 | The customer's answer went into a ticket comment; the criteria stayed at 24 hours | Everything downstream was built on 24 hours; the reminder arrived one day ahead |
| 4, 5, 6 | The assistant asked twice to confirm its 24-hour reading; nobody did, and the 6:40 pm review approved on the AI's description and the AI's tests | The wrong lead time shipped with six passing tests behind it |
| 7 | The release checklist was used without being read; the migration item was ticked with no migration in the change | The column that records a sent reminder was never created in production; each night the job sent reminders, then logged an error per customer; nobody read the logs; fourteen tickets |

One sentence: why did the team's checklist look right and not be?

It was a plausible generic list for a feature of this kind, and nothing in it was specific to Alder Box, because nothing specific was provided.

## Part E. Compare your checklist with the team's

Score your checklist against the three evaluation criteria in `scaffold.md`, the given one and the two you wrote:

| Your criterion | Pass or fail | The item that decides it (or "all", if every item passes) |
|---|---|---|
| 1. Does every item apply to Alder Box as described? | pass | all; the four uncertain items are marked "(confirm)" rather than left out |
| 2. Does every item have an owner? | pass | all; every item names a role and how it is verified |
| 3. Is there an item that checks the reminder goes out three days ahead? | pass | "Reminder is sent three days before the renewal date", verified against a test subscription renewing in three days |

Now open `team-prompts.md` and read Sam's prompt for workflow step 7, the release checklist. In one sentence: what did your direction give the assistant that his did not?

The context, the constraints, and the criteria: Sam gave one sentence and nothing about Alder Box.

## Part F. Optional: a direction from scratch, and your own workflow

Your direction for the reply email to the customer:

```
(context, constraints, examples, evaluation criteria, and one line saying what to produce)
```

The assistant's reply:

```
(paste here)
```

Scored against your own criteria:

| Your criterion | Pass or fail | Evidence |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |

The part of the direction you found hardest to write without the scaffold, and why:

Your own workflow, three to five steps:

| Step | What was the output checked against? | What was available and not used? | Move up a level? | Over-rely on AI? | Ensure quality? | Sustainable? |
|---|---|---|---|---|---|---|
| 1. | | | | | | |
| 2. | | | | | | |
| 3. | | | | | | |
| 4. | | | | | | |
| 5. | | | | | | |

One place where the same question gets a different answer in a different role, and whose map it came from:
