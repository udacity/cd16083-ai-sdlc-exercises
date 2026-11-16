# Alder Box: Monday morning

Alder Box sells a monthly book subscription. Customers manage their subscriptions in a web app, and a nightly job charges each renewal on its due date. Email goes out through a third-party sending service.

## The team

- **Priya**, product owner. Owns the backlog and talks to customers.
- **Marcus**, developer. Writes the code.
- **Dana**, QA engineer. Reviews changes and runs the release checks.
- **Sam**, platform engineer. Runs deployments and the production database.

## What shipped

Ticket ABX-212: email customers before their subscription renews. The customer who asked confirmed, in a comment on the ticket, that they wanted **3 days' notice**. The ticket's acceptance criteria still say **24 hours**, and the code was written to those criteria: the nightly job reminds anyone whose charge is between 24 and 48 hours away.

The change also needs a new column in the subscriptions table, to record that a reminder was sent. Marcus added the column to his own test database by hand. No migration was written, so nothing creates the column in production.

Sam deployed the change on **Friday at 7:05 pm**. The nightly job runs at **11:00 pm**.

## Monday, 8:15 am

- Priya has **fourteen support tickets**. Every customer due to renew on Saturday, Sunday or Monday got a reminder the night before the charge: one day's notice, not three.
- Each night the job sent its emails, then failed to record that it had, because the column was never created in production. It logged **one error per customer** and carried on.
- Nobody was watching the logs over the weekend.
- Renewals were charged as usual.
- The customer who asked for the feature writes again: "I got the reminder the night before. That isn't three days."
