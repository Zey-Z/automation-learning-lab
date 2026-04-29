# Week 2 Practice Block - Mixed Python, APIs, and Main Wiring

Estimated time: ~2 hours
Goal: fluency across Week 2 skills. No major new concepts - this block is for recall, debugging, speed, and orchestration.

---

## Part 1: Timed Warm-up (20 min)

Set a timer. Try to finish all 5 without looking at notes.

### W1 - list comp: filter + map

```python
leads = [
    {"name": "Alice", "score": 82, "active": True},
    {"name": "Bob", "score": 45, "active": True},
    {"name": "Carol", "score": 91, "active": False},
    {"name": "Dan", "score": 77, "active": True},
]
```

Return a list of names for leads where `active` is `True` and `score >= 70`.
Expected: `["Alice", "Dan"]`

Your answer:
[lead["name"] for lead in leads if lead["active"] and lead["score"] >= 70]
---

### W2 - group-by accumulation

```python
orders = [
    {"team": "sales", "amount": 120},
    {"team": "ops", "amount": 50},
    {"team": "sales", "amount": 80},
    {"team": "ops", "amount": 70},
    {"team": "sales", "amount": 100},
]
```

Build a dict that totals `amount` by `team`.
Expected: `{"sales": 300, "ops": 120}`

Your answer:
result = {}
for order in orders:
    if order["team"] not in result:
        result[order["team"]]= 0
    result[order["team"]] += order["amount"]
---

### W3 - safe dict lookup

```python
ticket = {"id": "T-100", "title": "Broken webhook"}
```

Write one line that stores the priority in `priority`, using `"normal"` as the default if the key is missing.

Your answer:
priority= ticket.get("priority", "normal")
---

### W4 - request lifecycle

Write the canonical Python shape that:
1. sends a GET request to `url`
2. uses `params={"userId": 1}` and `timeout=10`
3. if the status code is `200`, parses JSON into `data`
4. otherwise sets `data = []`

Your answer:
import json
import requests
raw= requests.get("url", params= {"userId":1}, timeout= 10)
if raw.status_code != 200:
    data =[]
else:
    data =raw.json()

---

### W5 - main wiring order

You already have these helper functions:

```python
load_data(path)
filter_valid(data)
transform_data(data)
build_summary(data)
save_output(result, path)
```

Write a realistic `main()` shape that wires them together and prints the summary.

Your answer:
def main():
    data = load_data(path)
    data= filter_valid(data)
    data= transform_data(data)
    result= build_summary(data)
    save_output(result, path)

    print(result)
---

## Part 2: API Debugging Exercises (30 min)

For each snippet:
1. explain the main bug
2. rewrite only the broken line(s)

### D1 - wrong library name

```python
import requests

response = request.get("https://jsonplaceholder.typicode.com/users")
```

Your answer:
should be request“s”.get("url")
but i dont know what is the kind of what needed to be imported at the first called
---

### D2 - params vs headers confusion

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    headers={"userId": 1},
)
```

The goal is to ask for todos for one user.

Your answer:
params={"userId": 1}
i forgot what s the difference between headers and params. should nt it have no comma at the end of seconde line?
---

### D3 - wrong response property

```python
if response.status == 200:
    data = response.json()
```

Your answer:
should be if response.status_code == 200
---

### D4 - JSON parsing shape

```python
with open("input.json", "r") as f:
    data = f.json()
```

Your answer:
data = json.load(f)
---

### D5 - JS async parsing

```js
const response = await fetch(url)
const data = response.json()
```

Your answer:
should be 
const data = await response.json()
i remember i asked why response.json also needs to await, but i forgot why 
---

## Part 3: Timed Coding Challenge (30 min)

Starter file:
- `exercises/week-02/session-14-practice-challenge.py`

Input file:
- `exercises/week-02/session-14-raw-tickets.json`

Run:

```powershell
python exercises/week-02/session-14-practice-challenge.py
```

Task:
1. Read and parse the JSON file.
2. Keep only tickets where:
   - `status == "open"`
   - `priority` is `"high"` or `"urgent"`
   - `owner` is not empty after `strip()`
3. Normalize the kept tickets into this shape:
   - `id`
   - `owner` (trimmed + lowercased)
   - `team`
   - `priority`
4. Build a summary with:
   - `ticketCount`
   - `byTeam` totals
   - `urgentIds`
5. Write output to `exercises/week-02/session-14-triage-output.json`

Record:
- your final code
- terminal output
- one bug you hit and how you fixed it

---

## Part 4: Memorization Pass (20 min)

Close notes. Write each from memory.

### M1 - list comp filter + map

Write one list comprehension that returns cleaned emails for active users only.

Your answer:
[user["email"].strip() for user in users if user["active"]]
---

### M2 - group-by pattern

Write the canonical for-loop pattern that totals `amount` by `team`.

Your answer:
total= {}
for user in users:
    if user["team"] not in total:
        total[user["team"]] = 0
    total[user["team"]] += user["amount"]

---

### M3 - JSON read shape

Write the canonical shape for loading `data.json` into `data`.

Your answer:
import json
with open("data.json", "r") as f:
    data= json.load(f)
---

### M4 - JSON write shape

Write the canonical shape for writing `result` to `out.json` with `indent=2`.

Your answer:
import json
with open("out.json", "w") as f:
    json.dump(result, f, indent= 2)
---

### M5 - Python request shape

Write the canonical shape for:
- `requests.get(url, params={"userId": 1}, timeout=10)`
- status check
- `response.json()`

Your answer:
import requests
response = requests.get(url, params={"userId":1}, timeout= 10)
if response.status_code == 200:
    data= response.json()
---

### M6 - JS fetch shape

Inside an `async` function, write the minimal 2-line shape for `fetch(url)` + parse JSON.

Your answer:
const response = await fetch(url)
const data = await response.json()
---

### M7 - `if __name__`

Write the 2-line pattern that runs `main()` only when the file is executed directly.

Your answer:
if __name__ == "__main__":
    main()
    
---

### M8 - safe dict lookup

Write one line that gets `status` from `ticket`, using `"unknown"` as the default.

Your answer:
status= ticket.get("status", "unknown")
---

## Part 5: Speed Round (20 min)

Answer quickly. One line each.

### S1

What does this return?

```python
[n * 10 for n in [1, 2, 3] if n > 1]
```

Your answer:
[20, 30]
---

### S2

What does this return?

```python
{"a": 1, "b": 2}.get("c", 0)
```

Your answer:
0
---

### S3

What does this slice return?

```python
[10, 20, 30, 40, 50][1:4]
```

Your answer:
[20, 30, 40]
---

### S4

Which HTTP method is the best fit for deleting `/orders/9`?

Your answer:
DELETE
---

### S5

Which Python response property do you check for `200`?

Your answer:
status_code
---

### S6

In JS `fetch`, what must usually appear before `response.json()` inside an async function?

Your answer:
await
---

### S7

Write one line that appends `"urgent"` to `tags`.

Your answer:
tags.append("urgent")
---

### S8

Write one line that extends `tags` with `["api", "retry"]`.

Your answer:
tags.extend(["api", "retry"])
---

### S9

Write one line that creates a venv called `.venv`.

Your answer:
python -m venv .venv
---

### S10

Write one example of a single-item endpoint using `users` as the resource.

Your answer:
/users/99
