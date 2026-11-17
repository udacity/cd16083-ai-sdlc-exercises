# Worksheet: evaluate delivery artifacts and assess responsible use
Your name:

Pass or fail, throughout: a row passes only when its own "pass when" sentence is true. Write what you found first; the verdict follows from it.


## Part H. An environment-specific defect

Keep `deployment-packet.md` open beside this worksheet. Suppose the pull request was corrected and merged; the packet is what the on-call engineer gathered twelve days later.

**H1. Four facts from the packet.** One row at a time: open the section the row names and fill both environments from it before the next row.

| Fact | Section | Staging | Production |
|---|---|---|---|
| Commit deployed: the hash in the Commit column, not the time | 2 | `5e1c2a9` | `5e1c2a9`, the same |
| `TZ` setting in the application container | 4 | `TZ=America/Los_Angeles` | not set; Sam's note: no `TZ` means UTC |
| The fee job's scheduled time and time zone | 3 | 18:00 America/Los_Angeles | the same |
| INV-1042 on October 19: `today=` and `days_overdue=` in the log | 5 | `today=2026-10-19`, `days_overdue=30` | `today=2026-10-20`, `days_overdue=31` |

**H2. Five hypotheses, yours before the assistant's.** A hypothesis is disproved when a packet section shows the two environments the same on that point, or shows the claim false. Row 1 is done for you.

| # | Hypothesis | Section that would disprove it | What it shows | Disproved? (yes/no) |
|---|---|---|---|---|
| 1 | The fix did not reach production: the code differs between the environments | 2 | the same commit `5e1c2a9` in both, nothing deployed since | yes |
| 2 | The due date is stored a day early in production's database | 6 | the same row in both, `due_date` 2026-09-19; both logs print `due=2026-09-19` | yes |
| 3 | The job runs at a different time in production | 3, and 5 | identical schedule; both runs at the same instant (18:00:03 PDT is 01:00:02Z) | yes |
| 4 | Production has a different version of Python or of the date library | 4 | the same Python and `python-dateutil` versions | yes |
| 5 | At 6 pm Pacific, the date the code calls "today" is already the next day in production | 4 and 5 | no `TZ` in production; `today=` one day apart at the same instant | no |

The hypothesis left standing: #5. The two sections that support it: 4 and 5.

**H3. The assistant's ranking.** Paste the whole answer between the marker lines, then score it.

```
---- assistant's answer starts ----

## Hypotheses

1. **Timezone mismatch: production's container clock is UTC, so `date.today()` is a day ahead at the 6 pm Pacific run.**
   - Evidence in the packet: the 6:00 pm Pacific run is 01:00 UTC the next day (section 5). Production logs `today=2026-10-20` against staging's `today=2026-10-19` for the same run. Staging sets `TZ=America/Los_Angeles` and production does not, and Sam notes that a container with no `TZ` stays in UTC (section 4).
   - Disproving item: the identical commit and the identical scheduler timezone (sections 2 and 3) would disprove it only if both environments read the same date. They don't.
   - Disproved by the packet? **No.** The packet supports it directly.

2. **The code differs between environments (for example, `>= 30` in production).**
   - Disproving item: the deploy record (section 2) shows the same commit `5e1c2a9` in both environments, with nothing deployed since.
   - Disproved? **Yes**, for the code as deployed. The packet does not show the file contents, so it cannot confirm the threshold is `> 30`. That value comes from the commit title only.

3. **The scheduler runs at a different time or in a different timezone in production.**
   - Disproving item: the scheduler config (section 3) is identical in both environments.
   - Disproved? **Yes.** Both runs fired at 6:00 pm Pacific (18:00 PDT and 01:00Z).

4. **A different Python or dateutil version changes the day-count behavior.**
   - Disproving item: section 4 shows the same `PYTHON_VERSION=3.12.6` and `python-dateutil==2.9.0` in both environments.
   - Disproved? **Yes.**

5. **The data differs: the due date is different in production.**
   - Disproving item: section 6 says staging is refreshed from production nightly, so the row is the same. Both logs show `due=2026-09-19`.
   - Disproved? **Yes.** One caveat: the refresh is nightly, so the packet does not prove the rows matched at the moment of each run.

6. **The customer's count is wrong, and the invoice really is 31 days overdue.**
   - Disproving item: September 19 to October 19 is 30 days, and the staging log shows 30 (sections 5 and 6). The production result of 31 comes from the clock being a day ahead.
   - Disproved? **Yes.** The customer's count of 30 on Oct 19 is correct.

7. **The `late_fee` logic has an off-by-one for certain dates.**
   - Disproving item: the same function and commit produce correct output in staging.
   - Disproved? **Mostly.** Section 1 shows fees on invoices at 30 in production's count, which is consistent with Hypothesis 1. The function's source is not in the packet, so this is not fully excluded.

## Missing

- The source of `late_fee` and `run_late_fees.py`. The `> 30` threshold is known only from the commit title.
- Direct evidence of the production container's actual clock or timezone, for example the output of `date` or `echo $TZ`. The UTC clock is inferred from Sam's note and the UTC log timestamps.
- Whether other jobs in production depend on the container clock being UTC.
- Whether the ticket's complaint is confirmed against invoice terms beyond the customer's quote.
- Whether the 23 invoices were already collected or emailed, and whether fees were posted to ledgers or reminder emails were sent.

## Plan

**Smallest change:** set `TZ=America/Los_Angeles` in production's container settings, matching staging, and restart or redeploy the container so the run at 6:00 pm Pacific sees the Pacific date. This needs no code change.

**Undo:** remove the `TZ` line and restart the container. This returns production to UTC.

**Check before the next 6 pm run:** run `date` in the production container, or look at the log line `today=`. It should show the Pacific date.

**Cleanup, separate from the fix:** reverse the 23 early fees ($286.50), including Hollis Garden Supply's $15.00 on INV-1042. Reversing them is a data fix, not part of the config change.

---- assistant's answer ends ----
```

| Question | Where to look | Answer |
|---|---|---|
| Which hypothesis did it rank first? | Its "Hypotheses" heading, item 1 | your #5 |
| How many of its hypotheses point at a section of the packet as the thing that would disprove them? | Under each hypothesis, its line for the prompt's "name the item in the packet that would disprove it" | 7 of its 7 hypotheses |
| How many hypotheses did it list that are not among your five? | Its list against H2 | 2 (the customer miscounted; an off-by-one for certain dates) |
| Is any fact it lists under "Missing" stated in one of the six sections? | Its "Missing" list against the six sections | no |
| Does its plan name who approves the change? | Its "Plan" heading | no |

**H4. The plan.** Keep one: mitigate. Rollback puts the previous version back and removes the late fee for every customer until a fix ships.

| Field | Your entry |
|---|---|
| The change itself: what is set or deployed, in one sentence | Set `TZ=America/Los_Angeles` in production's container settings, the line staging already has, and restart the container before the next 6:00 pm run |
| Where it is made: configuration or code | Configuration. No code change, no pull request |
| Who approves it (a role or a name from `case-file.md`) | Sam, the platform engineer; Elena, the product owner, is told |
| How you confirm it worked: the log line to look for after the next 6 pm run | `today=` shows the Pacific date, and an invoice at 30 days prints `days_overdue=30 fee=0.00` |
| How to undo it | Remove the line and restart; production is back to UTC in one step |
| Customers to make whole: how many, how much (section 1) | 23 invoices, $286.50, Hollis Garden Supply's $15.00 among them |
| What the change does not fix, and who owns that follow-up | The code still takes "today" from the container's clock, so the next container without `TZ` repeats this. The developer owns a code change that computes the business date explicitly, with a test for the 6 pm case, through the pipeline with review |
