# Python Basics Drill (Session 6)

**Topic:** Variables, strings, if/elif/else, for/while, basic functions, print, f-strings
**Format:** 10 questions — 5 basic (Q1–Q5) + 5 variants (Q6–Q10)
**Target time:** ~30 min
**Rule:** Write your answer directly under each question. Check `plan/js-to-python-map.md` if stuck on syntax.

**Note:** This drill does not touch list/dict operations — those come next session (Block C). Today only tests core Python syntax and JS → Python mental mapping.

---

## Q1 — String cleanup + f-string
Given:
```python
raw_name = "   alice JOHNSON  "
age = 28
```
Clean `raw_name` (strip whitespace, title case — hint: `.title()`) and print:
```
Alice Johnson is 28 years old.
```

Your answer:
```python
name = raw_name.strip().title()
print(f"{name} is {age} years old.")

```

---

## Q2 — If / elif / else
Write a function `grade_score(score)` that returns:
- `"A"` if score >= 90
- `"B"` if score >= 80
- `"C"` if score >= 70
- `"F"` otherwise

Your answer:
```python
def grade_score(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade

```

---

## Q3 — For loop + range
Print the numbers from 1 to 10 (inclusive), one number per line.

Your answer:
```python
for i in range(1,11):
    print(i)

```

---

## Q4 — Ternary (conditional expression)
Given `temperature = 32`. Use Python's ternary (`value if cond else value`) to create a variable `status` equal to:
- `"freezing"` if temperature <= 32
- `"ok"` otherwise

Then print the status using an f-string: `"Temperature is X, status: Y"`.

Your answer:
```python
status = "freezing" if temperature <=32 else "ok"
print(f"Temperature is {temperature}, status {status}") 

```

---

## Q5 — While loop + accumulator
Use a `while` loop to compute the sum of numbers from 1 to 100. Store it in a variable `total` and print it.

Your answer:
```python
total = 0
i = 1
while i <=100:
    total = total + i
    i += 1
print(total)

```

---

## Q6 — Variant: string validation + early return
Write a function `clean_email(email)` that:
1. Strips whitespace.
2. Lowercases the string.
3. If the result is an empty string, returns `None`.
4. Otherwise returns the cleaned email.

Test with: `clean_email("   ALICE@TEST.COM  ")` should return `"alice@test.com"`.
And: `clean_email("   ")` should return `None`.

Your answer:
```python
def clean_email(email):
    cleaned = email.strip().lower()
    if not cleaned:
        return None
    return cleaned
```

---

## Q7 — Variant: nested conditions + multiple criteria
Write a function `can_vote(age, citizenship, registered)` that returns:
- `"eligible"` if age >= 18 AND citizenship is `"US"` AND registered is `True`.
- `"not registered"` if age >= 18 AND citizenship is `"US"` AND registered is `False`.
- `"not eligible"` otherwise.

Use `and` / `or` (not `&&` / `||`).

Your answer:
```python
def can_vote(age, citizenship, registered):
    if age >= 18 and citizenship == "US" and registered == True :
        return "eligible" 
    if age >= 18 and citizenship == "US" and registered == False :
        return "not registered"
    else:
        return "not eligible"
```

---

## Q8 — Variant: for loop with skip condition
Use a `for` loop to print all **even** numbers from 1 to 20. (Hint: `%` is the modulo operator, same as JS.)

Your answer:
```python
for i in range(1,21):
    if i % 2 == 0:
        print(i)

```

---

## Q9 — Variant: accumulator with condition
Use a `for` loop to compute the sum of numbers from 1 to 50 that are **divisible by 3 or 5** (like FizzBuzz). Store the result in `total` and print it.

Expected: include only 3, 5, 6, 9, 10, 12, ... (multiples of 3 or multiples of 5).

Your answer:
```python
total = 0
for i in range(1,51):
    if i % 3 == 0 or i % 5 \
    
    \
     . \             0:
        total = total + i
print(total)
```

---

## Q10 — Variant: function + multiple returns + f-string report
Write a function `describe_user(name, age)` that:
1. If age < 0, return `"invalid age"`.
2. If age < 13, return `"{name} is a child"` (use an f-string).
3. If age < 20, return `"{name} is a teenager"`.
4. If age < 65, return `"{name} is an adult"`.
5. Otherwise return `"{name} is a senior"`.

Test:
```python
print(describe_user("Alice", 30))   # "Alice is an adult"
print(describe_user("Bob", 15))     # "Bob is a teenager"
print(describe_user("Cara", -5))    # "invalid age"
```

Your answer:
```python
def describe_user(name, age):
    if age < 0:
        return "invalid age"
    elif age < 13:
        return f"{name} is a child"
    elif age <20:
        return f"{name} is a teenager"
    elif age <65:
        return f"{name} is an adult"
    else:
        return f"{name} is a senior"
```

---

## Self-check after finishing

- [ ] Did I use `True` / `False` / `None` with capital letters?
- [ ] Did I indent consistently (4 spaces or tab, not mixed)?
- [ ] Did I use `==`, not `===`?
- [ ] Did I use `and` / `or` / `not`, not `&&` / `||` / `!`?
- [ ] Did I end every `if` / `for` / `while` / `def` line with `:`?
- [ ] Did I use `elif`, not `else if`?
- [ ] Did I use `f"..."` for string interpolation (not `+` or `${}`)?

Paste your answers in chat when done for review.
