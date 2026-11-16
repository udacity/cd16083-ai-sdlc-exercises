# The change

Alder Box sells a monthly book subscription. Customers manage their subscriptions in a web app with a database. A nightly job charges each renewal on its due date. Email goes out through a third-party sending service. There is no mobile app.

The change being released adds a renewal reminder email. It has three parts: a new reminded_for column in the subscriptions table, which requires a database migration to be run in production by hand; a new step in the nightly job that sends the reminder; and the reminder email itself. The agreed behavior, confirmed with the customer, is that the reminder arrives three days before the renewal, by email, with a cancel link.

The change ships through a pull request into the main branch. The platform engineer deploys from main and runs production migrations. The QA engineer runs release checks. The product owner talks to customers.
