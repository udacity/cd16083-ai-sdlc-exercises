# Module 3 demo prompts

Apply the Four Guiding Principles to AI-Assisted Workflows

Every prompt used in this module's demo videos, in the order it was pasted into Claude Code in the Udacity workspace. Where a prompt refers to a file, the file sits in the demo's workspace folder.

# Demo 1: Four questions, one team, one week

No live prompt. The demo reads `workflow-narrative.md` and the worksheet.

# Demo 2: Sam's prompt against a direction

Files: team-prompts.md, release-checklist-team.md, scaffold.md.

**Sam's original prompt** (shown, not run; from team-prompts.md, step 7):

> Write a release checklist for a feature that sends subscription renewal reminder emails.

**Prompt 1: the completed scaffold.**

> Using the context, constraints, example, and evaluation criteria below, write the release checklist for this change. Reply with the checklist only. Do not create or edit any files, and do not ask me questions first.
> 
> **Context**
> 
> Alder Box sells a monthly book subscription. Customers manage their subscriptions in a web app with a database. A nightly job charges each renewal on its due date. Email goes out through a third-party sending service. There is no mobile app.
> 
> The change being released adds a renewal reminder email. It has three parts: a new `reminded_for` column in the subscriptions table, which requires a database migration to be run in production by hand; a new step in the nightly job that sends the reminder; and the reminder email itself. The agreed behavior, confirmed with the customer, is that the reminder arrives three days before the renewal, by email, with a cancel link.
> 
> The change ships through a pull request into the main branch. The platform engineer deploys from main and runs production migrations. The QA engineer runs release checks. The product owner talks to customers.
> 
> **Constraints**
> 
> - The list is no longer than 15 items.
> - Every item must include an owner, one of: product owner, developer, QA engineer, platform engineer, and how it is verified.
> - If the assistant is unsure whether an item applies to Alder Box, it should include the item anyway, marked "(confirm)", rather than guess or leave it out.
> 
> **Examples**
> 
> - [ ] Database migration adding `reminded_for` run in production and verified against the subscriptions table. Owner: platform engineer.
> 
> **Evaluation criteria**
> 
> 1. Does every item apply to Alder Box as described?
> 2. Does every item have an owner?
> 3. Is there an item that checks the reminder goes out three days ahead?

**Prompt 2: restating a constraint** (instead of fixing the checklist by hand):

> One more constraint I left out: the deploy from main must not happen until the production migration is confirmed, and the checklist must say so as its own item with the platform engineer as owner. Rewrite the checklist with that constraint met. Change nothing else.

