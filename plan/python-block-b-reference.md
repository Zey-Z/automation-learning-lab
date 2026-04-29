# Python Block B Reference — lambda, import, `if __name__`

Quick reference for Week 2 Block B remaining concepts. Use this when you need to recall the pattern or syntax.

---

## 1. Lambda

### What it is
An anonymous function — a one-line function with no name.

### Pattern
```
lambda <parameter>: <expression>
```

The `:` separates the parameter from the expression. The name you choose for the parameter must be used consistently on both sides.

### Rule
**Same name** on both sides of `:`. You can pick any name.

```python
lambda x:    x["name"]       # OK, both use "x"
lambda lead: lead["name"]    # OK, both use "lead"
lambda item: items["name"]   # WRONG — "item" vs "items"
```

### Common uses

**As `key=` in `sorted()`:**
```python
leads = [{"name": "Zoe", "score": 70}, {"name": "Amy", "score": 90}]

sorted(leads, key=lambda l: l["score"])              # ascending
sorted(leads, key=lambda l: l["score"], reverse=True)  # descending
```

**As a one-line replacement for `def`:**
```python
# Regular function
def double(x):
    return x * 2

# Equivalent lambda
double = lambda x: x * 2
```

### When to use lambda
- When you need a tiny function only once (usually as an argument to `sorted()`, `map()`, `filter()`)
- When writing a `def` would be overkill

### When NOT to use lambda
- When the logic is more than one expression — use `def` instead
- When you need to reuse the function in multiple places — use `def` with a name

---

## 2. Import

### What a module is
A **module** is a Python file containing related functions, classes, or variables. Python groups functionality into modules so you only load what you need.

Examples of built-in modules:
- `json` — parse and write JSON
- `os` — operating system (files, paths)
- `datetime` — dates and times
- `math` — math functions
- `random` — random number generation

### Why import is needed
Python does not load every module by default. Only a small set of "built-in" functions is always available (`print`, `len`, `sorted`, `set`, `list`, `dict`, `int`, `str`, `type`, `range`, `sum`, `min`, `max`).

Everything else must be explicitly imported.

### Two import patterns

**Pattern 1: Import the whole module**
```python
import json

data = json.loads('{"name": "Alice"}')
text = json.dumps(data)
```
You must prefix every use with `json.`.

**Pattern 2: Import a specific thing**
```python
from json import loads

data = loads('{"name": "Alice"}')    # no prefix
```
Cleaner when you only need one function.

### When to use which
- **`import X`** — when you use multiple things from the module
- **`from X import Y`** — when you only use one or two things and want to skip the prefix

### Common examples
```python
import json
import os
import datetime

from datetime import datetime       # class
from json import loads, dumps       # multiple functions
from requests import get, post
```

### JS vs Python mapping
| JavaScript | Python |
|---|---|
| `JSON.parse(raw)` | `json.loads(raw)` |
| `JSON.stringify(data)` | `json.dumps(data)` |
| `require("fs")` | `import os` (for file ops) |
| `import { foo } from "bar"` | `from bar import foo` |

---

## 3. `if __name__ == "__main__":`

### What `__name__` is
Python automatically assigns a special variable `__name__` to every file. Its value depends on how the file is used:

| How the file is used | Value of `__name__` |
|---|---|
| Run directly (`python helper.py`) | `"__main__"` |
| Imported by another file (`import helper`) | `"helper"` |

### What the pattern does
```python
if __name__ == "__main__":
    # code here
```

Translates to: **"Only run this code block when this file is executed directly — not when it is imported by another file."**

### What it prevents
It prevents code inside the block from running automatically when the file is imported. Without this guard, any top-level `print()`, test calls, or demo code would run every time the file is imported, polluting output and potentially causing side effects.

### Example

```python
# helper.py
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    # This only runs when helper.py is executed directly
    print(greet("test"))
```

```python
# main.py
from helper import greet

print(greet("Alice"))    # uses helper.greet, but helper's print does NOT run
```

- Run `python helper.py` → prints `"Hello test"`
- Run `python main.py` → prints only `"Hello Alice"`

### When to use it
- Any file that defines reusable functions AND also has a script/demo section
- Every script you plan to both run directly and import from
- It becomes a standard habit once you start organizing Python projects

### Memory hook
**"Only do this when I am the main character."**

---

## Recurring mistakes to watch for

1. **Lambda parameter mismatch** — `lambda item: items["name"]` (typo: `item` vs `items`)
2. **`import` vs usage confusion** — `json.loads(x)` is usage, not an import statement
3. **`JSON.parse` muscle memory** — Python uses `json.loads`, not `json.parse`
4. **`=` vs `==`** — single `=` is assignment, double `==` is comparison
5. **`"__main__"` formatting** — must be exactly `"__main__"` with two underscores on each side