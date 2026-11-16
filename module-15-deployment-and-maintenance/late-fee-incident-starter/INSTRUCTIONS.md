# A Late Fee Charged a Day Early

A customer was charged a late fee one day early in production, while staging, running the same commit, charged nothing. Your job is to work out why from the evidence the on-call engineer gathered, check an AI assistant's analysis of the same evidence, and write the production plan to fix it.

## What you will produce

The completed `worksheet.md`, Part H (H1 to H4).

## Requirements

- **H1:** Record four facts for staging and production from `deployment-packet.md`: the commit deployed, the time zone setting, the job's schedule and time zone, and the log line for invoice INV-1042 on October 19.
- **H2:** For each of the five hypotheses (row 1 is worked for you), name the section of the packet that would disprove it and whether it does. Name the hypothesis left standing and the two sections that support it.
- **H3:** Run `ranking-prompt.md` in Claude Code, then score the assistant's answer on the five questions in the worksheet, including whether its plan names who approves.
- **H4:** Write the seven-field production plan, say whether you would mitigate or roll back, and list the customers to make whole.

## Files

- `deployment-packet.md`: the six sections the on-call engineer gathered
- `case-file.md`: background on the late-fee change
- `ranking-prompt.md`: the prompt for H3, with the packet included
- `worksheet.md`: your answers

## Tools

Claude Code in the workspace, for H3.
