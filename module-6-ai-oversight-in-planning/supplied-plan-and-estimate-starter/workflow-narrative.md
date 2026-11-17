# Workflow narrative: the renewal reminder at Alder Box

## The company and the team

Alder Box sells a monthly book subscription. Customers manage their subscriptions in a web app. A
nightly job charges each renewal on its due date. Email goes out through a third-party sending
service. There is no mobile app.

The product team is four people:

- **Priya**, product owner. Owns the backlog and talks to customers.
- **Marcus**, developer. Writes the code.
- **Dana**, QA engineer. Reviews changes and runs the release checks.
- **Sam**, platform engineer. Runs deployments and the production database.

All four use the same AI assistant in their browser.

Two terms the story uses. A **pull request** is where a developer proposes a change and someone
else reviews it before it joins the main code. A **migration** is a script that changes the
production database, such as adding a column. Someone has to run it on purpose.

## The request

On Monday morning a customer writes to support:

> Can you email me before my subscription renews? I got charged on Saturday when I meant to cancel.
> I'd have cancelled if I'd had a heads-up.

What follows is what the team did with it, step by step. The quotes are taken word for word from
the assistant's answers.

---

### Step 1. Monday 9:10 am. Priya turns the email into a user story

Priya pastes the customer's email into the assistant, with the customer's name, email address, and
card digits removed, and asks for a user story with acceptance criteria.

The assistant returns a story, seven criteria, and three open questions. For the reminder's timing
it offers "proposed: 7 days for annual plans, 3 days for monthly plans" and asks, as its first open
question, "What reminder lead times are right per plan type?" One line elsewhere says "at least 24
hours before the charge."

Priya keeps three criteria for the ticket. For the timing she takes 24 hours, the one number not
marked "proposed". She does not go back to the email. Ticket ABX-212 now says:

> 1. A reminder email is sent 24 hours before the renewal charge.
> 2. The email states the renewal date and the amount, and includes a link to cancel.
> 3. No reminder is sent for a subscription that has already been cancelled.

The customer never said 24 hours.

### Step 2. Monday 9:30 am. Priya asks what the request leaves open

Priya asks the assistant to list the questions the customer's email does not answer. It returns
eleven. The third is "How much notice would they want?"

Priya emails the customer that question and the one about a cancel link, and leaves the ticket
until the answer comes. On Tuesday morning the customer answers: "A few days. Three would be good.
And yes, a cancel link." Priya spends the next half hour rewording the story by hand, line by line,
and adds a comment to ABX-212: "Customer confirmed: 3 days ahead, email, cancel link." The three
criteria on the ticket still say 24 hours.

### Step 3. Tuesday 2:00 pm. Marcus asks for the code

Marcus picks up ABX-212. He pastes the story and its three criteria into the assistant and asks for
the code. He does not open the ticket's comments.

The assistant returns the code and a set of tests. It says it read "24 hours" as a window: the
nightly job will remind anyone whose charge is between 24 and 48 hours away. The change needs a new
column in the subscriptions table. Marcus adds the column to his own test database by hand, runs the
job against a test subscription due tomorrow, and the email arrives.

### Step 4. Tuesday 4:30 pm. Marcus asks whether the tests cover the criteria

Marcus asks the assistant whether its tests cover all three acceptance criteria.

It says "Mostly," fixes two of its own tests, and adds:

> Criterion 1 rests on an interpretation. The story says "24 hours before", and I implemented
> "between 24 and 48 hours before" [...] Please confirm it.

All six tests pass. Marcus commits the code and the tests. He does not confirm anything.

### Step 5. Tuesday 6:10 pm. Marcus asks for the pull request description

Marcus asks the assistant to write the pull request description. It returns one with a section
headed "Decision needed", asking the reviewer to confirm the 24-hour reading. Marcus opens the pull
request with the description as written and asks Dana for a review.

### Step 6. Tuesday 6:40 pm. Dana reviews

Dana has been working since 8:30 am on the regression run for another release. She opens the pull
request, reads the description, and sees the six tests passing. She approves it with the comment
"Looks good to me (LGTM), tests pass." She does not confirm the reading, does not run the feature, and does not open
ABX-212. The pull request is merged at 6:52 pm.

### Step 7. Wednesday 10:00 am. Sam asks for a release checklist

Sam types one sentence: a release checklist for a feature that sends renewal reminder emails.

The assistant returns about sixty items in eight sections. Sam pastes it into the release ticket and works through it
over two days, ticking items as he goes.

One item is "Database migrations applied". Marcus had added the new column to his own machine by
hand and had written no migration, so there was no script to add the column in production. Sam
looks in the change for migrations to run, finds none, and ticks the item as done. He does not ask
why code that needs a new column comes with no way to add it.

### Step 8. Friday 7:05 pm, and Monday morning

With every item ticked, Sam deploys on Friday at 7:05 pm. The nightly job runs at 11:00 pm.

On Monday at 8:15 am Priya has fourteen support tickets. Every customer due to renew on Saturday,
Sunday or Monday got a reminder the night before the charge: one day's notice, the 24-hour window
the code was written to. Each night the job sent its emails and then failed to record that it had,
because the column that was supposed to hold that record was never created in production; it
logged one error per customer and carried on. Nobody was watching the logs over the weekend.
Renewals were charged as usual.

The customer from Monday's email writes again: "I got the reminder the night before. That isn't
three days."

---

*End of narrative.*
