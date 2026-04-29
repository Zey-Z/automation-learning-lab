# Session 6 Warmup — First Python Script

**Goal:** Translate a small JS snippet from Week 1 into Python, end-to-end runnable.
**Target time:** ~15 min
**Deliverable:** `exercises/week-02/session-06-warmup.py` (create this file, write and run it)

---

## The original JS (from Week 1 thinking)

```js
const orders = [
  { id: "O1", customer: "Alice", amount: 120, status: "paid" },
  { id: "O2", customer: "Bob",   amount: 50,  status: "pending" },
  { id: "O3", customer: "Carol", amount: 300, status: "paid" },
  { id: "O4", customer: "Dan",   amount: 75,  status: "paid" },
]

for (const order of orders) {
  if (order.status === "paid") {
    console.log(`${order.customer} paid $${order.amount}`)
  }
}
```

Expected output:
```
Alice paid $120
Carol paid $300
Dan paid $75
```

---

## Your task

Translate this JS snippet into Python. Write it to `exercises/week-02/session-06-warmup.py`, then run:
```bash
python exercises/week-02/session-06-warmup.py
```

**Requirements:**
1. Use a **list of dicts** (Python equivalent of array of objects).
2. Use a **for loop** to iterate.
3. Use an **if statement** to filter by status.
4. Use an **f-string** for the print statement.
5. Output must match the expected result exactly.

**Do NOT use:** list comprehension, `.filter()`, or any collection method you have not learned yet. Today only practice basic loop + if + f-string.

---

## Hints (use only if stuck)

<details>
<summary>Hint 1 — Dict key access</summary>
In Python, access a dict value by key with `dict["key"]`, not `dict.key`.
Example: `order["customer"]`, not `order.customer`.
</details>

<details>
<summary>Hint 2 — For loop syntax</summary>
```python
for order in orders:
    # indented block here
```
No parentheses, no `const` / `let`, colon at end of line, 4-space indent for the body.
</details>

<details>
<summary>Hint 3 — f-string with dict access</summary>
```python
print(f"{order['customer']} paid ${order['amount']}")
```
Note: inside the f-string `{}`, use single quotes `'` for the dict key when the outer f-string uses double quotes.
</details>

---

## After you run it

Paste 3 things in chat:
1. Your `.py` file content.
2. The terminal output you got.
3. Any errors you hit and how you fixed them (learning log).

## Reflection questions (answer in chat, one sentence each)
1. What felt most different from JS?
2. What felt surprisingly similar?
3. Any syntax that tripped you up?
