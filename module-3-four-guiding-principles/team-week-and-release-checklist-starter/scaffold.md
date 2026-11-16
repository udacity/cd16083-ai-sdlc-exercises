# Direction scaffold: a release checklist for the renewal reminder

A direction has four parts: context, constraints, examples, evaluation criteria. The context, one
example item, and the first evaluation criterion are written for you. You finish the constraints,
add two more criteria, and write the one line that says what to produce. Then you select everything below the line, paste it into your AI assistant,
and send it.

- Under *Constraints*, finish the three sentences.
- Under *Evaluation criteria*, the first question is written. Add two more questions you will ask of
  the checklist before you read it, in the same shape: each answered yes or no by reading the
  checklist. Questions 2 and 3 of Part B of the worksheet (does any item name an owner; does the
  reminder item check for three days ahead), in your own words, are the start.
- Under *What to produce*, write one line, for example: "Using the context, constraints, example,
  and evaluation criteria below, write the release checklist for this change."

Do not open `team-prompts.md` until the lab guide tells you to.

---------- Everything below this line is what you paste ----------

## What to produce



## Context

Alder Box sells a monthly book subscription. Customers manage their subscriptions in a web app with
a database. A nightly job charges each renewal on its due date. Email goes out through a third-party
sending service. There is no mobile app.

The change being released adds a renewal reminder email. It has three parts: a new
`reminded_for` column in the subscriptions table, which requires a database migration to be run
in production by hand; a new step in the nightly job that sends the reminder; and the reminder email
itself. The agreed behavior, confirmed with the customer, is that the reminder arrives three days
before the renewal, by email, with a cancel link.

The change ships through a pull request into the main branch. The platform engineer deploys from
main and runs production migrations. The QA engineer runs release checks. The product owner talks
to customers.

## Constraints

- The list is no longer than
- Every item must include
- If the assistant is unsure whether an item applies to Alder Box, it should

## Examples

- [ ] Database migration adding `reminded_for` run in production and verified against the
  subscriptions table. Owner: platform engineer.

## Evaluation criteria

1. Does every item apply to Alder Box as described?
2.
3.
