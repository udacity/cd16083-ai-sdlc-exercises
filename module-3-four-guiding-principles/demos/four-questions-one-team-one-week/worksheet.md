# Worksheet: map an AI-assisted workflow to the guiding principles
Your name:

Keep `workflow-narrative.md` open beside this file; you will go back to it for every row. Do not open `team-prompts.md` until Part E asks for it.

## Part A. Principles map

Two rules. You are judging the team's handling of each step, not the person who acted. The step where a check was skipped gets the mark, not the step where the consequence showed up.

**First, the facts.** Pick from the lists. Workflow step 1 is done as the model, and steps 2 and 3 are worked in the first demo video. You do steps 6 and 7.

What was the output checked against? Pick one: **the email** · **the customer** · **the ticket comment** · **an AI output** (say which: the story's criteria, the code, the tests, or the description) · **nothing**

What was available to the team at this step and not used? Pick one or two: **the email** · **the ticket's criteria** · **the ticket comment** · **the change itself** · **the pull request** · **a fresher hour** · **nothing**

| Step | Checked against | Available and not used |
|---|---|---|
| 1. Priya turns the email into a user story | nothing | the email |
| 2. Priya asks what the request leaves open | | |
| 3. Marcus asks for the code | | |
| 6. Dana reviews | | |
| 7. Sam asks for a release checklist | | |

**Then, the marks.** **S**: the team satisfied the principle at this step. **V**: the team violated it. **–**: the question does not apply at this step. Each mark follows from the row's facts. Read the columns left to right and take the first that fits:

| Question | Mark V when | Mark S when | Mark – when |
|---|---|---|---|
| Where can you move up a level? | The team asked for a finished thing (a story, code, a description, a checklist) without saying what it must contain, or reworked the assistant's output by hand instead of restating what it must contain | The team asked for something it then judged itself: questions to choose from, or output checked against criteria it supplied | Nobody asked the assistant for anything at this step |
| Where might this over-rely on AI? | "Checked against" is an AI output or nothing | "Checked against" is the email, the customer, or the ticket comment | No AI output is produced or passed on at this step |
| How can we ensure quality? | A gate was due (code to run, a change to review, a release to check) and it checked only against an AI output, or was skipped | The gate checked against the email, the customer's answer, or a rule written from them; or a requirement was checked with the customer before anything was built | No gate was due: nothing was built, reviewed, or released at this step |
| Is it sustainable? | "Available and not used" includes a fresher hour | The narrative says the hour or the load was a factor and the team dealt with it (waited, or split the work); or the team waited for an answer instead of keeping the assistant's pace | The narrative mentions no hour or load pressure at this step |

| Step | Move up a level? | Over-rely on AI? | Ensure quality? | Sustainable? |
|---|---|---|---|---|
| 1. Priya turns the email into a user story | V | V | – | – |
| 2. Priya asks what the request leaves open | | | | |
| 3. Marcus asks for the code | | | | |
| 6. Dana reviews | | | | |
| 7. Sam asks for a release checklist | | | | |

Step 1, why: Priya asked for a story and criteria without saying what they must contain (V). The story went into the backlog with no check against the email (V). No quality gate was due yet, and time played no part (–, –).

## Part B. Evaluate the team's release checklist

Open `release-checklist-team.md`. Three questions. Quote item text; the list has no item numbers.

1. Name two items that describe something Alder Box does not have: a system, a tool, a process, or a team the narrative never mentions.
   -
   -
2. Does any item name an owner, someone who will do it and sign it off? Yes or no. If yes, quote one.

3. Find the item about when the reminder is sent (section 1 of `release-checklist-team.md`, first item). Does it check that the reminder goes out three days ahead, as the customer agreed? Yes or no. Quote the words that decide it.

## Part C. Direct the assistant with the scaffold

Open `scaffold.md`, finish the constraints and the evaluation criteria, and run it in your AI assistant. Paste the checklist it returned here.

```
(your assistant's checklist)
```

## Part D. Written evaluation

Three oversight decisions the team made, in the order they happened, and what went wrong on Monday morning because of each one. One line each.

| Step | The decision | What went wrong on Monday because of it |
|---|---|---|
| | | |
| | | |
| | | |

One sentence: why did the team's checklist look right and not be?

## Part E. Compare your checklist with the team's

Score your checklist against the three evaluation criteria in `scaffold.md`, the given one and the two you wrote:

| Your criterion | Pass or fail | The item that decides it (or "all", if every item passes) |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |

Now open `team-prompts.md` and read Sam's prompt for workflow step 7, the release checklist. In one sentence: what did your direction give the assistant that his did not?

## Part F. Optional: a direction from scratch, and your own workflow

Your direction for the reply email to the customer:

```
(context, constraints, examples, evaluation criteria, and one line saying what to produce)
```

The assistant's reply:

```
(paste here)
```

Scored against your own criteria:

| Your criterion | Pass or fail | Evidence |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |

The part of the direction you found hardest to write without the scaffold, and why:

Your own workflow, three to five steps:

| Step | What was the output checked against? | What was available and not used? | Move up a level? | Over-rely on AI? | Ensure quality? | Sustainable? |
|---|---|---|---|---|---|---|
| 1. | | | | | | |
| 2. | | | | | | |
| 3. | | | | | | |
| 4. | | | | | | |
| 5. | | | | | | |

One place where the same question gets a different answer in a different role, and whose map it came from:

## Part G. Optional: the repository evidence

Branches and commits, with times and messages:

For each question, where the evidence shows the principle satisfied or violated. Point to a commit, a time, or a line in the pull request.

| Question | Evidence | S or V |
|---|---|---|
| Where can you move up a level? | | |
| Where might this over-rely on AI? | | |
| How can we ensure quality? | | |
| Is it sustainable? | | |

What a reviewer would have needed that this history does not provide:

-
-
-
