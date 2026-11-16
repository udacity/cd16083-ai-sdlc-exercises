# The pipeline: four questions

The pipeline file, `ci.yml`, for the billing service.

- A **pipeline** is the set of automated steps that run when code changes.
- A **job** is one group of those steps. This file has two: **test** runs the tests, and **deploy** waits for test and then puts the change into production, where customers use it.
- A **secret** is a password or key the pipeline needs. It belongs in the pipeline's secret store, never in a file.

| # | Question, and what a "no" looks like | Find | Pass when |
|---|---|---|---|
| 1 | Does the pipeline run the tests? | The line `run: pytest` | It exists |
| 2 | Does a failing test stop the deploy? A no: the test step is told to carry on after a failure. | The line directly under `run: pytest` | That line is not `continue-on-error: true` |
| 3 | Are secrets kept out of the file? A no: a key or password written in the file. | A line containing `KEY` or `PASSWORD` with a value in quotes | No such line |
| 4 | Does a person approve a production deploy? A no: the deploy job names no environment, so nothing waits for a person and the deploy runs on every push to main. | A line `environment:` under the deploy job. (`env:` is a different thing: a list of variables.) | The deploy job names an environment, such as `environment: production` |
