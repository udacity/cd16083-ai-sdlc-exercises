# The team's prompts

Open this file only when the lab guide tells you to, after you have run your own scaffold.

These are the prompts the Alder Box team typed, one per workflow step. Each is reproduced as typed.
Steps 6 and 8 have no prompt. The full answers are in the `transcripts` folder.

## Step 1. Priya, Monday 9:10 am

```
Summarize this customer email and write a user story with acceptance criteria.

Subject: Charged when I meant to cancel

Can you email me before my subscription renews? I got charged on Saturday when I meant to cancel. I'd have cancelled if I'd had a heads-up.

[customer name, email address, and card digits removed]
```

## Step 2. Priya, Monday 9:30 am

```
What questions does this customer's request leave open? List them.
```

(Same conversation as step 1, so the assistant still had the email.)

## Step 3. Marcus, Tuesday 2:00 pm

Two prompts. The assistant answered the first by asking for a repository.

```
Write the code for this user story. It runs as part of our nightly job.

ABX-212

As a subscriber, I want an email reminder before my subscription renews, so that I can cancel before I am charged.

Acceptance criteria:
1. A reminder email is sent 24 hours before the renewal charge.
2. The email states the renewal date and the amount, and includes a link to cancel.
3. No reminder is sent for a subscription that has already been cancelled.
```

```
No repo yet. Write it standalone in Python so I can drop it into the nightly job.
```

(New conversation.)

## Step 4. Marcus, Tuesday 4:30 pm

```
Do these tests cover all three acceptance criteria?
```

(Same conversation as step 3. The assistant had written the tests with the code.)

## Step 5. Marcus, Tuesday 6:10 pm

```
Write a pull request description for this change.
```

(Same conversation as steps 3 and 4.)

## Step 6. Dana, Tuesday 6:40 pm

Dana did not use the assistant.

## Step 7. Sam, Wednesday 10:00 am

```
Write a release checklist for a feature that sends subscription renewal reminder emails.
```

(New conversation. Nothing else was provided.)
