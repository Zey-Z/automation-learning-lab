# Week 2 Closeout Check

**Goal:** verify that Week 2 ideas are explainable, not just runnable.
**Format:** 10 questions - 5 concept checks + 5 recognition / light application checks.

Write your answer directly under each question.

---

## Q1 - GET vs POST

In 2-3 sentences, explain the difference between `GET` and `POST` using a real example.

Your answer:
get is to request data, post is to send new data to create new resourse.
---

## Q2 - 401 vs 403

In plain language:
- what does `401` usually mean?
- what does `403` usually mean?

Your answer:
401 lack of valid authorization
403 the server refuse to authorize it
---

## Q3 - 404 vs 429

In plain language:
- what does `404` usually mean?
- what does `429` usually mean?

Your answer:
404 server can not find the page
429 too many request
---

## Q4 - Resource vs endpoint

Using `orders` as the example:
1. what is the resource?
2. what is a collection endpoint?
3. what is a single-item endpoint?

Your answer:
orders
/orders
/orders/99
---

## Q5 - `dict.get(...)` vs `requests.get(...)`

In 2-3 sentences, explain why these two are not the same kind of `get`.

Your answer:
dict get is safely lookup a value
requests get is a method in http
---

## Q6 - tuple recognition

What is the main difference between a `list` and a `tuple` in Python?

Your answer:
lists are mutable, while tuples are not
---

## Q7 - `*args`

In one sentence, what does `*args` mean in a Python function signature?

Your answer:
args allows a function to recieve multiple positional argument. tuple
---

## Q8 - `**kwargs`

In one sentence, what does `**kwargs` mean in a Python function signature?

Your answer:
it allows to revieve multiple keyword. dict
---

## Q9 - class basics

Read this code:

```python
class Ticket:
    def __init__(self, ticket_id, priority):
        self.ticket_id = ticket_id
        self.priority = priority

t = Ticket("T-100", "high")
```

Answer:
1. what is the class name?
2. what values does `t` store?

Your answer:
你没教过我class是什么
class name is Ticket
t: "T-100"--ticket_id, "high"--"priority"
---

## Q10 - `if __name__ == "__main__"`

In plain language, what problem does this pattern solve?

Your answer:
it make sure only runs the code chunk when is not being imported