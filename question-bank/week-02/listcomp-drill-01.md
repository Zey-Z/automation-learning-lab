# List Comprehension Drill — Week 2

**Instructions:** Write your answer directly below each question. Run your code to verify.

---

## Q1 — Basic map
Given `prices = [10, 25, 40, 60, 80]`, write a list comprehension that returns every price multiplied by 1.1 (10% markup).

**Your answer:**

---
```py
result = [price * 1.1 for price in prices]
```
## Q2 — Basic filter
Given the same `prices` list, return only prices greater than 30.

**Your answer:**
```py
result = [price for price in prices if price > 30]
```
---

## Q3 — Filter + map
Return prices greater than 30, each multiplied by 1.1.

**Your answer:**
```py
result = [price * 1.1 for price in prices if price > 30]
```
---

## Q4 — String transform
Given `tags = ["  crm ", "SALES", " marketing", "CRM"]`, return a list with each tag stripped and lowercased.

**Your answer:**
```py
result = [tag.strip().lower() for tag in tags]
```
---

## Q5 — Dict field extract
Given:
```python
users = [
    {"name": "Ana", "active": True},
    {"name": "Ben", "active": False},
    {"name": "Cara", "active": True},
]
```
Return a list of names for active users only.

**Your answer:**
```py
result = [user["name"] for user in users if user["active"] == True]
```
---

## Q6 — Ternary in expression
Using `prices = [10, 25, 40, 60, 80]`, return a list of strings: `"high"` if price >= 50, else `"low"`.

Expected: `["low", "low", "low", "high", "high"]`

**Your answer:**
```py
result = ["high" if price >= 50 else "low" for price in prices ]

```
---

## Q7 — Build new dicts
Using the `users` list from Q5, return a list of dicts with shape `{"name": ..., "label": "active"}` for active users only.

**Your answer:**
```py
result = [{"name":user["name"], "label":"active"} for user in users if user["active"] == True]
```
---

## Q8 — Nested field access
Given:
```python
orders = [
    {"id": 1, "customer": {"name": "Alice"}, "total": 120},
    {"id": 2, "customer": {"name": "Bob"},   "total": 45},
    {"id": 3, "customer": {"name": "Carol"}, "total": 200},
]
```
Return a list of customer names where total > 100.

**Your answer:**
```py
result = [cus["customer"]["name"] for cus in orders if cus["total"] > 100]
```
---

## Q9 — Dedup with set + comprehension
Given `emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]`, return a sorted list of unique emails.

Hint: `set()` removes duplicates. You can sort with `sorted()`.

**Your answer:**
```py
result = sorted(set(emails))
```
---

## Q10 — Combine two skills
Using the `orders` list from Q8, return a list of dicts with shape:
```python
{"name": "Alice", "total": 120, "size": "large"}
```
Rules:
- All orders (no filter)
- `name` comes from `order["customer"]["name"]`
- `size`: `"large"` if total >= 100, else `"small"`

**Your answer:**
```py
result = [{"name": order["customer"]["name"], "total": order["total"], "size":"large" if order["total"] >= 100 else "small" } for order in orders]
```

```py
leads = [
    {"name": "Carol", "score": 91},
    {"name": "Alice", "score": 82},
    {"name": "David", "score": 47},
]

sorted(leads, key=lambda lead: lead["score"], reverse= True)

```