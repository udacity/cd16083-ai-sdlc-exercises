# Lab 3 worksheet: evaluate delivery artifacts and assess responsible use

## Part A. The change, without reading the code

**The fee table.** Priya ran the code on six example invoices and pasted the results into pull request #412. The acceptance criterion is section 2 of `case-file.md`: a fee of 1.5% of the overdue balance, at least $5 and at most $25, when the payment is more than 30 days overdue. Fill the two right-hand columns for the four empty rows; two rows are done for you.

| Days overdue | Overdue balance | Fee the code produced | Fee by the acceptance criterion | Match? (yes/no) |
|---|---|---|---|---|
| 10 | $1,000 | $0.00 | $0.00 | yes |
| 29 | $1,000 | $0.00 | | |
| 30 | $1,000 | $15.00 | | |
| 31 | $1,000 | $15.00 | $15.00 (1.5% of $1,000) | yes |
| 45 | $200 | $5.00 | | |
| 60 | $4,000 | $25.00 | | |

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
| 1 | Does the code's behavior match the acceptance criterion? A no: any example fee that the criterion would not give. | The fee table above | Every row of the fee table is a yes | Rows marked no: ____ | |
| 2 | Does the change touch only what the developer's description says? A no: a changed file the description does not name. `test_late_fee.py` counts as named: section 1 says "its tests". | The list of changed files above, against section 1 of `case-file.md` ("Only `late_fee.py`, its tests, and `requirements.txt` changed") | Every file in the list is named in section 1 (`test_late_fee.py` is "its tests") | File not named: ____ | |
| 3 | Is every new dependency on the approved list? A no: a package added to `requirements.txt` that section 4 of `case-file.md` does not list. | The last line of the changed-files list, against section 4 of `case-file.md` | The added package is in section 4, or section 3 records an approval from Sam, the platform engineer section 4 names as the approver | Package: ____ on the list: yes / no | |
