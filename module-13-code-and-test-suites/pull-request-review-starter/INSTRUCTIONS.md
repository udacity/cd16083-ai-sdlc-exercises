# Review Pull Request #412

Ledgerline makes invoicing software for small businesses. Pull request #412 adds a late fee for overdue invoices, and it is waiting for someone to click Merge. Your job is to review it against what the team wrote down, decide whether it should merge, and say what has to be true before it does. You do not need to run any code.

## What you will produce

The completed `worksheet.md`, Parts A through F.

## Requirements

- **Part A:** Fill in the empty rows of the fee table using the acceptance criterion, not the code. Score the three review questions: behavior against the criterion, scope against the description, and dependencies against the approved list. The code-reading rows are optional.
- **Part B:** Answer the four test-quality questions on the printed tests (one row is worked for you), and count how many tests would fail if the code were correct.
- **Part C:** Answer the four pipeline questions on `ci.yml` (one row is worked for you): whether the tests run, whether a failing test stops the deploy, whether secrets are kept out of the file, and whether a person approves a production deploy.
- **Part D:** Score the AI review summary in section 3 of `case-file.md`, and say how many of the three problems it could have found, and why.
- **Part E:** Complete the three responsible-use rows and the table that tracks how each document words the rule for when the fee applies.
- **Part F:** Decide merge or defer, name the row that decides it, and say what has to be true before this merges. Finish with the short reflection.

## Files

- `case-file.md`: the developer's description, the acceptance criterion, who used AI for what, and the approved dependencies
- `late_fee.py` and `test_late_fee.py`: the change and its tests (also printed in the worksheet)
- `ci.yml`: the pipeline file as it is in the pull request (also printed in the worksheet). The deploy key in it is a placeholder, not a real key.
- `worksheet.md`: your answers

## Tools

None required.
