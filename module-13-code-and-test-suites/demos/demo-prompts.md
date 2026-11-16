# Module 13 demo prompts

Evaluate AI-Generated Code and Test Suites

Every prompt used in this module's demo videos, in the order it was pasted into Claude Code in the Udacity workspace. Where a prompt refers to a file, the file sits in the demo's workspace folder.

# Demo 1: The change, without reading the code

No live prompt. The demo reads the case file and the worksheet. The AI review it evaluates is quoted from the case file.

# Demo 2: A test written from the rule

Workspace folder: ledgerline-billing (the ILT challenge1-repo).

**Prompt 1: a test from the criterion.**

> This branch is pull request #412. The acceptance criterion is section 2 of case-file.md. Add one regression test to test_late_fee.py, written from the criterion's own example: an invoice due September 1 gets no fee on October 1 and a fee on October 2. Do not fix the code yet and do not change any other file. Run pytest and show me the result.

**Prompt 2: the fix.**

> Now fix late_fee.py so it follows the acceptance criterion. Change only what the criterion requires. Then run pytest again.

**Prompt 3: the old test** (used when the existing day-30 test fails after the fix):

> test_fee_at_30_days now fails. Was it written from the rule or from the code? Correct it so it matches the criterion, then run pytest.

