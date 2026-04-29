# JS → Python Quick Reference

Side-by-side mapping for everything you learned in Week 1.
Open this file whenever you are writing Python and cannot remember the equivalent.

---

## Variables & Types

| Concept | JavaScript | Python |
|---|---|---|
| Declare | `let x = 5` / `const x = 5` | `x = 5` (no keyword) |
| String | `"hello"` or `'hello'` | `"hello"` or `'hello'` |
| Number (int) | `42` | `42` |
| Number (float) | `3.14` | `3.14` |
| Boolean | `true` / `false` | `True` / `False` (capitalized!) |
| Null / nothing | `null`, `undefined` | `None` |
| Array / list | `[1, 2, 3]` | `[1, 2, 3]` |
| Object / dict | `{name: "Alice"}` | `{"name": "Alice"}` (keys quoted!) |

**Key Python quirks:**
- `True` / `False` / `None` are capitalized.
- Dict keys must be quoted: `{"name": "Alice"}`, not `{name: "Alice"}`.
- No `let` / `const`. Python has no block scope and no "constant" concept. Convention: `ALL_CAPS` for constants.

---

## String Operations

| JS | Python |
|---|---|
| `"  Hello  ".trim()` | `"  Hello  ".strip()` |
| `"HELLO".toLowerCase()` | `"HELLO".lower()` |
| `"hello".toUpperCase()` | `"hello".upper()` |
| `"abc" + "def"` | `"abc" + "def"` |
| `` `Hi ${name}!` `` (template literal) | `f"Hi {name}!"` (f-string) |
| `str.length` | `len(str)` |
| `str.includes("x")` | `"x" in str` |
| `str.split(",")` | `str.split(",")` |

**f-string is the most important pattern:** `f"..."` is nearly identical to JS template literal. Use `{}` to interpolate variables.

---

## Control Flow

### if / else
```js
// JS
if (score >= 90) {
  grade = "A"
} else if (score >= 80) {
  grade = "B"
} else {
  grade = "C"
}
```
```python
# Python — indentation defines the block, no braces
if score >= 90:
    grade = "A"
elif score >= 80:     # note: elif, not "else if"
    grade = "B"
else:
    grade = "C"
```

**Key differences:**
- **Indentation = block** (4 spaces is the standard). No `{}`.
- `elif` instead of `else if`.
- A trailing `:` is required on every header line.
- Conditions do not need `()` around them (allowed but not idiomatic).

### Ternary
```js
// JS
const label = age >= 18 ? "adult" : "minor"
```
```python
# Python — order is reversed! value1 first, condition in middle, value2 last
label = "adult" if age >= 18 else "minor"
```
**Memory hook:** "state the result first, then the condition." Reads like natural English: *"adult if age is 18 or more, else minor"*.

### Loops
```js
// JS
for (let i = 0; i < 5; i++) { ... }
for (const item of arr) { ... }
```
```python
# Python — use range() instead of C-style for
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for item in arr:          # nearly identical to JS for...of
    print(item)

while condition:
    ...
```

**Three forms of `range()`:**
- `range(5)` → 0, 1, 2, 3, 4
- `range(2, 7)` → 2, 3, 4, 5, 6
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (with step)

---

## Comparison & Logic

| JS | Python |
|---|---|
| `===` (strict equal) | `==` (Python `==` is strict by default) |
| `!==` | `!=` |
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |

**Critical:** Python `==` behaves like JS `===` (no weird type coercion). In Python, always use `==`. There is no `===` operator.

---

## Functions

```js
// JS
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`
}
const shout = (msg) => msg.toUpperCase()
```
```python
# Python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

shout = lambda msg: msg.upper()   # lambda = arrow function (limited, single expression)
```

**Differences:**
- `def` keyword instead of `function`.
- Default args use the same idea: `name="Alice"`.
- `lambda` is Python's equivalent of arrow function, but it only allows one expression, no statements.
- Function call syntax is the same: `greet("Bob")`.

---

## Printing / Debugging

| JS | Python |
|---|---|
| `console.log("hi")` | `print("hi")` |
| `console.log(a, b, c)` | `print(a, b, c)` |
| `` console.log(`x = ${x}`) `` | `print(f"x = {x}")` |

---

## Truthy / Falsy

Both languages have similar concepts, but the list of falsy values is slightly different.

| JS falsy | Python falsy |
|---|---|
| `false`, `0`, `""`, `null`, `undefined`, `NaN` | `False`, `0`, `""`, `None`, `[]`, `{}`, `set()` |

**Python has extras:** empty list `[]`, empty dict `{}`, and empty set are all **falsy**. In JS these are truthy.
So in Python you can write:
```python
if not my_list:
    print("list is empty")
```

---

## Collections (preview — will cover in Block C next session)

Do not memorize yet, just get familiar with the shape.

| JS pattern | Python equivalent |
|---|---|
| `arr.filter(x => x > 5)` | `[x for x in arr if x > 5]` (list comprehension) |
| `arr.map(x => x * 2)` | `[x * 2 for x in arr]` |
| `arr.filter(...).map(...)` | `[x * 2 for x in arr if x > 5]` (one expression!) |
| `arr.reduce((s,n) => s+n, 0)` | `sum(arr)` (built-in for sum) |
| `arr.length` | `len(arr)` |
| `arr.push(x)` | `arr.append(x)` |
| `obj.key` | `dict["key"]` or `dict.get("key")` |
| `Object.keys(obj)` | `dict.keys()` |
| `{...obj, key: val}` | `{**obj, "key": val}` |

**Big idea:** Python's **list comprehension** = JS filter + map in one line. This is the most powerful syntax you will learn this week.

---

## File I/O (preview)

```js
// JS — what you learned in Week 1
const fs = require("fs")
const raw = fs.readFileSync("input.json", "utf-8")
const data = JSON.parse(raw)
fs.writeFileSync("output.json", JSON.stringify(data, null, 2))
```
```python
# Python equivalent
import json

with open("input.json", "r") as f:      # context manager auto-closes the file
    data = json.load(f)                   # read + parse in one step

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)          # stringify + write in one step
```

**Python is more concise.** `json.load()` / `json.dump()` read and write directly from a file object, so you don't read a string first then parse. The `with` statement is a "context manager" — it closes the file automatically when the block exits.

---

## What to memorize first (priority order)

1. **f-string:** `f"Hi {name}"` — used constantly.
2. **List comprehension:** `[expr for x in arr if cond]` — Python's core idiom.
3. **Indentation rule:** 4 spaces, `:` at end of header line.
4. **`True` / `False` / `None`** are capitalized.
5. **`and` / `or` / `not`** instead of `&&` / `||` / `!`.
6. **Ternary reverse order:** `value if cond else value`.
7. **`len(x)`** instead of `x.length`.
8. **`print()`** instead of `console.log()`.
