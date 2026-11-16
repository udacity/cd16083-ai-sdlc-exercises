# Decision record

| Field | Your entry |
|---|---|
| Decision | A step in the nightly job (the plan's option), with three changes: a production migration step owned by the platform engineer, the template built without TemplateKit Pro unless it is approved, and the send log cut to what support needs, with a retention period. |
| Alternative considered | A separate reminder service with its own schedule. |
| Why it lost | One more service for a team of four to run, and about three more days. The nightly job already reads the subscriptions it needs; a failure in the reminder step can be kept from stopping the charges inside the job. |
| Assumptions to confirm | The sending limit, if any (platform engineer, with the sending service). Whether a paid library is allowed, and who approves it. What the send log keeps and for how long. Whether the developer is free full-time. How much QA and platform time the release needs. |
| Who decides | The product owner for the behavior and the send log; the platform engineer for the migration and the sending service. |
