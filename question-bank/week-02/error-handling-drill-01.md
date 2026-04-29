# Error Handling Drill — Week 2

**Topic:** `try`, `except`, `finally`, common exception patterns
**Format:** 10 questions — 5 basic (Q1–Q5) + 5 variants (Q6–Q10)
**Rule:** Write your answer directly under each question.

---

## Q1 — Basic `try` / `except`
Convert `raw = "42"` to an integer and print it. If conversion fails, print `"bad number"`.

Your answer:
```python
try:
    print(int(raw))
except ValueError:
    print("bad number")
```

---

## Q2 — Catch `ZeroDivisionError`
Given `divisor = 0`, write code that tries to compute `10 / divisor`. If division by zero happens, print `"cannot divide by zero"`.

Your answer:
```python
try:
    10 / divisor
except ZeroDivisionError:
    print("cannot divide by zero")
```

---

## Q3 — `finally`
Write code that:
1. Tries to convert `raw = "abc"` to an integer
2. Prints `"bad number"` if it fails
3. Always prints `"done"` in a `finally` block

Your answer:
```python
try:
    int(raw)
except ValueError:
    print("bad number")
finally:
    print("done")
```

---

## Q4 — File not found
Open `config.json` in read mode and load it with `json.load()`. If the file does not exist, print `"config file not found"`.

Your answer:
```python
import json
try: 
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("config file not found")
```

---

## Q5 — Function with fallback return
Write a function `safe_int(text)` that:
- returns `int(text)` if conversion works
- returns `None` if conversion fails with `ValueError`

Your answer:
```python
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
```

---

## Q6 — Loop + skip bad values
Given `raw_scores = ["10", "25", "oops", "40"]`, build a list called `scores` containing only the valid integers. Use a loop and `try` / `except`.

Expected result: `[10, 25, 40]`

Your answer:
```python
scores = []
for score in raw_scores:
    try:
        scores.append(int(score))
    except ValueError:
        continue
```

---

## Q7 — JSON parsing failure
Given:
```python
import json
raw = '{"name": "Alice", "score": 90'
```
Use `json.loads(raw)` inside `try` / `except`. If parsing fails, print `"bad json"` and set `data = {}`.

Your answer:
```python
import json
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    print("bad json")
    data = {}
```

---

## Q8 — Multiple exception types
Write code that:
1. Opens `users.json`
2. Loads it with `json.load()`
3. Prints `"missing file"` if the file is missing
4. Prints `"bad json"` if the file exists but contains invalid JSON

Your answer:
```python
import json
try:
    with open("users.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
        print("missing file")
except json.JSONDecodeError:
        print("bad json")
```

---

## Q9 — Function + process mistake guard
Write a function `safe_average(nums)` that:
- returns the average of the list
- returns `None` if the list is empty

Do not let it crash with `ZeroDivisionError`.

Your answer:
```python
def safe_average(nums):
    try:
        avg = sum(nums)/ len(nums)
        return avg
    except ZeroDivisionError:
        return None
```

---

## Q10 — Full mini pipeline
Given `raw_prices = ["19.99", "5", "bad", "12.5"]`, write code that:
1. Converts each valid item to `float`
2. Skips invalid values with `try` / `except`
3. Stores valid floats in `prices`
4. Prints the average rounded to 2 decimals if `prices` is not empty
5. Always prints `"finished price cleanup"` in a `finally` block

Your answer:
```python
prices = []
for price in raw_prices:
    try:
        prices.append(float(price))
    except ValueError:
        continue
try:
    if prices:
        print(round(sum(prices) / len(prices), 2))
finally:
    print("finished price cleanup")
```
