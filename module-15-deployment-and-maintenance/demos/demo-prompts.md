# Module 15 demo prompts

Apply Responsible Use Across Deployment and Maintenance

Every prompt used in this module's demo videos, in the order it was pasted into Claude Code in the Udacity workspace. Where a prompt refers to a file, the file sits in the demo's workspace folder.

# Demo 1: Reading a pipeline before you trust it

Workspace folder: pipeline-demo (pipeline-questions.md, ci.yml).

> Read pipeline-demo/ci.yml. Fix three things and nothing else: remove continue-on-error so a failing test stops the deploy; read DEPLOY_API_KEY from the pipeline's secret store instead of the file; add environment: production to the deploy job. Change only ci.yml, then show me the diff.

# Demo 2: A production plan in seven fields

Workspace folder: alder-box-incident (incident.md, production-plan.md).

> Read alder-box-incident/incident.md. Fill in alder-box-incident/production-plan.md, one entry for each of the seven fields. Use only what the incident file says. Where the file doesn't give you enough to fill a field, say so in that field instead of guessing.
