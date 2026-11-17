# Worksheet: evaluate delivery artifacts and assess responsible use
Your name:

Keep `case-file.md` open beside this worksheet; every Part sends you back to it. The two things you evaluate (the fee table and list of changed files, and the test file) and every checklist question are printed here where you use them.

Pass or fail, throughout: a row passes only when its own "pass when" sentence is true. Write what you found first; the verdict follows from it.

## Part A. The change, without reading the code

**The fee table.** Priya ran the code on six example invoices and pasted the results into pull request #412. The acceptance criterion is section 2 of `case-file.md`: a fee of 1.5% of the overdue balance, at least $5 and at most $25, when the payment is more than 30 days overdue. Fill the two right-hand columns for the four empty rows; two rows are done for you.

| Days overdue | Overdue balance | Fee the code produced | Fee by the acceptance criterion | Match? (yes/no) |
|---|---|---|---|---|
| 10 | $1,000 | $0.00 | $0.00 | yes |
| 29 | $1,000 | $0.00 | $0.00 | yes |
| 30 | $1,000 | $15.00 | $0.00 | no |
| 31 | $1,000 | $15.00 | $15.00 (1.5% of $1,000) | yes |
| 45 | $200 | $5.00 | $5.00 (1.5% of $200 is $3; the $5 minimum applies) | yes |
| 60 | $4,000 | $25.00 | $25.00 (1.5% of $4,000 is $60; the $25 maximum applies) | yes |

**The files the pull request changed**, from the pull request's Files tab:

```
late_fee.py         new, 14 lines
test_late_fee.py    new, 23 lines
invoice_email.py    changed, 3 lines added (puts the late fee in the reminder email)
requirements.txt    changed, 1 line added: python-dateutil
```

Three code-review questions. Each row says where to look and when it passes.

| # | Question, and what a "no" looks like | Where to look | Pass when | What you found | Pass or fail |
|---|---|---|---|---|---|
| 1 | Does the code's behavior match the acceptance criterion? A no: any example fee that the criterion would not give. | The fee table above | Every row of the fee table is a yes | Rows marked no: 30 days | fail |
| 2 | Does the change touch only what the developer's description says? A no: a changed file the description does not name. `test_late_fee.py` counts as named: section 1 says "its tests". | The list of changed files above, against section 1 of `case-file.md` ("Only `late_fee.py`, its tests, and `requirements.txt` changed") | Every file in the list is named in section 1 (`test_late_fee.py` is "its tests") | File not named: `invoice_email.py` | fail |
| 3 | Is every new dependency on the approved list? A no: a package added to `requirements.txt` that section 4 of `case-file.md` does not list. | The last line of the changed-files list, against section 4 of `case-file.md` | The added package is in section 4, or section 3 records an approval from Sam, the platform engineer section 4 names as the approver | Package: `python-dateutil` on the list: no | fail |

**Optional, if you read code.** The function as written. Skip this table if you do not read code; nothing later depends on it.

```python
from dateutil import parser


def late_fee(balance, due_date, today):
    due = parser.parse(due_date).date()
    days_overdue = (today - due).days
    if days_overdue >= 30:
        fee = balance * 0.015
        if fee < 5:
            fee = 5
        if fee > 25:
            fee = 25
        return round(fee, 2)
    return 0.0
```

| # | Question | Pass when | What you found | Pass or fail |
|---|---|---|---|---|
| 4 | Does the comparison on the "if days_overdue" line match "more than 30 days"? | The operator is `>` (more than), not `>=` (30 or more) | Operator: `>=` | fail |
| 5 | Could a reader learn the rule from the code alone? | A comment or docstring states the rule in words (the bare numbers 30, 0.015, 5 and 25 do not count) | Stated in words: no | fail |

## Part B. The tests

The test file, as generated. A **test** here is a short function that runs the code with one input and checks one expected answer; the test passes when the answer matches. The comment above each test says how many days overdue its example is. All four tests pass on the code as written (section 3 of `case-file.md`: "4 of 4 pass").

```python
from datetime import date

from late_fee import late_fee


def test_no_fee_under_30_days():
    # due September 20, checked September 30: 10 days overdue
    assert late_fee(1000.00, "2026-09-20", date(2026, 9, 30)) == 0.0


def test_fee_at_30_days():
    # due September 1, checked October 1: 30 days overdue
    assert late_fee(1000.00, "2026-09-01", date(2026, 10, 1)) == 15.00


def test_minimum_fee():
    # due August 1, checked September 15: 45 days overdue, 1.5% of $200 is $3
    assert late_fee(200.00, "2026-08-01", date(2026, 9, 15)) == 5.00


def test_returns_number():
    # due August 1, checked October 1: 61 days overdue
    assert isinstance(late_fee(500.00, "2026-08-01", date(2026, 10, 1)), float)
```

Four test-quality questions. Each row says which test to find and when it passes. Row 2 is done for you.

| # | Question, and what a "no" looks like | Find | Pass when | What you found | Pass or fail |
|---|---|---|---|---|---|
| 1 | Does every test check a behavior the acceptance criterion names? A no: a test that checks only that something came back. | The test whose check (`assert`) names no fee amount | Every test's check names a fee amount | Test: `test_returns_number` | fail |
| 2 | Is the $5 minimum tested? | The test with "minimum" in its name | A test expects $5.00 for a fee that 1.5% would put under $5 | `test_minimum_fee`, 45 days, $200, expects 5.00 | pass |
| 3 | Is the $25 maximum tested? A no: no test expects 25.00. | A test that expects 25.00 | One exists | Test: none | fail |
| 4 | Does the test at the boundary expect what the acceptance criterion says, not what the code does? A no: a test at 30 days that expects a fee. | The test named `test_fee_at_30_days` | Its expected fee at exactly 30 days is 0.0 | Expected fee at 30 days: 15.00 | fail |

Count. The tests pass 4 of 4. How many of the four would fail if the code charged no fee at 30 days, as the acceptance criterion says? 1 (`test_fee_at_30_days`) (A test that fails on correct code is written from the code, not from the rule.)

## Part D. The AI review

Paste the assistant's answer between the two lines:

---------- review start ----------

The function correctly applies a 1.5% late fee with a $5 minimum and $25 maximum for invoices 30 or more days overdue. No issues found.

---------- review end ----------

Score the review by finding things. Row 1 is about the explanation; rows 2 to 4 are about the review.

| # | Question | Find | What you found | Answer |
|---|---|---|---|---|
| 1 | Does the explanation state the rule as the acceptance criterion does? | The sentence in the Explanation that says when the fee applies | Its few words: "30 or more days overdue" | 30 days or more |
| 2 | Does the review find the day-30 problem? | "30" in the Review section | "No issues found" | no |
| 3 | Does the review mention `invoice_email.py` or `python-dateutil`? | Those two names in the Review section | neither name appears | no |
| 4 | How many items does the Review section list, and how many of them are about the 30-day boundary? The rest are claims the acceptance criterion does not mention; each is one more thing to check. | The numbered or bulleted items in the Review section | 0 items in all; 0 about the 30-day boundary | 0 other items |

Compare. Your Part A rows 1 to 3 found three problems: the fee at 30 days, the extra file `invoice_email.py`, and the package `python-dateutil`. The review found 0 of the three. It could find at most one: the other two need the changed-files list and the approved list in section 4 of `case-file.md`, and the prompt carried neither.

## Part E. Responsible use, across the whole case file

Three questions on section 3 of `case-file.md`, "Who used AI for what, and who approved what". Each row says what to find and when it passes.

| # | Question, and what a "no" looks like | Find in section 3 | Pass when | What you found | Pass or fail |
|---|---|---|---|---|---|
| 1 | Did the reviewer approve with evidence in hand? A no: an approval given on the AI's summary of the code. | Row 5 (Marcus), last column | He approved on the fee table, the tests, or the code | Approved on: the Copilot Chat summary (row 3) | fail |
| 2 | Did the person who owns the rule see the result? A no: the product owner's last contact is before the code existed. | Row 6 (Elena) | Her row shows her seeing the fee table or the pull request | Her last contact: writing the acceptance criterion, September 29 | fail |
| 3 | Was the new dependency approved by the person section 4 names? A no: no approval recorded. | Row 4 (`python-dateutil`), and section 4 for who approves | A recorded approval from that person | Approval: none ("No approval requested") | fail |

**The rule, in each place it was written**, in time order. Copy the words each document uses for when the fee applies, then say whether they agree with the acceptance criterion. The first row is done for you; the test row asks for a number.

| When | Where | The words used for when the fee applies | Agrees with the acceptance criterion, "more than 30 days"? (yes/no) |
|---|---|---|---|
| Sept 29 | Section 2 of `case-file.md`, the acceptance criterion | more than 30 days overdue | yes |
| Oct 6, 9:40 am | Section 1 of `case-file.md`, the first sentence of the developer's description (what Priya gave Copilot Chat, per section 3 row 1) | 30 days or more overdue | no |
| Oct 6, 9:52 am | Part B of this worksheet, the test named `test_fee_at_30_days` | at 30 days, expects a fee of $15.00 | no |
| Oct 6, 10:05 am | Section 3 of `case-file.md`, row 3, the Copilot Chat review summary Marcus approved on | 30 or more days overdue | no |

The earliest row marked no is where the wording left the acceptance criterion: Oct 6, 9:40 am, the first sentence of Priya's description. Every row after it followed that wording.

## Part F. The decision

Three questions, answered from what is already in this worksheet and the case file.

| Question | Where to look | Answer |
|---|---|---|
| Did any of rows 1 to 3 in Part A fail? | Part A of this worksheet | yes |
| If you clicked Merge now, would the fee at 30 days reach customers? | The last paragraph of section 3 of `case-file.md`: what happens after someone clicks Merge | yes |
| Has the change reached customers already? | The first paragraph of `case-file.md` | no |

Decision, keep one and delete the other: defer. Rollback is for a change that has already reached customers; your third answer says whether this one has.

Reasoning, two or three sentences: the row in Part A, B, or C that decides it, and what has to be true before this change merges.

Part A row 1 decides it: at exactly 30 days the code charges $15 where the acceptance criterion says $0. Before this merges, the 30-day fee must be $0, `test_fee_at_30_days` must expect 0.0, and `invoice_email.py` and `python-dateutil` must be reviewed (with Sam's recorded approval for the package) or removed.

Reflection. How many minutes did your review take, from Part A to here? ____ In which Part did you notice your attention drop? ____
