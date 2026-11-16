# Release checklist: renewal reminder emails

This is what the assistant returned to Sam in step 7, exactly as he pasted it into the release ticket. He gave it one sentence and nothing about Alder Box's systems. (Recorded 2026-10-11, Claude Sonnet 5.5 in GitHub Copilot Chat. Your own run will differ.)

# Release Checklist: Subscription Renewal Reminder Emails

## 1. Pre-Development / Planning

- Requirements documented: reminder timing (e.g., 30/7/1 days before renewal), eligible plans, and opt-out rules
- Legal and compliance review (CAN-SPAM, GDPR/ePrivacy, and local auto-renewal disclosure laws such as US state ARL rules and the EU consumer directive)
- Decide which emails are transactional and which are marketing. This determines whether unsubscribe is required.
- Email copy and design approved (product, legal, support)
- Localization and time zone handling confirmed

## 2. Implementation

- Scheduler or job finds subscriptions due for renewal within each reminder window
- **Idempotency:** each reminder is sent at most once per subscription, per window, per renewal cycle (unique key or sent-log)
- Edge cases handled:
  - Cancelled, paused, or already-renewed subscriptions are skipped
  - Plan changes, upgrades or downgrades, and price changes between the reminder and renewal
  - Trials ending, annual vs. monthly plans, and short billing cycles (reminder window longer than the cycle)
  - Failed payment methods and expiring cards
  - Users with no valid email, or with bounced or suppressed addresses
  - Time zones and DST
- Email contains correct data: plan, amount (including tax and currency), renewal date, payment method (last 4 digits only), and a manage/cancel link
- Links are secure and authenticated, or use signed tokens that expire
- Unsubscribe or preference-center link works (where required)
- No PII leaks in logs or in URLs
- Feature flag in place, with default off and per-cohort rollout support
- Rate limiting and batching so the job doesn't overload the email provider or database

## 3. Testing

- Unit tests for date-window logic and eligibility rules
- Integration tests with the email provider sandbox
- End-to-end test in staging with time-travel or a mocked clock
- Idempotency test: run the job twice, and confirm no duplicates
- Rendering tested across major clients (Gmail, Outlook, Apple Mail, mobile) and in dark mode
- Plain-text fallback and accessibility checks (alt text, contrast)
- Localization checks (RTL, long strings, currency and date formats)
- Load test for peak volume (e.g., many renewals on the 1st of the month)
- Spam score check (e.g., Mail-Tester)

## 4. Email Infrastructure

- SPF, DKIM, and DMARC configured for the sending domain
- Sending domain or IP reputation is healthy. Warm up if using a new one.
- Bounce, complaint, and unsubscribe webhooks wired to the suppression list
- Reply-to address monitored, or a clear no-reply policy stated
- Provider quotas and rate limits verified

## 5. Observability

- Metrics: emails queued, sent, delivered, bounced, opened, clicked, and complaints
- Business metrics: renewal rate, cancellations after reminder, support tickets
- Alerts: job failure, send-rate anomalies, bounce rate above threshold, and zero emails sent when some were expected
- Dashboards created and linked in the runbook
- Structured logging with correlation IDs, and no sensitive data in logs

## 6. Release Readiness

- Code reviewed and merged, and CI is green
- Config and secrets set in production (API keys, templates, sender addresses)
- Database migrations applied and backward-compatible
- Runbook written: how to pause sending, resend, and handle incidents
- **Rollback plan:** the kill switch (feature flag) is tested
- Support and CS briefed, with FAQ and macros ready
- Help center and docs updated
- Stakeholders notified of the release date

## 7. Rollout

- Send a test to internal staff accounts in production
- Enable for a small cohort (e.g., 1–5%) and monitor for 24–48 hours
- Verify the first real sends: content, links, timing, and no duplicates
- Gradually ramp to 100% if metrics stay healthy
- Avoid a backlog blast: confirm what happens to subscriptions already inside a reminder window at launch

## 8. Post-Release

- Review deliverability and error metrics after 1 week
- Review support tickets and user feedback
- Compare renewal and churn metrics against the baseline
- Remove or retire the feature flag once stable
- Retrospective and follow-up tasks (A/B tests on timing and copy)

I can turn this into a GitHub issue with task-list items, or tailor it to a specific repo and stack. Let me know the repository if you'd like that.
