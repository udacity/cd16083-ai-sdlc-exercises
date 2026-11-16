# Demo files: Evaluate AI-Generated Code and Test Suites

The files shown in this module's two demo videos. Both demos use pull request #412 at Ledgerline, which adds a late fee for overdue invoices. The prompts pasted into Claude Code are in `demo-prompts.md`.

| Demo | Folder | Files |
|---|---|---|
| The change, without reading the code | `the-change-without-reading-the-code/` | The case file and Part A of the worksheet (the fee table, scope and dependency checks) |
| A test written from the rule, not from the code | `a-test-written-from-the-rule/` | The `ledgerline-billing` project at pull request #412, plus `pull-request-412.patch` and `make-demo-repo.sh` |

## Setting up the second demo

The demo needs the project's two commits (the baseline and pull request #412), and a Git history can't be stored inside this repository. To rebuild it, run this from the `a-test-written-from-the-rule/` folder:

```bash
bash make-demo-repo.sh
cd ledgerline-billing
pip install -r requirements.txt
pytest
```

`git log --oneline` should show two commits, and `pytest` should show 4 passed.
