# Lab 3 worksheet: evaluate delivery artifacts and assess responsible use
Your name:

Fill this in as the lab guide directs. Keep `case-file.md` open beside this worksheet; every Part sends you back to it. The three things you evaluate (the fee table and list of changed files, the test file, and the pipeline file) and every checklist question are printed here where you use them. Do not open anything in `solutions/` until the lab guide says to.

Pass or fail, throughout: a row passes only when its own "pass when" sentence is true. Write what you found first; the verdict follows from it.

## Part H. Challenge 2: an environment-specific defect

Fill this in as Challenge 2 in the lab guide directs. Keep `deployment-packet.md` open beside this worksheet. Suppose the pull request was corrected and merged; the packet is what the on-call engineer gathered twelve days later.

**H1. Four facts from the packet.** One row at a time: open the section the row names and fill both environments from it before the next row.

| Fact | Section | Staging | Production |
|---|---|---|---|
| Commit deployed: the hash in the Commit column, not the time | 2 | | |
| `TZ` setting in the application container | 4 | | |
| The fee job's scheduled time and time zone | 3 | | |
| INV-1042 on October 19: `today=` and `days_overdue=` in the log | 5 | | |

**H2. Five hypotheses, yours before the assistant's.** A hypothesis is disproved when a packet section shows the two environments the same on that point, or shows the claim false. Row 1 is done for you.

| # | Hypothesis | Section that would disprove it | What it shows | Disproved? (yes/no) |
|---|---|---|---|---|
| 1 | The fix did not reach production: the code differs between the environments | 2 | the same commit `5e1c2a9` in both, nothing deployed since | yes |
| 2 | The due date is stored a day early in production's database | | | |
| 3 | The job runs at a different time in production | | | |
| 4 | Production has a different version of Python or of the date library | | | |
| 5 | At 6 pm Pacific, the date the code calls "today" is already the next day in production | | | |

The hypothesis left standing: #____. The two sections that support it: ____ and ____.

**H3. The assistant's ranking.** Paste the whole answer between the marker lines, then score it.

```
---- assistant's answer starts ----

---- assistant's answer ends ----
```

| Question | Where to look | Answer |
|---|---|---|
| Which hypothesis did it rank first? | Its "Hypotheses" heading, item 1 | your #____ / one not in H2 |
| How many of its hypotheses point at a section of the packet as the thing that would disprove them? | Under each hypothesis, its line for the prompt's "name the item in the packet that would disprove it" | ____ of its ____ hypotheses |
| How many hypotheses did it list that are not among your five? | Its list against H2 | ____ |
| Is any fact it lists under "Missing" stated in one of the six sections? | Its "Missing" list against the six sections | yes, item ____ / no |
| Does its plan name who approves the change? | Its "Plan" heading | yes / no |

**H4. The plan.** Keep one: mitigate / roll back. Rollback puts the previous version back and removes the late fee for every customer until a fix ships.

| Field | Your entry |
|---|---|
| The change itself: what is set or deployed, in one sentence | |
| Where it is made: configuration or code | |
| Who approves it (a role or a name from `case-file.md`) | |
| How you confirm it worked: the log line to look for after the next 6 pm run | |
| How to undo it | |
| Customers to make whole: how many, how much (section 1) | |
| What the change does not fix, and who owns that follow-up | |
