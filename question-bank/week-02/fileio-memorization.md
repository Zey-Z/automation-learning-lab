# File I/O Memorization Pass — Week 2

Goal: lock in the canonical shapes so they come out from muscle memory.
Write your answer from scratch — no looking at notes.

---

## M1 — Canonical: Read a text file

Write the 2-line canonical shape for reading a file called `notes.txt` into a variable `text`.

**Your answer:**
with open("notes.txt", "r") as f:
    text = f.read()

---

## M2 — Canonical: Write a text file

Write the 2-line canonical shape for writing the string `"log entry"` into a file called `log.txt`.

**Your answer:**
with open("log.txt", "w") as f:
    f.write("log entry")

---

## M3 — Canonical: Read JSON into a Python object

Write the 3-line canonical shape (including the import) for loading `data.json` into a variable called `data`.

**Your answer:**
import json
with open("data.json", "r") as f:
    data = json.load(f)

---

## M4 — Canonical: Write JSON with pretty print

Write the 2-line canonical shape for writing the variable `data` to `out.json` with 2-space indentation.

**Your answer:**
with open("out.json", "w") as f:
    json.dump(data, f, indent= 2)

---

## M5 — Built-ins quick recall

Fill in the function names (no args needed, just the names):

- sum of a list: `___(nums)`
- length of a list: `___(nums)`
- largest value: `___(nums)`
- smallest value: `___(nums)`
- round 3.14159 to 2 decimals: `___(3.14159, 2)`

**Your answer:**
sum
len
max
min
round
---

## M6 — Canonical: Group-by pattern

From scratch, write the group-by pattern that maps each user in `transactions` (list of dicts with `"user"` and `"amount"`) to their total amount.

```
transactions = [
    {"user": "alice", "amount": 50},
    {"user": "bob",   "amount": 80},
    {"user": "alice", "amount": 100},
]
# Goal: {"alice": 150, "bob": 80}
```

**Your answer:**
goal = {}
for t in transactions :
    if t["user"] not in goal:
        goal[t["user"]] = 0
    goal[t["user"]] += t["amount"]

---

## M7 — Canonical: Extract a field from a list of dicts

Given `leads` (list of dicts with `"score"` among other keys), write one line that produces a list of all scores.

**Your answer:**
scores = [lead["score"] for lead in leads]

---

## M8 — Full pipeline shape

From scratch, write a complete script shape that does:
1. Reads JSON from `input.json` into a variable
2. Filters some items (you can write `<condition>` as a placeholder)
3. Writes the filtered list to `output.json` with 2-space indent

No placeholders for `open`, `json.load`, `json.dump`, `with`, `for`, `if` — those you must write fully.

**Your answer:**
import json
with open("input.json", "r") as f:
    raw = json.load(f)
filtered = [fil for fil in raw if fil["score"] >= 70]
with open("output.json", "w") as f:
    json.dump(filtered, f, indent = 2)