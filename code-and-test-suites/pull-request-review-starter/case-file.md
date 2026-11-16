# Case file: late fee for overdue invoices, pull request #412

Ledgerline is an invoicing service used by small businesses. This pull request adds a late fee to
its billing service. It is waiting for someone to click Merge. The four sections below are
everything the team recorded about it.

## 1. The change, in the developer's words

From the pull request description, written by Priya (developer), October 6:

> Adds a late fee for overdue invoices: 1.5% of the overdue balance, at least $5 and at most $25,
> for invoices 30 days or more overdue. Only `late_fee.py`, its tests, and `requirements.txt`
> changed. I generated the function and the tests with Copilot Chat, ran the tests (4 of 4 pass),
> and had Copilot Chat review the code; its summary is below. Fees for six example invoices are in
> the pull request. Ready to merge.

## 2. The acceptance criterion, as agreed with the product owner

Written by Elena (product owner), September 29, in the ticket:

> When a payment is more than 30 days overdue, a late fee applies: 1.5% of the overdue balance, at
> least $5 and at most $25. Example: an invoice due September 1 gets no fee on October 1 and gets a
> fee on October 2.

## 3. Who used AI for what, and who approved what

| # | When | Who | What they did | What they gave the tool, or approved on |
|---|---|---|---|---|
| 1 | Oct 6, 9:40 am | Priya (developer) | Asked Copilot Chat to write the function | The first sentence of her description in section 1, the rule as she worded it |
| 2 | Oct 6, 9:52 am | Priya | Asked Copilot Chat for tests "for this function"; ran them, 4 of 4 pass | The function |
| 3 | Oct 6, 10:05 am | Priya | Asked Copilot Chat to review the code and pasted its summary into the pull request: "The function correctly applies a 1.5% late fee with a $5 minimum and $25 maximum for invoices 30 or more days overdue. No issues found." | The function |
| 4 | Oct 6, 10:10 am | Priya | Added the package `python-dateutil` to `requirements.txt` in the same pull request | No approval requested |
| 5 | Oct 7, 8:15 am | Marcus (reviewer) | Approved the pull request with the comment "Looks good to me (LGTM) per Copilot review". He opened the pull request at 8:11 am. | The Copilot Chat summary (row 3) |
| 6 | | Elena (product owner) | Not on the pull request. Her last contact with the change was writing the acceptance criterion on September 29. | |

How a change reaches customers at Ledgerline: a person clicks Merge after one approval. The
pipeline (`ci.yml`) then runs on the main branch and deploys to production.

## 4. Approved dependencies

Packages the team may use without a separate review, as of October 1. Anything else needs a
recorded approval from the platform engineer, Sam.

`requests`, `pytest`, `sqlalchemy`, `python-dotenv`, `stripe`
