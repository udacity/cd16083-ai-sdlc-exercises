# Deployment packet: a late fee charged a day early

Suppose pull request #412 was corrected to `> 30` and merged on October 8. This packet is what the on-call engineer gathered on the morning of October 20, after a support ticket. Six sections. Nothing else is known.

## 1. The support ticket

Ticket 7731, opened 2026-10-19 at 6:14 pm Pacific by Hollis Garden Supply, a customer:

> Invoice INV-1042 was due September 19. Tonight your reminder email shows a $15.00 late fee. By my count that is 30 days, and your terms say more than 30. Please remove it.

Support checked the fee runs since October 8. On each evening, the 6:00 pm run charged a fee to every invoice whose count stood at 30 that day. Twenty-three invoices in all, $286.50. No invoice at 29 days or fewer was charged.

## 2. The deploy record

| Environment | Commit | Deployed | By |
|---|---|---|---|
| staging | `5e1c2a9` Late fee for overdue invoices (#412), threshold `> 30` | 2026-10-08, 10:12 am Pacific | the pipeline |
| production | `5e1c2a9` the same commit | 2026-10-08, 10:40 am Pacific | the pipeline |

Nothing has been deployed to either environment since.

## 3. The fee job's schedule

From the scheduler, identical in both environments:

```
job: late-fee-run
schedule: "0 18 * * *"
timezone: America/Los_Angeles
command: python run_late_fees.py
```

`run_late_fees.py` reads every unpaid invoice and calls `late_fee(balance, due_date, today)` for each, with `today = date.today()`, the date on the container's own clock.

## 4. Environment configuration

The application container's settings. Staging:

```
PYTHON_VERSION=3.12.6
TZ=America/Los_Angeles        # added by Sam, 2024-03: "match the office clock"
DATABASE_URL=postgres://staging-db/ledgerline
python-dateutil==2.9.0
```

Production:

```
PYTHON_VERSION=3.12.6
DATABASE_URL=postgres://prod-db/ledgerline
python-dateutil==2.9.0
```

Note from Sam, the platform engineer: a container with no `TZ` setting keeps its clock in UTC.

## 5. Log excerpts: the same invoice, the same evening

Staging, the October 19 run (staging logs in Pacific time):

```
2026-10-19 18:00:03 PDT  late-fee-run start  today=2026-10-19
2026-10-19 18:00:03 PDT  INV-1042 due=2026-09-19 days_overdue=30 fee=0.00
2026-10-19 18:00:04 PDT  late-fee-run done   invoices=312 fees_applied=4
```

Production, the same run (production logs in UTC):

```
2026-10-20T01:00:02Z  late-fee-run start  today=2026-10-20
2026-10-20T01:00:02Z  INV-1042 due=2026-09-19 days_overdue=31 fee=15.00
2026-10-20T01:00:03Z  late-fee-run done   invoices=312 fees_applied=7
```

## 6. The invoice's database row

Staging's database is refreshed from production's every night, so the row is the same in both:

| invoice | customer | due_date (a DATE column, no time of day) | balance |
|---|---|---|---|
| INV-1042 | Hollis Garden Supply | 2026-09-19 | 1000.00 |
