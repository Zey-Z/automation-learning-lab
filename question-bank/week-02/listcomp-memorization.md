# List Comprehension — Memorization Pass

**Instructions:** Write each answer from memory. No looking at previous drills or exercises. If you get stuck, write what you remember and mark it with `[unsure]`.

---

## M1 — Basic pattern
Write the general pattern of a list comprehension that does filter + map, using placeholder words.

**Your answer:**
[lead["name"] for lead in leads if lead["active"] == True] 

---

## M2 — Map only
Given `nums = [1, 2, 3, 4, 5]`, write a list comprehension that returns each number squared.

**Your answer:**
[num * num for num in nums]
---

## M3 — Filter + map
Given `nums = [1, 2, 3, 4, 5]`, return only even numbers, each multiplied by 10.

**Your answer:**
[num * 10 for num in nums if num%2 == 0]
---

## M4 — Ternary in expression
Given `nums = [1, 2, 3, 4, 5]`, return `"even"` or `"odd"` for each number.

**Your answer:**
["even" if num % 2 == 0 else "odd" for num in nums]
---

## M5 — String method chain
Given `raw = ["  Hello ", "WORLD", " python "]`, return a list of stripped + lowercased strings.

**Your answer:**
[r.strip().lower() for r in raw]
---

## M6 — Dict field extract with filter
Given:
```python
tasks = [
    {"title": "Deploy", "done": True},
    {"title": "Test",   "done": False},
    {"title": "Review", "done": True},
]
```
Return a list of titles for completed tasks only.

**Your answer:**
[task["title"] for task in tasks if task["done"]]
---

## M7 — Build new dicts
Using the same `tasks` list, return a list of dicts: `{"title": ..., "status": "complete"}` for done tasks only.

**Your answer:**
#这个就没那么顺畅了
[{"title": task["title"], "status": "complete"} for task in tasks if task["done"]]
---

## M8 — sorted() with key=lambda
Given `items = [{"name": "C"}, {"name": "A"}, {"name": "B"}]`, sort by name alphabetically.

**Your answer:**
sorted(items,key=lambda item: item["name"])