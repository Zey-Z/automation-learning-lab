# Dict Methods + Dict Comprehension Drill — Week 2

**Instructions:** Write your answer directly below each question.

---

## Q1 — Basic `.items()` loop
Given `user = {"name": "Alice", "age": 30, "role": "engineer"}`, write a for loop that prints each key and value on its own line, like:
```
name -> Alice
age -> 30
role -> engineer
```

**Your answer:**
for key,value in user.items:
    print(f"{key} -> {value}")

---

## Q2 — Dict comprehension from list
Given `names = ["alice", "bob", "carol"]`, write a dict comprehension that maps each name to its length.
Expected: `{"alice": 5, "bob": 3, "carol": 5}`

**Your answer:**
{name:len(name) for name in names}
---

## Q3 — Dict comprehension from list of dicts
Given:
```python
products = [
    {"sku": "A1", "price": 20},
    {"sku": "B2", "price": 45},
    {"sku": "C3", "price": 10},
]
```
Build a dict mapping sku to price.
Expected: `{"A1": 20, "B2": 45, "C3": 10}`

**Your answer:**
{product["sku"]: product["price"] for product in products}
---

## Q4 — Filter with dict comprehension
Using the same `products` list, build a dict mapping sku to price for products where price > 15 only.
Expected: `{"A1": 20, "B2": 45}`

**Your answer:**
{product["sku"]:product["price"] for product in products if product["price"] > 15}
---

## Q5 — Group-by with for loop
Given `words = ["apple", "ant", "banana", "bat", "cherry"]`, group words by their first letter.
Expected: `{"a": ["apple", "ant"], "b": ["banana", "bat"], "c": ["cherry"]}`

Hint: use the same pattern as Task 3 from the exercise (`if key not in dict`, then `.append()`).

**Your answer:**
result = {}
for word in words:
    f = word[0]
    if f not in result:
        result[f] = []
    result[f].append(word)
---

## Q6 — Transform values with `.items()`
Given `temps_f = {"mon": 72, "tue": 85, "wed": 60}`, write a dict comprehension that converts each temperature from Fahrenheit to Celsius.
Formula: `(f - 32) * 5 / 9`

Round to 1 decimal: use `round(value, 1)`.

**Your answer:**
{key: round((f -32) * 5 / 9, 1) for key, f in temps_f.items()}
---

## Q7 — Ternary in dict comprehension
Given:
```python
tickets = [
    {"id": 1, "priority": 3},
    {"id": 2, "priority": 7},
    {"id": 3, "priority": 1},
    {"id": 4, "priority": 9},
]
```
Build a dict mapping id to label. Label is `"urgent"` if priority >= 5, else `"normal"`.
Expected: `{1: "normal", 2: "urgent", 3: "normal", 4: "urgent"}`

**Your answer:**
{ticket["id"]: "urgent" if ticket["priority"]>= 5 else "normal" for ticket in tickets}
---

## Q8 — Nested access + dict comprehension
Given:
```python
employees = [
    {"name": "Ana", "dept": {"name": "Sales", "floor": 2}},
    {"name": "Ben", "dept": {"name": "Engineering", "floor": 5}},
    {"name": "Cara", "dept": {"name": "Sales", "floor": 2}},
]
```
Build a dict mapping employee name to their department name.
Expected: `{"Ana": "Sales", "Ben": "Engineering", "Cara": "Sales"}`

**Your answer:**
{employee["name"]: employee["dept"]["name"] for employee in employees}
---

## Q9 — Group-by with transform
Using the same `employees` list from Q8, group employee names by department name.
Expected: `{"Sales": ["Ana", "Cara"], "Engineering": ["Ben"]}`

**Your answer:**
result = {}
for employee in employees:
    dept = employee["dept"]["name"]
    if dept not in result:
        result[dept] = []
    result[dept].append(employee["name"])
---

## Q10 — Combine everything
Given:
```python
orders = [
    {"customer": "Alice", "amount": 120, "status": "paid"},
    {"customer": "Bob",   "amount": 45,  "status": "pending"},
    {"customer": "Carol", "amount": 200, "status": "paid"},
    {"customer": "David", "amount": 80,  "status": "paid"},
    {"customer": "Eve",   "amount": 30,  "status": "pending"},
]
with open("", "w") as f:
    f.write("hello")
```
**Step A:** Write a dict comprehension that maps customer name to amount, for paid orders only.

**Step B:** From that result, use `.items()` and a dict comprehension to create a new dict where amount is replaced by tier: `"gold"` if amount >= 100, else `"silver"`.

**Your Step A answer:**
A = {order["customer"]:order["amount"] for order in orders if order["status"] == "paid"}
**Your Step B answer:**
B = {key: "gold" if value >= 100 else "silver" for key, value in A.items()}
