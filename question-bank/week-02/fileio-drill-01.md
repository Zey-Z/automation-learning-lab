# File I/O + json + Built-ins Drill — Week 2

**Instructions:** Write your answer directly below each question.

---

## Q1 — Basic read
Open a file called `config.txt` in read mode, read all its content into a variable called `text`, and print it.

**Your answer:**
with open("config.txt", "r") as f:
    text = f.read()
print(text)
---

## Q2 — Basic write
Open a file called `log.txt` in write mode and write the string `"Session complete"` to it.

**Your answer:**
with open("log.txt", "w") as f:
    f.write("Session complete")

---

## Q3 — Read JSON
Open `users.json` in read mode, load it with the json module, and store the result in a variable called `users`.

**Your answer:**
import json 
with open("users.json", "r") as f:
    users = json.load(f)

---

## Q4 — Write JSON
Given `data = {"name": "alice", "score": 90}`, write it to `out.json` with 2-space indentation.

**Your answer:**
with open("out.json", "w") as f:
    json.dump(data, f, indent= 2)

---

## Q5 — Built-ins quick check
Given `nums = [4, 9, 2, 7, 5]`, write one line each that produces:
- a) total of all numbers
- b) how many numbers
- c) the largest number
- d) the smallest number

**Your answer:**
a)sum(nums)
b)len(nums)
c)max(nums)
d)min(nums)

---

## Q6 — Read JSON + extract field
Open `products.json` (contains a list of dicts, each with `"sku"` and `"price"` keys), load it, and build a list of all prices using a list comprehension. Call the list `prices`.

**Your answer:**
with open("products.json", "r") as f:
    products = json.load(f)
prices = [product["price"] for product in products]
---

## Q7 — Compute average from file
Using `prices` from Q6, compute the average price rounded to 2 decimal places. Store it in `avg_price`.

**Your answer:**
avg_price = round(sum(prices) / len(prices), 2)

---

## Q8 — Read, filter, write
Open `leads.json` (list of dicts with `"name"` and `"score"`). Build a list of only the leads where `score >= 70`, then write that filtered list to `top-leads.json` with 2-space indent.

**Your answer:**
with open("leads.json", "r") as f:
    leads = json.load(f)
top_leads = [lead for lead in leads if lead["score"] >= 70]
with open("top-leads.json", "w") as f:
    json.dump(top_leads, f, indent = 2)

---

## Q9 — Combine summary + file write
Given a list of dicts called `orders` (each has `"customer"` and `"amount"` keys), build a summary dict with keys:
- `"count"`: total number of orders
- `"total_revenue"`: sum of all amounts
- `"top_amount"`: the largest amount

Then write this dict to `summary.json` with 2-space indent.

**Your answer:**
amounts = [order["amount"] for order in orders]
summary = {
    "count" : len(orders),
    "total_revenue" : sum(amounts),
    "top_amount" : max(amounts)
}
with open("summary.json", "w") as f:
    json.dump(summary, f, indent=2)
---

## Q10 — Full pipeline (read → transform → stats → write)
Open `raw-transactions.json` (list of dicts with `"user"`, `"amount"`, `"status"`). Do the following in one script:

**Step A:** Load the file.

**Step B:** Build `paid` — a list of only the transactions where `"status" == "paid"`.

**Step C:** Build `by_user` — a dict mapping each paid user to their total amount spent (group-by pattern).

**Step D:** Build `output` dict with:
- `"paid_transactions"`: `paid`
- `"totals_by_user"`: `by_user`
- `"grand_total"`: sum of all paid amounts

**Step E:** Write `output` to `transaction-summary.json` with 2-space indent.

**Your Step A answer:**
with open("raw-transactions.json", "r") as f:
    transactions = json.load(f)

**Your Step B answer:**
paid = [transaction for transaction in transactions if transaction["status"] == "paid"]
paid_total = sum(p["amount"] for p in paid)


**Your Step C answer:**
by_user= {}
for p in paid:
    if p["user"] not in by_user:
        by_user[p["user"]] = 0
    by_user[p["user"]] += p["amount"]


**Your Step D answer:**

output = {
    "paid_transactions": paid,
    "totals_by_user": by_user,
    "grand_total": paid_total
}

**Your Step E answer:**
with open("transaction-summary.json", "w") as f:
    json.dump(output, f, indent = 2)