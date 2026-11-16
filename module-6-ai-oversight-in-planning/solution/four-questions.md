# Four questions, scored

Score each row by finding something. Write pass or fail and what you found.

| # | Question, and what a "no" looks like | Where to look | Pass when | Pass or fail | What you found |
|---|---|---|---|---|---|
| 1 | Does everything it states come from the change? A no: a limit, rule, fact or system stated as certain that nobody gave it. | Every stated fact or constraint, against "The change" | Everything it states appears in the change, or is marked as something to confirm | fail | "At most 500 emails per day": the change says only "a third-party sending service". Nothing about a limit, and the plan states it as fact. |
| 2 | Does it cover everything the change names? A no: a part of the change with no step, or no one to do it. | The steps or items, against the three parts of the change | Every part has a step, including who runs the production migration | fail | Step 1 adds reminded_for to the development database only. No step runs the migration in production, and no one is named for it; the release step doesn't mention it either. |
| 3 | Does it add only what was asked for? A no: a library, service or feature nobody requested, especially one that costs money or needs approval. | Every step or item | Every addition traces to the change, or is marked as needing approval | fail | Step 3: TemplateKit Pro, a paid library ($39 per developer per month), with no request and no approval. |
| 4 | Does it say what it rests on, and who does the work? A no: no owner, or a number with no assumptions about who does the work, who else it needs, or what is left out. | Owners, and any estimate | Every item or step has an owner, and any estimate names who does the work, who else it needs (QA, platform), and what it assumes | fail | "6 developer-days" assumes one developer full-time, no QA time, no platform engineer time for the migration and deploy, and no review time. None of it is stated. |

Then one more line, the data the plan keeps: what does it keep, for how long, and who decides?

reminder_log keeps every customer's name, email address, renewal amount and the full email body, including a working cancel link, with no retention period and no owner. The product owner decides what support needs and how long it is kept.
