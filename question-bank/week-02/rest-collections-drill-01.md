# Session 13 Gap-Closing Drill - venv, REST, Collections

**Topic:** venv workflow, REST conventions, Python list/dict basics, JS fetch mapping
**Format:** 10 questions - 5 basic (Q1-Q5) + 5 variants (Q6-Q10)
**Rule:** write your answer directly under each question.

---

## Q1 - Create a venv

Write the PowerShell command to create a virtual environment called `.venv`.

Your answer:
python -m venv .venv #我感觉-m就是创建，第一个venv是有意思的venv，第二个.venv是给这个venv取名叫venv，就是后面写在路径里面的那个部分

---

## Q2 - Activate a venv

Write the PowerShell command to activate `.venv`.

Your answer:
.\.venv\Scripts\Activate.ps1 #每个部分是什么意思？
---

## Q3 - REST method

You want to update only the `status` field of task `42`.
Which HTTP method is the best fit?

Your answer:
PATCH 

---

## Q4 - List indexing and slicing

Given:

```python
nums = [10, 20, 30, 40, 50]
```

Write two lines:
1. store the first value in `first_num`
2. store `[20, 30, 40]` in `middle_nums`

Your answer:
first_num = nums[0]
middle_nums = nums[1:4]
---

## Q5 - Safe dict lookup

Given:

```python
lead = {"name": "Alice"}
```

Write one line that stores the lead's score in `score`, using `0` as the default if the key is missing.

Your answer:
score = lead.get("score", 0)
---

## Q6 - append vs extend

Given:

```python
items = ["a", "b"]
items.append("c")
items.extend(["d", "e"])
```

What is the final value of `items`?

Your answer:
["a", "b", "c", "d", "e"]
---

## Q7 - keys and values

Given:

```python
totals = {"alice": 120, "bob": 80}
```

Write:
1. one line that stores the keys view in `names`
2. one line that stores the values view in `amounts`

Your answer:
names = totals.keys()
amounts = totals.values()
---

## Q8 - Endpoint design

For each scenario, write the best endpoint and method.

1. Get all orders
2. Get order `99`
3. Delete order `99`

Your answer:
1. GET /orders
2. GET /orders/99
3. DELETE /orders/99
---

## Q9 - JS fetch JSON parsing

Inside an `async` function, write the two lines that:
1. send a GET request to `https://jsonplaceholder.typicode.com/users`
2. parse the JSON body into `data`

Your answer:
const response = await fetch(`https://jsonplaceholder.typicode.com/users`)
const data = await response.json()
---

## Q10 - Mini mapping question

In one or two sentences, explain the mapping below:

- Python: `response = requests.get(url, params={"userId": 1}, timeout=10)`
- JS: what are the closest equivalents to `params` and `timeout`?

Your answer:
1. Request the order with userID = 1 at this url, wait 10s at most.
2. In JS we need to mannually construct the params into a url, but in py the requests automaticly does that for us. For timeout in py, it is a client "how long I want to wait" strategy, has no relation to HTTP, but for JS, it does not work innately, we have to set a timer outside of the main request, and it functions as pull out the request when it hits the time. 
