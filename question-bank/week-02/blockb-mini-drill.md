# Block B Mini Drill — lambda, import, if __name__

**Instructions:** Write your answer from memory. These are quick recall questions.

---

## B1 — lambda syntax
Write a lambda that takes a number `x` and returns `x + 10`.

**Your answer:**
lambda x:x+10
---

## B2 — lambda in sorted
Given `people = [{"name": "Zoe", "age": 25}, {"name": "Amy", "age": 30}]`, use `sorted()` with a lambda to sort by age.

**Your answer:**
sorted(people, key=lambda p:p["age"])
---

## B3 — lambda vs def
Rewrite this lambda as a regular `def` function:
```python
double = lambda x: x * 2
```

**Your answer:**
def double(x):
    return x*2
---

## B4 — import
Write the import statement to use Python's built-in `json` module.

**Your answer:**
import json
---

## B5 — from import
Write the import statement to import only the `loads` function from the `json` module.

**Your answer:**
from json import loads
---

## B6 — import usage
After `import json`, write one line to parse this JSON string into a Python dict:
```python
raw = '{"name": "Alice", "score": 82}'
```

**Your answer:**
json.loads(raw)
---

## B7 — if __name__
Write the `if __name__` pattern. Inside it, print `"running directly"`.

**Your answer:**
if __name__ == "__main__":
    print("running directly")
---

## B8 — if __name__ purpose
In one sentence, explain: what does `if __name__ == "__main__":` prevent from happening?

**Your answer:**
Python assign each file a variable __name__, if its value is "__main__", it means the file is the current one, and it prevents the code imported from other files.
It prevents the code inside from running automatically when the file is imported by another file, it only runs when the file is executed directly