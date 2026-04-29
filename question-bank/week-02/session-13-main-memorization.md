# Session 13 Memorization Pass - Main Wiring + Tooling

Goal: recall the small canonical shapes from memory before Week 2 practice block.
Write each answer from scratch.

---

## M1 - Canonical: `if __name__`

Write the 2-line pattern that runs `main()` only when the file is executed directly.

Your answer:
if __name__ == "__main__":
    main()
---

## M2 - Canonical: main wiring

Write the general 5-line shape for a script that:
1. loads data
2. filters it
3. transforms it
4. summarizes it
5. saves it

Use placeholder function names if you want, but write a realistic `main()` shape.

Your answer:
def main():
    data = load_data(path)
    filtered = filter_data(data)
    transformed = transform_data(filtered)
    summary = summarize_data(transformed)
    save_data(summary)
    print(summary)
---

## M3 - Canonical: create and activate a venv

Write the two PowerShell commands to:
1. create `.venv`
2. activate `.venv`

Your answer:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
---

## M4 - Canonical: safe dict lookup

Write one line that gets `score` from `lead`, using `0` if the key is missing.

Your answer:
score = lead.get("score", 0)
---

## M5 - Canonical: append vs extend

Write one line that appends `"x"` to `items`, and one line that extends `items` with `["y", "z"]`.

Your answer:
items.append("x")
items.extend(["y", "z"])
---

## M6 - Canonical: Python API request

Write the 3-line shape that:
1. sends a GET request with `params={"userId": 1}` and `timeout=10`
2. checks for status code `200`
3. parses JSON into `data`

Your answer:
import requests
response = requests.get(url, params = {"userId": 1}, timeout= 10)
if response.status_code == 200:
    data = response.json()
---

## M7 - Canonical: JS fetch request

Inside an `async` function, write the 2-line shape that:
1. sends a GET request to `url`
2. parses the JSON body into `data`

Your answer:
const response = await fetch(url)
const data = await response.json()

---

## M8 - Canonical: collection endpoint vs single-item endpoint

Write one example of:
1. a collection endpoint
2. a single-item endpoint

Use `orders` as the resource.

Your answer:
/orders
/orders/99
