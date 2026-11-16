# Design checklist

Four yes-or-no questions to ask of any architecture sketch, with the scenario brief open beside
it. "Yes" means the sketch passes the item. For a "no", name the part of the sketch or the gap.

| # | Question | What a "no" looks like |
|---|---|---|
| 1 | Is the brief's system of record still the record, with the write to it and its failure described? | Appointments stored in a new place; the existing system "synced" or absent; nothing on a failed write. |
| 2 | Are the brief's existing systems reused rather than duplicated? | A new part that does what an existing system already does. |
| 3 | Is the reason for visit named, with where it is stored and who may read it? | The reason stored somewhere with no statement of who can see it. Encryption and logins say how data is protected, not who may read this field. |
| 4 | Does the number of parts fit the problem? | More than about six parts (every box in the diagram is a part) for a clinic this size, or the sketch itself saying a simpler shape would do. |
