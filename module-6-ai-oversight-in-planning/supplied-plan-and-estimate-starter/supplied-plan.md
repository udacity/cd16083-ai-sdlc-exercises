# The supplied plan and estimate

The developer asked the team's AI assistant: "Plan the renewal reminder feature and estimate it in days." This is what came back.

## Implementation plan: renewal reminder emails

### Summary

Add a step to the nightly job that emails each customer three days before their renewal, with the renewal date, the amount, and a link to cancel. Estimated effort: 6 days.

### Constraints

- The third-party sending service allows at most 500 emails per day on Alder Box's plan, so the job must spread reminders over several nights whenever more than 500 renewals fall on the same date.

### Work breakdown

1. Data model (0.5 day). Add the reminded_for column to the subscriptions table in the development database and update the subscription model.
2. Nightly job step (1.5 days). Select subscriptions that renew in three days, are not cancelled, and have not been reminded for this renewal. Send the reminder, then set reminded_for.
3. Email template (1 day). Build the email with TemplateKit Pro, a commercial templating library ($39 per developer per month), so reminders match the brand.
4. Send log (0.5 day). Save a copy of every reminder sent in a new reminder_log table: customer name, email address, renewal amount, and the full email body including the cancel link, so support can look up what a customer received.
5. Tests (1.5 days). Unit tests for the three-day selection, skipping cancelled subscriptions, and not sending twice.
6. Release (1 day). Merge to main, deploy, and switch on the new job step.

### Estimate

6 developer-days. Ready to release by the end of next week.

### Alternative considered

A separate reminder service with its own schedule, instead of a step in the nightly job. It keeps reminders apart from billing but adds a new service to run. Estimated 9 developer-days.

### Risks

- Email deliverability.
- Customers who change plan between the reminder and the renewal.
