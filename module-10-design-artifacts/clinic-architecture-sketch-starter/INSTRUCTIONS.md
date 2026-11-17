# Score the Vendor's Sketch, Direct Your Own, and Decide Between Two

Cedar Clinic's vendor pasted an AI-generated architecture sketch into its proposal for online booking. Your job is to score that sketch against the clinic's brief, direct the assistant to produce a better one, ask for an alternative, and write the decision record that says which design to build and who decides.

## What you will produce

The completed `worksheet.md`, Parts B, E and H, including the audit-log check.

## Requirements

- **Part B:** Score the vendor's sketch on design checklist items 1, 3 and 4 (item 2 is worked for you), and name which failure would need the most rebuilding.
- **Part E:** Finish `scaffold-sketch.md`, run it in Claude Code, paste the sketch with its assumptions, and score it on items 1 and 3.
- **Audit-log check:** Find what your sketch's audit log records. If it records the old and new values of every change, say where the reason for visit now also lives.
- **Part H:** Ask the assistant for an alternative sketch with its assumptions listed, then fill in the decision record: Decision, Alternative considered, Why it lost, Assumptions both share that the clinic must confirm, and Who decides. Complete the second table: three failure modes in the vendor's sketch, what each would cost in delivery, and the quality gate that would catch it.

## Files

- `scenario-brief.md`: the clinic, its users, its rules and its existing systems
- `architecture-sketch-supplied.md`: the vendor's sketch
- `design-checklist.md`: the four questions you score with
- `scaffold-sketch.md`: the direction you complete and run
- `user-stories-supplied.md`: the vendor's user stories, for the last row of the failure-mode table
- `worksheet.md`: your answers

## Tools

Claude Code in the workspace, for Parts E and H.
