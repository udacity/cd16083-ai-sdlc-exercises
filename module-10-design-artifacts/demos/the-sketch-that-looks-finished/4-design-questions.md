# Four design questions

Four yes-or-no questions to ask of any architecture sketch, with the design brief open beside it. "Yes" means the sketch passes. For a "no", name the part of the sketch or the gap.

| # | Question | What a "no" looks like |
|---|---|---|
| 1 | Is the brief's system of record still the record, with the write to it and its failure described? | The data stored in a new place; the existing system "synced" or absent; nothing on a failed write. |
| 2 | Are the brief's existing systems reused rather than duplicated? | A new part that does what an existing system already does. |
| 3 | Is the sensitive data named, with where it is stored and who may read it? | Sensitive data stored, or shown, with no statement of who may see it. Encryption and logins say how data is protected, not who may read it. |
| 4 | Does the number of parts fit the problem? | More than about six parts (every box in the diagram is a part) for a problem this size, or the sketch itself saying a simpler shape would do. |
